FROM python:3.9-alpine

RUN mkdir -p /tests
WORKDIR /tests

COPY ./requirements.txt /tests/requirements.txt
RUN pip3 install --no-cache-dir -r /tests/requirements.txt
COPY ./high_score_svc_tests /tests
RUN ["chmod", "+x", "/tests/wait-for-it.sh"]
