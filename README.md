# 🧠 Task Simplifier — AI Task Processor (Gemini 2.0 Flash)

Task Simplifier is a lightweight AI-powered tool that converts natural-language tasks into structured, actionable items using **Google Gemini 2.0 Flash**.  
It generates a clear task title, summary, priority score, and priority category — all from a single user input.

A simple **Streamlit web app** is included so anyone can try it without writing code.

---

## 🚀 Features
- ✨ AI-generated task title  
- ✨ Clean summary for each task  
- ✨ Priority score (0–100)  
- ✨ Priority label (high / medium / low)  
- ✨ Streamlit UI  
- ✨ Secure API key via Streamlit Secrets  
- ✨ Minimal setup, works instantly  

---

## 📂 Files in this repository
```
streamlit_task_simplifier.py   # Main Streamlit app
requirements.txt               # Dependencies
README.md                      # Documentation
```

---

## 🌐 Live App
*(Add your Streamlit Cloud link here after deployment)*  
Example:  
https://your-app-name.streamlit.app

---

## ▶️ Run Locally
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Add your Gemini API Key using Streamlit secrets:
Create `.streamlit/secrets.toml`:
```toml
GOOGLE_API_KEY = "your_api_key_here"
```

3. Run the app:
```bash
streamlit run streamlit_task_simplifier.py
```

---

## 🚀 Deploy on Streamlit Cloud
1. Push this repo to GitHub  
2. Go to https://share.streamlit.io  
3. Choose your repo and deploy  
4. Add your API key under **Settings → Secrets**:
```
GOOGLE_API_KEY = "your_real_gemini_api_key"
```

---

## 🧠 Example Output
Input:
```
Pay electricity bill by Friday, urgent
```

Output:
```json
{
  "title": "Pay Electricity Bill",
  "summary": "Settle the electricity bill before Friday.",
  "priority_score": 78,
  "priority": "high"
}
```

---

## 🙌 Credits
Built with:
- Streamlit  
- Google Gemini 2.0 Flash  
- Python  
