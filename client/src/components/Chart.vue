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