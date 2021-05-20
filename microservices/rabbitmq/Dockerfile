FROM python:3.9

RUN mkdir -p /reg
WORKDIR /reg

COPY ./src /reg
RUN pip3 install --no-cache-dir -r /reg/requirements.txt
RUN ["chmod", "+x", "/reg/wait-for-it.sh"]
