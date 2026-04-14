
# 🚀 Server Health Monitoring API

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-Lightweight-green)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📖 Project Overview

This project is a lightweight **Server Health Monitoring API** built using Flask.  
It provides real-time system metrics like CPU, memory, and disk usage.

This project is designed as a **DevOps practice application** to demonstrate:
- API development
- Cloud deployment (AWS EC2)
- Version control (GitHub)
- Future containerization & CI/CD

---

## 🧠 Architecture

Client (Browser / curl)
        ↓
Flask API (EC2 Server)
        ↓
System Metrics (psutil)

---

## ⚙️ Tech Stack

- Python 🐍
- Flask 🌐
- psutil 📊
- AWS EC2 ☁️
- Git & GitHub 🔧

---

## 📡 API Endpoints

### 🔹 Health Check

Response:

{
  "status": "OK"
}
   

### 🔹 GET /metrics

Response:

{
  "cpu_usage": 12.5,
  "memory_usage": 45.2,
  "disk_usage": 60.1
}


🚀 How to Run Locally

1️⃣ Clone repository
git clone https://github.com/YARAMASI-RAVI/Monitoring-app.git
cd Monitoring-app

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run application
python3 app.py

🌐 Access Application

http://<EC2-PUBLIC-IP>:5000/health
http://<EC2-PUBLIC-IP>:5000/metrics

🐳 Docker
docker build -t monitoring-app .
docker run -d -p 5000:5000 monitoring-app

📈 Future Enhancements

*Docker containerization
*Kubernetes deployment
*CI/CD pipeline using Jenkins
*Monitoring with Prometheus & Grafana
*Alerting system

🧑‍💻 Author

Yaramasi Ravi
DevOps Enthusiast 🚀

⭐ Support

If you like this project:

⭐ Star this repo
🍴 Fork it
🔧 Contribute

