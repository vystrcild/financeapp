import axios from 'axios';


const state = {
  investmentsTotalValue: 11.232,
  BTCUSDrateValue: 12,
};

const getters = {
  getInvestmentsTotalValue: state => state.investmentsTotalValue,
  getBTCUSDrateValue: state => state.BTCUSDrateValue
};

const actions = {
  async getCryptoRates({ commit }) {
    const response = await axios.get(
      'https://api.coincap.io/v2/rates/bitcoin'
    );
    console.log(response);

    commit('setRate', response.data.data.rateUsd);
  }
};

const mutations = {
  setRate: (state, rate) => (state.BTCUSDrateValue = rate),
};


export default {
  state,
  getters,
  actions,
  mutations
};
