import {State} from "@/js/ws/State";
import store from "@/store";
import ModalOk from "@/components/modals/ModalOk";
import ModalYeaNah from "@/components/modals/ModalYeaNah";
import {LobbiesState} from "@/js/ws/LobbiesState";

export class LobbyState extends State {
    constructor(context) {
        super(context);
    }

    onOpen(e) {
        super.onOpen(e);
    }

    onClose(e) {
        super.onClose(e);
    }

    onMessage(e) {
        let json = JSON.parse(e.data)
        if (json.code == 'otherJoined') {
            store.state.replica.plr2.name = json.payload
        }
        else if (json.code == 'startingPlayer') {
            store.state.replica.startingPlr = json.payload
        }
        else if (json.code == 'started') {
            let {turn, localPlayerId} = json.payload
            store.state.replica.localPlayerId = localPlayerId
            store.state.replica.initBoard()
            store.state.onlineScreen = 2
            store.state.replica.turn = turn
            store.state.replica.round = 1
            store.state.replica.started = true
            store.state.replica.uiState = 1
            store.state.replica.waitingForRematch = false
        }
        else if (json.code == 'played') {
            let {x, y, plr, next} = json.payload
            store.state.replica.mark(x, y, plr)
            store.state.replica.turn = next
            store.state.replica.round = store.state.replica.round + 1
        }
        else if (json.code == 'winner') {
            store.state.replica.canRematch = true
            store.state.replica.winner = json.payload
            store.state.replica.uiState = 2
        }
        else if (json.code == 'highlight') {
            store.state.replica.highlight = json.payload
        }
        else if (json.code == 'otherLeft') {
            store.state.replica.plr2.name = ''
        }
        else if (json.code == 'hostLeft') {
            store.state.onlineScreen = 0
            store.state.ws.refreshLobbies()
            this.context.state = new LobbiesState(this.context)
            store.state.root.modal.show(ModalOk, {header: 'Disconnected', msg: 'Host has left the lobby!'})
        }
        else if (json.code == 'ingameLeft') {
            store.state.replica.canRematch = false
            store.state.root.modal.show(ModalYeaNah, {header: 'Opponent has left', msg: 'Review the battlefield?', resolve: 'Yea', reject: 'Nah'},
                () => {store.state.replica.uiState = 3},
                () => {store.state.onlineScreen = 0; store.state.ws.disconnectFromLobby()}
            )
            store.state.replica.winner = store.state.replica.localPlayerId
        }
        else if (json.code == 'rematch') {
            if (store.state.replica.waitingForRematch) {}
            else {
                let resolve = store.state.replica.winner == store.state.replica.localPlayerId ? 'Ez win again' : 'I will win this time'
                let reject = store.state.replica.winner == store.state.replica.localPlayerId ? 'No time to deal with trash' : 'Ragequit'
                store.state.root.modal.show(ModalYeaNah, {header: 'Rematch?', msg: 'Opponent has asked for a rematch.', resolve, reject},
                    () => {store.state.ws.rematch()},
                    () => {store.state.ws.disconnect(); store.state.onlineScreen = 0}
                )
            }
        }
    }

    onError(e) {
        super.onError(e);
    }
}
