<template>
  <h2>Manuelle Einstellungen</h2>

  <button>EIN für 1 Minute</button>
  <button>EIN für 3 Minuten</button>
</template>
<script>
export default {
  name: 'ManualConfigDataComponent',

  methods: {
    async setData() {
      try {
        let res = await this.axios.put('http://localhost:3000/api/setData', {
          // data
        });
        console.log(res.data);
      } catch (error) {
        console.error(error);
      }
    },
  }

}


</script>
<style></style>
