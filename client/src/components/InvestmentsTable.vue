<template>
  <div>
    <!-- INVESTMENTS TABLE -->
    <div class="bg-virtus-nav rounded-md text-gray-300 shadow-xl mt-8">

        <table class="table-fixed w-full" id="investments">
            <thead class="pl-4 bg-virtus-header">
                <tr>
                    <th class="text-left font-extralight text-xs py-2 pl-4 rounded-tl">TICKER</th>
                    <th class="text-center font-extralight text-xs">DATE</th>
                    <th class="text-right font-extralight text-xs">INVESTMENT</th>
                    <th class="text-right font-extralight text-xs">VOLUME</th>
                    <th class="text-right font-extralight text-xs">VALUE</th>
                    <th class="text-right font-extralight text-xs">PROFIT</th>
                    <th class="text-right font-extralight text-xs pr-8 rounded-tr">ROI</th>
                </tr>
            </thead>
            <tbody class="font-sans font-light text-sm">

                <tr v-for="item in investments" :key= "item.id" class="hover:bg-virtus-menu hover:bg-opacity-30">
                  <td class="pl-4 pt-1">{{ item.ticker }}</td>
                  <td class="text-center">{{ item.date }}</td>
                  <td class="text-right">{{ item.investment }}</td>
                  <td class="text-right">{{ item.volume }}</td>
                  <td class="text-right">VALUE</td>
                  <td class="text-right">PROFIT</td>
                  <td class="text-right pr-8">ROI</td>
                </tr>


                <tr class="bg-virtus-header font-medium opacity-80">
                  <td class="pl-4 pt-2 pb-2 rounded-bl font-extralight text-xs">TOTAL</td>
                  <td class="text-right"></td>
                  <td class="text-right style-CZK">INVEST TOTAL</td>
                  <td class="text-right"></td>
                  <td class="text-right">VALUE TOTAL</td>
                  <td class="text-right">PROFIT TOTAL</td>
                  <td class="text-right rounded-br pr-8">Ahoj()</td>
                </tr>
          </tbody>
        </table>
        <!-- END OF INVESTMENTS TABLE -->
  </div>
    </div>

</template>

<script>
import axios from "axios";

export default {
  name: "InvestmentsTable",
  data() {
    return {
      investments: {
        ticker: 0,
        investment: 0,
        date: 0,
        volume: 0,
        id: 0
      }
    }
  },
  methods: {
    getInvestments() {
      const path = 'http://localhost:5000/investments';
      axios.get(path)
        .then((res) => {
          this.investments = res.data.investments;
        })
    },
  },
  created() {
    this.getInvestments();
  }
}
</script>

<style scoped>

</style>
