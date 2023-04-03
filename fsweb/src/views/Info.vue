<template>
  <div class="detail">
    <Header/>
    <div class="main">
      <div class="course-info">
        <div class="wrap-left">
          <!-- 课程封面或封面商品 -->
          <AliPlayerV3
              ref="player"
              class="h-64 md:h-96 w-full rounded-lg"
              style="height: 100%; width: 100%;"
              :source="course.info.course_video"
              :cover="course.info.course_cover"
              :options="options"
              @play="onPlay($event)"
              @pause="onPause($event)"
              @playing="onPlaying($event)"
              v-if="course.info.course_video"
          />
          <img :src="course.info.course_cover" style="width: 100%;" alt="" v-else>
        </div>
        <div class="wrap-right">
          <h3 class="course-name">{{ course.info.name }}</h3>
          <p class="data">
            {{ course.info.students }}人在学&nbsp;&nbsp;&nbsp;&nbsp;课程总时长：{{
              course.info.pub_lessons
            }}课时/{{ course.info.lessons }}课时&nbsp;&nbsp;&nbsp;&nbsp;难度：{{ course.info.get_level_display }}</p>
          <div class="sale-time" v-if="course.info.discount.type">
            <p class="sale-type">{{ course.info.discount.type }}</p>
            <p class="expire" v-if="course.info.discount.expire>0">距离结束：仅剩
              {{ parseInt(course.info.discount.expire / 86400) }}天
              {{ fill0(parseInt(course.info.discount.expire / 3600 % 24)) }}小时
              {{ fill0(parseInt(course.info.discount.expire / 60 % 60)) }}分 <span
                  class="second">{{ fill0(parseInt(course.info.discount.expire % 60)) }}</span> 秒</p>
          </div>
          <div class="sale-time" v-if="!course.info.discount.type">
            <p class="sale-type">课程价格 ¥{{ parseFloat(course.info.price).toFixed(2) }}</p>
          </div>
          <p class="course-price" v-if="course.info.discount.price>=0">
            <span>活动价</span>
            <span class="discount">¥{{ parseFloat(course.info.discount.price).toFixed(2) }}</span>
            <span class="original">¥{{ parseFloat(course.info.price).toFixed(2) }}</span>
          </p>
          <div class="buy">
            <div class="buy-btn">
              <button class="buy-now">立即购买</button>
              <button class="free">免费试学</button>
            </div>
            <el-popconfirm title="您确认添加当前课程加入购物车吗？" @confirm="add_cart" confirmButtonText="确定"
                           cancelButtonText="取消">
              <template #reference>
                <div class="add-cart"><img src="../assets/cart-yellow.svg" alt="">加入购物车</div>
              </template>
            </el-popconfirm>
          </div>
        </div>
      </div>
      <div class="course-tab">
        <ul class="tab-list">
          <li :class="course.tabIndex===1?'active':''" @click="course.tabIndex=1">详情介绍</li>
          <li :class="course.tabIndex===2?'active':''" @click="course.tabIndex=2">课程章节 <span
              :class="course.tabIndex!==2?'free':''" v-if="course.con_free_study">(试学)</span>
          </li>
          <li :class="course.tabIndex===3?'active':''" @click="course.tabIndex=3">用户评论 (42)</li>
          <li :class="course.tabIndex===4?'active':''" @click="course.tabIndex=4">常见问题</li>
        </ul>
      </div>
      <div class="course-content">
        <div class="course-tab-list">
          <div class="tab-item" v-if="course.tabIndex===1" v-html="course.info.description">

          </div>
          <div class="tab-item" v-if="course.tabIndex===2">
            <div class="tab-item-title">
              <p class="chapter">课程章节</p>
              <p class="chapter-length">共{{ course.chapter_list.count }}章 {{ course.info.lessons }}个课时</p>
            </div>
            <div class="chapter-item" v-for="chapter in course.chapter_list.results">
              <p class="chapter-title"><img src="../assets/1.svg" alt="">第{{ chapter.orders }}章·{{ chapter.name }}</p>
              <div class="chapter-title" style="padding-left: 2.4rem;" v-if="chapter.summary"
                   v-html="chapter.summary"></div>
              <ul class="lesson-list">
                <li class="lesson-item" v-for="lesson in chapter.get_lesson_list">
                  <p class="name">
                    <span class="index">{{ chapter.orders }}-{{ lesson.orders }}</span>
                    {{ lesson.name }}
                    <span class="free" v-if="lesson.free_trail">免费</span>
                  </p>
                  <p class="time">{{ lesson.duration }} <img src="../assets/chapter-player.svg" alt=""></p>
                  <button class="try" v-if="lesson.free_trail">立即试学</button>
                  <button class="try" v-else>购买课程</button>
                </li>
              </ul>
            </div>
          </div>
          <div class="tab-item" v-if="course.tabIndex===3">
            用户评论
          </div>
          <div class="tab-item" v-if="course.tabIndex===4">
            常见问题
          </div>
        </div>
        <div class="course-side">
          <div class="teacher-info">
            <h4 class="side-title"><span>授课老师</span></h4>
            <div class="teacher-content">
              <div class="cont1">
                <img :src="course.info.teacher.avatar">
                <div class="name">
                  <p class="teacher-name">{{ course.info.teacher.name }}</p>
                  <p class="teacher-title">
                    {{ course.info.teacher.get_role_display }}，{{ course.info.teacher.title }}</p>
                </div>
              </div>
              <div class="narrative" v-html="course.info.teacher.brief"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <Footer/>
  </div>
