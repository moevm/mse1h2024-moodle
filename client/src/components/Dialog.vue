<template>
        <v-dialog width="auto">
        <v-card text="Вы можете скачать выбранную статистику в формате json или html-код страниц" title="Скачать">
          <template v-slot:actions>
            <v-btn class="ms-auto" text="Статистика" @click="download"></v-btn>
            <v-btn class="ms-auto" text="Страницы" @click="download"></v-btn>
          </template>
        </v-card>
      </v-dialog>
</template>

<script>
import axios from "axios";

export default {
  emits: ['close'],
  name: 'Dialog',
  props: ["info"],
  data() {
    return {
      
    };
  },
  methods: {
    convertToCsv(arr){
      const header = []
      for (let key in this.info[0]){
        if(key !== "Date") header.push(key)
      }
      const resCsv = [
        header.join(';'),
        ...arr.map(row => header.map(fieldName=>JSON.stringify(row[fieldName])).join(';'))
      ].join('\r\n');
      return resCsv;
    },
    download(){
      // let csv = this.convertToCsv(this.info);
      // this.$emit('close');
      // const blob = new Blob([csv], {type: 'text/csv'})
      // const link = document.createElement('a')
      // link.href = URL.createObjectURL(blob)
      // link.download = 'download.csv'
      // link.click()
      // URL.revokeObjectURL(link.href)
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
