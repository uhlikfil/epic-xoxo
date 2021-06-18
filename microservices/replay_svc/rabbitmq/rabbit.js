const amqp = require('amqplib')

const queue = 'finished_games_replays'

class Rabbit {
    channel;

    constructor() {

    }

    async startReceiving(lambda) {
        if (this.channel) {
            const msg = await this.channel.consume(queue, (msg) => {
                if (msg != null) {
                    try {
                        lambda(msg.content.toString())
                        this.channel.ack(msg)
                    } catch (err) {
                        console.error('Message from rabbitMQ cannot be parsed!');
                    }
                }
            });
        }
        else {
            throw new Error('Channel is not established! Use the connect method first!')
        }
    }

    async send(msg) {
        if (this.channel) {
            this.channel.sendToQueue(queue, Buffer.from(msg))
        }
        else {
            throw new Error('Channel is not established! Use the connect method first!')
        }
    }

    async connect(address) {
        // if (!process.env.RABBIT_URL) {throw new Error('Please set the RABBIT_URL environmental variable!')}
        {
            const conn = await amqp.connect(address);
            const ch = await conn.createChannel();
            await ch.assertQueue(queue)
            this.channel = ch;
        }
    }
}

module.exports = new Rabbit()
