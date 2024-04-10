<template>
  <Navbar :username="name">
    <Filters>
      <Search v-model="search"></Search>
    </Filters>
    <StatisticsTable :info="statisticsInfo" v-model:search="search"></StatisticsTable>
  </Navbar>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import StatisticsTable from "@/components/Statistics/StatisticsTable.vue";
import axios from "axios";
import Filters from "@/components/Filters/Filters.vue";
import Search from "@/components/Filters/Search.vue";

const STAT_URL = "/api/statistics/";

export default {
  name: "Statistics",
  components: {Search, Filters, StatisticsTable, Navbar },

  data() {
    return {
      statisticsInfo: [],
      name: "",
      search: ""
    };
  },
  beforeMount() {
    let name = localStorage.getItem("name"); //name будет уже слепленным из имени и фамилии
    if (name) {
      this.name = name;
    } else {
      console.log("нет имени");
      this.$router.push("/start"); //переход на авторизацию, если не авторизован
    }
    //TODO редирект на страницу с ошибкой 401: не авторизован
  },
  mounted() {
    axios
        .get(STAT_URL)
        .then((response) => {
          console.log(response.data);
          response.data.forEach(element => {
            let firstLayer = {
              FIO: element.student,
              course: element.course,
              group: element.group,
            };
            element.actions.forEach(action =>{
              let secondLayer = {...firstLayer};
              secondLayer.action = `${action.action_type}\npage: ${action.page}\n${action.element_type} ${action.event_type}: "${action.element_name}"\n`;
              secondLayer.time = action.time;
              secondLayer.date = action.date;
              this.statisticsInfo.push(secondLayer);
            })
          });
        })
        .catch((error) => {
          alert("Ошибка при получении данных");
          console.error("Ошибка при получении данных:", error);
        });
  },
};
</script>

<style>
</style>
  