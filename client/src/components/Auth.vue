<template>
  <Navbar username="Марк Заславский">
    <StatisticsTable :info="statisticsInfo"></StatisticsTable>
  </Navbar>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import StatisticsTable from "@/components/Statistics/StatisticsTable.vue";

export default {
  name: "Auth",
  components: {StatisticsTable, Navbar},

  data() {
    return {
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
};
</script>

<style>
</style>
