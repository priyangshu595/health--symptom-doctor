# 🩺 Healthcare Symptom Checker

### AI-Powered Symptom Analysis with Actionable Insights

An intelligent web application that analyzes user-provided symptoms and generates **possible medical conditions, severity levels, and recommendations** using an LLM — designed strictly for **educational and awareness purposes**.

---

## 🚀 Live Project Overview

This project simulates a **real-world healthcare assistant system** by integrating:

* 🧠 **Large Language Model (LLM)** for reasoning
* ⚡ **FastAPI backend** for scalable API handling
* 🌐 **Interactive frontend UI** for user-friendly experience

---

## ✨ Key Features

* 🔍 **Symptom-based analysis** using AI
* 📊 **Structured JSON output** (clean & professional)
* ⚠️ **Severity classification** (Low / Medium / High)
* 💡 **Actionable recommendations**
* 👨‍⚕️ **Doctor consultation guidance**
* 📢 **Medical safety disclaimer**
* 🎨 **Modern UI with responsive design**
* ⚡ **Fast and lightweight backend**

---

## 🧠 System Architecture

```id="p9y1cz"
User Input → FastAPI Backend → OpenRouter API (LLM) → JSON Parsing → Frontend Display
```

---

## 🛠️ Tech Stack

| Layer     | Technology            |
| --------- | --------------------- |
| Backend   | FastAPI (Python)      |
| Frontend  | HTML, CSS, JavaScript |
| AI Model  | OpenRouter (LLaMA 3)  |
| Libraries | requests, pydantic    |

---

## ⚙️ How It Works

1. User enters symptoms (e.g., *fever, headache*)
2. Backend constructs a structured prompt
3. Request is sent to OpenRouter LLM API
4. LLM returns structured JSON response
5. Backend extracts and validates output
6. Frontend displays formatted results

---

## 📂 Project Structure

```id="1o4k3t"
healthcare-symptom-checker/
│
├── app.py              # FastAPI backend (API + LLM integration)
├── requirements.txt    # Dependencies
├── index.html          # Frontend UI
└── README.md           # Documentation
```

---

## 🚀 Installation & Setup

### 1️⃣ Clone Repository

```id="bbgqfc"
git clone https://github.com/yourusername/healthcare-symptom-checker.git
cd healthcare-symptom-checker
```

---

### 2️⃣ Install Dependencies

```id="6sl1ys"
pip install -r requirements.txt
```

---

### 3️⃣ Configure API Key

Open `app.py` and add your OpenRouter key:

```id="g0g3zw"
OPENROUTER_API_KEY = "YOUR_OPENROUTER_API_KEY"
```

---

### 4️⃣ Run Backend Server

```id="0bfqiz"
uvicorn app:app --reload
```

Server runs at:

```id="q5ap7j"
http://127.0.0.1:8000
```

---

### 5️⃣ Launch Frontend

* Open `index.html` in browser
* OR use Live Server in VS Code

---

## 🧪 API Documentation

### Endpoint

```id="vy9x7o"
POST /analyze
```

### Sample Request

```id="06o11t"
{
  "symptoms": "fever and headache"
}
```

### Sample Response

```id="zq1l4r"
{
  "conditions": ["Common Cold", "Viral Infection"],
  "severity": "Medium",
  "recommendations": [
    "Stay hydrated",
    "Take rest"
  ],
  "doctor_visit": "If symptoms worsen or persist beyond 3 days",
  "disclaimer": "This is not a medical diagnosis"
}
```

---

## 🎯 Design Decisions

* ✔️ **Structured JSON output** → improves readability & evaluation
* ✔️ **Low temperature (0.3)** → ensures consistent responses
* ✔️ **Regex-based JSON extraction** → handles imperfect LLM outputs
* ✔️ **Minimal dependencies** → lightweight & efficient project
* ✔️ **Separation of concerns** → clean frontend/backend architecture

---

## ⚠️ Disclaimer

This application is intended for **educational purposes only** and does not provide medical advice, diagnosis, or treatment.
Always consult a qualified healthcare professional for medical concerns.

---

## 🎥 Demo Video

👉 *[Add your demo video link here]*

---

## 🌟 Highlights

* Real-world AI application use case
* End-to-end system (UI + API + LLM)
* Clean code structure & modular design
* Professional UI/UX presentation
* Production-style output formatting

---

## 🚀 Future Enhancements

* 📊 Symptom severity scoring algorithm
* 🗂️ User history & tracking
* 🌍 Multi-language support
* ☁️ Cloud deployment (Render / Vercel / AWS)
* 📱 Mobile-friendly UI improvements
