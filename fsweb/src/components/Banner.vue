<template>
  <div class="bk"></div>
  <div class="bgfff banner-box">
    <div class="g-banner pr" @mouseleave="state.current_menu=-1">
      <!-- 商品课程分类信息 -->
      <div class="submenu" v-if="state.current_menu===0">
        <div class="inner-box">
          <h2 class="type">前端开发</h2>
          <div class="tag clearfix">
          </div>
          <div class="lore">
            <span class="title">知识点：</span>
            <p class="lores clearfix"><a target="_blank" href="">Vue.js</a>
              <a target="_blank" href="">Typescript</a>
              <a target="_blank" href="">React.JS</a>
              <a target="_blank" href="">HTML/CSS</a>
              <a target="_blank" href="">JavaScript</a>
              <a target="_blank" href="">Angular</a>
              <a target="_blank" href="">Node.js</a>
              <a target="_blank" href="">jQuery</a>
              <a target="_blank" href="">Bootstrap</a>
              <a target="_blank" href="">Sass/Less</a>
              <a target="_blank" href="">WebApp</a>
              <a target="_blank" href="">小程序</a>
              <a target="_blank" href="">前端工具</a>
              <a target="_blank" href="">CSS</a>
              <a target="_blank" href="">Html5</a>
              <a target="_blank" href="">CSS3</a>
            </p>
          </div>
        </div>
        <div class="recomment clearfix">
          <a href="" target="_blank" title="" class="recomment-item">
            <div class="img"
                 style="background-image: url('/src/assets/60a7779909e3fc1206960344.png'); background-size: 100%; "></div>
            <div class="details">
              <!--路径单独写-->
              <div class="title-box">
                <p class="title"><span class="text">前端工程师2021</span> <span class="tag tixi">体系</span></p>
              </div>
              <div class="bottom">
                <span class="discount-name">优惠价</span>
                <span class="price">￥4599.00</span> &middot;
                <span class="difficulty"> 零基础 </span> &middot;
                <span class="num"><i class="imv2-set-sns"></i> 19322</span>
              </div>
            </div>
          </a>
          <a href="" target="_blank" title="前端框架及项目面试 聚焦Vue3/React/Webpack" class="recomment-item">
            <div class="img" style="background-image: url('/src/assets/5e3cfea008e9a61b06000338-360-202.jpg')"></div>
            <div class="details">
              <!--路径单独写-->
              <div class="title-box">
                <p class="title"><span class="text">前端框架及项目面试 聚焦Vue3/React/Webpack</span> <span
                    class="tag shizhan">实战</span></p>
              </div>
              <div class="bottom">
                <span class="price">399.00</span> &middot;
                <span class="difficulty"> 中级 </span> &middot;
                <span class="num"><i class="imv2-set-sns"></i> 2946</span>
              </div>
            </div>
          </a>
          <a href="" target="_blank" title="从0打造微前端框架，实战汽车资讯平台，系统掌握微前端架构设计与落地能力" class="recomment-item">
            <div class="img" style="background-image: url('/src/assets/60d44ec8084b799712000676-360-202.jpg')"></div>
            <div class="details">
              <!--路径单独写-->
              <div class="title-box">
                <p class="title"><span class="text">从0打造微前端框架，实战汽车资讯平台，系统掌握微前端架构设计与落地能力</span><span class="tag shizhan">实战</span>
                </p>
              </div>
              <div class="bottom">
                <span class="discount-name">限时优惠</span>
                <span class="price">￥328.00</span> &middot;
                <span class="difficulty"> 高级 </span> &middot;
                <span class="num"><i class="imv2-set-sns"></i> 109</span>
              </div>
            </div>
          </a>
          <a href="" target="_blank" title="" class="recomment-item">
            <div class="img"
                 style="background-image: url('/src/assets/604f2bab0952610803240324-140-140.png'); background-size: 100%; "></div>
            <div class="details">
              <!--路径单独写-->
              <div class="title-box">
                <p class="title"><span class="text">Vue.js 从入门到精通</span> <span class="tag lujing">路线</span></p>
              </div>
              <div class="bottom">
                <span class="difficulty">4步骤</span> &middot;
                <span class="difficulty">4门课</span> &middot;
                <span class="num">19697人收藏</span>
              </div>
            </div>
          </a>
        </div>
      </div>
      <div class="submenu" v-if="state.current_menu===1">
        <div class="inner-box">
          <h2 class="type">后端开发</h2>
          <div class="tag clearfix">
          </div>
          <div class="lore">
            <span class="title">知识点：</span>
            <p class="lores clearfix">
              <a target="_blank" href="">Java</a>
              <a target="_blank" href="">SpringBoot</a>
              <a target="_blank" href="">Spring Cloud</a>
              <a target="_blank" href="">SSM</a>
              <a target="_blank" href="">PHP</a>
              <a target="_blank" href="">.net</a>
              <a target="_blank" href="">Python</a>
              <a target="_blank" href="">爬虫</a>
              <a target="_blank" href="">Django</a>
              <a target="_blank" href="">Flask</a>
              <a target="_blank" href="">Tornado</a>
              <a target="_blank" href="">Go</a>
              <a target="_blank" href="">C</a>
              <a target="_blank" href="">C++</a>
              <a target="_blank" href="">C#</a>
              <a target="_blank" href="">Ruby</a></p>
          </div>
        </div>
        <div class="recomment clearfix">
          <a href="" target="_blank" title="Java工程师2021" class="recomment-item">
            <div class="img"
                 style="background-image: url('/src/assets/60a777ef0942d7bf06960344.png'); background-size: 100%; "></div>
            <div class="details">
              <div class="title-box">
                <p class="title"><span class="text">Java工程师2021</span> <span class="tag tixi">体系</span></p>
              </div>
              <div class="bottom">
                <span class="discount-name">优惠价</span>
                <span class="price">￥4399.00</span> &middot;
                <span class="difficulty"> 零基础 </span> &middot;
                <span class="num"><i class="imv2-set-sns"></i> 15052</span>
              </div>
            </div>
          </a>
          <a href="" target="_blank" title="Python工程师（全能型）" class="recomment-item">
            <div class="img"
                 style="background-image: url('/src/assets/60a77721093df37606960344.png'); background-size: 100%; "></div>
            <div class="details">
              <!--路径单独写-->
              <div class="title-box">
                <p class="title"><span class="text">Python工程师（全能型）</span> <span class="tag tixi">体系</span></p>
              </div>
              <div class="bottom">
                <span class="discount-name">优惠价</span>
                <span class="price">￥4366.00</span> &middot;
                <span class="difficulty"> 零基础 </span> &middot;
                <span class="num"><i class="imv2-set-sns"></i> 10786</span>
              </div>
            </div>
          </a>
          <a href="" target="_blank" title="Java全栈工程师" class="recomment-item">
            <div class="img"
                 style="background-image: url('/src/assets/5dd6567b09d9d01c06000338.png'); background-size: 100%; "></div>
            <div class="details">
              <!--路径单独写-->
              <div class="title-box">
                <p class="title"><span class="text">Java全栈工程师</span> <span class="tag tixi">体系</span></p>
              </div>
              <div class="bottom">
                <span class="discount-name">优惠价</span>
                <span class="price">￥3380.00</span> &middot;
                <span class="difficulty"> 进阶 </span> &middot;
                <span class="num"><i class="imv2-set-sns"></i> 1853</span>
              </div>
            </div>
          </a>
          <a href="" target="_blank" title="" class="recomment-item">
            <div class="img"
                 style="background-image: url('/src/assets/604f2bb6099d6a8803240324-140-140.png'); background-size: 100%; "></div>
            <div class="details">
              <!--路径单独写-->
              <div class="title-box">
                <p class="title"><span class="text">SpringBoot从入门到精通</span> <span class="tag lujing">路线</span></p>
              </div>
              <div class="bottom">
                <span class="difficulty">3步骤</span> &middot;
                <span class="difficulty">5门课</span> &middot;
                <span class="num">11092人收藏</span>
              </div>
            </div>
          </a>
        </div>
      </div>
      <div class="submenu" v-if="state.current_menu===2">
        <div class="inner-box">
          <h2 class="type">移动开发</h2>
          <div class="tag clearfix">
          </div>
          <div class="lore">
            <span class="title">知识点：</span>
            <p class="lores clearfix"></p>
          </div>
        </div>
        <div class="recomment clearfix">
          <a href="" target="_blank" title="移动端架构师成长体系课" class="recomment-item">
            <div class="img"
                 style="background-image: url('/src/assets/5ec5ddf209cd2c8606000338.png'); background-size: 100%; "></div>
            <div class="details">
              <!--路径单独写-->
              <div class="title-box">
                <p class="title"><span class="text">移动端架构师成长体系课</span> <span class="tag tixi">体系</span></p>
              </div>
              <div class="bottom">
                <span class="discount-name">优惠价</span>
                <span class="price">￥4888.00</span> &middot;
                <span class="difficulty"> 进阶 </span> &middot;
                <span class="num"><i class="imv2-set-sns"></i> 402</span>
              </div>
            </div>
          </a>
          <a href="" target="_blank" title="Flutter高级进阶实战  仿哔哩哔哩APP 一次性深度掌握Flutter高阶技能" class="recomment-item">
            <div class="img"
                 style="background-image: url('/src/assets/60497caf0971842912000676-360-202.png'); background-size: 100%; "></div>
            <div class="details">
              <!--路径单独写-->
              <div class="title-box">
                <p class="title"><span class="text">Flutter高级进阶实战 仿哔哩哔哩APP 一次性深度掌握Flutter高阶技能</span> <span
                    class="tag shizhan">实战</span></p>
              </div>
              <div class="bottom">
                <span class="price">368.00</span> &middot;
                <span class="difficulty"> 高级 </span> &middot;
                <span class="num"><i class="imv2-set-sns"></i> 646</span>
              </div>
            </div>
          </a>
          <a href="" target="_blank" title="音视频基础+ffmpeg原理+项目实战 一课完成音视频技术开发入门" class="recomment-item">
            <div class="img"
                 style="background-image: url('/src/assets/5e5621d0092c054612000676-360-202.png'); background-size: 100%; "></div>
            <div class="details">
              <!--路径单独写-->
              <div class="title-box">
                <p class="title"><span class="text">音视频基础+ffmpeg原理+项目实战 一课完成音视频技术开发入门</span> <span class="tag shizhan">实战</span>
                </p>
              </div>
              <div class="bottom">
                <span class="price">288.00</span> &middot;
                <span class="difficulty"> 入门 </span> &middot;
                <span class="num"><i class="imv2-set-sns"></i> 1303</span>
              </div>
            </div>
          </a>
          <a href="" target="_blank" title="" class="recomment-item">
            <div class="img"
                 style="background-image: url('/src/assets/604f2b52090de67603240324-140-140.png'); background-size: 100%; "></div>
            <div class="details">
              <!--路径单独写-->
              <div class="title-box">
                <p class="title"><span class="text">Android工程师高薪面试突破路线</span> <span class="tag lujing">路线</span></p>
              </div>
              <div class="bottom">
                <span class="difficulty">3步骤</span> &middot;
                <span class="difficulty">3门课</span> &middot;
                <span class="num">1471人收藏</span>
              </div>
            </div>
          </a>
        </div>
      </div>
      <div class="menuContent">
        <div class="item" :class="{'js-menu-item-on': state.current_menu===0}" @mouseover="state.current_menu=0">
          <span class="title">前端开发：</span>
          <span class="sub-title">HTML5 / Vue.js / Node.js</span>
          <i class="imv2-arrow1_r"></i>
        </div>
        <div class="item" :class="{'js-menu-item-on': state.current_menu===1}" @mouseover="state.current_menu=1">
          <span class="title">后端开发：</span>
          <span class="sub-title">Java / Python / Go</span>
          <i class="imv2-arrow1_r"></i>
        </div>
        <div class="item" :class="{'js-menu-item-on': state.current_menu===2}" @mouseover="state.current_menu=2">
          <span class="title">移动开发：</span>
          <span class="sub-title">Flutter / Android / iOS </span>
          <i class="imv2-arrow1_r"></i>
        </div>
      </div>
      <!-- 轮播图-->
      <div class="g-banner-content" @mouseover="state.current_menu=-1">
        <el-carousel :interval="5000" arrow="always" height="482px" v-if="banner.banner_list[0]">
          <el-carousel-item v-for="(item, key) in banner.banner_list" :key="key">
            <a :href="item.link" v-if="item.is_http">
              <img :src="item.image" alt="" style="width: 100%;height: 100%;">
            </a>
            <router-link :to="item.link" v-else>
              <img :src="item.image" alt="" style="width: 100%;height: 100%;">
            </router-link>
          </el-carousel-item>
        </el-carousel>
      </div>
    </div>
  </div>
