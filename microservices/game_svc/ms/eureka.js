// Or, if you're not using a transpiler:
const Eureka = require('eureka-js-client').Eureka;

const eureka_host = process.env.EUREKA_HOSTNAME || 'localhost';
const eureka_port = process.env.EUREKA_PORT || 8761;
const service_name = process.env.SERVICE_NAME || 'game_service'
const service_hostName = process.env.SERVICE_HOSTNAME || 'localhost'
const service_port = process.env.SERVICE_PORT || process.env.ENDPOINT_PORT || 8081

// example configuration
const client = new Eureka({
    // application instance information
    instance: {
        instanceId: '127.0.0.1:aaa:8090',
        homePageUrl: 'http://localhost:8090/',
        app: 'aaasd',
        hostName: service_hostName,
        ipAddr: '127.0.0.1',
        port: {
            '$': service_port,
            '@enabled': 'true',
        },
        vipAddress: 'jq.test.something.com',
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
client.start(()=>{
    console.log(client.getInstancesByAppId('USER_SVC'))
    console.log(client.getInstancesByAppId('aaasd'))
})

module.exports = client;
