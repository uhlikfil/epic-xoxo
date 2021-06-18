<template>
  <div class="users">
    <details>
      <summary><h2>Users</h2></summary>
      <label>
        <input type="text" v-model="username">
      </label>
      <button @click="search">Search</button>
      <h3>User detail</h3>
      <div v-if="user == '404'">
        Uživatel nenalezen
      </div>
      <div v-if="user && user != '404'" class="user">
        <div class="name">{{ user.username }}</div>
        <div class="ip">Last recorded I.P.: {{ user.last_ip }}</div>
        <div v-if="user.loses != 'Unavailable'">
          <div class="wr">Winrate: {{ user.high_score.winrate * 100 + '%' }}</div>
          <div class="wins">Wins: {{ user.high_score.wins }}</div>
          <div class="loss">Losses: {{ user.high_score.loses }}</div>
          <div class="rqs">Ragequits: {{ user.high_score.ragequits }}</div>
        </div>
      </div>
    </details>
  </div>
</template>

<script>
import {Gateway} from "../../js/Gateway";

export default {
  name: "Users",
  data() {
    return {
      username: null,
      user: null
    }
  },
  methods: {
    search() {
      fetch(Gateway.users + '/userdetail/' + this.username, {method: 'GET'})
          .then((res) => {
                return res.json()
              }
          )
          .then((data) => {
            console.log(data);
            if (data.status && data.status == 404)
              this.user = '404'
            else this.user = data
          })
    }
  }
}
</script>

<style scoped lang="less">
h3 {
  margin-bottom: .3rem;
}

.name {
  font-size: 1.25rem;
  font-weight: bold;
}

.wins {
  color: green;
}

.loss {
  color: red;
}

h2 {
  display: inline-block;
}

.users {
  min-height: 300px;
}
</style>
