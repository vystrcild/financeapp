<template>
  <div class="pr-4">

    <!-- EXPENSES TABLE -->
    <div class="bg-virtus-nav rounded-md text-gray-300 shadow-xl">

        <table class="table-fixed w-full" id="expenses">
            <thead class="pl-4 bg-virtus-header">
                <tr>
                    <th class="text-left font-extralight text-xs py-2 pl-4 rounded-tl">EXPENSES</th>
                    <th class="text-center font-extralight text-xs pr-9">LAST 3 MONTHS</th>
                    <th class="text-center font-extralight text-xs pr-7">EXPECTATIONS</th>
                    <th class="text-center font-extralight text-xs">REALITY</th>
                    <th class="w-3/12 text-center font-extralight text-xs pr-5 rounded-tr">AVAILABLE</th>
                </tr>
            </thead>
            <tbody class="font-sans font-light text-sm">
                <tr class="hover:bg-virtus-menu hover:bg-opacity-30">
                  <td class="pl-4 pt-1">Bydlení</td>
                  <td class="text-right pr-20">{{ overview.bydleni.last_3M | formatCZK }}</td>
                  <td class="text-right pr-20">{{ expectationsExpenses.bydleni | formatCZK }}</td>
                  <td class="text-right pr-20">{{ overview.bydleni.this_month | formatCZK }}</td>
                  <td class="flex justify-between items-center text-right pr-6 py-1">
                      <div class="w-1/2">
                          <div class='border border-virtus-menu h-3 rounded-full'>
                            <div class='h-full' :class=" computeProgressBar(overview.bydleni.this_month, expectationsExpenses.bydleni)"></div>
                          </div>
                      </div>
                      <div class="style-CZK available-column">{{ overview.bydleni.this_month - expectationsExpenses.bydleni | formatCZK }}</div>
                  </td>
                </tr>
                <tr class="hover:bg-virtus-menu hover:bg-opacity-30">
                  <td class="pl-4 pt-1">Jídlo</td>
                  <td class="text-right pr-20">{{ overview.jidlo.last_3M | formatCZK }}</td>
                  <td class="text-right pr-20">{{ expectationsExpenses.jidlo | formatCZK }}</td>
                  <td class="text-right pr-20">{{ overview.jidlo.this_month | formatCZK }}</td>
                  <td class="flex justify-between items-center text-right pr-6 py-1">
                      <div class="w-1/2">
                          <div class='border border-virtus-menu h-3 rounded-full'>
                            <div class='h-full' :class=" computeProgressBar(overview.jidlo.this_month, expectationsExpenses.jidlo) "></div>
                          </div>
                      </div>
                      <div>{{ overview.jidlo.this_month - expectationsExpenses.jidlo | formatCZK }}</div>
                  </td>
                </tr>
                <tr class="hover:bg-virtus-menu hover:bg-opacity-30">
                  <td class="pl-4 py-1">Volný čas</td>
                  <td class="text-right pr-20 ">{{ overview.volny_cas.last_3M | formatCZK }}</td>
                  <td class="text-right pr-20 ">{{ expectationsExpenses.volny_cas | formatCZK }}</td>
                  <td class="text-right pr-20 ">{{ overview.volny_cas.this_month | formatCZK }}</td>
                  <td class="flex justify-between items-center text-right pr-6 py-1">
                      <div class="w-1/2">
                          <div class='border border-virtus-menu h-3 rounded-full'>
                            <div class='h-full':class=" computeProgressBar(overview.volny_cas.this_month, expectationsExpenses.volny_cas)"></div>
                          </div>
                      </div>
                      <div>{{ overview.volny_cas.this_month - expectationsExpenses.volny_cas | formatCZK }}</div>
                  </td>
                </tr>
                <tr class="hover:bg-virtus-menu hover:bg-opacity-30">
                  <td class="pl-4 py-1">Majetek</td>
                  <td class="text-right pr-20 ">{{ overview.majetek.last_3M | formatCZK }}</td>
                  <td class="text-right pr-20 ">{{ expectationsExpenses.majetek | formatCZK }}</td>
                  <td class="text-right pr-20 ">{{ overview.majetek.this_month | formatCZK }}</td>
                  <td class="flex justify-between items-center text-right pr-6 py-1">
                      <div class="w-1/2">
                          <div class='border border-virtus-menu h-3 rounded-full'>
                            <div class='h-full' :class=" computeProgressBar(overview.majetek.this_month, expectationsExpenses.majetek)"></div>
                          </div>
                      </div>
                      <div>{{ overview.majetek.this_month - expectationsExpenses.majetek | formatCZK }}</div>
                  </td>
                </tr>
                <tr class="hover:bg-virtus-menu hover:bg-opacity-30">
                  <td class="pl-4 py-1">Doprava</td>
                  <td class="text-right pr-20">{{ overview.doprava.last_3M | formatCZK }}</td>
                  <td class="text-right pr-20">{{ expectationsExpenses.doprava | formatCZK }}</td>
                  <td class="text-right pr-20">{{ overview.doprava.this_month | formatCZK }}</td>
                  <td class="flex justify-between items-center text-right pr-6 py-1">
                      <div class="w-1/2">
                          <div class='border border-virtus-menu h-3 rounded-full'>
                            <div class='h-full' :class=" computeProgressBar(overview.doprava.this_month, expectationsExpenses.doprava)"></div>
                          </div>
                      </div>
                      <div>{{ overview.doprava.this_month - expectationsExpenses.doprava | formatCZK }}</div>
                  </td>
                </tr>
                <tr class="hover:bg-virtus-menu hover:bg-opacity-30">
                  <td class="pl-4 py-1">Služby</td>
                  <td class="text-right pr-20">{{ overview.sluzby.last_3M | formatCZK }}</td>
                  <td class="text-right pr-20">{{ expectationsExpenses.sluzby | formatCZK }}</td>
                  <td class="text-right pr-20">{{ overview.sluzby.this_month | formatCZK }}</td>
                  <td class="flex justify-between items-center text-right pr-6 py-1">
                      <div class="w-1/2">
                          <div class='border border-virtus-menu h-3 rounded-full'>
                            <div class='h-full' :class=" computeProgressBar(overview.sluzby.this_month, expectationsExpenses.sluzby)"></div>
                          </div>
                      </div>
                      <div>{{ overview.sluzby.this_month - expectationsExpenses.sluzby | formatCZK }}</div>
                  </td>
                </tr>
                <tr class="hover:bg-virtus-menu hover:bg-opacity-30">
                  <td class="pl-4 py-1">Rozvoj a vzdělání</td>
                  <td class="text-right pr-20">{{ overview.rozvoj_vzdelani.last_3M | formatCZK }}</td>
                  <td class="text-right pr-20">{{ expectationsExpenses.rozvoj_vzdelani | formatCZK }}</td>
                  <td class="text-right pr-20">{{ overview.rozvoj_vzdelani.this_month | formatCZK }}</td>
                  <td class="flex justify-between items-center text-right pr-6 py-1">
                      <div class="w-1/2">
                          <div class='border border-virtus-menu h-3 rounded-full'>
                            <div class='h-full' :class=" computeProgressBar(overview.rozvoj_vzdelani.this_month, expectationsExpenses.rozvoj_vzdelani)"></div>
                          </div>
                      </div>
                      <div>{{ overview.rozvoj_vzdelani.this_month - expectationsExpenses.rozvoj_vzdelani | formatCZK }}</div>
                  </td>
                </tr>
                <tr class="hover:bg-virtus-menu hover:bg-opacity-30">
                  <td class="pl-4 py-1">Práce</td>
                  <td class="text-right pr-20">{{ overview.prace_vydaje.last_3M | formatCZK }}</td>
                  <td class="text-right pr-20">{{ expectationsExpenses.prace_vydaje | formatCZK }}</td>
                  <td class="text-right pr-20">{{ overview.prace_vydaje.this_month | formatCZK }}</td>
                  <td class="flex justify-between items-center text-right pr-6 py-1">
                      <div class="w-1/2">
                          <div class='border border-virtus-menu h-3 rounded-full'>
                            <div class='h-full' :class=" computeProgressBar(overview.prace_vydaje.this_month, expectationsExpenses.prace_vydaje)"></div>
                          </div>
                      </div>
                      <div>{{ overview.prace_vydaje.this_month - expectationsExpenses.prace_vydaje | formatCZK }}</div>
                  </td>
                </tr>
                <tr class="hover:bg-virtus-menu hover:bg-opacity-30">
                  <td class="pl-4 py-1">Další výdaje</td>
                  <td class="text-right pr-20">{{ overview.dalsi_vydaje.last_3M | formatCZK }}</td>
                  <td class="text-right pr-20">{{ expectationsExpenses.dalsi_vydaje | formatCZK }}</td>
                  <td class="text-right pr-20">{{ overview.dalsi_vydaje.this_month | formatCZK }}</td>
                  <td class="flex justify-between items-center text-right pr-6 py-1">
                      <div class="w-1/2">
                          <div class='border border-virtus-menu h-3 rounded-full'>
                            <div class='h-full' :class=" computeProgressBar(overview.dalsi_vydaje.this_month, expectationsExpenses.dalsi_vydaje)"></div>
                          </div>
                      </div>
                      <div>{{ overview.dalsi_vydaje.this_month - expectationsExpenses.dalsi_vydaje | formatCZK }}</div>
                  </td>
                </tr>
                <tr class="bg-virtus-header font-medium opacity-80">
                  <td class="pl-4 pt-2 pb-2 rounded-bl font-extralight text-xs">TOTAL</td>
                  <td class="text-right pr-20">{{ overview.vydaje_total.last_3M | formatCZK }}</td>
                  <td class="text-right pr-20">{{ expectationsExpensesTotal | formatCZK }}</td>
                  <td class="text-right pr-20">{{ overview.vydaje_total.this_month | formatCZK }}</td>
                  <td class="text-center rounded-br pr-4 font-light text-base style-negative">{{ overview.vydaje_total.this_month - expectationsExpensesTotal | formatCZK }}</td>
                </tr>
          </tbody>
        </table>

    </div>

    <!-- INCOME TABLE -->
    <div class="bg-virtus-nav rounded-md text-gray-300 shadow-xl mt-8">

        <table class="table-fixed w-full" id="income">
            <thead class="pl-4 bg-virtus-header">
                <tr>
                    <th class="text-left font-extralight text-xs py-2 pl-4 rounded-tl">INCOME</th>
                    <th class="text-center font-extralight text-xs pr-9">LAST 3 MONTHS</th>
                    <th class="text-center font-extralight text-xs pr-7">EXPECTATIONS</th>
                    <th class="text-center font-extralight text-xs">REALITY</th>
                    <th class="w-3/12 text-center font-extralight text-xs pr-5 rounded-tr"></th>
                </tr>
            </thead>
            <tbody class="font-sans font-light text-sm">
                <tr class="hover:bg-virtus-menu hover:bg-opacity-30">
                  <td class="pl-4 pt-1">Práce</td>
                  <td class="text-right pr-20">46736.96</td>
                  <td class="text-right pr-20">0.00</td>
                  <td class="text-right pr-20">0</td>
                  <td class="flex justify-between items-center text-right pr-6 py-1">
                      <div></div>
                  </td>
                </tr>
                <tr class="hover:bg-virtus-menu hover:bg-opacity-30">
                  <td class="pl-4 pt-1">Freelance</td>
                  <td class="text-right pr-20">10402.17</td>
                  <td class="text-right pr-20">0</td>
                  <td class="text-right pr-20">0</td>
                  <td class="flex justify-between items-center text-right pr-6 py-1">
                      <div></div>
                  </td>
                </tr>
                <tr class="hover:bg-virtus-menu hover:bg-opacity-30">
                  <td class="pl-4 py-1">Další příjmy</td>
                  <td class="text-right pr-20">4014.39</td>
                  <td class="text-right pr-20">5000</td>
                  <td class="text-right pr-20">0</td>
                  <td class="flex justify-between items-center text-right pr-6 py-1">
                      <div></div>
                  </td>
                </tr>


                <tr class="bg-virtus-header font-medium opacity-80">
                  <td class="pl-4 pt-2 pb-2 rounded-bl font-extralight text-xs">TOTAL</td>
                  <td class="text-right pr-20"></td>
                  <td class="text-right pr-20"></td>
                  <td class="text-right pr-20"></td>
                  <td class="text-center rounded-br pr-4"></td>
                </tr>
          </tbody>
        </table>

    </div>

    <!-- PROFIT TABLE -->
    <div class="text-gray-300 shadow-xl mt-8">

        <table class="table-fixed w-full" id="profit">
            <thead class="pl-4 bg-virtus-header">
                <tr>
                    <th class="text-left font-extralight text-base py-2 pl-4 rounded-l">PROFIT</th>
                    <th class="text-center font-light style-CZK pr-6" id="profit-last3m-total"></th>
                    <th class="text-center font-light style-CZK pr-9" id="profit-expectations-total"></th>
                    <th class="text-center font-light style-CZK pr-8 style-negative" id="profit-reality-total"></th>
                    <th class="w-3/12 text-center font-extralight text-xs pr-5 rounded-r"></th>
                </tr>
            </thead>
        </table>

    </div>

  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "OverviewTable",
  data() {
    return {
      overview: {
        bydleni: {
          last_3M: 0,
          this_month: 0,
        },
        jidlo: {
          last_3M: 0,
          this_month: 0,
        },
        volny_cas: {
          last_3M: 0,
          this_month: 0,
        },
        majetek: {
          last_3M: 0,
          this_month: 0,
        },
        doprava: {
          last_3M: 0,
          this_month: 0,
        },
        sluzby: {
          last_3M: 0,
          this_month: 0,
        },
        rozvoj_vzdelani: {
          last_3M: 0,
          this_month: 0,
        },
        prace_vydaje: {
          last_3M: 0,
          this_month: 0,
        },
        dalsi_vydaje: {
          last_3M: 0,
          this_month: 0,
        },
        prace_prijmy: {
          last_3M: 0,
          this_month: 0,
        },
        freelance: {
          last_3M: 0,
          this_month: 0,
        },
        dalsi_prijmy: {
          last_3M: 0,
          this_month: 0,
        },
        vydaje_total: {
          last_3M: 0,
          this_month: 0,
        },
        prijmy_total: {
          last_3M: 0,
          this_month: 0,
        },
      },
      expectationsExpenses: {
        bydleni: -13250,
        jidlo: -12000,
        volny_cas: -500,
        majetek: 0,
        doprava: 0,
        sluzby: -2500,
        rozvoj_vzdelani: -500,
        prace_vydaje: 0,
        dalsi_vydaje: -1000
      },
    }
  },
  methods: {
    getOverview() {
      const path = 'http://localhost:5000/overview';
      axios.get(path)
        .then((res) => {
          this.overview = res.data.overview;
        })
    },
    computeProgressBar(reality, expectations) {
      let progress = reality / expectations;
      if ((progress < 1/12) || (isNaN(progress))){
          return "bg-virtus-green w-0";
      } else if (progress <= 1/12){
          return "bg-virtus-green w-0";
      } else if (progress <= 2/12){
          return "bg-virtus-green w-2/12 rounded-l-full";
      } else if (progress <= 3/12){
          return "bg-virtus-green w-3/12 rounded-l-full";
      } else if (progress <= 4/12){
          return "bg-virtus-green w-4/12 rounded-l-full";
      } else if (progress <= 5/12){
          return "bg-virtus-green w-5/12 rounded-l-full";
      } else if (progress <= 6/12){
          return "bg-virtus-green w-6/12 rounded-l-full";
      } else if (progress <= 7/12){
          return "bg-virtus-green w-7/12 rounded-l-full";
      } else if (progress <= 8/12){
          return "bg-yellow-500 w-8/12 rounded-l-full";
      } else if (progress <= 9/12){
          return "bg-yellow-500 w-9/12 rounded-l-full";
      } else if (progress <= 10/12){
          return "bg-yellow-500 w-10/12 rounded-l-full";
      } else if (progress <= 11/12){
          return "bg-yellow-500 w-11/12 rounded-l-full";
      } else if (progress < 12/12){
          return "bg-yellow-500 w-11/12 rounded-l-full";
      } else if (progress >= 12/12){
          return "bg-virtus-red w-12/12 rounded-full";
      }
    }
  },
  computed: {
    expectationsExpensesTotal: function() {
      let sum = 0
      for (let el in this.expectationsExpenses) {
        sum += parseFloat( this.expectationsExpenses[el]);
      }
      return sum
    },
  },

  created() {
    this.getOverview();
  }
}
</script>

<style scoped>

</style>
