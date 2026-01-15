FROM python:3.13-slim-bullseye

EXPOSE 8000

WORKDIR /app
COPY . ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--port", "8000", "--host", "0.0.0.0"]
