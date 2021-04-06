<template>
  <div class="modal-ok">
    <div class="header">{{header}}</div>
    <div class="msg">{{msg}}</div>
  </div>
</template>

<script>
export default {
  name: "ModalProgress",
  props: ['msg', 'header'],
  mounted() {
  }
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
