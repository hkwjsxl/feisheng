<template>
  <div class="player">
    <div id="player"></div>
    <div class="chapter-list">
      <h2>{{ course.course_info.name }}</h2>
      <el-tree
          v-if="course.current_lesson"
          highlight-current
          class="filter-tree"
          :data="course.lesson_list"
          default-expand-all
          node-key="id"
          @node-click="node_click"
          :current-node-key="`lesson-`+course.current_lesson"
      >
      </el-tree>
    </div>
  </div>
</template>

<script setup>
import {onMounted, reactive, watch} from "vue"
import http from "../utils/http"
import course from "../api/course";
import "../utils/player"
import {useRoute} from "vue-router";
import store from "../store/index.js";
import settings from "../settings.js";

const route = useRoute()

// 获取路由参数[课程ID]
course.course_id = route.params.course;

// 获取课程信息
course.get_course().then(response => {
  course.course_info = response.data.data;
  // console.log("course_info", course.course_info)
  let ret = []
  let chapter_item = {}

  for (let chapter of course.course_info.get_chapter_list) {
    chapter_item = {id: 'chapter-' + chapter.id, label: `${chapter.orders}. ${chapter.name}`, children: []}
    // 判断当前章节下如果有课时列表
    if (chapter.lesson_list) {
      for (let lesson of chapter.lesson_list) {
        chapter_item.children.push({
          id: 'lesson-' + lesson.id,
          label: `${chapter.orders}.${lesson.orders} ${lesson.name}`,
          lesson: lesson
        })
      }
    }
    ret.push(chapter_item)
  }

  course.lesson_list = ret
})

// 当用户点击右侧课程的章节课时的回调函数
const node_click = (data) => {
  // 先删除原来的播放器
  // course.player?.destroy(); // 如果course.player为True，则调用course.player.destroy();// 新建一个播放器
  // console.log(data.lesson.lesson_link)
  if (!data.lesson) {
    return;
  }

  let token = sessionStorage.token || localStorage.token;
  course.get_lesson_study_time(data.lesson.id, token,).then(response => {
    // 先删除原来的播放器
    try {
      course.player.destroy();
    } catch (error) {
    }
    // 重置视频播放时间
    course.current_time = response.data.data;
    // 重置当前播放的课时ID
    course.current_lesson = data.lesson.id
    // console.log("course.current_lesson", course.current_lesson)
    // 新建一个播放器
    polyv(data.lesson.lesson_link);
  })
}

let polyv = (vid) => {
  let token = sessionStorage.token || localStorage.token;
  // 1. 到数据库中查询用户购买的课程，是否有当前章节
  // let vid = "";
  // 2. 到数据库中查询当前用户购买的课程是否在有效期内
  course.player = polyvPlayer({
    wrap: '#player',
    width: document.documentElement.clientWidth - 300, // 页面宽度
    height: document.documentElement.clientHeight,     // 页面高度
    forceH5: true,
    vid: vid,
    // code: "root", // 一般是用户昵称
    code: store.state.user.username, // 一般是用户昵称
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

  // 设置播放进度
  course.player.on('s2j_onPlayerInitOver', (e) => {
    course.player.j2s_seekVideo(course.current_time);
  });

  // 设置自动播放，但是谷歌浏览器会拦截自动播放
  try {
    course.player.j2s_resumeVideo();
  } catch (error) {

  }

  let video = document.querySelector(".pv-video")
  // 监听是否是否播放中
  video.ontimeupdate = () => {
    let watch_time = parseInt(video.currentTime);
    // console.log("watch_time", watch_time)
    if (watch_time % settings.seed_time === 0) {
      if (course.current_time < watch_time) {
        // 监听当前课时的播放时间
        course.current_time = watch_time;
      }
    }
  }

}

onMounted(() => {
  // 页面加载完成以后，自动从服务端获取用户在当前课程课程的学习进度。【要直到当前学到第几章、第几节、什么时间？】
  let token = sessionStorage.token || localStorage.token

  course.get_user_course(token).then(response => {
    // 获取到服务端返回的课程学习进度记录
    let response_data = response.data.data;
    course.user_course = response_data   // 用户在当前课程的学习进度记录
    course.current_chapter = 'chapter-' + response_data.chapter_id // 正在学习的章节ID
    course.current_lesson = 'lesson-' + response_data.lesson_id   // 正在学习的课时ID
    course.lesson_link = response_data.lesson_link               // 当前正在学习的课时视频ID

    // 从学习进度记录中提取正在学习的课时的视频ID
    polyv(course.lesson_link);
  })

  // 监听当前浏览器窗口的大小是否发生变化，让播放器随着窗口变化大小
  window.onresize = () => {
    document.querySelector(".pv-video-player").style.width = `${document.documentElement.clientWidth - 300}px`;
    document.querySelector(".pv-video-player").style.height = `${document.documentElement.clientHeight}px`;
  }

  // 开始自动播放
  try {
    course.player.j2s_resumeVideo();
  } catch (error) {

  }
})


watch(
    () => course.current_time,
    () => {
      console.log("current_time", course.current_time);
      let token = sessionStorage.token || localStorage.token;
      let lesson = course.current_lesson;
      course.update_user_study_progress(lesson, settings.seed_time, token).then(response => {
        console.log(response.data.message);
      })
    }
)

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