FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV PORT=8000
EXPOSE 8000

CMD python -u main.py