</template>

<script setup>
import {reactive, ref} from "vue"
import {useRoute, useRouter} from "vue-router"
import Header from "../components/Header.vue"
import Footer from "../components/Footer.vue"
import {AliPlayerV3} from "vue-aliplayer-v3"
import course from "../api/course"
import {ElMessage} from 'element-plus'
import {fill0} from "../utils/func";
import cart from "../api/cart";
import {useStore} from "vuex";

const store = useStore()
let route = useRoute()
let router = useRouter()
let player = ref(null)


// 获取url地址栏上的课程ID
course.course_id = route.params.id;

// 简单判断课程ID是否合法
if (course.course_id > 0) {
  // 根据课程ID到服务端获取课程详情数据
  course.get_course().then(response => {
    course.info = response.data.data;
    clearInterval(course.timer);
    course.timer = setInterval(() => {
      if (course.info.discount.expire && course.info.discount.expire > 0) {
        course.info.discount.expire--
      }
    }, 1000);
    // 获取课程章节信息
    course.get_course_chapters().then(response => {
      course.chapter_list = response.data.data;
    })
  }).catch(error => {
    ElMessage.error({
      message: "非法的URL地址，无法获取课程信息！",
      duration: 1000,
      onClose() {
        router.go(-1)
      }
    })
  })
} else {
  ElMessage.error({
    message: "非法的URL地址，无法获取课程信息！",
    duration: 1000,
    onClose() {
      router.go(-1)
    }
  })
}

// 阿里云播放器的选项参数
const options = reactive({
  // source: "/src/assets/1.mp4",
  // cover: "/src/assets/course-1.png",

  autoplay: false,   // 是否自动播放
  preload: true,     // 是否自动预加载
  isLive: false,     // 切换为直播流的时候必填true
  // format: 'm3u8'  // 切换为直播流的时候必填
})

const onPlay = (event) => {
  console.log("播放视频");
  console.log(player.value.getCurrentTime());
}

const onPause = (event) => {
  console.log("暂停播放");
  console.log(player.value.getCurrentTime());
  console.log(player.value.getDuration());  // 获取视频长度
}

const onPlaying = (event) => {
  console.log("播放中");
  console.log(player.value.getCurrentTime());
}