</template>

<script setup>
import {reactive} from "vue"
import banner from "../api/banner";

// 获取轮播广告列表
banner.get_banner_list().then(response => {
  banner.banner_list = response.data.data
})

const state = reactive({
  current_menu: -1,
})
</script>


<style scoped>
.banner-box {
  padding: 32px 0;
}

.system-class-show {
  width: 1152px;
  height: 100px;
  margin: 0 auto;
  background: #FFFFFF;
  box-shadow: 0 5px 20px 0 rgba(0, 0, 0, 0.3);
  border-radius: 0 0 8px 8px;
}

.system-class-show .show-box {
  display: block;
  width: 192px;
  height: 45px;
  float: left;
  margin: 28px 0 0 16px;
  cursor: pointer;
}

.system-class-show .show-box .system-class-icon {
  float: left;
  width: 45px;
  height: 45px;
  border-radius: 50%;
  background-size: cover;
  margin-right: 8px;
  transition: all .2s;
}

.system-class-show .show-box .describe {
  float: left;
}

.system-class-show .show-box .describe h4 {
  width: 139px;
  font-family: PingFangSC-Medium;
  font-size: 16px;
  color: #1C1F21;
  letter-spacing: 0.76px;
  line-height: 22px;
  margin-bottom: 4px;
  white-space: nowrap;
  overflow: hidden;
}

