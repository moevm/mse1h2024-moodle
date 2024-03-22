<template>
  <AuthForm
      :title="title"
      :width="containerWidth"
      :height="containerHeight"
  >
    <DataForm fast-fail>
      <DataInput v-model="email" label="Почта"></DataInput>
      <DataInput v-model="surname" label="Фамилия"></DataInput>
      <DataInput v-model="name" label="Имя"></DataInput>
      <DataInput v-model="lastname" label="Отчество"></DataInput>
      <DataInput
          :append-inner-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
          v-model="password"
          label="Пароль"
          :type="show1 ? 'text' : 'password'"
          @click:append-inner="show1 = !show1">
      </DataInput>
      <DataButton title='готово' @click="createUser"></DataButton>
      <DataButton class="cancel" title='отмена' @click.prevent="cancel"></DataButton>
    </DataForm>
  </AuthForm>
</template>

<script>
import DataInput from "@/components/Data/DataInput.vue";
import DataForm from "@/components/Data/DataForm.vue";
import DataButton from "@/components/Data/DataButton.vue";
import AuthForm from "@/components/AuthForm.vue";

import axios from 'axios';

const CREATE_URL = '/api/user/'

export default {
  name: "CreateUser",
  components: {AuthForm, DataButton, DataForm, DataInput},

  data() {
    return {
      title: 'Регистрация',
      containerWidth: '27%',
      containerHeight: '75%',
      email: '',
      surname: '',
      name: '',
      lastname: '',
      password: '',
      show1: false
    };
  },

  methods: {
    async createUser() {
      const userData = {
        email: this.email,
        surname: this.surname,
        name: this.name,
        lastname: this.lastname,
        password: this.password
      };

      try {
        const response = await axios.post(CREATE_URL, userData);
        alert('Пользователь успешно создан');
        console.log('Пользователь успешно создан:', response.data);
        this.cancel();
      } catch (error) {
        alert('Ошибка при создании пользователя');
        console.error('Ошибка при создании пользователя:', error);
      }
    },

    cancel() {
      this.email = '';
      this.surname = '';
      this.name = '';
      this.lastname = '';
      this.password = '';
    }
  }
};
</script>

<style>
@import '@/colors.css';

.cancel {
  background-color: var(--grey-5);
  margin-left: 2%;
}
</style>
