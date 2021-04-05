FROM python:3.9

RUN mkdir -p /app
WORKDIR /app

COPY ./src/requirements.txt /app/
RUN pip3 install --no-cache-dir -r /app/requirements.txt
COPY ./src /app
