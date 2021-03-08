<template>
<!-- Sidebar -->
    <aside class="flex fixed flex-col z-30 w-44 h-screen pt-16 bg-virtus-nav shadow-lg text-white font-light justify-between">
        <div class="mt-4 mx-4">
        <div>
        <div class="flex border-gray-600 border-b">
                <p class="font-extralight">Total Assets</p>
            </div>
            <div class="flex mt-2 mr-2 justify-end font-sans">{{ bilance.total | formatCZK }}</div>
            <div class="flex text-sm mr-2 justify-end" :class="(totalAssetsChange > 0 ? 'text-virtus-green': 'text-virtus-red')">{{ totalAssetsChange | formatCZK }}</div>
        </div>
        <div class="mt-4">
        <div class="flex border-gray-600 border-b">
                <p class="font-extralight">Investments</p>
            </div>
            <div class="flex mt-2 mr-2 justify-end">{{totalInvestments | formatCZK }}</div>
            <div class="flex text-sm mr-2 justify-end" :class="(totalInvestmentsChange > 0 ? 'text-virtus-green': 'text-virtus-red')">{{totalInvestmentsChange | formatCZK }}</div>


        </div>
        </div>
        <div class="mx-4 mb-4">
            <div>
            <div class="flex border-gray-600 border-b">
                    <p class="font-extralight">Cash</p>
                </div>
                <div class="flex mt-2 mr-2 justify-end">{{bilance.acc_1 | formatCZK }}</div>
            </div>
            <div class="mt-4">
            <div class="flex border-gray-600 border-b">
                    <p class="font-extralight">Twisto</p>
                </div>
                <div class="flex mt-2 mr-2 justify-end">{{bilance.acc_2 | formatCZK }}</div>
            </div>
            <div class="mt-4">
            <div class="flex border-gray-600 border-b">
                    <p class="font-extralight">Unicredit</p>
                </div>
                <div class="flex mt-2 mr-2 justify-end">{{bilance.acc_3 | formatCZK }}</div>
            </div>
            <div class="mt-4">
            <div class="flex border-gray-600 border-b">
                    <p class="font-extralight">Revolut</p>
                </div>
                <div class="flex mt-2 mr-2 justify-end">{{bilance.acc_4 | formatCZK }}</div>
            </div>
        </div>
    </aside>
</template>

<script>
import axios from 'axios';
import { mapGetters, mapActions, mapMutations } from 'vuex';

export default {
  name: "Sidebar",
  data() {
    return {
      totalAssets: 0,
      totalAssetsChange: 0,
      totalInvestments: 666666.66,
      totalInvestmentsChange: 2132.32,
      cash: 0,
      twisto: 0,
      unicredit: 0,
      revolut: 0,
      bilance: 0,
    };
  },
  methods: {
    getBilance(){
      const path = 'http://localhost:5000/get';
      axios.get(path)
        .then((res) => {
          this.bilance = res.data.bilance;
          this.totalAssetsChange = res.data.assets_change;
        })
    },
    ...mapActions(["getCryptoRates", "getCZKRate"]),
    ...mapMutations(['setBTCCZKrate'])
  },
  computed: {
    ...mapGetters(['getBTCUSDrate','getUSDCZKrate', 'getBTCCZKrate', 'test']),
  },

  created() {
    this.getBilance();
    this.getCryptoRates();
    this.getCZKRate();

  },
  beforeUpdate() {
    this.setBTCCZKrate();
  }
}
</script>

<style scoped>

</style>
