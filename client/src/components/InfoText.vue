<template>
  <p>{{ info }}</p>
</template>

<script>
export default {
  name: 'InfoText',
  props: ['info']
};
</script>

<style>
p {
  font-family: Inter, sans-serif;
  font-size: 14px;
  font-weight: 300;
  color: #101E29;
  padding-bottom: 3%;
  padding-top: 0;
  text-align: center;
  background-color: white;
}
</style>