.system-class-show .show-box .describe p {
  width: 139px;
  font-family: PingFangSC-Regular;
  font-size: 12px;
  color: #545C63;
  line-height: 18px;
  white-space: nowrap;
  overflow: hidden;
}

.system-class-show .show-box:hover .system-class-icon {
  transform: translateY(-2px);
}

.system-class-show .show-box:hover .describe h4 {
  color: #F01414;
}

.system-class-show .line {
  float: left;
  height: 36px;
  border: 1px solid #E8E8E8;
  margin-left: 16px;
  margin-top: 33px;
}

.system-class-show .all-btn {
  position: relative;
  display: block;
  height: 100%;
  cursor: pointer;
  overflow: hidden;
}

.system-class-show .all-btn .mini-title {
  font-family: PingFangSC-Medium;
  font-size: 12px;
  color: #1C1F21;
  text-align: center;
  line-height: 14px;
  margin-top: 40px;
}

.system-class-show .all-btn .more-btn {
  font-family: PingFangSC-Regular;
  font-size: 12px;
  color: #545C63;
  line-height: 12px;
  margin-left: 30px;
  position: relative;
}

.system-class-show .all-btn .more-btn .icon-right2 {
  position: absolute;
  top: 1px;
  left: 28px;
  transition: all .2s;
}

