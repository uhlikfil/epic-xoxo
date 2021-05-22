'use strict';

let path = require('path');
let http = require('http');
const rabbit = require('./rabbitmq/rabbit')
const service = require('./service/ReplayService')
const cors = require('cors');

let oas3Tools = require('oas3-tools');
const express = require("express");
let serverPort = process.env.ENDPOINT_PORT || 8081;

// swaggerRouter configuration
let options = {
    routing: {
        controllers: path.join(__dirname, './controllers'),
    },
};

let expressAppConfig = oas3Tools.expressAppConfig(path.join(__dirname, 'api/openapi.yaml'), options);
let oas_app = expressAppConfig.getApp();
const app = express();
app.use(cors());
app.options('*', cors())

for (let i = 2; i < oas_app._router.stack.length; i++) {
    app._router.stack.push(oas_app._router.stack[i])
}

// Initialize the Swagger middleware
http.createServer(app).listen(serverPort, function () {
    console.log('Your server is listening on port %d (http://localhost:%d)', serverPort, serverPort);
    console.log('Swagger-ui is available on http://localhost:%d/docs', serverPort);

    const eureka = require('./eureka/eureka');
    eureka.start((error, stuff) => {
        if (error) {console.log('Error registering with eureka:', error);}
        else {
            console.log('Successfully connected to Eureka!');
            console.log(eureka.getInstancesByAppId('GAME_SERVICE'));
        }
    })
    rabbit.connect()
        .then(() => {
            rabbit.startReceiving((msg) => {
                service.add_replay(JSON.parse(msg))
                    .then((data) => {console.log('Handled new rabbit message!')})
                    .catch((err) => {console.error(err);})
            })
        })
        .catch((err)=>{
            console.error('Error when connecting to rabbitMQ:',err);
        })
});

