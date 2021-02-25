import Vue from 'vue';
import Vuex from 'vuex';
import Investments from "./modules/investments";

// Load Vuex
Vue.use(Vuex);

// Create store
export default new Vuex.Store({
  modules: {
    Investments
  }
});
