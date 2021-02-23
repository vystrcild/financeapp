<template>
  <div class="pt-10 pl-48">
    <h1 class="text-white font-light font-sans pt-3 pb-2 text-xl">Cashflow</h1>
    <CashflowTable />
  </div>
</template>

<script>
import CashflowTable from "@/components/CashflowTable";

export default {
  name: "Cashflow",
  components: {
    CashflowTable
  }

}
</script>

<style scoped>

</style>