.system-class-show .all-btn:hover .more-btn {
  color: #1C1F21;
}

.system-class-show .all-btn:hover .more-btn .icon-right2 {
  transform: translateX(3px);
}

.g-banner {
  position: relative;
  overflow: hidden;
  width: 1440px;
  margin: auto;
  border-radius: 8px 8px 0 0;
}

.g-banner .g-banner-content {
  position: relative;
  float: left;
  width: 68%;
}

.g-banner .g-banner-content .g-banner-box {
  position: relative;
  height: 316px;
}

.g-banner .g-banner-content .notice {
  position: absolute;
  top: 8px;
  left: 0;
  background: #FF9900;
  box-shadow: 0 2px 4px 0 rgba(7, 17, 27, 0.2);
  padding: 6px 12px 6px 8px;
  z-index: 1;
  border-top-right-radius: 20px;
  border-bottom-right-radius: 20px;
}

.g-banner .g-banner-content .notice .imv2-vol_up {
  font-size: 16px;
  color: #FFFFFF;
  display: inline-block;
  line-height: 20px;
  margin-top: 1px;
  margin-right: 4px;
  vertical-align: sub;
}

.g-banner .g-banner-content .notice .notice-txt {
  display: inline-block;
  width: auto;
  font-size: 12px;
  color: #FFFFFF;
  line-height: 20px;
  z-index: 1;
  white-space: nowrap;
}

