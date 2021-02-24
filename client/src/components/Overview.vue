<template>
  <div class="pt-14 pl-48">
    <h1 class="text-white font-light font-sans pt-3 pb-2 text-xl">Overview</h1>
    <OverviewTable />
    <div>
      <p></p>
    </div>
  </div>
</template>

<script>
import OverviewTable from '../components/OverviewTable.vue';

export default {
  name: "Overview",
  components: {
    OverviewTable
  },
}
</script>

<style scoped>

</style>
