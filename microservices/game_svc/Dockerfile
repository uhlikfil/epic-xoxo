FROM node:15.14.0-alpine
WORKDIR /usr/app
COPY ["package.json", "package-lock.json*", "./"]
RUN npm install
COPY . .