<template>
  <v-form class="custom-form">
    <slot></slot>
  </v-form>
</template>

<script>
export default {
  name: 'DataForm',
};
</script>

<style>
.custom-form {
  text-align: center;
  background-color: white;
}
</style>