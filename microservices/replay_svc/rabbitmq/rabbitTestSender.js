const rabbit = require('./rabbit')

rabbit.connect('amqp://localhost:5555').then(() => {
    sendStuff()
});

const names = ['asd', 'dsfnajsidas', 'mates', 'filip', 'ondra', 'david', 'petr', 'jonas', 'theodore', 'sadnauid', 'your mom']

function randomName(except = -1) {
    let rnd = except;
    while (except === rnd) {
        rnd = Math.floor(Math.random() * names.length);
    }
    return [rnd, names[rnd]];
}

function sendStuff() {
    setTimeout(() => {
        let [idx, plr1] = randomName();
        let [, plr2] = randomName(idx)
        let winner = Math.random() > 0.5 ? plr1 : plr2
        let starter = Math.random() > 0.5 ? plr1 : plr2
        let completed = Math.random() < 0.95
        const replay = {
            "date": new Date().toISOString(),
            "player1Id": plr1,
            "player2Id": plr2,
            "winnerId": winner,
            "completed": completed,
            "startingId": starter,
            "rounds": Math.floor(Math.random() * 60),
            "plays": [
                [
                    0,
                    0
                ],
                [
                    0,
                    0
                ]
            ]
        }

        rabbit.send(JSON.stringify(replay))
        console.log('sent msg');
        sendStuff()
    }, Math.floor(500 + Math.random() * 1000))
}
