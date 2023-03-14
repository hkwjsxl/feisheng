<template>
  <div class="footer">
    <ul>
      <li>
        <router-link to="">企业服务</router-link>
      </li>
      <li>
        <router-link to="">关于我们</router-link>
      </li>
      <li>
        <router-link to="">联系我们</router-link>
      </li>
      <li>
        <router-link to="">商务合作</router-link>
      </li>
      <li>
        <router-link to="">帮助中心</router-link>
      </li>
      <li>
        <router-link to="">意见反馈</router-link>
      </li>
      <li>
        <router-link to="">新手指南</router-link>
      </li>
    </ul>
    <p>Copyright © luffycity.com版权所有 | 京ICP备17072161号-1</p>
  </div>
</template>

<script setup>

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
  margin: 0 10px;
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
</style>