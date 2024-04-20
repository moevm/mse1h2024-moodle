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
      function compareDate(a, b) {
        if (a.Date < b.Date) return -1;
        if (a.Date > b.Date) return 1;
        return 0;
      }
      console.log(typeof this.search, this.search)
      let searchLow = this.search.toLocaleLowerCase();
      let cloneInfo = this.info.filter((action, index)=>{
        return (index+1).toString().toLocaleLowerCase().includes(searchLow)
         || action.FIO.toLocaleLowerCase().includes(searchLow)
         || action.course.toLocaleLowerCase().includes(searchLow) 
         || action.typeAction.toLocaleLowerCase().includes(searchLow) 
         || action.action.toLocaleLowerCase().includes(searchLow)
         || action.page.toLocaleLowerCase().includes(searchLow) 
         || action.time.toLocaleLowerCase().includes(searchLow) 
         || action.date.toLocaleLowerCase().includes(searchLow)
      })
      cloneInfo.sort(compareDate);
      let arr = cloneInfo
      let limit = 20;
      let delta = 100;
      if(cloneInfo.length > limit){
        let min = cloneInfo.at(0).Date;
        let max = cloneInfo.at(-1).Date;
        delta = (max - min)/(limit*100)
      }

      const dateCount = [];
      arr.forEach((action) => {
        let key = +action.Date;
        let ind = dateCount.findIndex(element => Math.abs(element[0]-key)<delta)
        if (ind<0) {
          dateCount.push([key, 1]);
        } else {
          dateCount[ind][1] +=1;
        }
      });
      dateCount.forEach(([key, value]) => {
        labels.push(key)
        data.push(new Date(value));
      });
      console.log(data);
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