<template>
        <v-dialog width="auto">
        <v-card text="Вы хотите скачать выбранную статистику в формате scv?" title="Скачать">
          <template v-slot:actions>
            <v-btn class="ms-auto" text="да" @click="download"></v-btn>
          </template>
        </v-card>
      </v-dialog>
</template>

<script>
export default {
  emits: ['close'],
  name: 'Dialog',
  props: {
    
  },
  data() {
    return {
      
    };
  },
  methods: {
    download(){
      this.$emit('close');
      console.log("успех")
    }
  }
}
</script>

<style scoped>
@import '@/colors.css';

</style>
