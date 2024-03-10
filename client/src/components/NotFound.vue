<template>
  <AuthForm
      :title="title"
      :width="containerWidth"
      :height="containerHeight"
  >
    <DataForm>
      <DataInput v-model="inputLogin" label="Почта"></DataInput>
      <DataInput v-model="inputPassword" label="Фамилия"></DataInput>
      <p>В случае проблем пишите на admin@mail ru</p>
      <DataButton title='вход'></DataButton>
    </DataForm>
  </AuthForm>
</template>

<script>
import DataInput from "@/components/Data/DataInput.vue";
import DataForm from "@/components/Data/DataForm.vue";
import DataButton from "@/components/Data/DataButton.vue";
import AuthForm from "@/components/AuthForm.vue";

export default {
  name: "NotFound",
  components: {AuthForm, DataButton, DataForm, DataInput},

  data() {
    return {
      title: 'e.moevm statistics',
      containerWidth: '31%',
      containerHeight: '45%',
      inputLogin: '',
      inputPassword: '',
    };
  },
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
