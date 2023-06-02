FROM python:3.11-alpine

ENV PYTHONUNBUFFERED=1
WORKDIR /backend

RUN pip install --upgrade pip
COPY requirements.txt ./ 
RUN pip install -r requirements.txt

COPY . ./   

EXPOSE 8000