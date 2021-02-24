<template>
<div>
  <Plotly :data="chartData" :layout="layout" :display-mode-bar="false"></Plotly>
</div>
</template>

<script>
import {Plotly} from "vue-plotly"
import axios from "axios";

export default {
  name: "Crypto",
  components: {
    Plotly
  },
  data() {
    return {
      chartData: [{
        x: [],
        y: [],
        type:"scatter"
      }],
      layout:{},
      test: [],
    }
  },
  methods: {
    getCryptoRates() {
      axios.get('https://api.coincap.io/v2/assets/bitcoin/history?interval=d1')
        .then(response => {
          response.data.data.forEach(row => {
            this.chartData[0].x.push(row.date);
            this.chartData[0].y.push(row.priceUsd);
          })
        });
    },
  },
  created() {
    this.getCryptoRates();
  },
}

</script>

<style scoped>

</style>
