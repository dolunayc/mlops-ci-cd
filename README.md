# CI/CD Pipeline for FastAPI Service

This project implements a complete CI/CD pipeline for a FastAPI-based backend service using GitHub Actions.

The pipeline automatically runs tests, checks code quality, builds a Docker image, runs the container, and performs a smoke test on every push to the main branch.

---

## Project Overview

The application is a simple FastAPI service with two endpoints:

- Health check endpoint
- Prediction endpoint using a deterministic hashing function

The main goal of this project is to demonstrate a real-world CI/CD workflow following DevOps best practices.

---

## Endpoints

### Health Check
GET /health

Response:
{"status": "ok"}

### Prediction
POST /predict

Request:
{"user_id": "user123"}

Response:
{"user_id": "user123", "bucket": 42}

---

## CI/CD Pipeline

The pipeline is implemented using GitHub Actions and runs automatically on every push to the main branch.

Pipeline stages:

1. Install dependencies
2. Run unit tests
3. Run lint checks
4. Build Docker image
5. Run Docker container
6. Perform smoke test on /health endpoint
7. Stop container

A stop-the-line mechanism is implemented to prevent faulty code from being deployed.

---

## Running Locally

Create virtual environment:
python3 -m venv .venv  
source .venv/bin/activate  

Install dependencies:
pip install -r requirements.txt  
pip install -r requirements-dev.txt  

Run tests:
pytest  
flake8 app.py tests  

Run service:
uvicorn app:app --reload --port 8000  

---

## Docker

Build image:
docker build -t mlops-service .

Run container:
docker run -p 8000:8000 mlops-service

Test:
curl http://127.0.0.1:8000/health

---

## Technologies

- Python 3
- FastAPI
- Pytest
- Flake8
- Docker
- GitHub Actions

---

## Repository

https://github.com/dolunayc/mlops-ci-cd

---

## Author

Dolunay Çimen
