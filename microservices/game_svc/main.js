const WebSocket = require('ws');
const port = process.env.PORT_INSIDE || 8083
const wss = new WebSocket.Server({port: port});

const eureka = require('./ms/eureka')
const rabbit = require('./ms/rabbit')

const GameBank = new (require('./GameBank'))()
const MessageHandler = new (require('./MessageHandler'))
let globals = require('./Globals')

globals.gb = GameBank

console.log(`Started server on port ${port}`);

const motds = [
    'Apple a day keeps the doctor away.',
    'Docker ain\'t that bad, except the memory consumption.',
    'Dota2 > LoL',
    'No message today...',
    'After 3 years, I finally made online connect five.',
    'God damned CORS man, so annoying.'
]

wss.on('connection', function connection(ws) {
    let context = {
        lobby: null,
        socket: ws,
        state: 'lobbies',
        id: null,
        _close() {
            this.socket.close();
            if (this.id !== null) {
                delete globals.gb.users[this.id]
            }
            if (this.lobby !== null) {
                this.lobby.disconnect(this)
            }
        }
    }

    ws.on('message', (message) => {
        try {
            const data = JSON.parse(message)
            MessageHandler.handle(data, ws, context)
        } catch (Error) {
            console.log(Error);
            this.close()
        }
    });
    ws.on('close', () => {
        console.log('rip close', context.id);
        context._close()
    })
    ws.on('error', () => {
        console.log('rip error', context.id);
        context._close()
    })

    ws.send(JSON.stringify({code: 'motd', payload: motds[Math.floor(Math.random()*motds.length)]}));
});

eureka.start(()=>{
    console.log('Connected to eureka!');
    connectToRabbit(eureka)
})

function connectToRabbit(eureka) {
    console.log('Connecting to rabbitMq...');
    let instances = eureka.getInstancesByAppId('rabbitmq')
    if (instances.length > 0) {
        const address = 'amqp://' + instances[0].hostName + ':' + instances[0].port['$'];
        rabbit.connect(address)
            .then(() => {
                console.log('Connected to rabbitMq');
            })
            .catch((err) => {
                console.error('Error when connecting to rabbitMQ:', err);
            })
    }
    else {
        console.log('No rabbit is registered in eureka, retrying in 10 seconds');
        setTimeout(()=>{connectToRabbit(eureka)}, 10000)
    }
}
