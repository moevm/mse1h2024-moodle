<template>
  <v-data-table
      class="custom-table"
      :headers="headers"
      :items="statistics"
      outlined
  >
    <template v-slot:[`item.checkbox`]="{ item }">
      <v-checkbox
          v-model="item.checked"
          color="primary"
          hide-details
      ></v-checkbox>
    </template>

    <template v-slot:[`item.FIO`]="{ item }">
      <p align="start">{{ item.FIO }}</p>
    </template>

    <template v-slot:[`item.group`]="{ item }">
      <v-chip :color="getColor(item.group)">
        {{ item.group }}
      </v-chip>
    </template>

    <template v-slot:[`item.course`]="{ item }">
      <p align="start">{{ item.course }}</p>
    </template>

    <template v-slot:[`item.action`]="{ item }">
      <p align="start">{{ item.action }}</p>
    </template>
  </v-data-table>
</template>

<script>
export default {
  name: 'StatisticsTable',
  props: {
    info: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      selected: [],
      selectedRows: [],
      headers: [
        { title: '№', key: 'number', sortable: false, align: 'center' },
        { title: '', key: 'checkbox', sortable: false, align: 'center' },
        { title: 'ФИО', key: 'FIO', sortable: false, align: 'center' },
        { title: 'Группа', key: 'group', sortable: false, align: 'center' },
        { title: 'Дата', key: 'date', sortable: false, align: 'center' },
        { title: 'Время', key: 'time', sortable: false, align: 'center' },
        { title: 'Название курса', key: 'course', sortable: false, align: 'center' },
        { title: 'Действие', key: 'action', sortable: false, align: 'center' },
      ],
    };
  },
  computed: {
    statistics() {
      return this.info.map((item, index) => ({
        ...item,
        number: (index + 1).toString()
      }));
    },
  },
  methods: {
    getColor(group) {
      const colors = ['red', 'blue', 'green', 'orange', 'purple', 'pink', 'magenta', 'teal', 'indigo', 'lime', 'brown'];
      const index = group % 11;
      return colors[index];
    },
  },
}
</script>

<style>
.custom-table {
  width: 95%;
  margin: 0 auto;
}

.custom-table tbody tr:nth-child(odd) {
  background-color: #F9F9F9;
}

.custom-table tbody tr {
  font-family: Inter, sans-serif;
  font-size: 15px;
}

.v-data-table .v-data-table-header th {
  font-weight: bolder !important;
  font-family: Inter, sans-serif;
}

.custom-table th, .custom-table td {
  border: 1px solid #DDDDDD;
}

</style>
