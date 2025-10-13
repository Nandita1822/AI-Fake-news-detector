# AI Fake News Detector

A web application that helps students identify fake news and misinformation by analyzing articles using AI.

## 📥 Download Instructions

### Option 1: Download as ZIP
1. Download the ZIP of this repository
2. Extract it on your computer

### Option 2: Clone via Git
```bash
git clone https://github.com/Nandita1822/AI-Fake-news-detector.git
cd AI-Fake-news-detector
💻 Running Offline on Your Computer
Prerequisites

Python 3.10 or higher

OpenAI API key (get it from https://platform.openai.com/
)

Hugging Face token (get it from https://huggingface.co/settings/tokens
)
Setup Instructions

Navigate to the project folder:

cd path/to/AI-Fake-news-detector

Install required packages:

pip install -r requirements.txt


Set environment variables:

Windows (CMD):

set OPENAI_API_KEY=your_openai_key_here
set HF_TOKEN=your_huggingface_token_here


Mac/Linux:

export OPENAI_API_KEY='your_openai_key_here'
export HF_TOKEN='your_huggingface_token_here'


Or create a .env file with:

OPENAI_API_KEY=your_openai_key_here
HF_TOKEN=your_huggingface_token_here


Run the application:

python app.py


Open your browser at:

http://localhost:5000

🚀 Quick Start
Windows:
pip install -r requirements.txt
set OPENAI_API_KEY=your_openai_key_here
set HF_TOKEN=your_huggingface_token_here
python app.py

Mac/Linux:
pip install -r requirements.txt
export OPENAI_API_KEY='your_openai_key_here'
export HF_TOKEN='your_huggingface_token_here'
python app.py

📁 Project Structure
AI-Fake-news-detector/
│
├── app.py                 # Main Flask application
├── templates/
│   └── index.html        # Frontend interface
├── README.md             # This file
├── requirements.txt      # Python dependencies
└── .gitignore            # Git ignore file

⚙️ Configuration

Default port: 5000

Model: Hugging Face distilbert-base-uncased-finetuned-sst-2-english

Web framework: Flask

Production server: Gunicorn (optional)

To change port, edit:

app.run(host='0.0.0.0', port=5000)

🛠️ Troubleshooting

Python not found: use python3 instead of python

Module not found: run pip install -r requirements.txt

API key error: check OPENAI_API_KEY and HF_TOKEN

Port already in use: change port number in app.py

🔒 Security Notes

Never commit your API keys

Use .env or environment variables

.env is in .gitignore by default

🎓 How It Works

Paste a news article or social media post

App sends text to AI for analysis

AI returns:

Credibility score (0-100)

Summary

Explanation

Warning signs

Results displayed:

🟢 70-100: Likely Reliable

🟠 40-69: Questionable

🔴 0-39: Likely Unreliable

📄 License

Open for educational use.

Happy Fact-Checking! 🔍📰


---
