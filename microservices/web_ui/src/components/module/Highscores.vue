<template>
  <div class="highscores">
    <h2>Highscores</h2>
    <h3>Top 10</h3>
    <div v-for="t in top10">{{ t.username }} - <span class="wins">{{ t.wins }}</span>/<span class="loses">{{ t.loses }}</span> ({{
        t.winrate * 100
      }}% winrate) - RANK {{ t.rank }} [{{ t.ragequits }} ragequits]
    </div>
    <h3>Search for player</h3>
    <label><input type="text">
      <button>Search</button>
    </label>
    <div v-if="specific">{{ this.specific.username }} - <span class="wins">{{ this.specific.wins }}</span>/<span
        class="loses">{{ this.specific.loses }}</span> ({{ this.specific.winrate * 100 }}% winrate) - RANK {{ this.specific.rank }} [{{
        this.specific.ragequits
      }} ragequits]
    </div>
    <div v-else-if="specific === null">User not found</div>
  </div>
</template>

<script>
import {Gateway} from "@/js/Gateway";

export default {
  name: "Highscores",
  data() {
    return {
      top10: [],
      specific: false,
    }
  },
  methods: {
    gettop10() {
      fetch('http://localhost:8090/high_scores/api/v1/high_score', {
        method: 'GET',
      }).then((data) => {
        console.log(data);
        return data.json()
      }).then((parsed) => {
        console.log(parsed);
        this.top10 = parsed.high_scores
      })
    },
    getSpecific(name) {
      fetch(Gateway.highscores + '/high_score/' + name, {
        method: 'GET',
      })
          .then((data) => {
            return data.json()
          })
          .then((parsed) => {
            this.specific = parsed
          })
    }
  },
  mounted() {
    console.log('pls');
    this.gettop10()
  }
}
</script>

<style scoped lang="less">
.wins {color: green}

.loses {color: red}
</style>
