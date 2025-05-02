
FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
ENV PYTHONPATH=/app

CMD ["python", "app/main.py"]