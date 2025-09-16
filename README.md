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

---

## Installation
```bash
git clone https://github.com/Tannsxerd/DooKluay.git
cd DooKluay
cp .env.example .env   # แก้ค่าใน .env ให้ถูกต้อง
docker compose -f docker-compose.dev.yml up --build
```

---

## Development commands ที่ใช้บ่อย

รันแบบฉากหลัง:  
```bash
docker compose -f docker-compose.dev.yml up -d --build
```

ดูสถานะคอนเทนเนอร์:  
```bash
docker compose -f docker-compose.dev.yml ps
```

ดู logs ทั้งหมด:  
```bash
docker compose -f docker-compose.dev.yml logs -f
```

หยุดบริการ:  
```bash
docker compose -f docker-compose.dev.yml stop
```

ปิดและลบคอนเทนเนอร์:  
```bash
docker compose -f docker-compose.dev.yml down
```

---

## Cleanup / Reset (เคลียร์ให้เกลี้ยง)

ปิดและลบคอนเทนเนอร์ + ลบ volumes ทั้งหมด (รวมฐานข้อมูลและไฟล์ถาวรที่ผูกกับ volume):  
```bash
docker compose -f docker-compose.dev.yml down -v
```

ลบ image/containers/cache ที่ไม่ใช้งาน:  
```bash
docker system prune -f
```

ลบอิมเมจที่ dangling:  
```bash
docker image prune -f
```

ลบ volumes ที่ไม่ได้ใช้งานทั้งหมด:  
```bash
docker volume prune -f
```

ถ้ารู้ชื่อ volume และอยากลบเฉพาะอัน:  
```bash
docker volume ls
docker volume rm <VOLUME_NAME>
```

สร้างใหม่หลังเคลียร์:  
```bash
docker compose -f docker-compose.dev.yml up -d --build
```

---

## Tech Stack
- Backend: Python (Django)
- Model: TensorFlow
- Deploy: Docker
