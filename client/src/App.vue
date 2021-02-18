<template>
  <div id="app" class="bg-virtus-back text-white">

    <Nav />
    <Sidebar />
    <h1>Welcome to my APP!!!</h1>
    <router-view/>
  </div>
</template>

<script>
import Nav from './components/Nav.vue';
import Sidebar from './components/Sidebar.vue';
import Overview from './components/Overview.vue';
import Cashflow from './components/Cashflow.vue';
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
    DatePicker
  },
};
</script>

<style>
#app {

}
</style>
