import Vue from 'vue';
import Router from 'vue-router';
import Overview from '../components/Overview.vue'
import Cashflow from "@/components/Cashflow";
import Trends from "@/components/Trends";
import Investments from "@/components/Investments";

Vue.use(Router);


export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Overview',
      component: Overview,
    },
    {
      path: '/cashflow',
      name: 'Cashflow',
      component: Cashflow,
    },
    {
      path: '/trends',
      name: 'Trends',
      component: Trends,
    },
    {
      path: '/investments',
      name: 'Investments',
      component: Investments,
    },
  ],
});
