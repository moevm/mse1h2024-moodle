<template>
        <v-dialog width="auto">
        <v-card text="Выберите файлы, которые вы хотите скачать:" title="Скачать">
          <v-container fluid>
            <v-checkbox v-model="selected" label="Выбранная статистика в формате json" value="statistics"></v-checkbox>
            <v-checkbox v-model="selected" label="Html-код страниц в формате json" value="pages"></v-checkbox>
          </v-container>
          <template v-slot:actions>
            <v-btn class="ms-auto" text="Отмена" @click="$emit('close')"></v-btn>
            <v-btn color="primary" variant="tonal" text="Скачать" @click="download" :disabled=!selected.length></v-btn>
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
      selected: ['statistics'],
      dis: false
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
