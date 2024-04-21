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
    search:{
      type: String,
      required: true
    }
  },
  data() {
    return {
      chartOptions: {
        scales: {
          x: {
            type: 'time',
            time:{
              unit: "day"
            },
            barThickness: 10,
            title: {
              display: true,
              text: "Временной промежуток"
            },
            display: true,
            ticks:{
              // autoSkip: false,
              maxTicksLimit: 20,
              minRotation: 80,
              callback: function(value){
                let date = new Date(value);
                const hours = date.getHours().toString().padStart(2, '0');
                const minutes = date.getMinutes().toString().padStart(2, '0');
                const seconds = date.getSeconds().toString().padStart(2, '0');
                const milliseconds = date.getMilliseconds().toString().padStart(3, '0');
                return `${date.toLocaleDateString('ru-RU')} ${hours}:${minutes}:${seconds}.${milliseconds}`;
                }
            }
          },
          y: {
            title: {
              display: true,
              text: "Количество событий"
            },
            suggestedMin: 0,
            display: true,
            ticks: {
              stepSize: 1
            },
          },
        },
        zoom: {
          enabled: true,
          drag: true
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
      
      return {
        labels,
        datasets: [
          {data,showLine: true, backgroundColor: "#61dafb", borderColor: "#61dafb", label: "график", label: "активность", barThickness: 2},
        ],
      };
    },
  },
};
</script>


<style>
</style>