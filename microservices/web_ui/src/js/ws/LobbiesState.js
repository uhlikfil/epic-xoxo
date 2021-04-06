import {State} from "@/js/ws/State";
import Vue from 'vue'
import store from '@/store/index'
import ModalOk from "@/components/modals/ModalOk";
import ModalInput from "@/components/modals/ModalInput";
import {LobbyState} from "@/js/ws/LobbyState";
import {Replica} from "@/js/Replica";

export class LobbiesState extends State {
    constructor(context) {
        super(context);
    }

    onOpen(e,soc) {
        store.state.root.modal.forceAccept()
        store.state.root.modal.show(ModalInput,
            {header: 'Choose your nickname', prompt: 'nickname', resolve: 'Accept', reject: 'Back'},
            (name) => {soc.send(JSON.stringify({code: 'nick', payload: name}))},
            () => {
                store.state.root.modal.hide();
                store.state.root.$router.push('/');
                store.state.ws.close();
            }
        )
    }

    onMessage(e, ctx) {
        let json = JSON.parse(e.data)
        if (json.code == 'motd') {
            store.commit('setMessageOfTheDay', json.payload)
        }
        else if (json.code == 'lobbies') {
            store.commit('setLobbies', json.payload)
        }
        else if (json.code == 'hosted') {
            store.state.root.modal.hide()
            store.state.onlineScreen = 1
            this.context.state = new LobbyState(this.context)
            /**             * @type {Replica}             */
            let replica = new Replica()
            replica.isHost = true
            replica.plr1.name = store.state.nick;
            replica.startingPlr = 'Player 1'

            Vue.set(store.state, 'replica', replica)
        }
        else if (json.code == 'joined') {
            store.state.root.modal.hide()
            store.state.onlineScreen = 1
            this.context.state = new LobbyState(this.context)

            /**             * @type {Replica}             */
            let replica = new Replica()
            replica.plr1.name = json.payload.plr1Name
            replica.plr2.name = json.payload.plr2Name
            replica.startingPlr = json.payload.startingPlr

            Vue.set(store.state, 'replica', replica)
        }
        else if (json.code == 'regsucc') {
            store.state.nick = json.payload
            this.context.refreshLobbies()
        }
    }

    onError(e) {
        super.onError(e);
    }
}
