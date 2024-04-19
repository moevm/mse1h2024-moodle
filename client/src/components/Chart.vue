<template>
  <Line :data="chartData"/>
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
import { Line } from "vue-chartjs";

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
  components: { Line },
  props: {
    info: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      chartOptions: {
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
      let cloneInfo = this.info.slice(0);
      cloneInfo.sort(compareDate);
      console.log("After sort", cloneInfo);

      const dateCount = new Map();
      cloneInfo.forEach((action) => {
        let key = action.date + action.time;
        if (!dateCount.has(key)) {
          dateCount.set(key, 1);
        } else {
          let val = dateCount.get(key);
          dateCount.set(key, val + 1);
        }
      });
      console.log(dateCount);
      dateCount.entries().forEach(([key, value]) => {
        labels.push(key);
        data.push(value);
      });
      return {
        labels,
        datasets: [
          {data, borderColor: "#61dafb", label: "график", pointRadius: 1 },
        ],
      };
    },
  },
};
</script>


<style>
</style>