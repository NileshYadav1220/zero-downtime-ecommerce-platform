# 🚀 Zero-Downtime E-Commerce Deployment Platform

A production-style DevOps project demonstrating containerization,
CI/CD, Kubernetes deployment, zero-downtime releases,
health checks, monitoring and infrastructure automation.

## Architecture

Developer
    ↓
GitHub
    ↓
Jenkins CI/CD
    ↓
Docker Image
    ↓
Container Registry
    ↓
Kubernetes
    ↓
Ingress
    ↓
E-Commerce Application

## Current Stack

- Python Flask
- Nginx
- Docker
- Docker Compose
- Git/GitHub

## Application

Frontend:
http://localhost:8080

Backend:
http://localhost:5001

Health Check:
http://localhost:5001/health

Products API:
http://localhost:5001/api/products

## Run Locally

```bash
docker compose up --build -d
