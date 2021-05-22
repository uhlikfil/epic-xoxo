<template>
  <div class="replay-browser">
    <form>
      <fieldset>
        <legend><h2>Search</h2></legend>
        <label>
          Player 1
          <input type="text" v-model="plr1">
        </label>
        <label>
          Player 2
          <input type="text" v-model="plr2">
        </label>
        <label>
          Winning player
          <input type="text" v-model="winner">
        </label>
        <label>
          Starting player
          <input type="text" v-model="starting">
        </label>
        <label>
          Rounds min
          <input type="number" value="0" min="0" v-model="roundsMin">
        </label>
        <label>
          Round max
          <input type="number" value="100" min="1" v-model="roundsMax">
        </label>
        <label>
          Only completed
          <input type="checkbox" checked="checked" v-model="completed">
        </label>
        <br/>
        <button @click.prevent="search">Search</button>
      </fieldset>
    </form>
    <div><h2>Search results</h2></div>
    <Replay v-for="r in results" :r="r"></Replay>
  </div>
</template>

<script>
import {Gateway} from "@/js/Gateway";
import Replay from "@/components/Replay";

function createBody(data) {
  const obj = {}
  if (data.plr1) {obj.player1Id = data.plr1}
  if (data.plr2) {obj.player2Id = data.plr2}
  if (data.winner) {obj.winnerId = data.winner}
  if (data.starting) {obj.startingId = data.starting}
  if (data.completed) {obj.completed = data.completed}
  if (data.roundsMin) {if (!obj.rounds) obj.rounds = {}; obj.rounds.gte = Number.parseInt(data.roundsMin)}
  if (data.roundsMin) {if (!obj.rounds) obj.rounds = {}; obj.rounds.lte = Number.parseInt(data.roundsMax)}
  return obj;
}

export default {
  name: "ReplayBrowser",
  components: {Replay},
  data() {
    return {
      plr1: null,
      plr2: null,
      winner: null,
      starting: null,
      roundsMin: 1,
      roundsMax: 100,
      completed: true,

      canSearch: true,
      results: []
    }
  },
  methods: {
    search(e) {
      const body = JSON.stringify(createBody(this.$data));
      console.log('request body', body);
      this.canSearch = false
      fetch(Gateway.replays + 'replay/filter/', {
        body: body, method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        }, mode: 'cors'
      }).then((data) => {
        return data.json()
      }).then((parsed) => {
        this.results = parsed
      })
      .finally(()=>{this.canSearch = true})
    }
  }
}
</script>

<style scoped lang="less">

</style>
