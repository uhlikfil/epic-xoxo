<template>
  <div class="home">
    <button @click="$router.push('local')">Local</button>
    <button @click="$router.push('online')">Online</button>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  components: {
    HelloWorld
  },
  methods: {
    goOnline() {

    }
  }
}
</script>

<style lang="less">
.home {
  color:red;
}
</style>
