<template>
  <div class="lobbies">
    <div class="message-of-the-day">Message of the day: {{ $store.state.messageOfTheDay }}</div>
    <table class="list">
      <tr class="nohigh">
        <th>Lobby</th>
        <th>Host</th>
        <th>Players</th>
      </tr>
      <tr v-for="l in lobbies" class="lobby" @click="selectedLobby = l" :class="{selected: l === selectedLobby}">
        <td class="name">{{ l.name }}</td>
        <td class="author">{{ l.author }}</td>
        <td class="players">{{ l.players }}/2</td>
      </tr>
    </table>
    <div class="buttons">
      <button @click="join" :disabled="!selectedLobby">Join</button>
      <button @click="host">Host</button>
      <button @click="refresh">Refresh</button>
    </div>
  </div>
</template>

<script>
import ModalInput from "@/components/modals/ModalInput";
import ModalProgress from "@/components/modals/ModalProgress";

export default {
  name: "LobbyList",
  methods: {
    join() {
      this.$root.modal.show(ModalProgress, {header: 'Joining', msg: 'Joining a lobby'},
          (data) => {
          },
          (data) => {}
      )
      this.$store.state.ws.connectToLobby(this.selectedLobby.id)
    },
    host() {
      this.$root.modal.show(ModalInput, {header: 'Host lobby', prompt: 'Lobby name', resolve: 'host', reject: 'nah'},
          (data) => {
            this.$store.state.ws.host(data)
            this.$root.modal.show(ModalProgress, {header: 'Hosting', msg:'Setting up server...'})
          },
          (data) => {}
      )
    },
    refresh() {
      this.$store.state.ws.refreshLobbies()
    }
  },
  data() {
    return {
      selectedLobby: null,
    }
  },
  computed: {
    lobbies() {return this.$store.state.lobbies}
  }
}
</script>

<style scoped lang="less">
.lobbies {
  max-width: 800px;

  .list {
    width: 100%;
    border-collapse: collapse;
    border: 1px solid black;

    tr.nohigh:hover {
      background-color: transparent;
    }

    tr:hover, tr.selected {
      background-color: red;
    }

    tr.selected:hover {
      background-color: darkred;
    }

    th, td {
      border: 1px solid black;
    }

    .lobby {
    }

    .buttons {

    }
  }
}

</style>