// 添加商品到购物车
let add_cart = () => {
  let token = sessionStorage.token || localStorage.token
  // 详情页中添加商品到购物车，不用传递参数，直接使用state.course来获取课程信息
  cart.add_course_to_cart(course.course_id, token).then(response => {
    ElMessage.success(response.data.message.msg);
  }).catch(error => {
    console.log(error)
    ElMessage.error("error,请查看终端报错信息");
  })
}

</script>


<style scoped>
.main {
  background: #fff;
  padding-top: 30px;
}

.course-info {
  width: 1200px;
  margin: 0 auto;
  overflow: hidden;
}

.wrap-left {
  float: left;
  width: 690px;
  height: 388px;
  background-color: #000;
}

.wrap-right {
  float: left;
  position: relative;
  height: 388px;
}

.course-name {
  font-size: 20px;
  color: #333;
  padding: 10px 23px;
  letter-spacing: .45px;
}

.data {
  padding-left: 23px;
  padding-right: 23px;
  padding-bottom: 16px;
  font-size: 14px;
  color: #9b9b9b;
}

.sale-time {
  width: 464px;
  background: #fa6240;
  font-size: 14px;
  color: #4a4a4a;
  padding: 10px 23px;
  overflow: hidden;
}

.sale-type {
  font-size: 16px;
  color: #fff;
  letter-spacing: .36px;
  float: left;
}

.sale-time .expire {
  font-size: 14px;
  color: #fff;
  float: right;
}

.sale-time .expire .second {
  width: 24px;
  display: inline-block;
  background: #fafafa;
  color: #5e5e5e;
  padding: 6px 0;
  text-align: center;
}

.course-price {
  background: #fff;
  font-size: 14px;
  color: #4a4a4a;
  padding: 5px 23px;
}

.discount {
  font-size: 26px;
  color: #fa6240;
  margin-left: 10px;
  display: inline-block;
  margin-bottom: -5px;
}

.original {
  font-size: 14px;
  color: #9b9b9b;
  margin-left: 10px;
  text-decoration: line-through;
}

.buy {
  width: 464px;
  padding: 0px 23px;
  position: absolute;
  left: 0;
  bottom: 20px;
  overflow: hidden;
}

.buy .buy-btn {
  float: left;
}

.buy .buy-now {
  width: 125px;
  height: 40px;
  border: 0;
  background: #ffc210;
  border-radius: 4px;
  color: #fff;
  cursor: pointer;
  margin-right: 15px;
  outline: none;
}

.buy .free {
  width: 125px;
  height: 40px;
  border-radius: 4px;
  cursor: pointer;
  margin-right: 15px;
  background: #fff;
  color: #ffc210;
  border: 1px solid #ffc210;
}

.add-cart {
  float: right;
  font-size: 14px;
  color: #ffc210;
  text-align: center;
  cursor: pointer;
  margin-top: 10px;
}

.add-cart img {
  width: 20px;
  height: 18px;
  margin-right: 7px;
  vertical-align: middle;
}

.course-tab {
  width: 100%;
  background: #fff;
  margin-bottom: 30px;
  box-shadow: 0 2px 4px 0 #f0f0f0;

}

.course-tab .tab-list {
  width: 1200px;
  margin: auto;
  color: #4a4a4a;
  overflow: hidden;
}

.tab-list li {
  float: left;
  margin-right: 15px;
  padding: 26px 20px 16px;
  font-size: 17px;
  cursor: pointer;
}

.tab-list .active {
  color: #ffc210;
  border-bottom: 2px solid #ffc210;
}

.tab-list .free {
  color: #fb7c55;
}

.course-content {
  width: 1200px;
  margin: 0 auto;
  background: #FAFAFA;
  overflow: hidden;
  padding-bottom: 40px;
}

.course-tab-list {
  width: 880px;
  height: auto;
  padding: 20px;
  background: #fff;
  float: left;
  box-sizing: border-box;
  overflow: hidden;
  position: relative;
  box-shadow: 0 2px 4px 0 #f0f0f0;
}

