<template>
  <Header></Header>
  <main class="clearfix">
    <div class="bg-other user-head-info">
      <div class="user-info clearfix">
        <div class="user-pic" data-is-fans="0" data-is-follows="">
          <div class="user-pic-bg"><img class="img" :src="settings.host + store.state.user.avatar" alt=""></div>
        </div>
        <div class="user-info-right">
          <h3 class="user-name clearfix">
            <span v-if="store.state.user.username">{{ store.state.user.username }}</span>
            <span v-else>None</span>
          </h3>
          <p class="about-info">
            <!--<span>CG影视动画师</span>-->
            <span>一级码农</span>
          </p>
        </div>
        <div class="user-sign hide">
          <p class="user-desc">这位同学很懒，木有签名的说～</p>
        </div>
        <div class="study-info clearfix">
          <div class="item follows">
            <div class="u-info-learn" title="学习时长16分" style="cursor:pointer;">
              <em>{{ store.state.user.study_time }}</em>
              <span>学习时长 </span>
            </div>
          </div>
          <div class="item follows">
            <router-link to="/u/index/credit"><em>{{ store.state.user.credit }}</em></router-link>
            <span>积分</span>
          </div>
          <div class="item follows">
            <router-link to="/user/setbindsns" class="set-btn"><i class="icon-set"></i>个人设置</router-link>
          </div>
        </div>
      </div>
    </div>
    <div class="main clearfix">
      <div class="slider l">
        <h1>个人中心</h1>
        <ul class="nav-menu">
          <li class="clearfix" :class="{active:route.path === '/user'}">
            <router-link to="/user">
              <p class="nav-name l">个人信息</p>
              <span class="el-icon-caret-right r"></span>
            </router-link>
          </li>
          <li class="clearfix" :class="{active:route.path === '/user/course'}">
            <router-link to="/user/course">
              <p class="nav-name l">我的课程</p>
              <span class="el-icon-caret-right r"></span>
            </router-link>
          </li>
          <li class="clearfix" :class="{active:route.path === '/user/order'}">
            <router-link to="/user/order">
              <p class="nav-name l">我的订单</p>
              <span class="el-icon-caret-right r"></span>
            </router-link>
          </li>
          <li class="clearfix" :class="{active:route.path === '/user/balance'}">
            <router-link to="/user/balance">
              <p class="nav-name l">我的余额</p>
              <span class="el-icon-caret-right r"></span>
            </router-link>
          </li>
          <li class="clearfix" :class="{active:route.path === '/user/coupon'}">
            <router-link to="/user/coupon">
              <p class="nav-name l">我的优惠券</p>
              <span class="el-icon-caret-right r"></span>
            </router-link>
          </li>
          <li class="clearfix" :class="{active:route.path === '/user/bill'}">
            <router-link to="/user/bill">
              <p class="nav-name l">我的消费记录</p>
              <span class="el-icon-caret-right r"></span>
            </router-link>
          </li>
        </ul>
      </div>
      <!-- 嵌套路由，也是依靠router-view来加载不同的子页面内容 -->
      <router-view></router-view>
    </div>
  </main>
  <Footer></Footer>
</template>

<script setup>
import Header from "../components/Header.vue"
import Footer from "../components/Footer.vue"
import settings from "../settings";
import {useStore} from "vuex"
import {useRoute} from "vue-router"

const store = useStore()
const route = useRoute()

</script>

<style scoped>
main {
  margin-bottom: 40px;
}

.bg-other {
  background: url("../assets/user_bg.png") no-repeat center top #000;
  background-size: cover;
}

.user-head-info {
  min-height: 200px;
}

.user-head-info .user-info {
  position: relative;
  width: 1500px;
  margin: 0 auto;
  min-height: 200px;
}

.user-head-info .user-info .user-pic {
  float: left;
  width: 148px;
  height: 148px
}

.user-head-info .user-info .user-pic .user-pic-bg {
  border: 4px solid #fff;
  box-shadow: 0 4px 8px 0 rgba(7, 17, 27, .1);
  width: 140px;
  height: 140px;
  position: relative;
  border-radius: 50%;
  background: #fff;
  top: 24px
}

