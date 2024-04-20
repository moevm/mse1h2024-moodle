<template>
  <Scatter :data="chartData" :options="chartOptions" />
</template>


<script>
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
import { Scatter } from "vue-chartjs";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);
export default {
  name: "Chart",
  components: { Scatter },
  props: {
    info: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      chartOptions: {
        scales: {
          x: {
            display: true,
          },
          y: {
            suggestedMin: 0,
            display: true,
            ticks: {
              stepSize: 1
            },
          },
        },
        responsive: true,
      },
    };
  },
  computed: {
    chartData() {
      // let labels = ['u', 'a', 'y'];
      let data = [];
      // let maxTime = null;
      // let minTime = null;
      function compareDate(a, b) {
        if (a.Date < b.Date) return -1;
        if (a.Date > b.Date) return 1;
        return 0;
      }
      let cloneInfo = this.info.slice(0);
      cloneInfo.sort(compareDate);
      let arr = cloneInfo
      // if(cloneInfo.length > 10){
        // let min = cloneInfo.at(0).Date;
        // let max = cloneInfo.at(-1).Date;
      //   let medium = +min + (max - min)/2
      //   console.log(new Date(medium))
      //   //cloneInfo.forEach()
      //   arr = cloneInfo
      // }else{
      //   arr = cloneInfo
      // }

      const dateCount = new Map();
      arr.forEach((action) => {
        let key = +action.Date;
        if (!dateCount.has(key)) {
          dateCount.set(key, 1);
        } else {
          let val = dateCount.get(key);
          dateCount.set(key, val + 1);
        }
      });
      dateCount.entries().forEach(([key, value]) => {
        data.push({x:key, y:value});
      });
      console.log(data);
      console.log(data.length)
      return {
        // labels,
        datasets: [
          {data, showLine: true, borderColor: "#61dafb", label: "график", pointRadius: 3 },
        ],
      };
    },
  },
};
</script>


<style>
</style>