.g-banner .g-banner-content .notice .notice-close {
  font-size: 16px;
  margin: 6px 0 6px 12px;
  color: rgba(255, 255, 255, 0.6);
  line-height: 20px;
}

.g-banner .g-banner-content .notice .notice-close:hover {
  color: #fff;
}

.g-banner .g-banner-content .notice.closed {
  transition: all .3s;
  background: rgba(255, 153, 0, 0.6);
  box-shadow: 0 2px 4px 0 rgba(7, 17, 27, 0.2);
}

.g-banner .g-banner-content .notice.closed .notice-txt {
  overflow: hidden;
}

.g-banner .g-banner-content .notice.closed .notice-close {
  display: none;
}

.g-banner .banner-anchor {
  position: absolute;
  top: 50%;
  margin-top: -24px;
  width: 48px;
  height: 48px;
  background: rgba(28, 31, 33, 0.1) url(/src/assets/icon-left-small.png) no-repeat center / 16px auto;
  border-radius: 50%;
  color: #FFFFFF;
  transition: all .2s;
}

.g-banner .banner-anchor:hover {
  background-color: rgba(28, 31, 33, 0.5);
}

.g-banner .next {
  right: 16px;
  transform: rotate(180deg);
}

.g-banner .prev {
  left: 16px;
}

.g-banner .g-banner-box > a:first-child .banner-slide {
  display: block;
}

.g-banner .banner-slide {
  position: absolute;
  display: none;
  width: 896px;
  height: 316px;
  /*margin: auto;*/
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  background-repeat: no-repeat;
  background-position: center 0;
}

.g-banner .banner-slide .festival {
  position: absolute;
  top: 450px;
  right: 75px;
}

.g-banner .banner-slide .festival a {
  display: block;
  width: 190px;
  height: 120px;
}

.g-banner .banner-slide .festival a:hover {
  background-position: 0 0;
}

.g-banner .banner-slide img {
  width: 100%;
  height: 100%;
}

.g-banner .inner {
  position: relative;
  width: 1200px;
  margin: 0 auto;
}

.g-banner .banner-dots {
  position: absolute;
  bottom: 20px;
  left: 0;
  right: 0;
  text-align: right;
  padding-right: 24px;
  line-height: 12px;
}

.g-banner .banner-dots span {
  display: inline-block;
  *display: inline;
  *zoom: 1;
  width: 8px;
  height: 8px;
  border-radius: 4px;
  margin-left: 8px;
  background: rgba(255, 255, 255, 0.75);
  transition: all .2s;
  cursor: pointer;
}

.g-banner .banner-dots span.active {
  width: 20px;
}

.submenu {
  position: absolute;
  left: 256px;
  width: 776px;
  height: 482px;
  background: #FFFFFF;
  box-shadow: 0 4px 8px 0 rgba(7, 17, 27, 0.1);
  border-radius: 0 12px 12px 0;
  z-index: 33;
  box-sizing: border-box;
}

.submenu .inner-box {
  height: 188px;
  padding: 28px 36px 0;
  box-sizing: border-box;
}

.submenu .inner-box .type {
  margin-bottom: 10px;
  font-size: 16px;
  color: #1C1F21;
  line-height: 22px;
  font-weight: bold;
}

.submenu .inner-box .tag {
  margin-bottom: 12px;
}

.submenu .inner-box .tag a {
  float: left;
  font-size: 12px;
  line-height: 1;
  color: #E02020;
  border-radius: 100px;
  border: 1px solid #E02020;
  padding: 5px 10px;
  margin-right: 10px;
}

.submenu .inner-box .tag a:last-child {
  margin-right: 0;
}

.submenu .inner-box .lore {
  font-size: 12px;
  line-height: 24px;
  color: #6D7278;
  margin-bottom: 8px;
  display: -webkit-box;
  display: -ms-flexbox;
  display: -webkit-flex;
  display: flex;
}

.submenu .inner-box .lore .title {
  color: #1C1F21;
  font-weight: bold;
}

.submenu .inner-box .lore .lores {
  width: 0;
  -webkit-box-flex: 1;
  -ms-flex: 1;
  -webkit-flex: 1;
  flex: 1;
}

.submenu .inner-box .lore .lores a {
  float: left;
  color: #6D7278;
  margin-right: 24px;
}

.submenu .inner-box .lore .lores a:last-child {
  margin-right: 0;
}

