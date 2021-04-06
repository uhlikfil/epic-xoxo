<template>
  <div class="board-wrapper">
    <div class="round">Round: {{game.round}}</div>
    <div class="ui">
      <div :style="{color: game.plr1.color}" :class="{bold: game.turn == 1}">{{ game.plr1.name }} [{{game.plr1.symbol}}]</div>
      <div>VS</div>
      <div :style="{color: game.plr2.color}" :class="{bold: game.turn == 2}">{{ game.plr2.name }} [{{game.plr2.symbol}}]</div>
    </div>
    <div class="board">
      <div class="row" v-for="(h,i) in game.board">
        <div class="cell" v-for="(w,j) in h" @click="$emit('cell', [j, i])" :class="{highlight: isHighlighted(j,i)}">
          <span :style="{color: game.plr1.color}" v-if="game.board[i][j] === 1">{{ game.plr1.symbol }}</span>
          <span :style="{color: game.plr2.color}" v-if="game.board[i][j] === 2">{{ game.plr2.symbol }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Board",
  props: ['game', 'highlights'],
  data() {
    return {}
  },
  methods: {
    isHighlighted(x, y) {
      return this.highlights[x + 'x' + y] === true
    },
  }
}
</script>

<style scoped lang="less">
.board {
  margin: 40px auto 0 auto;
  counter-set: y 0 x 0;
}

.round {
  text-align: center;
  margin-bottom: .5em;
}

.ui {
  display: flex;
  flex-flow: row nowrap;
  justify-content: space-around;
}

.row {
  display: flex;
  margin: 0;
  justify-content: center;
  align-items: center;

  &:last-child {
    .cell {
      border-bottom: none;
    }
  }
}

.row:first-child {
  .cell {
    position: relative;
  }

  .cell::after {
    font-size: 1rem;
    counter-increment: x;
    position: absolute;
    top: -30px;
    width: 30px;
    text-align: center;
    content: counter(x);
  }
}

.bold {
  font-weight: bold;
}

.cell:first-child::before {
  font-size: 1rem;
  counter-increment: y;
  position: absolute;
  left: -30px;
  width: 30px;
  text-align: center;
  content: counter(y);
}

.cell {
  font-size: 1.1rem;
  position: relative;
  width: 25px;
  height: 25px;
  border-right: 1px solid black;
  border-bottom: 1px solid black;
  user-select: none;

  display: flex;
  justify-content: center;
  align-items: center;

  &:last-child {
    border-right: none;
  }

  &.highlight {
    background-color: yellow;
  }
}
</style>
