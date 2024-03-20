<template>
  <AuthForm
      :title="title"
      :width="containerWidth"
      :height="containerHeight"
  >
    <DataForm fast-fail @submit.prevent="signIn">
      <DataInput v-model="email" label="Почта"></DataInput>
      <DataInput
          :append-inner-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
          v-model="password"
          label="Пароль"
          :type="show1 ? 'text' : 'password'"
          @click:append-inner="show1 = !show1">
      </DataInput>
      <p class="problems">В случае проблем пишите на admin@mail ru</p>
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
  name: "Authorization",
  components: {AuthForm, DataButton, DataForm, DataInput},

  data() {
    return {
      title: 'e.moevm statistics',
      containerWidth: '31%',
      containerHeight: '45%',
      email: '',
      password: '',
      show1: false,
    };
  },

  methods: {
    signIn() {
      const userName = "Тестовый Пользователь";
      localStorage.setItem("name", userName);
      this.$router.push('/e.moevm.statistics/statistics');
    }
  }
};
</script>

<style>
@import '@/colors.css';

.problems {
  font-family: Inter, sans-serif;
  font-size: 14px;
  font-weight: 300;
  color: var(--blue-3);
  padding-bottom: 3%;
  padding-top: 0;
  text-align: center;
  background-color: var(--white-1);
}
</style>