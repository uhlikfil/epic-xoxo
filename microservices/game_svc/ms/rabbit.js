const amqp = require('amqplib')

const queueReplays = 'finished_games_replays'
const queueHighScores = 'finished_games_high_score'

class Rabbit {
    channel;

    constructor() {

    }

    async sendGameResults(game) {
        if (this.channel) {
            let replay = {
                date: new Date().toISOString(),
                player1Id: game.plr1.id,
                player2Id: game.plr2.id,
                winnerId: game.winner.id,
                completed: game.completed,
                startingId: game.startingId,
                rounds: game.rounds,
                plays: game.plays
            }
            let highscore = {
                player1: game.plr1.id,
                player2: game.plr2.id,
                p1winner: game.winner == game.plr1 ? true : false,
                completed: game.completed
            }

            console.log(replay);
            console.log(highscore);

            this.channel.sendToQueue(queueReplays, Buffer.from(JSON.stringify(replay)))
            this.channel.sendToQueue(queueHighScores, Buffer.from(JSON.stringify(highscore)))
        }
        else {
            throw new Error('Channel is not established! Use the connect method first!')
        }
    }

    async connect(address) {
        const conn = await amqp.connect(address);
        const ch = await conn.createChannel();
        await ch.assertQueue(queueReplays)
        await ch.assertQueue(queueHighScores)
        this.channel = ch;
    }


    // async startReceiving(lambda) {
    //     if (this.channel) {
    //         const msg = await this.channel.consume(queue, (msg) => {
    //             if (msg != null) {
    //                 try {
    //                     lambda(msg.content.toString())
    //                     this.channel.ack(msg)
    //                 } catch (err) {
    //                     console.error('Message from rabbitMQ cannot be parsed!');
    //                 }
    //             }
    //         });
    //     }
    //     else {
    //         throw new Error('Channel is not established! Use the connect method first!')
    //     }
    // }
}

module.exports = new Rabbit()
