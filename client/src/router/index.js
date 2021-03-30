import Vue from 'vue';
import VueRouter from 'vue-router';
import About from '../views/About.vue';
import Home from '../views/Home.vue';
import Theory from '../views/Theory.vue';
import Color from '../views/Color.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/about',
    name: 'About',
    component: About,
  },
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/theory',
    name: 'Theory',
    component: Theory,
  },
  {
    path: '/color',
    name: 'Color',
    component: Color,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
