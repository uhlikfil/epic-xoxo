let assert = require('assert');
const ServerGame = require('./../ServerGame')

describe('Game', function () {
    let game = new ServerGame();

    beforeEach(() => {
        game = new ServerGame()
        game.initBoard()
        game.initStartingPlr()
        game.plr1 = 'a'
        game.plr2 = 'b'
    })

    it('should be winnable', function () {
        game.play(4, 2)
        game.play(5, 2)
        game.play(4, 3)
        game.play(5, 3)
        game.play(4, 4)
        game.play(5, 4)
        game.play(4, 5)
        game.play(5, 5)
        game.play(4, 6)

        assert.equal(game.winner, 'a');
    });

    it('should not be playable after win', function () {
        game.play(4, 2)
        game.play(5, 2)
        game.play(4, 3)
        game.play(5, 3)
        game.play(4, 4)
        game.play(5, 4)
        game.play(4, 5)
        game.play(5, 5)
        game.play(4, 6)

        let playsN = game.plays.length
        game.play(1, 1)
        assert.equal(game.plays.length, playsN)
    });

    it('should not allow to play over a symbol', () => {
        game.play(4, 3)
        game.play(4, 3)
        assert.equal(game.plays.length, 1)
    })

    it('reset resets all game variables', () => {
        game.play(5,2)
        game.play(6,2)
        game.play(5,3)
        game.play(6,3)
        game.play(5, 4)
        game.play(6, 4)
        game.play(5, 5)
        game.play(6, 5)
        game.play(5, 6)

        assert.notEqual(game.rounds, 0)
        assert.notEqual(game.plays.length, 0)

        game.reset()

        assert.equal(game.rounds, 0)
        assert.equal(game.plays.length, 0)
        assert.equal(game.winner, null)
    })
});
