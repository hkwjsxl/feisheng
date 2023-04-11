<template>
  <div class="right-container l">
    <div class="right-title">
      <h2>我的课程</h2>
      <ul>
        <li :class="{action: course.current_course_type===-1}"><a href="" @click.prevent="course.current_course_type=-1">全部<i v-if="course.current_course_type===-1">{{course.user_count}}</i></a></li>
        <li :class="{action: course.current_course_type===0}"><a href="" @click.prevent="course.current_course_type=0">免费课<i v-if="course.current_course_type===0">{{course.user_count}}</i></a></li>
        <li :class="{action: course.current_course_type===1}"><a href="" @click.prevent="course.current_course_type=1">项目课<i v-if="course.current_course_type===1">{{course.user_count}}</i></a></li>
        <li :class="{action: course.current_course_type===2}"><a href="" @click.prevent="course.current_course_type=2">学位课<i v-if="course.current_course_type===2">{{course.user_count}}</i></a></li>
      </ul>
    </div>
    <div class="all-course-main">
      <div class="allcourse-content">
        <div class="courseitem">
          <div class="img-box">
            <a href=""><img alt="3天javascript入门到进阶" src="/src/assets/course-9.png" /> </a>
          </div>
          <div class="info-box">
            <div class="title">
              <span>免费课</span>
              <a href="" class="hd">3天javascript入门到进阶</a>
            </div>
            <div class="study-info">
              <span class="i-left">已学0%</span>
              <span class="i-mid">用时13分</span>
              <span class="i-right">学习至7.01 课程回顾</span>
            </div>
            <div class="catog-points">
              <span> <a href="">笔记 <i>0</i></a> </span>
              <span class="i-mid"> <a href="">代码 <i>0</i></a> </span>
              <span class="i-right"> <a href="">问答 <i>0</i></a> </span>
              <a href="" class="continute-btn">继续学习</a>
            </div>
            <div class="share-box clearfix">
              <div class="show-btn">
                <i class="el-icon-arrow-down"></i>
              </div>
              <div class="share-box-con">
                <a href="javascript:;" title="删除" class="del"><i class="el-icon-delete"></i></a>
                <a href="javascript:;" title="置顶课程"><i class="el-icon-top"></i></a>
              </div>
            </div>
          </div>
        </div>
        <div class="courseitem">
          <div class="img-box">
            <a href=""><img alt="3天javascript入门到进阶" src="/src/assets/course-9.png" /> </a>
          </div>
          <div class="info-box">
            <div class="title">
              <span>免费课</span>
              <a href="" class="hd">3天javascript入门到进阶</a>
            </div>
            <div class="study-info">
              <span class="i-left">已学0%</span>
              <span class="i-mid">用时13分</span>
              <span class="i-right">学习至7.01 课程回顾</span>
            </div>
            <div class="catog-points">
              <span> <a href="">笔记 <i>0</i></a> </span>
              <span class="i-mid"> <a href="">代码 <i>0</i></a> </span>
              <span class="i-right"> <a href="">问答 <i>0</i></a> </span>
              <a href="" class="continute-btn">继续学习</a>
            </div>
            <div class="share-box clearfix">
              <div class="show-btn">
                <i class="el-icon-arrow-down"></i>
              </div>
              <div class="share-box-con">
                <a href="javascript:;" title="删除" class="del"><i class="el-icon-delete"></i></a>
                <a href="javascript:;" title="置顶课程"><i class="el-icon-top"></i></a>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- 分页 -->
    </div>
  </div>
</template>

<script setup>
import course from "../../api/course";
</script>

<style scoped>

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

/*****/
.right-container {
	width: 1284px;
}

.right-container .right-title {
	margin-bottom: 24px
}

.right-container .right-title::after {
	content: '';
	clear: both;
	display: block
}

.right-container .right-title h2 {
	margin-right: 24px;
	float: left;
	font-size: 16px;
	color: #07111b;
	line-height: 32px;
	font-weight: 700
}

.right-container .right-title ul {
	float: left
}

.right-container .right-title ul:before {
	float: left;
	margin-top: 2px;
	margin-right: 20px;
	content: "|";
	color: #d9dde1
}

.right-container .right-title ul li {
	float: left;
	width: 95px;
	line-height: 32px;
	text-align: center;
	font-size: 14px
}

