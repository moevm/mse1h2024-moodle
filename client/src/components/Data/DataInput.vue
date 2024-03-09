<template>
  <v-text-field
      class="custom-text-field"
      variant="outlined"
      v-model="model"
      :label="label"
  ></v-text-field>
</template>

<script>
export default {
  name: 'DataInput',
  props: {
    value: String,
    label: String,
  },
  data() {
    return {
      model: this.value || "",
    };
  },
};
</script>

<style>
.custom-text-field {
  width: 85%;
  min-height: 20px;
  margin-left: auto;
  margin-right: auto;
  color: #C8C8C8;
}

.custom-text-field .v-label {
  font-size: 14px !important;
  font-family: Inter, sans-serif;
  font-weight: 300;
}

.custom-text-field .v-input__control input {
  font-size: 14px;
  font-family: Inter, sans-serif;
  font-weight: 300;
  color: #7e7e7e;
}
</style>
