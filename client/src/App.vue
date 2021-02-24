<template>
  <div id="app" class="bg-virtus-back text-white">

    <Nav />
    <Sidebar />
    <router-view/>
  </div>
</template>

<script>
import Nav from './components/Nav.vue';
import Sidebar from './components/Sidebar.vue';
import Overview from './components/Overview.vue';
import Cashflow from './components/Cashflow.vue';
import Trends from './components/Trends.vue';
import Investments from './components/Investments.vue';
import TransactionModal from './components/TransactionModal.vue';
import DatePicker from './components/DatePicker.vue';

export default {
  name: 'App',
  components: {
    Nav,
    Sidebar,
    Overview,
    Cashflow,
    TransactionModal,
    DatePicker,
    Investments,
    Trends
  },
};
</script>

<style>
#app {

}
</style>
