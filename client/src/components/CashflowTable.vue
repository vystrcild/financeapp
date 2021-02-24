<template>
  <div>
    <!-- CASHFLOW TABLE -->
    <div class="bg-virtus-nav rounded-md text-gray-300 shadow-xl mr-4">

        <table class="table-fixed w-full" id="investments">
            <thead class="pl-4 bg-virtus-header">
                <tr>
                    <th @click="sort('date')" class="w-20 text-center font-extralight text-xs py-2 pl-4 rounded-tl">DATE</th>
                    <th class="w-28 text-right font-extralight text-xs">ACCOUNT</th>
                    <th class="w-3/12 text-right font-extralight text-xs">DESCRIPTION</th>
                    <th class="w-3/12 text-right font-extralight text-xs">CATEGORY</th>
                    <th class="w-32 text-right font-extralight text-xs pr-4 rounded-tr">AMOUNT</th>
                </tr>
            </thead>
            <tbody class="font-sans font-light text-sm">

                <tr v-for="item in sortedTransactions" :key= "item.id" class="hover:bg-virtus-menu hover:bg-opacity-30">
                  <td class="text-right">{{ item.date }}</td>
                  <td class="text-right">{{item.account.accounts}}</td>
                  <td class="text-right">{{ item.description }}</td>
                  <td class="text-right">{{ item.category.categories }}</td>
                  <td class="text-right pr-4">{{ item.amount | formatCZK }}</td>
                </tr>

                <tr class="bg-virtus-header font-medium opacity-80">
                  <td class="pl-4 pt-2 pb-2 rounded-bl font-extralight text-xs">TOTAL</td>
                  <td class="text-right"></td>
                  <td class="text-right"></td>
                  <td class="text-right"></td>
                  <td class="text-right rounded-br pr-8"></td>
                </tr>

          </tbody>
        </table>
    </div>
        <!-- END OF CASHFLOW TABLE -->
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "CashflowTable",
  data() {
    return {
      transactions: [],
      currentSort: 'date',
      currentSortDir: 'desc'
    }
  },
  methods: {
    getTransactions() {
      const path = 'http://localhost:5000/transactions';
      axios.get(path)
        .then((res) => {
          this.transactions = res.data.transactions;
        })
    },
    sort: function(s) {
    //if s == current sort, reverse
    if(s === this.currentSort) {
      this.currentSortDir = this.currentSortDir==='asc'?'desc':'asc';
    }
    this.currentSort = s;
    },
  },
  computed: {
    sortedTransactions: function() {
    return this.transactions.sort((a,b) => {
      let modifier = 1;
      if(this.currentSortDir === 'desc') modifier = -1;
      if(a[this.currentSort] < b[this.currentSort]) return -1 * modifier;
      if(a[this.currentSort] > b[this.currentSort]) return 1 * modifier;
      return 0;
    });
  }
  },
  created() {
    this.getTransactions();
  },
}
</script>

<style scoped>

</style>
