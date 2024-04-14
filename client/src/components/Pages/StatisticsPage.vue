<template>
  <Navbar :username="name">
    <Filters>
      <div class="search-info">
        <Search v-model="search"></Search>
      </div>
      <div class="choose-type">
        <v-btn-toggle class="stat-type" v-model="selectedType" variant="outlined" color="blue">
          <v-btn value="graphic" class="graphic" icon="mdi-chart-line"></v-btn>
          <v-btn value="table" icon="mdi-format-align-justify"></v-btn>
        </v-btn-toggle>
      </div>
    </Filters>
    <StatisticsTable v-if="selectedType === 'table'" :info="statisticsInfo" v-model:search="search"></StatisticsTable>
    <Chart v-else></Chart>
  </Navbar>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import StatisticsTable from "@/components/Statistics/StatisticsTable.vue";
import axios from "axios";
import Filters from "@/components/Filters/Filters.vue";
import Search from "@/components/Filters/Search.vue";
import Chart from "@/components/Chart.vue";

const STAT_URL = "/api/statistics/";

export default {
  name: "Statistics",
  components: {Chart, Search, Filters, StatisticsTable, Navbar },

  data() {
    return {
      statisticsInfo: [],
      name: "",
      search: "",
      selectedType: 'table'
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
  }
};
</script>

<style>
@import '@/colors.css';
.search-info {
  width: 25%;
  margin: 0;
}

.choose-type {
  margin-right: 0;
}

.stat-type {
  transform: translateY(15%);
}

.stat-type .v-btn {
  color: var(--grey-7);
}
</style>
  