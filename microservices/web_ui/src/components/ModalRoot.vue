<template>
  <div v-if="visible" id="modal">
    <div id="modal-body">
      <component v-if="component" :is="component" v-bind="props" @accept="accept" @reject="reject"/>
    </div>
  </div>
</template>

<script>
export default {
  name: "ModalRoot",
  data() {
    return {
      visible: false,
      component: null,
      props: null,
      acceptFn: null,
      rejectFn: null,
    }
  },
  created() {
    this.$root.modal = this;
  },
  methods: {
    show(component, props, acceptFn, rejectFn) {
      this.visible = true;
      this.component = component
      this.props = props
      this.acceptFn = acceptFn
      this.rejectFn = rejectFn
    },
    accept(e) {
      this.hide()
      if (this.acceptFn) this.acceptFn(e)
    },
    reject(e) {
      this.hide()
      if (this.rejectFn) this.rejectFn(e)
    },
    hide() {
      this.visible = false;
    },
    forceAccept(data) {
      this.hide()
      if (this.acceptFn) this.acceptFn(data)
    },
    forceReject(data) {
      this.hide()
      if (this.rejectFn) this.rejectFn(data)
    }
  },
}
</script>

<style scoped lang="less">
#modal {
  background-color: rgba(0, 0, 0, .25);
  position: fixed;
  z-index: 1000;

  top: 0;
  left: 0;
  right: 0;
  bottom: 0;

  &-body {
    position: fixed;
    margin: auto;
    left: 50%;
    top: 50%;
    transform: translateX(-50%) translateY(-50%);
  }
}
</style>
