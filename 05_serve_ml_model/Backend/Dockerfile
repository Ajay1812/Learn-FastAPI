# Backend/Dockerfile
FROM python:3.11-slim

WORKDIR /Backend

COPY Backend/ /Backend
RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
