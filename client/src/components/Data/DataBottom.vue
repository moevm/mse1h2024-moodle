<template>
  <v-btn class="bottom-custom" type="submit">{{ bottomTitle }}</v-btn>
</template>

<script>
export default {
  name: 'DataBottom',
  props: ['bottomTitle']
};
</script>

<style>
v-btn{
  background-color: white;
}

.bottom-custom {
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
