# Frontend/frontend.Dockerfile
FROM python:3.11-slim

WORKDIR /Frontend

COPY Frontend/ /Frontend

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "frontend.py", "--server.port=8501", "--server.address=0.0.0.0"]
