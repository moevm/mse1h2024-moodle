<template>
  <Navbar :username="name" :position="position">
    <Filters>
      <div class="search-info">
        <Search v-model="search" id="search-input"></Search>
      </div>
      <div class="date-time-info">
        <DateTime
            v-model="beginTimestamp"
            :max="endTimestamp || today"
            id="start-date"
        ></DateTime>
        <button id="reset-begin-date" class="reset-date" @click="resetBeginDate">Сброс</button>
        <p>—</p>
        <DateTime
            v-model="endTimestamp"
            :min="beginTimestamp"
            :max="today"
            id="end-date"
        ></DateTime>
        <button id="reset-end-date" class="reset-date" @click="resetEndDate">Сброс</button>
      </div>
      <v-btn variant="outlined" value="download" icon="mdi-download" class="download-button" @click="downloadDialog=true"></v-btn>
      <Dialog v-model="downloadDialog" @close="downloadDialog=false"></Dialog>
      <div class="choose-type">
        <v-btn-toggle class="stat-type" v-model="selectedType" variant="outlined" color="blue">
          <v-btn value="graphic" class="graphic" icon="mdi-chart-line" id="graph-button"></v-btn>
          <v-btn value="table" icon="mdi-format-align-justify" id="table-button"></v-btn>
        </v-btn-toggle>
      </div>
    </Filters>
    <StatisticsTable v-if="selectedType === 'table'" :info="statisticsInfo" v-model:search="search"></StatisticsTable>
    <Chart v-else :info="statisticsInfo" :search="search"></Chart>
  </Navbar>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import StatisticsTable from "@/components/Tables/StatisticsTable.vue";
import axios from "axios";
import Filters from "@/components/Filters/Filters.vue";
import Search from "@/components/Filters/Search.vue";
import Chart from "@/components/Chart.vue";
import DateTime from "@/components/Filters/DateTime.vue";
import Dialog from "@/components/Dialog.vue";

//const STAT_URL = "/api/statistics/";
const STAT_URL = "/data.json";

export default {
  name: "Statistics",
  components: {DateTime, Chart, Search, Filters, StatisticsTable, Navbar, Dialog},

  data() {
    return {
      statisticsInfo: [],
      name: "",
      search: "",
      selectedType: 'table',
      beginTimestamp: '',
      endTimestamp: '',
      today: '',
      position: '',
      downloadDialog: false
    };
  },
  beforeMount() {
    this.today = new Date().toISOString().slice(0, 16);
    let name = sessionStorage.getItem("name");
    if (name) {
      this.name = name;
      this.position = sessionStorage.getItem("position");
    } else {
      const error = 'Request failed with status code 401. You are not sign in!'
      alert(error)
      console.log("Не авторизован");
      this.$router.push("/e.moevm.statistics/auth");
    }
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
    resetBeginDate() {
      this.beginTimestamp = '';
    },

    resetEndDate() {
      this.endTimestamp = '';
    },

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
                studentId: element.student_id,
                email: element.email
              };
              element.actions.forEach(action =>{
                let secondLayer = {...firstLayer};
                secondLayer.typeAction = action.action_type;
                secondLayer.eventType = action.event_type;
                secondLayer.elementType = action.element_type;
                secondLayer.elementName = action.element_name;
                secondLayer.page = action.page
                const dateTime = new Date(action.timestamp);
                const hours = dateTime.getHours().toString().padStart(2, '0');
                const minutes = dateTime.getMinutes().toString().padStart(2, '0');
                const seconds = dateTime.getSeconds().toString().padStart(2, '0');
                const milliseconds = dateTime.getMilliseconds().toString().padStart(3, '0');
                secondLayer.time = `${hours}:${minutes}:${seconds}.${milliseconds}`;
                secondLayer.date = dateTime.toLocaleDateString('ru-RU');
                secondLayer.Date = dateTime;
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
  margin-right: 1%;
  margin-left: 1%;
  font-size: 16px;
  font-family: Inter, sans-serif;
  color: var(--grey-6);
}

.reset-date {
  margin-left: 1%;
  transform: translateY(12.5%);
  padding: 6px 10px 6px 10px;
  border-radius: 10px;
  background-color: var(--white-4);
  color: var(--blue-4);
}

.reset-date:hover {
  background-color: var(--white-5);
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

.download-button{
  border-radius: 7px;
  border: 1px solid var(--grey-1);
  color: var(--grey-7);
  transform: translateY(12.5%);
  
}
</style>
  