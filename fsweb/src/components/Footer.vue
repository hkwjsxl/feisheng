<template>
  <div class="footer">
    <ul>
      <li v-for="nav in nav.footer_nav_list">
        <a :href="nav.link" v-if="nav.is_http">{{ nav.name }}</a>
        <router-link :to="nav.link" v-else>{{ nav.name }}</router-link>
      </li>
    </ul>
    <p>Copyright © 韩科伟版权所有 | <a href="http://beian.miit.gov.cn/" target="_blank">冀ICP备2023015113号</a></p>
  </div>
</template>

<script setup>
import nav from "../api/nav.js";
// 获取脚部导航列表
nav.get_footer_nav().then(response => {
  nav.footer_nav_list = response.data.data.results;
})

</script>

<style scoped>
.footer {
  width: 100%;
  height: 128px;
  color: #545C63;
}

.footer ul {
  margin: 0 auto 16px;
  padding-top: 38px;
  width: 930px;
}

.footer ul li {
  float: left;
  width: 112px;
  margin: 0 35px;
  text-align: center;
  font-size: 14px;
}

.footer ul::after {
  content: "";
  display: block;
  clear: both;
}

.footer p {
  text-align: center;
  font-size: 12px;
}

.footer a {
  font-size: 12px;
}
</style>