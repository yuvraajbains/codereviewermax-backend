# 🧪 CodeReviewerMax Backend (Optional Flask Server)

This is an **optional Flask backend** originally created to support [CodeReviewerMax](https://github.com/yuvraajbains/codereviewermax), a VS Code extension for local AI-powered code review.

It allows you to run Hugging Face transformer models (e.g., CodeT5+, StarCoder) locally using Python + Flask — but has been replaced in the main setup by the faster and more flexible [GPT4All](https://gpt4all.io) local server.

---

## ⚠️ Note

> ✅ This backend is **not required** if you're using the GPT4All app with CodeReviewerMax (the recommended approach).  
> 🧪 Use this only if you want to host your own model with Hugging Face and Python.

---

## 🚀 How It Works

- Loads a Hugging Face-supported model (e.g. `codet5p-770m`)
- Starts a Flask server at `http://localhost:5000/review`
- Accepts `POST` requests with code and returns generated feedback

---

## 🧰 Requirements

- Python 3.9+
- Flask
- Hugging Face Transformers
- PyTorch (CPU or GPU)

---

## ⚙️ Setup Instructions

```bash
git clone https://github.com/YOUR_USERNAME/codereviewer-backend.git
cd codereviewer-backend

python -m venv venv
venv\Scripts\activate         # On Windows
# or: source venv/bin/activate (Mac/Linux)

pip install -r requirements.txt
python server.py

