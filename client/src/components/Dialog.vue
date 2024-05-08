<template>
        <v-dialog width="auto">
        <v-card text="Вы хотите скачать выбранную статистику в формате csv?" title="Скачать">
          <template v-slot:actions>
            <v-btn class="ms-auto" text="Да" @click="download"></v-btn>
          </template>
        </v-card>
      </v-dialog>
</template>

<script>
import axios from "axios";

export default {
  emits: ['close'],
  name: 'Dialog',
  data() {
    return {
      
    };
  },
  methods: {
    download(){
      const STAT_URL = "/download.csv";
      this.$emit('close');
      axios.get(STAT_URL, {responseType: 'blob'})
        .then(response => {
          const blob = new Blob([response.data], {type: 'text/csv'})
          const link = document.createElement('a')
          link.href = URL.createObjectURL(blob)
          link.download = 'download.csv'
          link.click()
          URL.revokeObjectURL(link.href)
        }).catch(console.error)
    }
  }
}
</script>

<style scoped>
@import '@/colors.css';

</style>
