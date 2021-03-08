import axios from 'axios';

const state = {
  USDCZKrate: "",
  BTCUSDrate: "",
  LTCUSDrate: "",
  ETHUSDrate: "",
  BTCCZKrate: "",
};

const getters = {
  getUSDCZKrate: state => state.USDCZKrate,
  getBTCUSDrate: state => state.BTCUSDrate,
  getBTCCZKrate: state => {
    return state.USDCZKrate * state.BTCUSDrate;
  },
  test: state => state.BTCCZKrate,
};

const actions = {
  async getCryptoRates({ commit }) {
    const responseBTC = await axios.get(
      'https://api.coincap.io/v2/rates/bitcoin'
    );
    const responseLTC = await axios.get(
      'https://api.coincap.io/v2/rates/litecoin'
    );
    const responseETH = await axios.get(
      'https://api.coincap.io/v2/rates/ethereum'
    );
    commit('setRates', [
      responseBTC.data.data.rateUsd,
      responseLTC.data.data.rateUsd,
      responseETH.data.data.rateUsd,
    ]);
  },
  async getCZKRate({ commit }) {
    const response = await axios.get(
      'https://api.exchangeratesapi.io/latest?base=USD&symbols=CZK'
    );
    commit('setCZK', response.data.rates.CZK);
  },
};

const mutations = {
  setRates: (state, rates) => {
    state.BTCUSDrate = rates[0];
    state.LTCUSDrate = rates[1];
    state.ETHUSDrate = rates[2];
  },
  setCZK: (state, rate) => (state.USDCZKrate = rate),
  setBTCCZKrate (state) {
    state.BTCCZKrate = state.USDCZKrate * state.BTCUSDrate;
  }
};

export default {
  state,
  getters,
  actions,
  mutations
};
