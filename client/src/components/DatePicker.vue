<template>
  <div>
    <vc-date-picker v-model="date" is-dark trim-weeks :attributes='attrs' is-required>
        <template v-slot="{ inputValue, inputEvents }" >
          <input
            class="h-9 mt-2 pl-2 text-sm rounded bg-virtus-gray focus:outline-none focus:border-transparent focus:ring-virtus-primary text-white"
            :value="inputValue"
            v-on="inputEvents"
          />
        </template>
    </vc-date-picker>
  </div>
</template>

<script>
import VCalendar from 'v-calendar';

export default {
  name: "DatePicker",
  components: VCalendar,
  data() {
    return {
      attrs: [
        {
          key: 'today',
          highlight: {
            color: 'blue',
            fillMode: 'outline',
          },
        },
      ],
      date: new Date(),
    };
  },
  computed: {
    formattedDate() {
      return ( this.date.getFullYear() + "-" + ('0' + (this.date.getMonth()+1)).slice(-2) + "-" + ('0' + this.date.getDate()).slice(-2) ); },
  },
  updated(){
      this.$emit('updatedate', this.formattedDate)
  }
}
</script>

<style scoped>

</style>
