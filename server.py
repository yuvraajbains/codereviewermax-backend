from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

app = Flask(__name__)

print("⏳ Loading CodeT5-Small model...")

tokenizer = AutoTokenizer.from_pretrained("Salesforce/codet5-small")
model = AutoModelForSeq2SeqLM.from_pretrained("Salesforce/codet5-small").to("cpu")

print("✅ CodeT5-Small model loaded and ready!")

@app.route("/review", methods=["POST"])
def review():
    data = request.get_json()
    code = data.get("code", "")

    if not code.strip():
        return jsonify({"error": "No code provided"}), 400

    input_text = (
        f"You are a senior engineer. Review the code below and provide 3 bullet points of feedback. "
        f"Focus on improvements, readability, or bugs.\n\n"
        f"```python\n{code}\n```"
    )

    inputs = tokenizer(input_text, return_tensors="pt", truncation=True).to("cpu")

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_length=256,
            do_sample=True,
            temperature=0.7,
            top_k=40
        )

    review = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
    lines = review.splitlines()
    bullets = [line for line in lines if line.strip().startswith("-")]
    cleaned = "\n".join(bullets[:3]) if bullets else "\n".join(lines[:5])

    return jsonify({"review": cleaned})

if __name__ == "__main__":
    app.run(port=5000)
