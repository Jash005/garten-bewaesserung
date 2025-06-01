<template>
  <table border="1">
    <tr>
      <td>aktueller Status</td>
      <td class="colored"> {{ state2print || "Fehler im Aufruf" }}</td>
    </tr>
    <tr>
      <td>letzte Bewässerung</td>
      <td>{{ lastWatering || "Fehler im Aufruf" }}</td>
    </tr>
    <tr>
      <td>Dauer einer Bewässerung</td>
      <td>{{ durationWatering || "Fehler im Aufruf" }}</td>
    </tr>
  </table>


</template>
<script>
export default {
  name: 'StatusComponent',

  data() {
    return {
      state2print: "run", //this.allData.state,
      lastWatering: "12:30", //this.allData.lastWatering,
      durationWatering: "2 min", //this.allData.durationWatering
    }
  },

  // created() {
  //   this.getData();
  //   console.log('StatusComponent created');
  // },


  methods: {
    async getData() {
      let res = await this.axios.get('http://localhost:3000/api/status');
      this.allData = res.data;
    }
  }
};
</script>
<style>
.colored {
  color: red;
  font-weight: bolder;
}

table {
  border: 2px solid green;
}
table tr td:first-child {
  text-align: right;
}
table tr td:last-child {
  text-align: left;
}
</style>
