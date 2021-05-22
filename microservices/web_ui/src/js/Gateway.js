class GatewayClass {
    constructor() {
        this.replays = process.env.VUE_APP_OVERRIDE_REPLAY_SERVICE ? process.env.VUE_APP_OVERRIDE_REPLAY_SERVICE : process.env.VUE_APP_GATEWAY_HOSTNAME
        if (process.env.VUE_APP_OVERRIDE_REPLAY_SERVICE) {
            this.replays = process.env.VUE_APP_OVERRIDE_REPLAY_SERVICE;
        }
        else {
            this.replays = process.env.VUE_APP_GATEWAY_ADDR || 'localhost:8090'
        }

        this.highscores = process.env.VUE_APP_OVERRIDE_HIGHSCORE_SERVICE ? process.env.VUE_APP_OVERRIDE_HIGHSCORE_SERVICE : process.env.VUE_APP_GATEWAY_HOSTNAME
        if (process.env.VUE_APP_OVERRIDE_HIGHSCORE_SERVICE) {
            this.highscores = process.env.VUE_APP_OVERRIDE_HIGHSCORE_SERVICE;
        }
        else {
            this.highscores = process.env.VUE_APP_GATEWAY_ADDR || 'localhost:8090'
        }

        this.users = process.env.VUE_APP_OVERRIDE_USER_SERVICE ? process.env.VUE_APP_OVERRIDE_USER_SERVICE : process.env.VUE_APP_GATEWAY_HOSTNAME
        if (process.env.VUE_APP_OVERRIDE_USER_SERVICE) {
            this.users = process.env.VUE_APP_OVERRIDE_USER_SERVICE;
        }
        else {
            this.users = process.env.VUE_APP_GATEWAY_ADDR || 'localhost:8090'
        }
    }
}

const Gateway = new GatewayClass();
export {Gateway};
