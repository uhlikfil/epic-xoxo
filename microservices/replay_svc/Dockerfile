FROM node:15.14.0-alpine
RUN apk update && apk add bash
WORKDIR /usr/app
COPY package.json .
RUN npm install