.submenu .recomment {
  padding: 35px 36px;
  height: 204px;
  background-color: #F3F5F6;
  box-sizing: border-box;
}

.submenu .recomment .recomment-item {
  width: 329px;
  float: left;
  display: -webkit-box;
  display: -ms-flexbox;
  display: -webkit-flex;
  display: flex;
}

.submenu .recomment .recomment-item:nth-child(2n) {
  margin-left: 30px;
}

.submenu .recomment .recomment-item:nth-child(-n+2) {
  margin-bottom: 30px;
}

.submenu .recomment .recomment-item .img {
  width: 90px;
  height: 50px;
  margin-right: 11px;
  border-radius: 4px;
  background-position: center;
  image-rendering: -moz-crisp-edges;
  /* Firefox */
  image-rendering: -o-crisp-edges;
  /* Opera */
  /*image-rendering: -webkit-optimize-contrast;*/
  /*image-rendering: -webkit-crisp-edges;*/
  /*Webkit (non-standard naming) */
  image-rendering: crisp-edges;
  -ms-interpolation-mode: nearest-neighbor;
  /* IE (non-standard property) */
  box-shadow: 0 6px 10px 0 rgba(95, 101, 105, 0.15);
}

.submenu .recomment .recomment-item .details {
  height: 50px;
  font-size: 12px;
  width: 0;
  -webkit-box-flex: 1;
  -ms-flex: 1;
  -webkit-flex: 1;
  flex: 1;
}

.submenu .recomment .recomment-item .details .title-box {
  margin-bottom: 10px;
  display: -webkit-box;
  display: -ms-flexbox;
  display: -webkit-flex;
  display: flex;
  -webkit-box-align: center;
  -ms-flex-align: center;
  -webkit-align-items: center;
  align-items: center;
}

.submenu .recomment .recomment-item .details .title-box .title {
  display: flex;
  align-items: center;
  color: #1C1F21;
  width: 228px;
}

.submenu .recomment .recomment-item .details .title-box .title .text {
  display: inline-block;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  max-width: calc(100% - 4em);
}

.submenu .recomment .recomment-item .details .title-box .title .tag {
  display: inline-block;
  width: 2em;
  color: #fff;
  opacity: .6;
  border-radius: 2px;
  line-height: 1;
  padding: 2px 4px;
  margin-left: 5px;
}

.submenu .recomment .recomment-item .details .title-box .title .tag.shizhan {
  background-color: #FA6400;
}

.submenu .recomment .recomment-item .details .title-box .title .tag.tixi {
  background-color: #E02020;
}

.submenu .recomment .recomment-item .details .title-box .title .tag.lujing {
  background-color: #0091FF;
}

.submenu .recomment .recomment-item .details .bottom {
  color: #9199A1;
  line-height: 18px;
}

.submenu .recomment .recomment-item .details .bottom .discount-name,
.submenu .recomment .recomment-item .details .bottom .tag {
  display: inline-block;
  color: #fff;
  background-color: rgba(242, 13, 13, 0.6);
  border-radius: 2px;
  padding: 2px 4px;
  line-height: 1;
}

.submenu .recomment .recomment-item .details .bottom .discount-name {
  background: rgba(242, 13, 13, 0.6);
}

.submenu .recomment .recomment-item .details .bottom .price:not(.free) {
  font-weight: bold;
  color: #F01414;
}

.menuContent {
  position: relative;
  float: left;
  width: 20%;
  height: 482px;
  z-index: 2;
  padding-top: 17px;
  box-sizing: border-box;
  background: #39364d;
  border-bottom-left-radius: 4px;
  font-weight: 400;
}

.menuContent .item {
  line-height: 50px;
  cursor: pointer;
  position: relative;
  color: #fff;
  padding: 0 14px;
  border-top-left-radius: 4px;
  border-bottom-left-radius: 4px;
  height: 50px;
  transition: all .1s;
  font-size: 14px;
}

.menuContent .item .sub-title {
  font-size: 12px;
}

.menuContent .item i {
  position: absolute;
  right: 4px;
  top: 16px;
  color: rgba(255, 255, 255, 0.5);
  font-size: 16px;
}

.menuContent .item.js-menu-item-on {
  color: #fff;
  background-color: rgba(255, 255, 255, 0.1);
}
</style>