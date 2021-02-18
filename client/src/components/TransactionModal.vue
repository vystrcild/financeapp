<template>
  <div>

    <div @click.self="closeModal" @keyup.esc="closeModal" class="fixed w-screen h-screen top-0 left-0 z-50 bg-black bg-opacity-50">
        <div class="absolute top-40 left-72 w-8/12 rounded-lg shadow-lg bg-virtus-header text-white">

          <!-- header -->
            <div class="flex justify-end border-b border-virtus-menu text-white">
                <div @click="closeModal" class="py-2 pr-4 hover:text-virtus-primary">
                    <svg class="w-5 h-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                    </svg>
                </div>
            </div>
            <!-- body -->
            <form @submit.prevent="handleSubmit" id="transaction-form" class="flex p-4 justify-between items-center">

                <input type="text" placeholder="Kč" ref="amountField" required v-model="amount"
                       class="h-9 mt-2 text-sm pt-2 rounded bg-virtus-gray pl-2 w-32 focus:outline-none focus:border-transparent focus:ring-virtus-primary"
                       :class="{ 'border-virtus-red focus:border-virtus-red': errors.amountError.length }">

              <select name="from_account"  v-model="fromAccount" required class="h-9 mt-2 text-sm pt-2 rounded bg-virtus-gray focus:outline-none focus:border-transparent focus:ring-virtus-primary">
                <option value="Twisto">Twisto</option>
                <option value="Unicredit">Unicredit</option>
                <option value="Cash">Cash</option>
                <option value="Revolut">Revolut</option>
              </select>

              <select name="to_account" v-model="toAccount" class="h-9 mt-2 text-sm pt-2 rounded bg-virtus-gray focus:outline-none focus:border-transparent focus:ring-virtus-primary">
                <option value=""> </option>
                <option value="Twisto">Twisto</option>
                <option value="Unicredit">Unicredit</option>
                <option value="Cash">Cash</option>
                <option value="Revolut">Revolut</option>
              </select>

              <select name="category" v-model="category" required class="h-9 mt-2 text-sm pt-2 rounded bg-virtus-gray focus:outline-none focus:border-transparent focus:ring-virtus-primary">
                <option value="Nákupy">Nákupy</option>
                <option value="Volný čas">Volný čas</option>
                <option value="Bydlení">Bydlení</option>
                <option value="Služby">Služby</option>
              </select>

              <input type="text" v-model="description" placeholder="Description" class="h-9 mt-2 text-sm pt-2 rounded bg-virtus-gray focus:outline-none focus:border-transparent focus:ring-virtus-primary">

              <DatePicker @updatedate="pickDate" />

              <input type="checkbox" v-model="billable" class="mt-2 text-sm pt-2 rounded bg-virtus-gray focus:outline-none focus:border-transparent focus:ring-virtus-primary">

            </form>

            <!-- footer -->
            <div class="flex pt-2 pb-4 pl-4 pr-4 justify-between items-center">
                <div class="flex text-virtus-secondary font-light hover:underline items-center">
                    <svg class="w-5 h-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                    </svg>
                    <div>Add Transaction</div>
                </div>
                <div>
                  <button form="transaction-form" id="send-transaction" class="py-2 px-4 capitalize tracking-wide bg-virtus-primary text-gray-200 text-xs font-medium rounded hover:bg-virtus-menu focus:outline-none focus:bg-gray-700">Send</button>
                </div>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
import DatePicker from '../components/DatePicker.vue';
import axios from 'axios';

export default {
  name: "TransactionModal",
  components: {
    DatePicker
  },
  data() {
    return {
      amount : "",
      fromAccount: "Twisto",
      toAccount: "",
      category: "Nákupy",
      description: "",
      date: "",
      billable : false,
      errors: {
        amountError: ""
      },
    }
  },
  methods: {
    closeModal() {
      this.$emit("close")
    },
    handleSubmit(e) {
      const regex = new RegExp("-?\\d+(,|.)?\\d+"); // Is it number?
      console.log(regex.test(this.amount))
      if (!regex.test(this.amount)) {
        this.errors.amountError = "Error"
        console.log("Error")
        e.preventDefault()
      } else {
        const path = 'http://localhost:5000/send'
        const payload = {
          amount: this.amount,
          fromAccount: this.fromAccount,
          toAccount: this.toAccount,
          category: this.category,
          date: this.date,
          description: this.description,
          billable: this.billable
        }
        axios.post(path, payload)
          .then(() => {
            this.closeModal()
          })
      }
    },
    pickDate(value) {
      this.date = value
    }
  },
  mounted() {
    this.$refs.amountField.focus()
  }
}
</script>

<style scoped>

</style>
