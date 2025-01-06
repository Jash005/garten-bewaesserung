<script setup>
  import Status from './Status.vue';
  import ManualConfigData from './ManualConfigData.vue';
</script>
<template>
  <button>NOT AUS</button>

  <Status />

  <ManualConfigData />
</template>
<script>
  export default {
    name: 'WrapperComponent',

    methods: {
      async setOff() {
        try {
          let res = await this.axios.put('http://localhost:3000/api/setOff');
          console.log(res.data);
        } catch (error) {
          console.error(error);
        }
      },
    }
  }
</script>
<style></style>
