<template>
  <div class="pt-10 pl-48">
    <h1 class="text-white font-light font-sans pt-3 pb-2 text-xl">Overview</h1>
    <OverviewTable />
    <div>
      <p> {{ expenses["AppStores"] }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import OverviewTable from '../components/OverviewTable.vue';

export default {
  name: "Overview",
  components: {
    OverviewTable
  },
  data() {
    return {
      expenses: [],
    };
  },
  methods: {
    getExpenses(){
      const path = 'http://localhost:5000/expenses';
      axios.get(path)
        .then((res) => {
          this.expenses = res.data.expenses;
        })
    }
  },
  created() {
    this.getExpenses();
  }
}
</script>

<style scoped>

</style>
