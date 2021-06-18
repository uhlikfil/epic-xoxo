<template>
  <div class="highscores">
    <details>
      <summary><h2>Highscores</h2></summary>
      <h3>Top 10</h3>
      <div v-for="t in top10">{{ t.username }} - <span class="wins">{{ t.wins }}</span>/<span class="loses">{{
          t.loses
        }}</span> ({{
          t.winrate * 100
        }}% winrate) - RANK {{ t.rank }} [{{ t.ragequits }} ragequits]
      </div>
      <h3>Search for player</h3>
      <label><input type="text" v-model="name">
        <button @click="getSpecific(name)">Search</button>
      </label>
      <div class="results">
        <div v-if="!exists && specific"><span>Uživatel neexistuje nebo neodehrál aspoň 10 her!</span></div>
        <div v-if="specific && exists">{{ this.specific.username }} - <span class="wins">{{
            this.specific.wins
          }}</span>/<span
            class="loses">{{ this.specific.loses }}</span> ({{ this.specific.winrate * 100 }}% winrate) - RANK
          {{ this.specific.rank }} [{{
            this.specific.ragequits
          }} ragequits]
        </div>
        <div v-else-if="specific === null">User not found</div>
      </div>
    </details>
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
      name: null,
      exists: false
    }
  },
  methods: {
    gettop10() {
      fetch(Gateway.highscores + '/high_score', {
        method: 'GET',
      }).then((data) => {
        return data.json()
      }).then((parsed) => {
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
            if (parsed && parsed.status && parsed.status == 404) {
              this.exists = false
            }
            else {
              this.exists = true
            }
          })
    }
  },
  mounted() {
    this.gettop10()
  }
}
</script>

<style scoped lang="less">
.wins {color: green}

.loses {color: red}

h2 {
  display: inline-block;
}
.results {
  margin-top: .6rem;
}
</style>
