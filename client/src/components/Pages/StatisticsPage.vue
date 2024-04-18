<template>
  <Navbar :username="name">
    <Filters>
      <div class="search-info">
        <Search v-model="search"></Search>
      </div>
      <div class="date-time-info">
        <DateTime
            v-model="beginTimestamp"
            :max="endTimestamp || today"
        ></DateTime>
        <p>—</p>
        <DateTime
            v-model="endTimestamp"
            :min="beginTimestamp"
            :max="today"
        ></DateTime>
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
import DateTime from "@/components/Filters/DateTime.vue";

const STAT_URL = "/api/statistics/";

export default {
  name: "Statistics",
  components: {DateTime, Chart, Search, Filters, StatisticsTable, Navbar },

  data() {
    return {
      statisticsInfo: [],
      name: "",
      search: "",
      selectedType: 'table',
      beginTimestamp: '',
      endTimestamp: '',
      today: ''
    };
  },
  beforeMount() {
    this.today = new Date().toISOString().slice(0, 16);
    let name = localStorage.getItem("name");
    if (name) {
      this.name = name;
    } else {
      console.log("нет имени");
      this.$router.push("/start");
    }
    //TODO редирект на страницу с ошибкой 401: не авторизован
  },
  mounted() {
    this.getStatistics();
  },
  watch: {
    beginTimestamp() {
      this.getStatistics();
    },
    endTimestamp() {
      this.getStatistics();
    }
  },
  methods: {
    getStatistics() {
      this.statisticsInfo = []
      let params = {}
      if (this.beginTimestamp.length === 0 && this.endTimestamp.length === 0) {
        params = {}
      }
      else if (this.beginTimestamp.length !== 0 && this.endTimestamp.length === 0) {
        params = {
          begin_timestamp: this.beginTimestamp
        }
      }
      else if (this.beginTimestamp.length === 0 && this.endTimestamp.length !== 0) {
        params = {
          end_timestamp: this.endTimestamp
        }
      }
      else {
        params = {
          begin_timestamp: this.beginTimestamp,
          end_timestamp: this.endTimestamp
        }
      }


      axios
          .get(STAT_URL, { params })
          .then((response) => {
            console.log(response);
            response.data.forEach(element => {
              let firstLayer = {
                FIO: element.student,
                course: element.course,
              };
              element.actions.forEach(action =>{
                let secondLayer = {...firstLayer};
                secondLayer.typeAction = action.action_type
                secondLayer.action = `${action.event_type} ${action.element_type} "${action.element_name}"`;
                secondLayer.page = action.page
                const dateTime = new Date(action.timestamp);
                const hours = dateTime.getHours().toString().padStart(2, '0');
                const minutes = dateTime.getMinutes().toString().padStart(2, '0');
                const seconds = dateTime.getSeconds().toString().padStart(2, '0');
                const milliseconds = dateTime.getMilliseconds().toString().padStart(3, '0');
                secondLayer.time = `${hours}:${minutes}:${seconds}.${milliseconds}`;
                secondLayer.date = dateTime.toLocaleDateString('ru-RU');
                this.statisticsInfo.push(secondLayer);
              })
            });
          })
          .catch((error) => {
            alert("Ошибка при получении данных");
            console.error("Ошибка при получении данных:", error);
          });
    }
  }
};
</script>

<style>
@import '@/colors.css';
.search-info {
  width: 25%;
  margin: 0;
}

.date-time-info {
  margin: 0;
  display: flex;
  align-items: center;
}

.date-time-info p {
  margin-top: 1%;
  margin-right: 2%;
  margin-left: 2%;
  font-size: 16px;
  font-family: Inter, sans-serif;
  color: var(--grey-6);
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
  