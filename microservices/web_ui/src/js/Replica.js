import {Player} from "@/js/Player";

export class Replica {
    isHost = false
    plr1 = null;
    plr2 = null;
    width = 15;
    height = 15;
    board = [];
    turn = 0; // current player id
    round = 0;
    started = false;
    startingPlr = null;
    winner = null;
    uiState = 0 // 0 = not started, 1 = in game, 2 = game ended, 3 = forever alone
    localPlayerId = null
    highlight = {}

    waitingForRematch = false;
    canRematch = false;

    constructor() {
        this.plr1 = new Player()
        this.plr1.color = 'black';
        this.plr1.symbol = 'X';
        this.plr1.name = null;
        this.plr2 = new Player()
        this.plr2.color = 'black';
        this.plr2.symbol = 'O';
        this.plr2.name = null;
    }

    initBoard() {
        this.round = 0
        this.winner = null
        this.board = []
        if (this.width < 5) this.width = 5;
        if (this.height < 5) this.height = 5;
        for (let i = 0; i < this.width; i++) {
            this.board[i] = []
            for (let j = 0; j < this.height; j++) {
                this.board[i][j] = 0;
            }
        }
    }

    mark(x, y, plr) {
        this.board[y][x] = plr;
    }
}
