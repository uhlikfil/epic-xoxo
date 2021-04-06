<template>
  <div class="local-setup">
    <div class="player1">
      <PlayerSetup :player="game.plr1"/>
    </div>
    <div class="player2">
      <PlayerSetup :player="game.plr2"/>
    </div>
    <div class="game-setup">
      <label>Board width
        <input type="number" name="width" v-model="game.width">
      </label>
      <label>Board height
        <input type="number" name="height" v-model="game.height">
      </label>
      <label>
        Starting player
        <select v-model="game.startingPlr">
          <option value="plr1">{{ game.plr1.name }}</option>
          <option value="plr2">{{ game.plr2.name }}</option>
          <option value="random">Random</option>
        </select>
      </label>
    </div>
    <div class="buttons">
      <button @click="$emit('start')">Start</button>
      <button>Back</button>
    </div>
  </div>
</template>

<script>
import PlayerSetup from "@/components/PlayerSetup";

export default {
  name: "LocalSetup",
  components: {PlayerSetup},
  props: ['game'],
}
</script>

<style lang="less" scoped>

</style>
