import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import LocalSetup from "@/views/LocalSetup";
import Local from "@/views/Local";
import Online from "@/views/Online";
import ReplayBrowser from "@/views/ReplayBrowser";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/local',
    name: 'LocalSetup',
    component: Local
  },
  {
    path: '/online',
    name: 'Online',
    component: Online
  },
  {
    path: '/replaybrowser',
    name: 'ReplayBrowser',
    component: ReplayBrowser
  },
]

const router = new VueRouter({
  routes
})

export default router
