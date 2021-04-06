<template>
  <div id="app">
    <ModalRoot/>
    <router-view/>
  </div>
</template>

<style lang="less">
</style>

<script>
import ModalRoot from "@/components/ModalRoot";
import fu from "@/components/modals/ModalOk";
import ModalOk from "@/components/modals/ModalOk";

export default {
  components: {ModalRoot},
  mounted() {
    this.$store.commit('setRoot', this.$root)
  }
}
</script>
