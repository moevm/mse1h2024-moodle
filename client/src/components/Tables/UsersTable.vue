<template>
  <v-data-table
      class="custom-table-users"
      :headers="headers"
      :items="info"
      outlined
  >

    <template v-slot:[`item.actions`]>
      <v-icon>mdi-pencil</v-icon>
      <v-icon>mdi-delete</v-icon>
    </template>

  </v-data-table>
</template>

<script>
export default {
  name: "UsersTable",
  props: {
    info: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      headers: [
        { title: "ФИО", key: "FIO", sortable: false, align: "center" },
        { title: "Почта", key: "email", sortable: false, align: "center" },
        { title: "Роль", key: "position", sortable: false, align: "center" },
        { title: "Действия", key: "actions", sortable: false, align: "center" },
      ],
    };
  }
};
</script>

<style>
.custom-table-users {
  width: 80%;
  margin: 2% auto;
}

.custom-table-users  tbody tr:nth-child(odd) {
  background-color: var(--white-3);
}

.custom-table-users  tbody tr {
  font-family: Inter, sans-serif;
  font-size: 15px;
}

.custom-table-users .v-data-table-header th {
  font-weight: bolder !important;
  font-family: Inter, sans-serif;
}

.custom-table-users  th,
.custom-table-users td {
  border: 1px solid var(--white-2);
}

.custom-table-users .v-icon {
  color: var(--grey-7);
}

.custom-table-users .v-icon + .v-icon {
  margin-left: 10px;
}

#action {
  white-space: pre-line;
}
</style>