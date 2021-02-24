<template>
  <div class="bg-blue-500">

    <!-- NavBar -->
    <header class="flex fixed w-full h-14 z-40 bg-virtus-nav shadow-lg text-white">
        <div class="flex w-full justify-between pl-4 pr-8">
            <div class="flex items-center justify-between">
                <div class="flex items-center">
                    <svg class="w-8 text-virtus-primary" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                      <path d="M8.433 7.418c.155-.103.346-.196.567-.267v1.698a2.305 2.305 0 01-.567-.267C8.07 8.34 8 8.114 8 8c0-.114.07-.34.433-.582zM11 12.849v-1.698c.22.071.412.164.567.267.364.243.433.468.433.582 0 .114-.07.34-.433.582a2.305 2.305 0 01-.567.267z" />
                      <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-13a1 1 0 10-2 0v.092a4.535 4.535 0 00-1.676.662C6.602 6.234 6 7.009 6 8c0 .99.602 1.765 1.324 2.246.48.32 1.054.545 1.676.662v1.941c-.391-.127-.68-.317-.843-.504a1 1 0 10-1.51 1.31c.562.649 1.413 1.076 2.353 1.253V15a1 1 0 102 0v-.092a4.535 4.535 0 001.676-.662C13.398 13.766 14 12.991 14 12c0-.99-.602-1.765-1.324-2.246A4.535 4.535 0 0011 9.092V7.151c.391.127.68.317.843.504a1 1 0 101.511-1.31c-.563-.649-1.413-1.076-2.354-1.253V5z" clip-rule="evenodd" />
                    </svg>
                    <div class="ml-4 font-medium text-sm">FINANCE APP</div>
                </div>
                <div class="ml-9 flex items-baseline">
                    <router-link @click.native="isActive = 'overview'" :to="{name: 'Overview'}" class="px-3 hover:bg-virtus-menu py-2 rounded-md text-sm font-medium" :class="{'text-virtus-secondary hover:text-white': isActive == 'overview'}">Overview</router-link>
                    <router-link @click.native="isActive = 'cashflow'" :to="{name: 'Cashflow'}" class="px-3 hover:bg-virtus-menu py-2 rounded-md text-sm font-medium" :class="{'text-virtus-secondary hover:text-white': isActive == 'cashflow'}">Cashflow</router-link>
                    <router-link @click.native="isActive = 'trends'" :to="{name: 'Trends'}" class="px-3 hover:bg-virtus-menu py-2 rounded-md text-sm font-medium" :class="{'text-virtus-secondary hover:text-white': isActive == 'trends'}">Trends</router-link>
                    <router-link @click.native="isActive = 'investments'" :to="{name: 'Investments'}" class="px-3 hover:bg-virtus-menu py-2 rounded-md text-sm font-medium" :class="{'text-virtus-secondary hover:text-white': isActive == 'investments'}">Investments</router-link>
                </div>
            </div>
            <div class="flex items-center">
                <div class="flex justify-center h-screen">
                <div class="flex items-center">
                <button @click="toggleModal" class="py-2 px-4 capitalize tracking-wide bg-virtus-primary text-gray-200 text-xs font-medium rounded hover:bg-virtus-menu focus:outline-none focus:bg-gray-700">+ Add Transaction</button>

                <span class="hidden border-2 border-virtus-nav"></span>

                  <div class="relative">
                    <button class="hidden relative z-10 block bg-virtus-primary rounded p-2 hover:bg-virtus-menu focus:outline-none focus:bg-gray-700">
                      <svg class="h-4 w-4 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                        </svg>
                    </button>
              </div>
        </div>
                    </div>
                </div>
            </div>
    </header>
    <div v-if="showModal">
      <TransactionModal @close="toggleModal"/>
    </div>

  </div>
</template>

<script>
import TransactionModal from '../components/TransactionModal.vue';

export default {
  name: 'Nav',
  components: {
    TransactionModal,
  },
  data() {
    return {
      showModal: false,
      isActive: ''
    }
  },
  methods: {
    toggleModal() {
      this.showModal = !this.showModal
    }
  }
}
</script>
