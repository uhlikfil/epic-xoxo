<template>
  <div class="player-setup">
    <div class="specific-setup">
      <label>Nickname
        <input type="text" name="nick" v-model="player.name">
      </label>
    </div>
    <div class="specific-setup">
      <label>Color
        <input type="color" name="color" v-model="player.color"></label>
    </div>
    <div>
      <label>Symbol
        <input type="text" name="symbol" v-model="player.symbol"></label>
    </div>
  </div>
</template>

<script>
export default {
  name: "PlayerSetup",
  data() {
    return {

    }
  },
  props: ['player'],
}
</script>

<style lang="less" scoped>

</style>
