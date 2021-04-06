import Vue from 'vue'
import Vuex from 'vuex'
import {Replica} from "@/js/Replica";

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        ws: null,
        root: null,
        onlineScreen: 0,
        replica: new Replica(),
        messageOfTheDay: '',
        lobbies: [],
        nick: null,
    },
    mutations: {
        setLobbies(state, payload) {
            Vue.set(state, 'lobbies', payload);
        },
        setMessageOfTheDay(state, payload) {
            state.messageOfTheDay = payload
        },
        setWs(state, payload) {
            state.ws = payload
            window.ws = payload
        },
        setRoot(state, payload) {
            state.root = payload
        },
        setOnlineScreen(state, payload) {
            state.onlineScreen = payload
        }
    },
    actions: {
        showModal(context, {modal, props, acceptFn, rejectFn}) {
            console.log('context', context);
            context.state.root.modal.show(modal, props, acceptFn, rejectFn)
        }
    }
    ,
    modules: {}
})
