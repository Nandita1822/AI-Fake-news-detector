# Fake News Detector for Students

A web application that helps students identify fake news and misinformation by analyzing articles using AI.

## 📥 Download Instructions

### Option 1: Download as ZIP from Replit
1. Click on the three dots (•••) menu in the file explorer
2. Select "Download as ZIP"
3. Extract the ZIP file on your computer

### Option 2: Clone via Git (if connected to GitHub)
```bash
git clone <your-repo-url>
cd <your-project-folder>
```

## 💻 Running Offline on Your Computer

### Prerequisites
- Python 3.10 or higher installed on your computer
- OpenAI API key (get it from https://platform.openai.com/)

### Step-by-Step Setup

#### 1. Install Python (if not already installed)
- **Windows**: Download from https://www.python.org/downloads/
- **Mac**: Download from https://www.python.org/downloads/ or use `brew install python3`
- **Linux**: Usually pre-installed, or use `sudo apt-get install python3 python3-pip`

#### 2. Navigate to the Project Folder
Open Terminal (Mac/Linux) or Command Prompt (Windows):
```bash
cd path/to/fake-news-detector
```

#### 3. Install Required Packages
```bash
pip install Flask openai gunicorn
```

Or install from requirements file (if you create one):
```bash
pip install -r requirements.txt
```

#### 4. Set Up Your OpenAI API Key

**Windows (Command Prompt):**
```cmd
set OPENAI_API_KEY=your_api_key_here
```

**Windows (PowerShell):**
```powershell
$env:OPENAI_API_KEY="your_api_key_here"
```

**Mac/Linux:**
```bash
export OPENAI_API_KEY='your_api_key_here'
```

**Or create a `.env` file** (recommended):
1. Create a file named `.env` in the project folder
2. Add this line: `OPENAI_API_KEY=your_api_key_here`
3. Install python-dotenv: `pip install python-dotenv`
4. The app will automatically load it

#### 5. Run the Application

**Development Mode (for testing):**
```bash
python app.py
```

**Production Mode (recommended):**
```bash
gunicorn --bind=0.0.0.0:5000 app:app
```

#### 6. Open in Your Browser
- Open your web browser
- Go to: `http://localhost:5000`
- The Fake News Detector will load!

## 🚀 Quick Start (All-in-One)

### Windows:
```cmd
pip install Flask openai gunicorn
set OPENAI_API_KEY=your_api_key_here
python app.py
```
Then open: http://localhost:5000

### Mac/Linux:
```bash
pip install Flask openai gunicorn
export OPENAI_API_KEY='your_api_key_here'
python app.py
```
Then open: http://localhost:5000

## 📁 Project Structure
```
fake-news-detector/
│
├── app.py                 # Main Flask application
├── templates/
│   └── index.html        # Frontend interface
├── README.md             # This file
├── replit.md             # Project documentation
└── .gitignore            # Git ignore file
```

## 🔑 Getting an OpenAI API Key

1. Go to https://platform.openai.com/
2. Sign up or log in
3. Navigate to API Keys section
4. Click "Create new secret key"
5. Copy the key and save it somewhere safe
6. Use it in step 4 above

## ⚙️ Configuration

The app uses:
- **Port 5000** by default
- **OpenAI GPT-3.5-turbo** model
- **Flask** web framework for development
- **Gunicorn** WSGI server for production

To change the port, edit `app.py` line 54:
```python
app.run(host='0.0.0.0', port=5000)  # Change 5000 to your preferred port
```

## 🛠️ Troubleshooting

### "Command not found: python"
- Try `python3` instead of `python`
- Make sure Python is installed and added to PATH

### "Module not found" errors
- Run: `pip install Flask openai gunicorn`
- Or try: `pip3 install Flask openai gunicorn`

### "API key not found" error
- Make sure you set the OPENAI_API_KEY environment variable
- Check that your API key is valid and has credits
- Try restarting your terminal after setting the environment variable

### Port already in use
- Change the port number in app.py to something else (e.g., 5001, 8000)
- Or stop the process using port 5000

### OpenAI API errors
- Check your API key is valid
- Ensure you have credits in your OpenAI account
- Check your internet connection

## 📝 Requirements File

Create a `requirements.txt` file with:
```
Flask>=2.1.3
openai>=0.27.8
gunicorn>=23.0.0
```

Then install with: `pip install -r requirements.txt`

## 🔒 Security Notes

- **Never commit your API key** to version control
- Use environment variables or `.env` files for sensitive data
- The `.env` file is already in `.gitignore` to prevent accidental commits
- For production, use HTTPS and proper security headers

## 📱 Using on Mobile/Other Devices

1. Run the app on your computer
2. Find your computer's local IP address:
   - Windows: `ipconfig` 
   - Mac/Linux: `ifconfig` or `ip addr`
3. On your mobile device, connect to same WiFi
4. Open browser and go to: `http://YOUR_IP:5000`

## 🎓 How It Works

1. Student pastes a news article or social media post
2. App sends text to OpenAI for analysis
3. AI evaluates credibility and provides:
   - Credibility score (0-100)
   - Article summary
   - Explanation suitable for students
   - Warning signs or positive indicators
4. Results displayed with color coding:
   - 🟢 Green (70-100): Likely Reliable
   - 🟠 Orange (40-69): Questionable
   - 🔴 Red (0-39): Likely Unreliable

## 📄 License

This project is open for educational use.

## 🆘 Need Help?

If you encounter issues:
1. Check the Troubleshooting section above
2. Make sure all prerequisites are installed
3. Verify your OpenAI API key is set correctly
4. Check that you have internet connection for API calls

---

**Happy Fact-Checking! 🔍📰**
