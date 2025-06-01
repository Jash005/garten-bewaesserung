<template>
  <h2>Manuelle Einstellungen</h2>

  <section>
    <button>einmalig EIN für 1 Minute</button>
    <button>einmalig EIN für 3 Minuten</button>
  </section>

  <section>
    <h3>aktuelle Einstellungen ändern:</h3>
    <form>
      <label name="nameConfiguration">Bezeichnung:</label>
      <input for="nameConfiguration" type="text">

      <label name="duration">Dauer (in min):</label>
      <input for="duration" type="number">

      <label name="zyklus">Zyklus (Uhrzeit):</label>
      <input for="zyklus">

      <button>Speichern</button>
    </form>
  </section>

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
