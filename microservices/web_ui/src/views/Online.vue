<template>
  <div class="online">
    <LobbyList v-if="screen === 0"/>
    <OnlineSetup :replica="replica" v-if="screen === 1" @start="start" @swap="swap" @disconnect="disconnect"/>
    <div v-if="screen === 2">
      <Board @cell="clickCell" :game="replica" :highlights="replica.highlight"/>
      <div v-if="replica.uiState === 1">
        <button @click="promptDisconnect">Leave</button>
      </div>
      <div v-if="replica.uiState === 2">
        <button @click="promptDisconnect">Leave</button>
        <button :disabled="!replica.canRematch" @click="rematch">Rematch</button>
      </div>
      <div v-if="replica.uiState === 3">
        <button @click="disconnect">Leave</button>
      </div>
    </div>
  </div>
</template>

<script>
import LobbyList from "@/views/LobbyList";
import {WebsocketHandler} from "@/js/ws/WebsocketHandler";
import ModalOk from "@/components/modals/ModalOk";
import ModalProgress from "@/components/modals/ModalProgress";
import OnlineSetup from "@/views/OnlineSetup";
import Board from "@/components/Board";
import ModalYeaNah from "@/components/modals/ModalYeaNah";

export default {
  name: "Online",
  components: {Board, OnlineSetup, LobbyList},
  methods: {
    rematch() {
      if (this.$store.state.replica.canRematch) {
        this.$store.state.replica.waitingForRematch = true
        this.$store.state.replica.canRematch = false
        this.$store.state.ws.rematch()
      }
    },
    promptDisconnect() {
      this.$root.modal.show(ModalYeaNah, {header: 'Are u sure u want to leave?', resolve: 'ragequit', rejrect: 'not yet'},
          ()=>{this.disconnect()}
      )
    },
    promptSurrender() {
      this.$root.modal.show(ModalYeaNah, {header: 'Are u sure u want to leave?', resolve: 'ragequit', rejrect: 'not yet'},
          ()=>{this.$store.state.ws.surrender()}
      )
    },
    clickCell([x,y]) {
      if (this.replica.turn === this.replica.localPlayerId) {
        this.$store.state.ws.clickField(x, y)
      }
    },
    start() {
      this.$store.state.ws.startLobby()
    },
    swap() {
      this.$store.state.ws.swapStartingPlayer()
    },
    disconnect() {
      this.$store.state.ws.disconnectFromLobby()
      this.$store.state.onlineScreen = 0
    }
  },
  computed: {
    screen() {
      return this.$store.state.onlineScreen
    },
    replica() {
      return this.$store.state.replica
    }
  },
  created() {
    try {
      const hostname = process.env.VUE_APP_WEBSOCKET_HOSTNAME || 'localhost'
      const port = process.env.VUE_APP_WEBSOCKET_PORT || 8083
      let ws = new WebsocketHandler(hostname, port)
      this.$store.commit('setWs', ws)
      this.$root.modal.show(ModalProgress, {header: 'Connecting', msg: 'Establishing connection with the backend service, please wait...'},
          () => {}, () => {}
      )
    } catch (Error) {
      // this.$root.modal.show(ModalOk, {header: 'Connection error', msg: 'Cannot connect to the backend service. Please try again later.'}, (d)=>{this.$router.push('/')})
      this.$root.modal.show(ModalOk, {header: 'sam tin wong', msg: 'nop, not working', button: 'rage quit'}, (d) => {this.$router.push('/')})
      console.log(Error);
    }
  }
}
</script>

<style scoped>

</style>