.right-container .right-title ul li.action {
	background: #4d555d;
	border-radius: 16px
}

.right-container .right-title ul li.action a {
	color: #fff
}

.right-container .right-title ul li i {
	padding-left: 5px;
	font-style: normal
}

.right-container .right-title span {
	position: relative;
	float: right;
	color: #93999f;
	font-size: 14px;
	cursor: pointer;
	width: 128px;
	line-height: 32px
}

.right-container .right-title span i {
	float: left;
	margin-top: 8px;
	margin-left: 28px;
	margin-right: 4px;
	font-size: 16px
}

.right-container .right-title span a {
	display: block
}

.right-container .right-title span.action {
	background: #4d555d;
	border-radius: 16px
}

.right-container .right-title span.action a {
	color: #fff
}

.all-course-main {
  margin-top: 28px
}
.allcourse-content {
  width: 100%;
  box-sizing: border-box
}

.courseitem {
	position: relative;
	display: flex;
	flex-direction: row;
	margin-top: 28px
}

.courseitem:first-child {
	margin-top: 0
}

.courseitem .img-box {
	width: 240px;
	margin-right: 30px
}

.courseitem .img-box img {
	vertical-align: top
}

.courseitem .info-box {
	display: flex;
	flex-direction: column;
	border-bottom: 1px solid #d9dde1;
	position: relative;
	padding-bottom: 28px;
	width: 1014px;
}

.courseitem .info-box .title {
	display: flex;
	flex-direction: row;
	align-items: center
}

.courseitem .info-box .title span:first-child {
	background: #f5f7fa;
	border-radius: 2px;
	width: 62px;
	height: 20px;
	text-align: center;
	line-height: 20px;
	font-size: 12px;
	color: #9199a1;
	font-weight: 400;
	margin-right: 12px
}

.courseitem .info-box .title .hd {
	font-size: 20px;
	color: #07111b;
	font-weight: 700;
	line-height: 36px;
	overflow: hidden;
	white-space: nowrap;
	text-overflow: ellipsis
}

.courseitem .info-box .study-info {
	display: flex;
	flex-direction: row;
	align-items: center;
	margin-bottom: 12px
}

.courseitem .info-box .study-info span {
	line-height: 24px;
	font-size: 14px;
	color: #4d555d;
	margin-right: 24px
}

.courseitem .info-box .study-info span.i-left {
	color: #f20d0d
}

.courseitem .info-box .follows-path i {
	font-style: normal;
	margin: 0 4px
}

.courseitem .info-box .catog-points {
	display: flex;
	flex-direction: row;
	align-items: center
}

.courseitem .info-box .catog-points span {
	font-size: 14px;
	line-height: 36px;
	color: #4d555d;
	margin-right: 36px
}

.courseitem .info-box .catog-points span a {
	color: #4d555d
}

.courseitem .info-box .catog-points span a:hover {
	color: #14191e
}

.courseitem .info-box .catog-points span i {
	color: #93999f;
	font-style: normal
}

.courseitem .info-box .catog-points .continute-btn {
	display: inline-block;
	position: absolute;
	right: 0;
	font-size: 14px;
	border: none;
	color: #fff;
	width: 104px;
	height: 36px;
	line-height: 36px;
	text-align: center;
	background: rgba(240,20,20,.6);
	border-radius: 18px
}

.courseitem .info-box .catog-points .continute-btn:hover {
	background-color: #f01414;
	color: #fff
}

.courseitem .info-box .path-course span {
	margin-right: 6px;
	display: inline-block
}

.courseitem .info-box .share-box .show-btn {
	top: -20px
}
.share-box .show-btn {
    position: absolute;
    top: 8px;
    right: 0;
    width: 30px;
    height: 20px;
    font-size: 18px;
    text-align: center;
    line-height: 20px;
    color: #bdc0c3;
    cursor: pointer;
}
.courseitem .info-box .share-box-con {
	width: auto;
	top: 0;
	height: auto
}
.share-box:hover .share-box-con {
  display: block;
}
.share-box .share-box-con {
  display: none;
  position: absolute;
  z-index: 99;
  top: 22px;
  right: 0;
  font-size: 20px;
  background-color: #fff;
  padding: 0 8px;
  box-shadow: 4px 4px 10px 2px #e1e1e1;
}
</style>