FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11-slim

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY ./app /app/app
