<template>
  <div class="setup">
    <div>Player 1: {{plr1Name}}</div>
    <div>Player 2: {{plr2Name}}</div>
    <div>Starting player: {{replica.startingPlr}}</div>
    <div class="controls">
      <button :disabled="!replica.isHost" @click="$emit('start')">Start</button>
      <button :disabled="!replica.isHost" @click="$emit('swap')">Swap starting player</button>
      <button @click="$emit('disconnect')">Disconnect</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "OnlineSetup",
  props: ['replica'],
  computed: {
    plr1Name() {
      return this.replica.plr1 ? this.replica.plr1.name : 'Waiting for someone to join'
    },
    plr2Name() {
      return this.replica.plr2 ? this.replica.plr2.name : 'Waiting for someone to join'
    },
  },
}
</script>

<style scoped lang="less">

</style>
