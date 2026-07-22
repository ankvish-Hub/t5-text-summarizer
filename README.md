# 📝 T5 Text Summarizer

A web-based **Text Summarization** application built with **FastAPI**, **Hugging Face Transformers**, and **PyTorch**. This project uses a fine-tuned **T5 Transformer** model to generate concise summaries from long pieces of text through an intuitive web interface.

---

## 🚀 Features

- 🤖 AI-powered text summarization using T5 Transformer
- ⚡ FastAPI backend for high-performance API requests
- 🎨 Clean and responsive user interface
- 🧹 Automatic text preprocessing
- 📄 Summarizes long text efficiently
- 💻 Supports CPU, CUDA (GPU), and Apple Silicon (MPS)

---

## 🛠️ Tech Stack

### Backend
- Python
- FastAPI
- PyTorch
- Hugging Face Transformers
- Pydantic
- Jinja2

### Frontend
- HTML
- CSS
- JavaScript

---

## 📁 Project Structure

```text
TextSummarizerApp/
│
├── templates/
│   └── index.html
│
├── static/
│
├── saved_summary_model/      # Local trained model (Not uploaded to GitHub)
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/ankvish-Hub/t5-text-summarizer.git
cd t5-text-summarizer
```

### 2. Create Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
uvicorn app:app --reload
```

Open your browser:

```
http://127.0.0.1:8000
```

---

## 📌 API Endpoint

### POST `/summarize/`

#### Request

```json
{
  "dialogue": "Your text goes here..."
}
```

#### Response

```json
{
  "summary": "Generated summary."
}
```

---

## 🧠 How It Works

1. User enters or pastes text.
2. Input text is cleaned and preprocessed.
3. The tokenizer converts text into tokens.
4. The T5 Transformer generates a concise summary.
5. The generated summary is displayed on the webpage.

---

## 💻 Device Support

The application automatically selects the best available device:

- ✅ NVIDIA GPU (CUDA)
- ✅ Apple Silicon (MPS)
- ✅ CPU

---

## 📦 Requirements

- Python 3.10+
- FastAPI
- Transformers
- Torch
- Pydantic
- Jinja2
- Uvicorn

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## 📸 Screenshot

![Text Summarizer](screenshots/home.png)

---

## 🔮 Future Improvements

- PDF Summarization
- DOCX Summarization
- URL Summarization
- Multi-language Support
- Copy Summary Button
- Download Summary
- Docker Deployment
- Hugging Face Spaces Deployment

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create your feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push to the branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Ankit Vishwakarma**

- GitHub: https://github.com/ankvish-Hub

---

⭐ If you found this project useful, consider giving it a **Star** on GitHub!
