<template>
  <div class="local">
    <LocalSetup v-if="screen === 0" :game="game" @start="start"/>
    <Board ref="board" v-if="screen === 1" :game="game" @cell="clickCell" :highlights="highlights"/>
    <div @click="replay">
      <div>Status</div>
      <div>{{debug}}</div>
    </div>
  </div>
</template>

<script>
import LocalSetup from "@/views/LocalSetup";
import {Player} from "@/js/Player";
import Board from "@/components/Board";
import {Game} from "@/js/Game";

export default {
  name: "Multiplayer",
  components: {Board, LocalSetup},
  data() {
    return {
      game: new Game(),
      screen: 0,
      highlights: {},
      debug: '',
    }
  },
  methods: {
    start() {
      this.screen = 1;
      this.game.initBoard()
      this.game.initStartingPlr()
      this.$set(this.game, 'board', this.game.board)
    },
    clickCell([x, y]) {
      if (this.game.isFieldEmpty(x, y) && this.game.winner == null) {
        let result = this.game.play(x, y)
        this.$set(this, 'highlights', result.highlight)
      }
    },
    replay() {
      this.game.reset()
      this.$set(this, 'highlights', {})
    }
  },
  created() {
    // this.game.plr1.name = 'Player 1';
    // this.game.plr1.color = '#ff0000';
    // this.game.plr1.symbol = 'X';
    // this.game.plr2.name = 'Player 2';
    // this.game.plr2.color = '#0000ff';
    // this.game.plr2.symbol = 'O';
  }
}
</script>

<style scoped>

</style>
