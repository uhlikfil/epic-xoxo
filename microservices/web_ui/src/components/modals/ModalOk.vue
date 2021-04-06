<template>
  <div class="modal-ok">
    <div class="header">{{header}}</div>
    <div class="msg">{{msg}}</div>
    <div class="buttons">
      <button @click="$emit('accept')">{{ button }}</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "ModalOk",
  props: {
    msg: {
      default: 'msg'
    },
    header: {
      default: 'header'
    },
    button: {
      default: 'Ok'
    }
  },
  mounted() {
    console.log('this.$props', this.$props);
    console.log('this.$attrs', this.$attrs);
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
