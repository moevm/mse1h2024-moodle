<template>
  <Navbar :username="name">
    <StatisticsTable :info="statisticsInfo"></StatisticsTable>
  </Navbar>
</template>
  
  <script>
import Navbar from "@/components/Navbar.vue";
import StatisticsTable from "@/components/Statistics/StatisticsTable.vue";

export default {
  name: "Statistics",
  components: { StatisticsTable, Navbar },

  data() {
    return { statisticsInfo: [], name: '' };
  },
  beforeMount(){
    let name = localStorage.getItem("name"); //name будет уже слепленным из имени и фамилии
      if (name) {
        this.name = name;
      }else{
          console.log("нет имени");
          this.$router.push('/start'); //переход на авторизацию, если не авторизован
      }
      //TODO редирект на страницу с ошибкой 401: не авторизован
  },
  mounted() {
    fetch("/data.json", { method: "GET" })
      .then((res) => res.json())
      .then(
        (res) => {
          console.log(res);
          this.statisticsInfo = res.map((element) => {
            return {
              ...element,
              FIO: element.surName + " " + element.firstName + " " + element.patronymic,
            };
          });
        },
        (error) => {
          console.log("error in statistics fetch", error);
        }
      );
  },
};
</script>
  
  <style>
</style>
  