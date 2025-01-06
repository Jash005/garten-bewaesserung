<script setup>
import Wrapper from './components/Wrapper.vue'
</script>

<template>
  <div id="app">
    <header>
      <h1>Gewächshaus Bewässerungsanlage</h1>
    </header>

    <main>
      <div class="wrapper">
        <Wrapper />
      </div>
    </main>

    <footer>
      <div id="letzteZeile">Diese Website ist erstellt von <a href="http://jasminh.de/">Jasmin Hauschild</a> und dient ausschließlich für private Zwecke.</div>
    </footer>
  </div> <!-- ENDE #app -->
</template>

<style>
  body {
    font-family: Arial, Helvetica, sans-serif;
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    background-color: #25262e;
    color: #fff;
  }
</style>
<style scoped>

header {
  position: fixed;
  top: 0;
  left: 0;
  background-color: #1bcc50;
  color: #111;
  width: 100vw;
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

/* ====================================
            letzte Zeile
==================================== */
div#letzteZeile {
  font-family: Arial, Helvetica, sans-serif;
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  background-color: #111;
  color: #eee;
  text-align: center;
  padding: 6px;
  z-index: 5;
}
div#letzteZeile a {
  text-decoration: none;
  color: #ff8000;
}
div#letzteZeile a:hover {
  color: #eee;
  background-color: none;
}



@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
