// Or, if you're not using a transpiler:
const Eureka = require('eureka-js-client').Eureka;

const eureka_host = process.env.EUREKA_HOSTNAME || 'localhost';
const eureka_port = process.env.EUREKA_PORT || 8761;
const service_name = process.env.SERVICE_NAME || 'game_service'
const service_hostName = process.env.SERVICE_HOSTNAME || 'host.docker.internal'
const service_port = process.env.SERVICE_PORT || process.env.ENDPOINT_PORT || 8083

// example configuration
const client = new Eureka({
    instance: {
        id: service_name,
        instanceId: '127.0.0.1' + ':' + service_name + ':' + service_port,
        app: service_name,
        hostName: service_hostName,
        ipAddr: '127.0.0.1',
        homePageUrl: 'http://' + service_hostName + ':' + service_port + '/',
        statusPageUrl: 'http://' + service_hostName + ':' + service_port + '/info',
        healthCheckUrlPageUrl: 'http://' + service_hostName + ':' + service_port + '/health',
        port: {
            '$': service_port,
            '@enabled': 'true',
        },
        vipAddress: service_name,
        dataCenterInfo: {
            '@class': 'com.netflix.appinfo.InstanceInfo$DefaultDataCenterInfo',
            name: 'MyOwn',
        },
    },
    eureka: {
        // eureka server host / port
        host: eureka_host,
        port: eureka_port,
        servicePath: '/eureka/apps/'
    },
});

module.exports = client;
