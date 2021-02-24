<template>
  <div class="pt-14 pl-48">
    <h1 class="text-white font-light font-sans pt-3 pb-2 text-xl">Investments</h1>
    <div>
      <InvestmentsTable />
    </div>
  </div>
</template>

<script>
import InvestmentsTable from "@/components/InvestmentsTable";

export default {
  name: "Investments",
  components: {
    InvestmentsTable
  }
}
</script>

<style scoped>

</style>
