<script setup>
  import Status from './Status.vue';
  import ManualConfigData from './ManualConfigData.vue';
</script>
<template>
  <button>NOT AUS</button>

  <button @click="normalbetrieb">Normalbetrieb</button>


<hr>

  <p v-if="loading">Lade Wasserstand...</p>
  <p v-else>Aktueller Wasserstand: {{ wasserstand }}</p>

  <Status />

  <ManualConfigData />
</template>
<script>
  import axios from 'axios';

  export default {
    data() {
      return {
        wasserstand: null, // Wert des Wasserstands
        loading: true,     // Status für das Laden der Daten
        isRunning: false   // Status für den Betrieb der Anlage
      };
    },

    name: 'WrapperComponent',

    methods: {
      async testMethod() {
        console.log('testMethod');
        try {
          let res = await axios.get('http://192.168.178.135:5000/api/wasserstand');
          this.wasserstand = res.data.wasserstand;
          console.log(res.data);
        } catch (error) {
          console.error(error);
        } finally {
          this.loading = false;
        }
      },

      async normalbetrieb() {
        if (this.isRunning) {
          console.log('Anlage ist bereits in Betrieb.');
          return;
        }

        this.isRunning = true;
        console.log('Normalbetrieb wird gestartet.');

        try {
          // Normalbetrieb im Backend starten
          const response = await axios.put('http://192.168.178.135:5000/api/normalbetrieb');
          console.log(response.data);
        } catch (error) {
          console.error('Fehler beim Starten des Normalbetriebs:', error);
        } finally {
          this.isRunning = false;
        }
      },

      async setOff() {
        try {
          let res = await axios.put('http://localhost:3000/api/setOff');
          console.log(res.data);
        } catch (error) {
          console.error(error);
        }
      },
    }
  }
</script>
<style></style>
