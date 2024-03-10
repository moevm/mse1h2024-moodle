<template>
  <v-btn class="button-custom" type="submit">{{ title }}</v-btn>
</template>

<script>
export default {
  name: 'DataButton',
  props: ['title']
};
</script>

<style>
v-btn{
  background-color: white;
}

.button-custom {
  font-family: Inter, sans-serif;
  font-size: 14px;
  font-weight: 300;
  width: 37%;
  color: white;
  background-color: #6B93B0;
  letter-spacing: -0.3px;
  border-radius: 5px;
  align-self: center;
}
</style>
