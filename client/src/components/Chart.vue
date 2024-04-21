<template>
  <Bar :data="chartData" :options="chartOptions" />
</template>


<script>
/* eslint-disable */
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  TimeScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  BarElement,
} from "chart.js";
import { Bar } from "vue-chartjs";
import "chartjs-adapter-moment";

ChartJS.register(
  CategoryScale,
  LinearScale,
  TimeScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  BarElement
);
export default {
  name: "Chart",
  components: { Bar },
  props: {
    info: {
      type: Array,
      required: true,
    },
    search: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      chartOptions: {
        scales: {
          x: {
            type: "time",
            time: {
              displayFormats: {
                day: "DD MMM YYYY HH:mm:ss.sss",
              },
            },
            barThickness: 10,
            title: {
              display: true,
              text: "Временной промежуток",
            },
            display: true,
            ticks: {
              maxTicksLimit: 20,
              minRotation: 80,
              
            },
          },
          y: {
            title: {
              display: true,
              text: "Количество событий",
            },
            suggestedMin: 0,
            display: true,
            ticks: {
              stepSize: 1,
            },
          },
        },
        plugins: {
          tooltip: {
            callbacks: {
              title: function (tooltipItem) {
                console.log("tooltipItem", tooltipItem);
                let date = tooltipItem[0].parsed.x;
                return new Date(date).toISOString();
              },
            },
          },
        },
        responsive: true,
      },
    };
  },
  computed: {
    chartData() {
      let labels = [];
      let data = [];
      // let maxTime = null;
      // let minTime = null;
      function compareDate(a, b) {
        if (a.Date < b.Date) return -1;
        if (a.Date > b.Date) return 1;
        return 0;
      }
      console.log(typeof this.search, this.search);
      let searchLow = "";
      if (this.search) {
        searchLow = this.search.toLocaleLowerCase();
      }
      let cloneInfo = this.info.filter((action) => {
        return (
          action.studentId.toString().toLocaleLowerCase().includes(searchLow) ||
          action.FIO.toLocaleLowerCase().includes(searchLow) ||
          action.course.toLocaleLowerCase().includes(searchLow) ||
          action.typeAction.toLocaleLowerCase().includes(searchLow) ||
          action.action.toLocaleLowerCase().includes(searchLow) ||
          action.page.toLocaleLowerCase().includes(searchLow) ||
          action.time.toLocaleLowerCase().includes(searchLow) ||
          action.date.toLocaleLowerCase().includes(searchLow)
        );
      });
      cloneInfo.sort(compareDate);
      let arr = cloneInfo;
      let limit = 20;
      let delta = 100;
      if (cloneInfo.length > limit) {
        let min = cloneInfo.at(0).Date;
        let max = cloneInfo.at(-1).Date;
        delta = (max - min) / (limit * 100);
      }

      const dateCount = [];
      arr.forEach((action) => {
        let key = +action.Date;
        let ind = dateCount.findIndex(
          (element) => Math.abs(element[0] - key) < delta
        );
        if (ind < 0) {
          dateCount.push([key, 1]);
        } else {
          dateCount[ind][1] += 1;
        }
      });
      dateCount.forEach(([key, value]) => {
        labels.push(key);
        data.push(new Date(value));
      });
      console.log(data);
      return {
        labels,
        datasets: [
          {
            data,
            showLine: true,
            backgroundColor: "#61dafb",
            borderColor: "#61dafb",
            label: "график",
            label: "активность",
            barThickness: 4,
          },
        ],
      };
    },
  },
};
</script>


<style>
</style>