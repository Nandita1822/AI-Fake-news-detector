import os
import json
from flask import Flask, render_template, request, jsonify
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

# -----------------------------
# Hugging Face token
# -----------------------------
HF_TOKEN = "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"

# -----------------------------
# Load tokenizer and model with token
# -----------------------------
tokenizer = AutoTokenizer.from_pretrained(
    "distilbert-base-uncased-finetuned-sst-2-english",
    use_auth_token=HF_TOKEN
)

model = AutoModelForSequenceClassification.from_pretrained(
    "distilbert-base-uncased-finetuned-sst-2-english",
    use_auth_token=HF_TOKEN
)

# -----------------------------
# Initialize Hugging Face pipeline
# -----------------------------
hf_classifier = pipeline(
    "text-classification",
    model=model,
    tokenizer=tokenizer
)

# -----------------------------
# Initialize Flask app
# -----------------------------
app = Flask(__name__)

# -----------------------------
# Routes
# -----------------------------
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze_article():
    try:
        data = request.json
        article_text = data.get('article', '').strip()

        if not article_text or len(article_text) < 10:
            return jsonify({'error': 'Please enter at least 10 characters of text to analyze'}), 400

        # -----------------------------
        # Hugging Face model prediction
        # -----------------------------
        results = hf_classifier(article_text)

        # Results are usually in form: [{'label': 'POSITIVE', 'score': 0.95}]
        prediction = results[0]
        label = prediction['label']
        score = round(float(prediction['score']) * 100)

        # Map label to credibility score
        if label.lower() in ['negative', 'fake', 'unreliable']:
            credibility_score = 20  # low
            status_text = "Likely Unreliable"
        else:
            credibility_score = 85  # high
            status_text = "Likely Reliable"

        analysis = {
            "credibility_score": credibility_score,
            "status": status_text,
            "label": label,
            "score_percent": score,
            "summary": article_text[:150] + "..."  # simple summary
        }

        return jsonify({'success': True, 'analysis': analysis})

    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500


# -----------------------------
# Run Flask app
# -----------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
