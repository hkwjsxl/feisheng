<template>
  <router-view></router-view>
</template>

<script setup>

</script>

<style>
/* 声明全局样式和项目的初始化样式 */
body,h1,h2,h3,h4,p,table,tr,td,ul,li,a,form,input,select,option,textarea{
  margin:0;
  padding: 0;
  font-size: 15px;
}
a{
  text-decoration: none;
  color: #333;
  cursor: pointer;
}
ul,li{
  list-style: none;
}
table{
  border-collapse: collapse; /* 合并边框 */
}
img{
  max-width: 100%;
  max-height: 100%;
}
input{
  outline: none;
}
</style>
