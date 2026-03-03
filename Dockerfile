FROM python:3.12-slim
WORKDIR /app
COPY . .
USER 65534:65534
ENV PYTHONDONTWRITEBYTECODE=1
CMD ["python", "scripts/demo.py"]
