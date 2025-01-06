<template>
  <h2>aktueller Status von ...</h2>
</template>
<script>
export default {
  name: 'StatusComponent',

  created() {
    this.getData();
    console.log('StatusComponent created');
  },


  methods: {
    async getData() {
      let res = await this.axios.get('http://localhost:3000/api/status');
      this.allData = res.data;
    },
  }
};
</script>
<style></style>
