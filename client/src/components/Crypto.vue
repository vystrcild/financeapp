<template>
<div class="shadow-xl rounded-xl mr-8">
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
        type:"scatter",
        line: {color: '#2481ce'}
      }],
      layout:{
        paper_bgcolor: '#2b2d3c',
        plot_bgcolor: '#2b2d3c',
        font: {
          color: "white"
        },
        margin: {
          l: 50,
          r: 50
        }
      },
      test: [],
    }
  },
  methods: {
    getCryptoRates() {
      axios.get('https://api.coincap.io/v2/assets/bitcoin/history?interval=m1')
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
