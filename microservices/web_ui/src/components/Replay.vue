<template>
  <li><span class="result" :class="{winner: r.player1id === r.winnerid}">{{
      r.player1id
    }}</span> vs <span class="result" :class="{winner: r.player2id === r.winnerid}">{{ r.player2id }}</span>, took
    {{ r.rounds }} rounds, played {{ timeSince(r.date) }} ago, <a href="#" @click="downloadReplay(r)">download</a>
  </li>
</template>

<script>
import {timeSince} from "@/js/timesince";

export default {
  name: "Replay",
  props: ['r'],
  methods: {
    timeSince: timeSince,
    downloadReplay(r) {
      let e = document.createElement('a');
      e.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(JSON.stringify(r)));
      e.setAttribute('download', r.player1id + '_vs_' + r.player2id + '_' + new Date(r.date).toISOString());

      e.style.display = 'none';
      document.body.appendChild(e);

      e.click();

      document.body.removeChild(e);
    }
  },
}
</script>

<style scoped lang="less">
.result {
  color: red;

  &.winner {
    color: green;
  }
}
</style>
