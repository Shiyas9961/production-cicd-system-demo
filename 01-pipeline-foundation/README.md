# Flask App with Docker & CI/CD

A simple Flask application containerized using Docker and automated with a GitHub Actions CI/CD pipeline.

---

## Features

- Flask web application
- Multi-stage Docker build
- Lightweight Docker image
- Runs as a non-root user
- GitHub Actions CI/CD pipeline
- Easy to deploy

---

## Project Structure

```text
.
├── app/
│   └── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .github/
│   └── workflows/
│       └── pipeline.yml
├── README.md
└── LICENSE
```

---

## Prerequisites

- Python 3.13+
- Docker
- Git

---

## Clone Repository

```bash
git clone https://github.com/<your-username>/<repository>.git
cd <repository>
```

---

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the Flask application:

```bash
python app/app.py
```

Open your browser:

```
http://localhost:5000
```

---

## Build Docker Image

```bash
docker build -t flask-app:latest .
```

---

## Run Docker Container

```bash
docker run -d \
  --name flask-app \
  -p 5000:5000 \
  flask-app:latest
```

Check running containers:

```bash
docker ps
```

---

## Stop Container

```bash
docker stop flask-app
docker rm flask-app
```

---

## CI/CD Pipeline

The GitHub Actions pipeline performs the following steps:

1. Checkout source code
2. Set up Python
3. Install dependencies
4. Build Docker image
5. Verify successful build

Workflow location:

```
.github/workflows/pipeline.yml
```

---

## Docker Security

This project follows Docker best practices:

- Multi-stage build
- Minimal `python:3.13-slim` base image
- Non-root application user
- No pip cache
- No unnecessary build tools in the final image

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.