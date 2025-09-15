# DooKluay 🍌

โปรเจ็คตรวจโรคใบกล้วยจากภาพถ่ายด้วย Machine Learning / Deep Learning  
อัปโหลดภาพ → ระบบทำนายโรคและให้คำแนะนำเบื้องต้น

---

## Features
- ตรวจโรคใบกล้วยจากภาพ
- API + เว็บอินเตอร์เฟซ
- รองรับ Docker

---

## Project Structure
```
DooKluay/
├── banana_api/      # API
├── DooKluayWeb/     # Configuration
├── docker-compose.dev.yml
├── requirements.txt
└── manage.py
```

## Installation
```bash
git clone https://github.com/Tannsxerd/DooKluay.git
cd DooKluay
cp .env.example .env # Edit .env and update configuration values
docker-compose -f docker-compose.dev.yml up --build
```



## Tech Stack
- Backend: Python (Django)
- Model: TensorFlow 
- Deploy: Docker

---