.tab-item {
  width: 880px;
  background: #fff;
  padding-bottom: 20px;
  box-shadow: 0 2px 4px 0 #f0f0f0;
}

.tab-item-title {
  justify-content: space-between;
  padding: 25px 20px 11px;
  border-radius: 4px;
  margin-bottom: 20px;
  border-bottom: 1px solid #333;
  border-bottom-color: rgba(51, 51, 51, .05);
  overflow: hidden;
}

.chapter {
  font-size: 17px;
  color: #4a4a4a;
  float: left;
}

.chapter-length {
  float: right;
  font-size: 14px;
  color: #9b9b9b;
  letter-spacing: .19px;
}

.chapter-title {
  font-size: 16px;
  color: #4a4a4a;
  letter-spacing: .26px;
  padding: 12px;
  background: #eee;
  border-radius: 2px;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
}

.chapter-title img {
  width: 18px;
  height: 18px;
  margin-right: 7px;
  vertical-align: middle;
}

.lesson-list {
  padding: 0 20px;
}

.lesson-list .lesson-item {
  padding: 15px 20px 15px 36px;
  cursor: pointer;
  justify-content: space-between;
  position: relative;
  overflow: hidden;
}

.lesson-item .name {
  font-size: 14px;
  color: #666;
  float: left;
}

.lesson-item .index {
  margin-right: 5px;
}

.lesson-item .free {
  font-size: 12px;
  color: #fff;
  letter-spacing: .19px;
  background: #ffc210;
  border-radius: 100px;
  padding: 1px 9px;
  margin-left: 10px;
}

.lesson-item .time {
  font-size: 14px;
  color: #666;
  letter-spacing: .23px;
  opacity: 1;
  transition: all .15s ease-in-out;
  float: right;
}

.lesson-item .time img {
  width: 18px;
  height: 18px;
  margin-left: 15px;
  vertical-align: text-bottom;
}

.lesson-item .try {
  /*width: 86px;*/
  width: 90px;
  height: 28px;
  background: #ffc210;
  border-radius: 4px;
  font-size: 14px;
  color: #fff;
  position: absolute;
  right: 20px;
  top: 10px;
  opacity: 0;
  transition: all .2s ease-in-out;
  cursor: pointer;
  outline: none;
  border: none;
}

.lesson-item:hover {
  background: #fcf7ef;
  box-shadow: 0 0 0 0 #f3f3f3;
}

.lesson-item:hover .name {
  color: #333;
}

.lesson-item:hover .try {
  opacity: 1;
}

.course-side {
  width: 300px;
  height: auto;
  margin-left: 20px;
  float: right;
}

.teacher-info {
  background: #fff;
  margin-bottom: 20px;
  box-shadow: 0 2px 4px 0 #f0f0f0;
}

.side-title {
  font-weight: normal;
  font-size: 17px;
  color: #4a4a4a;
  padding: 18px 14px;
  border-bottom: 1px solid #333;
  border-bottom-color: rgba(51, 51, 51, .05);
}

.side-title span {
  display: inline-block;
  border-left: 2px solid #ffc210;
  padding-left: 12px;
}

.teacher-content {
  padding: 30px 20px;
  box-sizing: border-box;
}

.teacher-content .cont1 {
  margin-bottom: 12px;
  overflow: hidden;
}

.teacher-content .cont1 img {
  width: 54px;
  height: 54px;
  margin-right: 12px;
  float: left;
}

.teacher-content .cont1 .name {
  float: right;
}

.teacher-content .cont1 .teacher-name {
  width: 188px;
  font-size: 16px;
  color: #4a4a4a;
  padding-bottom: 4px;
}

.teacher-content .cont1 .teacher-title {
  width: 188px;
  font-size: 13px;
  color: #9b9b9b;
  white-space: nowrap;
}

.teacher-content .narrative {
  font-size: 14px;
  color: #666;
  line-height: 24px;
}
</style>