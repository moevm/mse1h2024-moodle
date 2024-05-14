<template>
  <v-dialog width="auto">
    <v-card text="Выберите файлы, которые вы хотите скачать:" title="Скачать">
      <v-container fluid>
        <v-checkbox
          v-model="selected"
          label="Выбранная статистика в формате json"
          value="statistics"
        ></v-checkbox>
        <v-checkbox
          v-model="selected"
          label="Html-код страниц в формате json"
          value="pages"
        ></v-checkbox>
      </v-container>
      <template v-slot:actions>
        <v-btn class="ms-auto" text="Отмена" @click="$emit('close')"></v-btn>
        <v-btn
          color="primary"
          variant="tonal"
          text="Скачать"
          @click="download"
          :disabled="!selected.length"
        ></v-btn>
      </template>
    </v-card>
  </v-dialog>
</template>

<script>
import axios from "axios";
// const STAT_FILE_URL = "/api/download/";
const STAT_FILE_URL = "/data.json";

export default {
  emits: ["close"],
  name: "Dialog",
  props: ["info"],
  data() {
    return {
      selected: ["statistics"],
    };
  },
  methods: {
    download() {
      axios
        .get(STAT_FILE_URL, { responseType: "json" })
        .then((response) => {
          const blob = new Blob([JSON.stringify(response.data)], { type: "text/json" });
          const link = document.createElement("a");
          link.href = URL.createObjectURL(blob);
          link.download = "download.json";
          link.click();
          URL.revokeObjectURL(link.href);
        })
        .catch(console.error);
      this.$emit("close");
    },
  },
};
</script>

<style scoped>
@import "@/colors.css";
</style>
