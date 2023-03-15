<template>
  <div class="home">
    <!--引入头部-->
    <Header></Header>

    <!--轮播图-->
    <div id="main">
      <Banner></Banner>
    </div>

    <!--引入尾部-->
    <Footer></Footer>
  </div>
</template>

<script setup>
import Header from "../components/Header.vue"
import Footer from "../components/Footer.vue"
import Banner from "../components/Banner.vue"
</script>

<style scoped>

</style>