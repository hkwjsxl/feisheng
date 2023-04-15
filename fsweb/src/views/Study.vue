<template>
  <div class="player">
    <div id="player"></div>
    <div class="chapter-list">
      <h2>3天django基础</h2>
      <el-tree
          class="filter-tree"
          :data="state.data"
          :props="state.defaultProps"
          default-expand-all
          :filter-node-method="filterNode"
          :ref="ref_tree">
      </el-tree>
    </div>
  </div>
</template>

<script setup>
import {onMounted, reactive, watch} from "vue"
import http from "../utils/http"
import "../utils/player"

const state = reactive({
  // 章节课时列表
  data: [{
    id: 1,
    label: '1. 概述',
    children: [
      {id: 4, label: '1.1 基础环境'},
    ]
  }, {
    id: 2,
    label: '2. 快速入门',
    children: [
      {id: 5, label: '2.1 基本使用步骤'},
      {id: 6, label: '2.2 常用写法'}
    ]
  }, {
    id: 3,
    label: '3. 路由基础',
    children: [
      {id: 7, label: '3.1 路由基本概念'},
      {id: 8, label: '3.2 普通路由'}
    ]
  }],
  defaultProps: {
    children: 'children',
    label: 'label'
  }
})

let polyv = () => {
  let token = sessionStorage.token || localStorage.token;
  // 1. 到数据库中查询用户购买的课程，是否有当前章节
  let vid = "085a2e302a675951ad88c4480a8920df_0";

  // 2. 到数据库中查询当前用户购买的课程是否在有效期内
  var player = polyvPlayer({
    wrap: '#player',
    width: document.documentElement.clientWidth - 300, // 页面宽度
    height: document.documentElement.clientHeight,        // 页面高度
    forceH5: true,
    vid: vid,
    code: "root", // 一般是用户昵称
    // 视频加密播放的配置
    playsafe(vid, next) { // 向后端发送请求获取加密的token
      http.get(`course/polyv/token/${vid}/`, {
        headers: {
          "Authorization": "jwt " + token,
        }
      }).then(response => {
        // 获取播放视频的token令牌
        next(response.data.data.token);
      })
    }
  });
}

onMounted(() => {
  polyv();
  // 监听当前浏览器窗口的大小是否发生变化，让播放器随着窗口变化大小
  window.onresize = () => {
    document.querySelector(".pv-video-player").style.width = `${document.documentElement.clientWidth - 300}px`;
    document.querySelector(".pv-video-player").style.height = `${document.documentElement.clientHeight}px`;
  }

  let video = document.querySelector(".pv-video")
  // 监听是否是否播放中
  video.ontimeupdate = () => {
    console.log(video.currentTime)
    // 每隔几秒，发送一次ajax到服务端更新学习进度和课时进度
  }
})

</script>

<style scoped>
.chapter-list {
  position: absolute;
  top: 0;
  right: 0;
  width: 300px;
  background-color: #ccc;
}

.chapter-list h2 {
  height: 40px;
  line-height: 40px;
  text-indent: 1rem;
}
</style>