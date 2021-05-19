'use strict';

let path = require('path');
let http = require('http');

let oas3Tools = require('oas3-tools');
let serverPort = process.env.ENDPOINT_PORT || 8081;

// swaggerRouter configuration
let options = {
    routing: {
        controllers: path.join(__dirname, './controllers')
    },
};

let expressAppConfig = oas3Tools.expressAppConfig(path.join(__dirname, 'api/openapi.yaml'), options);
let app = expressAppConfig.getApp();

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
});

