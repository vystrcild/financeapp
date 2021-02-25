import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import './assets/styles/index.css';
import VCalendar from 'v-calendar';


Vue.config.productionTip = false;

Vue.filter('formatCZK', function (value) {
  let formatter = new Intl.NumberFormat('cs-CZ', {
        style: 'currency',
        currency: 'CZK'
    });
    return formatter.format(value);
});

Vue.use(VCalendar,{
  componentPrefix: 'vc',
})

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
