<template>
  <Line :data="chartData" />
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
  props: ["stock"],
  data() {
    return { chartOptions: { responsive: true } };
  },
  computed: {
    chartData() {
      let labels = ["один", "два", "три"];
      let data = [1, 2, 3];
      return {
        labels,
        datasets: [{ data, borderColor: "#61dafb", label: "график", pointRadius: 1 }],
      };
    },
  },
};
</script>


<style>
</style>