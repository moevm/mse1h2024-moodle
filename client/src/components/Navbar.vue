<template>
  <v-app>
    <v-app-bar app color="white accent-4" dark>
      <v-menu rounded="0">
        <template v-slot:activator="{ props }">
          <v-btn icon="mdi-menu" class="menu" v-bind="props"></v-btn>
        </template>
        <v-list rounded="0">
          <v-list-item
              class="custom-list-item"
              v-for="(item, i) in items"
              :key="i"
              @click="navigateTo(item.path)"
          >
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
      <v-img src="moevm.jpg" alt="Image Description" max-width="55px" max-height="50px"></v-img>
      <v-toolbar-title class="site-title">moevm statistics</v-toolbar-title>
      <v-spacer></v-spacer>
      <span class="custom-text">{{ username }}</span>
      <v-icon size="36" class="user">mdi-account-circle</v-icon>
    </v-app-bar>
    <div class="container">
      <StatisticsTable :info="statisticsInfo"></StatisticsTable>
    </div>
  </v-app>
</template>

<script>
import StatisticsTable from "@/components/Statistics/StatisticsTable.vue";

export default {
  name: 'Navbar',
  components: {StatisticsTable},
  props: ['username'],
  data() {
    return {
      items: [
        { title: "Добавить пользователя", path: '/addUser' },
        { title: "Выдать новый пароль", path: '/newPassword' }
      ],
      statisticsInfo: [
        {
          FIO: 'Беззубов Даниил Викторович',
          group: '1303',
          date: '25-02-2024',
          time: '23:33',
          course: 'Основы промышленной разработки ПО',
          action: 'Переключение вкладки'
        },
        {
          FIO: 'Чубан Дмитрий Вадимович',
          group: '1303',
          date: '24-02-2024',
          time: '23:33',
          course: 'Основы промышленной разработки ПО',
          action: 'Нажатие на кнопку "отправить"'
        },
        {
          FIO: 'Королева Полина Андреевна',
          group: '1303',
          date: '15-02-2024',
          time: '21:06',
          course: 'Web-технологии',
          action: 'Переключение вкладки'
        },
        {
          FIO: 'Чернякова Валерия',
          group: '1304',
          date: '24-12-2023',
          time: '20:00',
          course: 'Объектно-ориентированное программирование',
          action: 'Нажатие на кнопку "лекции"'
        },
        {
          FIO: 'Романенко Диана Сергеевна',
          group: '9303',
          date: '27-10-2023',
          time: '12:09',
          course: 'Web-технологии',
          action: 'Нажатие на кнопку "отправить"'
        }
      ],
    };
  },
  methods: {
    navigateTo(path) {
      this.$router.push(path);
    }
  }
}
</script>

<style scoped>
.container {
  margin-top: 8%;
}

.menu {
  color: #3C6170;
  border-radius: 0 !important;
}
.custom-list-item {
  font-family: Inter, sans-serif;
  font-size: 20px;
  color: #000000;
  font-weight: 400;
  border-radius: 0;
}
.site-title {
  font-family: Inter, sans-serif;
  font-size: 23px;
  color: #3C6170;
  font-weight: 300;
}
.custom-text {
  font-family: Inter, sans-serif;
  font-size: 19px;
  color: #000000;
  font-weight: 300;
}
.user {
  color: #a6a5a5;
  margin: 10px;
}
</style>
