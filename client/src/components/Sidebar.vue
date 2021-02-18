<template>
<!-- Sidebar -->
    <aside class="flex fixed flex-col z-30 w-44 h-screen pt-16 bg-virtus-nav shadow-lg text-white font-light justify-between">
        <div class="mt-4 mx-4">
        <div>
        <div class="flex border-gray-600 border-b">
                <p class="font-extralight">Total Assets</p>
            </div>
            <div class="flex mt-2 mr-2 justify-end font-sans">{{ totalAssets | formatCZK }}</div>
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
                <div class="flex mt-2 mr-2 justify-end">{{cash | formatCZK }}</div>
            </div>
            <div class="mt-4">
            <div class="flex border-gray-600 border-b">
                    <p class="font-extralight">Twisto</p>
                </div>
                <div class="flex mt-2 mr-2 justify-end">{{twisto | formatCZK }}</div>
            </div>
            <div class="mt-4">
            <div class="flex border-gray-600 border-b">
                    <p class="font-extralight">Unicredit</p>
                </div>
                <div class="flex mt-2 mr-2 justify-end">{{unicredit | formatCZK }}</div>
            </div>
            <div class="mt-4">
            <div class="flex border-gray-600 border-b">
                    <p class="font-extralight">Revolut</p>
                </div>
                <div class="flex mt-2 mr-2 justify-end">{{revolut | formatCZK }}</div>
            </div>
        </div>
    </aside>
</template>

<script>
import axios from 'axios';

export default {
  name: "Sidebar",
  data() {
    return {
      totalAssets: 123456,
      totalAssetsChange: -12345.32,
      totalInvestments: 628666.32,
      totalInvestmentsChange: 2132.32,
      cash: 4181.00,
      twisto: 23233.32,
      unicredit: 300000.00,
      revolut: 0.00,
    };
  },
  methods: {
    getBilance(){
      const path = 'http://localhost:5000/get';
      axios.get(path)
        .then((res) => {
          this.bilance = res.data.bilance;
        })
    }
  },
  computed: {
    formatColor(value) {
      let color = (value > 0) ? "text-virtus-green" : "text-virtus-red";
      return color;
    }
  },
  created() {
    this.getBilance();
  }
}
</script>

<style scoped>

</style>
