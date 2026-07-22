from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
import re

# ---------------------------------------------------
# FastAPI App
# ---------------------------------------------------

app = FastAPI(
    title="Text Summarizer",
    description="Text Summarization using Fine-Tuned T5",
    version="1.0"
)

templates = Jinja2Templates(directory="templates")

# ---------------------------------------------------
# Device
# ---------------------------------------------------

if torch.cuda.is_available():
    device = torch.device("cuda")
elif torch.backends.mps.is_available():
    device = torch.device("mps")
else:
    device = torch.device("cpu")

print(f"Using Device : {device}")

# ---------------------------------------------------
# Load Model Once
# ---------------------------------------------------

MODEL_PATH = "./saved_summary_model"

model = T5ForConditionalGeneration.from_pretrained(MODEL_PATH)
tokenizer = T5Tokenizer.from_pretrained(MODEL_PATH)

model.to(device)
model.eval()

# ---------------------------------------------------
# Request Model
# ---------------------------------------------------

class DialogueInput(BaseModel):
    dialogue: str


# ---------------------------------------------------
# Text Cleaning
# ---------------------------------------------------

def clean_text(text: str):

    text = re.sub(r"<.*?>", " ", text)
    text = re.sub(r"\r\n", " ", text)
    text = re.sub(r"\n", " ", text)
    text = re.sub(r"\s+", " ", text)

    return text.strip()


# ---------------------------------------------------
# Summarization
# ---------------------------------------------------

def summarize_dialogue(dialogue: str):

    dialogue = clean_text(dialogue)

    # T5 requires this prefix
    dialogue = "summarize: " + dialogue

    inputs = tokenizer(
        dialogue,
        max_length=512,
        truncation=True,
        padding=True,
        return_tensors="pt"
    )

    input_ids = inputs.input_ids.to(device)
    attention_mask = inputs.attention_mask.to(device)

    with torch.inference_mode():

        outputs = model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,

            max_length=80,
            min_length=20,

            num_beams=6,
            early_stopping=True,

            length_penalty=2.0,
            repetition_penalty=2.5,

            no_repeat_ngram_size=3
        )

    summary = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return summary


# ---------------------------------------------------
# Routes
# ---------------------------------------------------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.post("/summarize/")
async def summarize(dialogue_input: DialogueInput):

    if len(dialogue_input.dialogue.strip()) == 0:
        return {
            "summary": "Please enter some text."
        }

    summary = summarize_dialogue(dialogue_input.dialogue)

    return {
        "summary": summary
    }