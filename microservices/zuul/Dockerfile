FROM maven:3.8.1-jdk-8 AS build
COPY app /app
WORKDIR /app
RUN mvn clean package

FROM openjdk:8-alpine
COPY --from=build /app/target/zuul-1.jar /app/zuul-1.jar 
