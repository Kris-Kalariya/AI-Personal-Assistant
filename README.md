# 🤖 AI Chat Assistant (Flask + OpenAI)

A smart AI-powered personal assistant web application built using **Flask** and **OpenAI API**.  
This project allows users to interact with an AI chatbot in real-time through a clean and responsive web interface.

---

## 🚀 Features

- 💬 Real-time AI chat interaction
- ⚡ Fast Flask backend
- 🎨 Clean and responsive UI
- 🔐 Secure API key handling using `.env`
- 📦 Easy to deploy and extend
- 🧠 Uses OpenAI for intelligent responses

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS
- **Backend:** Flask (Python)
- **AI Engine:** OpenAI API
- **Environment Management:** python-dotenv

---

## 📁 Project Structure
```
AI-Assistant/
│
├── app/
│ ├── init.py
│ ├── routes.py
│ ├── openai_service.py
│
├── static/
│ ├── style.css
│
├── templates/
│ ├── index.html
│
├── .env
├── .gitignore
├── requirements.txt
├── run.py
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/AI-Assistant.git
cd AI-Assistant
```

2️⃣ Create Virtual Environment
```
python -m venv venv
venv\Scripts\activate   # Windows
```

3️⃣ Install Dependencies
```
pip install -r requirements.txt
```

4️⃣ Setup Environment Variables
Create .env file:
```
OPENAI_API_KEY=your_api_key_here
```

▶️ Run the Application
```
python run.py
```

Then open:
```
http://127.0.0.1:5000
```

📸 UI Preview
- Clean chat interface
- Light modern design
- User-friendly interaction

🧑‍💻 Author
- Kris Kalariya
- GitHub: https://github.com/Kris-Kalariya

⭐ Contribution
- Feel free to fork this repo and improve it!

📜 License
- This project is open-source and available under the MIT License.
---

# ✅ 6. GitHub Push Commands
```bash
git init
git add .
git commit -m "Initial commit - AI Assistant project"
git branch -M main
git remote add origin https://github.com/your-username/AI-Assistant.git
git push -u origin main
```
