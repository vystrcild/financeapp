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
                  <td class="text-right pr-20 style-CZK">{{ overview.bydleni.last_3M | formatCZK }}</td>
                  <td class="text-right pr-20 style-CZK">{{ -13250 | formatCZK }}</td>
                  <td class="text-right pr-20 style-CZK">{{ overview.bydleni.this_month | formatCZK }}</td>
                  <td class="flex justify-between items-center text-right pr-6 py-1">
                      <div class="w-1/2">
                          <div class='border border-virtus-menu h-3 rounded-full'>
                            <div class='h-full'></div>
                          </div>
                      </div>
                      <div class="style-CZK available-column"></div>
                  </td>
                </tr>
                <tr class="hover:bg-virtus-menu hover:bg-opacity-30">
                  <td class="pl-4 pt-1">Jídlo</td>
                  <td class="text-right pr-20 style-CZK">{{ overview.jidlo.last_3M | formatCZK }}</td>
                  <td class="text-right pr-20 style-CZK">{{ -12000 | formatCZK }}</td>
                  <td class="text-right pr-20 style-CZK">{{ overview.jidlo.this_month | formatCZK }}</td>
                  <td class="flex justify-between items-center text-right pr-6 py-1">
                      <div class="w-1/2">
                          <div class='border border-virtus-menu h-3 rounded-full'>
                            <div class='h-full'></div>
                          </div>
                      </div>
                      <div class="style-CZK available-column"></div>
                  </td>
                </tr>
                <tr class="hover:bg-virtus-menu hover:bg-opacity-30">
                  <td class="pl-4 py-1">Volný čas</td>
                  <td class="text-right pr-20 style-CZK">{{ overview.volny_cas.last_3M | formatCZK }}</td>
                  <td class="text-right pr-20 style-CZK">{{ -500 | formatCZK }}</td>
                  <td class="text-right pr-20 style-CZK">{{ overview.volny_cas.this_month | formatCZK }}</td>
                  <td class="flex justify-between items-center text-right pr-6 py-1">
                      <div class="w-1/2">
                          <div class='border border-virtus-menu h-3 rounded-full'>
                            <div class='h-full'></div>
                          </div>
                      </div>
                      <div class="style-CZK available-column"></div>
                  </td>
                </tr>
                <tr class="hover:bg-virtus-menu hover:bg-opacity-30">
                  <td class="pl-4 py-1">Majetek</td>
                  <td class="text-right pr-20 style-CZK">{{ overview.majetek.last_3M | formatCZK }}</td>
                  <td class="text-right pr-20 style-CZK">{{ 0 | formatCZK }}</td>
                  <td class="text-right pr-20 style-CZK">{{ overview.majetek.this_month | formatCZK }}</td>
                  <td class="flex justify-between items-center text-right pr-6 py-1">
                      <div class="w-1/2">
                          <div class='border border-virtus-menu h-3 rounded-full'>
                            <div class='h-full'></div>
                          </div>
                      </div>
                      <div class="style-CZK available-column"></div>
                  </td>
                </tr>
                <tr class="hover:bg-virtus-menu hover:bg-opacity-30">
                  <td class="pl-4 py-1">Doprava</td>
                  <td class="text-right pr-20 style-CZK">{{ overview.doprava.last_3M | formatCZK }}</td>
                  <td class="text-right pr-20 style-CZK">{{ 0 | formatCZK }}</td>
                  <td class="text-right pr-20 style-CZK">{{ overview.doprava.this_month | formatCZK }}</td>
                  <td class="flex justify-between items-center text-right pr-6 py-1">
                      <div class="w-1/2">
                          <div class='border border-virtus-menu h-3 rounded-full'>
                            <div class='h-full'></div>
                          </div>
                      </div>
                      <div class="style-CZK available-column"></div>
                  </td>
                </tr>
                <tr class="hover:bg-virtus-menu hover:bg-opacity-30">
                  <td class="pl-4 py-1">Služby</td>
                  <td class="text-right pr-20 style-CZK">{{ overview.sluzby.last_3M | formatCZK }}</td>
                  <td class="text-right pr-20 style-CZK">{{ -2500 | formatCZK }}</td>
                  <td class="text-right pr-20 style-CZK">{{ overview.sluzby.this_month | formatCZK }}</td>
                  <td class="flex justify-between items-center text-right pr-6 py-1">
                      <div class="w-1/2">
                          <div class='border border-virtus-menu h-3 rounded-full'>
                            <div class='h-full'></div>
                          </div>
                      </div>
                      <div class="style-CZK available-column"></div>
                  </td>
                </tr>
                <tr class="hover:bg-virtus-menu hover:bg-opacity-30">
                  <td class="pl-4 py-1">Rozvoj a vzdělání</td>
                  <td class="text-right pr-20 style-CZK">{{ overview.rozvoj_vzdelani.last_3M | formatCZK }}</td>
                  <td class="text-right pr-20 style-CZK">{{ -500 | formatCZK }}</td>
                  <td class="text-right pr-20 style-CZK">{{ overview.rozvoj_vzdelani.this_month | formatCZK }}</td>
                  <td class="flex justify-between items-center text-right pr-6 py-1">
                      <div class="w-1/2">
                          <div class='border border-virtus-menu h-3 rounded-full'>
                            <div class='h-full'></div>
                          </div>
                      </div>
                      <div class="style-CZK available-column"></div>
                  </td>
                </tr>
                <tr class="hover:bg-virtus-menu hover:bg-opacity-30">
                  <td class="pl-4 py-1">Práce</td>
                  <td class="text-right pr-20 style-CZK">{{ overview.prace_vydaje.last_3M | formatCZK }}</td>
                  <td class="text-right pr-20 style-CZK">{{ 0 | formatCZK }}</td>
                  <td class="text-right pr-20 style-CZK">{{ overview.prace_vydaje.this_month | formatCZK }}</td>
                  <td class="flex justify-between items-center text-right pr-6 py-1">
                      <div class="w-1/2">
                          <div class='border border-virtus-menu h-3 rounded-full'>
                            <div class='h-full'></div>
                          </div>
                      </div>
                      <div class="style-CZK available-column"></div>
                  </td>
                </tr>
                <tr class="hover:bg-virtus-menu hover:bg-opacity-30">
                  <td class="pl-4 py-1">Další výdaje</td>
                  <td class="text-right pr-20 style-CZK">{{ overview.dalsi_vydaje.last_3M | formatCZK }}</td>
                  <td class="text-right pr-20 style-CZK">{{ -1000 | formatCZK }}</td>
                  <td class="text-right pr-20 style-CZK">{{ overview.dalsi_vydaje.this_month | formatCZK }}</td>
                  <td class="flex justify-between items-center text-right pr-6 py-1">
                      <div class="w-1/2">
                          <div class='border border-virtus-menu h-3 rounded-full'>
                            <div class='h-full'></div>
                          </div>
                      </div>
                      <div class="style-CZK available-column"></div>
                  </td>
                </tr>
                <tr class="bg-virtus-header font-medium opacity-80">
                  <td class="pl-4 pt-2 pb-2 rounded-bl font-extralight text-xs">TOTAL</td>
                  <td class="text-right pr-20 style-CZK">{{ overview.vydaje_total.last_3M | formatCZK }}</td>
                  <td class="text-right pr-20 style-CZK"></td>
                  <td class="text-right pr-20 style-CZK">{{ overview.vydaje_total.this_month | formatCZK }}</td>
                  <td class="text-center rounded-br pr-4 style-CZK font-light text-base style-negative"></td>
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
                  <td class="text-right pr-20 style-CZK">46736.96</td>
                  <td class="text-right pr-20 style-CZK">0.00</td>
                  <td class="text-right pr-20 style-CZK">0</td>
                  <td class="flex justify-between items-center text-right pr-6 py-1">
                      <div class=""></div>
                  </td>
                </tr>
                <tr class="hover:bg-virtus-menu hover:bg-opacity-30">
                  <td class="pl-4 pt-1">Freelance</td>
                  <td class="text-right pr-20 style-CZK">10402.17</td>
                  <td class="text-right pr-20 style-CZK">0</td>
                  <td class="text-right pr-20 style-CZK">0</td>
                  <td class="flex justify-between items-center text-right pr-6 py-1">
                      <div class=""></div>
                  </td>
                </tr>
                <tr class="hover:bg-virtus-menu hover:bg-opacity-30">
                  <td class="pl-4 py-1">Další příjmy</td>
                  <td class="text-right pr-20 style-CZK">4014.39</td>
                  <td class="text-right pr-20 style-CZK">5000</td>
                  <td class="text-right pr-20 style-CZK">0</td>
                  <td class="flex justify-between items-center text-right pr-6 py-1">
                      <div class=""></div>
                  </td>
                </tr>


                <tr class="bg-virtus-header font-medium opacity-80">
                  <td class="pl-4 pt-2 pb-2 rounded-bl font-extralight text-xs">TOTAL</td>
                  <td class="text-right pr-20 style-CZK" id="income-last3m-total"></td>
                  <td class="text-right pr-20 style-CZK" id="income-expectations-total"></td>
                  <td class="text-right pr-20 style-CZK" id="income-reality-total"></td>
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
      overview: 0
    }
  },
  methods: {
    getOverview() {
      const path = 'http://localhost:5000/overview';
      axios.get(path)
        .then((res) => {
          this.overview = res.data.overview;
        })
    }
  },
  created() {
    this.getOverview()
  }
}
</script>

<style scoped>

</style>
