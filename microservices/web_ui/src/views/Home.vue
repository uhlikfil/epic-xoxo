<template>
  <div class="home">
    <h1>Connect 5</h1>
    <section class="section-play">
    <h2>Play</h2>
    <button @click="$router.push('local')">Local</button>
    <button @click="$router.push('online')">Online</button>
    </section>
    <Highscores></Highscores>
    <Replays></Replays>
    <Users></Users>
  </div>
</template>

<script>
// @ is an alias to /src
import Replays from "../components/module/Replays";
import Highscores from "@/components/module/Highscores";
import Users from "@/components/module/Users";

export default {
  name: 'Home',
  components: {Users, Highscores, Replays},
  data() {
    return {}
  },
  methods: {
    goOnline() {

    }
  }
}
</script>

<style lang="less">
.home {
  h2 {
    margin-top: .3rem;
    margin-bottom: .3rem;
  }
}
.section-play {
  margin-bottom: .8rem;
}
</style>
