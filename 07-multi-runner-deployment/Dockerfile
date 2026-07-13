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

RUN groupadd \
      --system \
      --gid 10001 \
      appgroup \
    && useradd \
      --system \
      --uid 10001 \
      --gid appgroup \
      --home-dir /app \
      --shell /usr/sbin/nologin \
      appuser

COPY --from=builder /install /usr/local

COPY --chown=10001:10001 . .

USER 10001:10001

EXPOSE 5000

CMD ["python", "app/app.py"]