.user-head-info .user-info .user-pic .user-pic-bg .img {
  text-align: center;
  width: 140px;
  height: 140px;
  border-radius: 50%
}

.user-head-info .user-info .user-info-right {
  float: right;
  width: 1330px;
}

.user-head-info .user-info .user-name {
  font-weight: 600;
  text-align: left;
  font-size: 24px;
  color: #fff;
  line-height: 28px;
  margin-top: 48px;
  margin-bottom: 10px;
}

.user-head-info .user-info .about-info {
  font-size: 14px;
  color: #fff;
  line-height: 20px;
  text-align: left;
  margin-top: 6px;
  display: block;
}

.user-head-info .user-info .about-info span {
  display: inline-block;
  margin-right: 10px;
  font-size: 14px;
  color: #fff;
  line-height: 20px
}

.user-head-info .user-info .user-sign {
  font-size: 14px;
  color: #fff;
  line-height: 24px;
  width: 440px;
  overflow: hidden;
  word-break: break-all;
  word-wrap: break-word
}

.user-head-info .user-info .user-desc {
  font-size: 14px;
  line-height: 24px;
  color: #fff;
  text-align: left;
  margin-top: 20px;
  word-break: break-all;
  word-wrap: break-word;
  opacity: .8;
  margin-left: 24px
}

.user-head-info .study-info {
  position: absolute;
  top: 48px;
  right: 10px;
  min-width: 200px;
  text-align: right
}

.user-head-info .study-info .item {
  line-height: 48px;
  vertical-align: middle;
  height: 48px;
  float: left
}

.user-head-info .study-info .item em {
  display: block;
  text-align: center;
  font-weight: 700;
  font-size: 24px;
  color: rgba(255, 255, 255, .8);
  line-height: 28px
}

.user-head-info .study-info .item span {
  display: block;
  text-align: center;
  font-size: 14px;
  color: rgba(255, 255, 255, .8);
  line-height: 20px;
  margin-top: 4px
}

.user-head-info .study-info .follows {
  margin-right: 24px
}

.user-head-info .study-info .set-btn {
  padding: 8px 16px;
  border: 1px solid rgba(255, 255, 255, .4);
  border-radius: 18px;
  font-size: 14px;
  color: rgba(255, 255, 255, .8);
  line-height: 20px;
  height: 20px
}

.user-head-info .study-info .set-btn i {
  font-size: 16px;
  display: inline-block;
  margin-right: 4px
}

.user-head-info .study-info .set-btn:hover {
  color: #fff;
  border-color: #fff
}

.l {
  float: left;
}

.r {
  float: right;
}

.clearfix:after {
  content: '\0020';
  display: block;
  height: 0;
  clear: both;
  visibility: hidden;
}

.main {
  width: 1500px;
  margin: 36px auto;
}

.slider {
  margin-right: 32px;
  width: 180px;
  box-sizing: border-box
}

.slider h1 {
  padding-bottom: 16px;
  font-size: 14px;
  color: #4d555d;
  line-height: 32px;
  border-bottom: 1px solid #d9dde1
}

.slider .nav-menu {
  width: 100%
}

.slider .nav-menu li {
  margin-top: 16px;
  width: 100%;
  height: 32px;
  line-height: 32px;
  box-sizing: border-box;
  cursor: pointer;
  font-size: 14px;
  color: #4d555d
}

.slider .nav-menu li a {
  color: #07111b
}

.slider .nav-menu li a:hover {
  color: #f01414
}

.slider .nav-menu li .nav-name {
  font-size: 14px
}

.slider .nav-menu li .el-icon-caret-right {
  font-size: 16px;
  line-height: 32px
}

.slider .nav-menu li:hover {
  color: #07111b
}

.slider .nav-menu li:hover a {
  color: #07111b
}

.slider .nav-menu li:hover .el-icon-caret-right {
  color: #07111b
}

.slider .nav-menu li.active {
  color: #f01414
}

.slider .nav-menu li.active a {
  color: #f01414
}

.slider .nav-menu li.active a:hover {
  color: #f01414
}

.slider .nav-menu li.active .el-icon-caret-right {
  color: #f01414
}
</style>