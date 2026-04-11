This project is a lightweight **Server Health Monitoring API** built using Flask.  
It provides real-time system metrics like CPU, memory, and disk usage.

This project is designed as a **DevOps practice application** to demonstrate:
- API development
- Cloud deployment (AWS EC2)
- Version control (GitHub)
- Future containerization & CI/CD

🧠 Architecture

Client (Browser / curl)
        ↓
Flask API (EC2 Server)
        ↓
System Metrics (psutil)

⚙️ Tech Stack

- Python 🐍
- Flask 🌐
- psutil 📊
- AWS EC2 ☁️
- Git & GitHub 🔧

## 📡 API Endpoints

### 🔹 Health Check

Your Public Ip Address :5000/health

Response:
```json
{
  "status": "OK"
}
🔹 System Metrics

Your Public Ip Address :5000/metrics

Response:

{
  "cpu_usage": 12.5,
  "memory_usage": 45.2,
  "disk_usage": 60.1
}
