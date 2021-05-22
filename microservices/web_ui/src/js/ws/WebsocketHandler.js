import {LobbiesState} from "@/js/ws/LobbiesState";

export class WebsocketHandler {
    constructor(hostname, port) {
        this.socket = new WebSocket(`ws://${hostname}:${port}`)
        this.state = new LobbiesState(this)

        this.socket.addEventListener('close', (msg) =>{this.state.onClose(msg, this.socket)})
        this.socket.addEventListener('error', (msg) =>{this.state.onError(msg, this.socket)})
        this.socket.addEventListener('message', (msg) =>{this.state.onMessage(msg, this.socket)})
        this.socket.addEventListener('open', (msg) =>{this.state.onOpen(msg, this.socket)})

        // always debug
        this.socket.addEventListener('message', (msg) => {
            console.log(JSON.parse(msg.data));
        })
    }

    debug() {
        this.socket.send(JSON.stringify({code: 'debug'}))
    }

    host(name) {
        this.socket.send(JSON.stringify({code: 'host', payload: name}))
    }

    refreshLobbies() {
        this.socket.send(JSON.stringify({code: 'lobbies'}))
    }

    swapStartingPlayer() {
        this.socket.send(JSON.stringify({code: 'swapStartingPlayer'}))
    }

    disconnectFromLobby() {
        this.socket.send(JSON.stringify({code: 'disconnect'}))
        this.state = new LobbiesState(this)
    }

    startLobby() {
        this.socket.send(JSON.stringify({code: 'start'}))
    }

    clickField(x,y) {
        this.socket.send(JSON.stringify({code: 'play', payload: {x,y}}))
    }

    connectToLobby(lobby) {
        this.socket.send(JSON.stringify({code: 'connect', payload: lobby}))
    }

    surrender() {
        this.socket.send(JSON.stringify({code: 'surrender'}))
    }

    rematch() {
        this.socket.send(JSON.stringify({code: 'rematch'}))
    }

    close() {
        this.socket.close()
    }
}
