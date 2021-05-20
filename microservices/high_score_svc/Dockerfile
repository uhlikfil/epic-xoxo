FROM python:3.9

RUN mkdir -p /app
WORKDIR /app

COPY ./src /app
RUN pip3 install --no-cache-dir -r /app/requirements.txt
