# 🧠 CodeReviewerMax Backend

This is the **Flask-powered backend** for [CodeReviewerMax](https://github.com/YOUR_USERNAME/codereviewermax), a local AI-powered code review extension for VS Code.

It loads a local language model (like [CodeT5+](https://huggingface.co/Salesforce/codet5p-770m), [StarCoderBase](https://huggingface.co/bigcode/starcoderbase), or others) and serves a simple API endpoint to generate reviews for selected code.

---

## 🚀 How It Works

- Runs a local LLM model using Hugging Face Transformers
- Accepts POST requests at `/review` with selected code
- Returns a short review string formatted by the model
- Meant to be connected to the CodeReviewerMax extension

---

## 🧰 Requirements

- Python 3.8+
- HuggingFace Transformers
- Flask
- PyTorch (CPU or GPU)
- One of:
  - `Salesforce/codet5p-770m`
  - `bigcode/starcoderbase`
  - Any lightweight model with text-to-text capability

---

## ⚙️ Setup Instructions

```bash
git clone https://github.com/YOUR_USERNAME/codereviewer-backend.git
cd codereviewer-backend

python -m venv venv
venv\Scripts\activate          # or source venv/bin/activate on Mac/Linux

pip install -r requirements.txt

python server.py
