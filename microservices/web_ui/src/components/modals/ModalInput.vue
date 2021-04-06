<template>
  <div class="modal-ok">
    <div class="header">{{header}}</div>
    <div class="msg">{{msg}}</div>
    <div class="inputs">
      {{ prompt }}: <input type="text" v-model="nick">
    </div>
    <div class="buttons">
      <button @click="$emit('accept', nick)">{{resolve}}</button>
      <button @click="$emit('reject')">{{reject}}</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "ModalInput",
  props: ['msg', 'header', 'prompt', 'resolve', 'reject'],
  data() {
    return {nick: ''}
  },
}
</script>

<style scoped lang="less">
.modal-ok {
  width: 400px;
  background-color: white;
  padding: .25rem;

  .header {
    font-size: 1.25rem;
    margin-bottom: .6rem;
  }

  .buttons {
    text-align: right;
  }
}
</style>
