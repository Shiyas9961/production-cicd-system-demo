FROM python:3.13-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --prefix=/install --no-cache-dir -r requirements.txt

FROM python:3.13-slim AS runtime

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 

RUN groupadd -r appgroup \
    && useradd -r -g appgroup -d /app -s /usr/sbin/nologin appuser

COPY --from=builder /install /usr/local

COPY --chown=appuser:appugroup . .

USER appuser

EXPOSE 5000

CMD ["python", "app/app.py"]