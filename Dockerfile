# Dockerfile

# 1. ใช้ Python base image
FROM python:3.11-slim

# 2. ตั้งค่า Environment Variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. ตั้งค่า work directory ภายใน container
WORKDIR /app

# 4. คัดลอกและติดตั้ง dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. คัดลอกโค้ดโปรเจกต์ทั้งหมดเข้าไปใน container
COPY . .