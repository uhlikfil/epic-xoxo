const replaysZ = '/replays'
const highscoresZ = '/high_scores'
const usersZ = '/users'

const replaysS = '/api/v3'
const highscoresS = '/api/v1';
const userS = '/api/v1';

class GatewayClass {
    _root;
    replays;
    highscores;
    users;

    constructor() {
        this._root = process.env.VUE_APP_GATEWAY_ADDR;

        if (!process.env.VUE_APP_OVERRIDE_REPLAY_SERVICE) this.replays = this._root + replaysZ;
        else this.replays = process.env.VUE_APP_OVERRIDE_REPLAY_SERVICE;
        this.replays += replaysS

        if (!process.env.VUE_APP_OVERRIDE_USER_SERVICE) this.users = this._root + usersZ;
        else this.users = process.env.VUE_APP_OVERRIDE_USER_SERVICE;
        this.users += userS

        if (!process.env.VUE_APP_OVERRIDE_HIGHSCORE_SERVICE) this.highscores = this._root + highscoresZ;
        else this.highscores = process.env.VUE_APP_OVERRIDE_HIGHSCORE_SERVICE;
        this.highscores += highscoresS
    }
}

const Gateway = new GatewayClass();
export {Gateway};
