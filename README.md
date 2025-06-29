# 🌐 CitizenAI: AI-Powered Citizen Engagement Platform

🎥 **[Watch Demo Video](https://drive.google.com/file/d/1nVB1lq9imblp9PeRAi2ruO74_RdzIUR4/view)**

CitizenAI is a web-based AI platform designed to improve citizen engagement by offering an intelligent chatbot, sentiment analysis, issue reporting, and interactive dashboards. It uses **IBM Granite (Generative AI model)** to understand citizen concerns, provide empathetic responses, and generate insights for better governance.

---

## 🛠️ Features

- 🤖 **AI Chatbot**: Understands and responds to citizen queries using IBM Granite model.
- 📊 **Sentiment Analysis**: Classifies citizen feedback as Positive, Negative, or Neutral.
- 📋 **Concern Reporting**: Users can report civic issues with category and description.
- 📈 **Admin Dashboard**: Visualizes reported issues and sentiment trends using dynamic charts.
- 🔐 **Login System**: Basic user login functionality (extendable for role-based access).
- 🧠 **Generative Model Integration**: Real-time integration with IBM Granite via Hugging Face.

---

## 📽️ Demo

📌 [Click here to watch the demo](https://drive.google.com/file/d/1nVB1lq9imblp9PeRAi2ruO74_RdzIUR4/view)

---

## 📂 Project Structure

CitizenAI/


│
├── app.py # Flask app entry point


├── templates/ # HTML templates (Jinja2)


│ ├── index.html


│ ├── login.html


│ ├── chat.html


│ ├── sentiment.html


│ ├── report.html


│ └── dashboard.html


├── static/ # Static assets (CSS, JS)


│ └── style.css


├── ai_model/


│ └── granite_model.py # IBM Granite integration


├── utils/


│ └── sentiment.py # Sentiment classification logic


├── requirements.txt


└── README.md

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip
- Internet connection for model APIs

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/CitizenAI.git
cd CitizenAI

pip install -r requirements.txt

python app.py

Open your browser and visit: http://127.0.0.1:5000


🧪 Tech Stack
Backend: Flask (Python)

Frontend: HTML5, CSS3, Bootstrap

AI Model: IBM Granite via Hugging Face Transformers

Visualization: Chart.js, Altair (optional)

Sentiment Analysis: Rule-based or ML classifier (TextBlob, Custom logic)

Deployment: Localhost (optionally deployable on Render/Heroku)

📌 Future Scope
Role-based authentication (citizens, admins)

Multilingual support for chatbot

Real-time database (e.g., Firebase, MongoDB)

Geo-tagging for reports

Notification system for updates

👨‍💻 Author
Gowtham Majjiga
📧 majjigagowtham21@gmail.com
