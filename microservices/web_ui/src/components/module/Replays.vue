<template>
  <div class="replays">
    <h2>Replays</h2>
    <h3>Recent</h3>
    <ul>
      <Replay v-for="r in replaysIntro" :r="r"/>
    </ul>
    <button @click="$router.push('/replaybrowser')">Browse replays</button>
  </div>
</template>

<script>
import {Gateway} from "@/js/Gateway";
import Replay from "@/components/Replay";

export default {
  name: "Replays",
  components: {Replay},
  computed: {
    replaysIntro() {
      return this.$store.state.replaysRecent
    }
  },
  data() {
    return {
      replays: null
    }
  },
  mounted() {
    fetch(Gateway.replays + 'replay/filter/', {
      body: '{"completed":true}', method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      }, mode: 'cors'
    }).then((data) => {
      return data.json()
    }).then((parsed) => {
      this.$store.commit('setReplays', parsed)
      console.log(parsed);
      console.log('commited');
    })
  },
  methods: {
    downloadReplay(r) {
      let e = document.createElement('a');
      e.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(JSON.stringify(r)));
      e.setAttribute('download', r.player1id + '_vs_' + r.player2id + '_' + new Date(r.date).toISOString());

      e.style.display = 'none';
      document.body.appendChild(e);

      e.click();

      document.body.removeChild(e);
    }
  }
}
</script>

<style scoped lang="less">
</style>
