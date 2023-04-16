<template>
  <div class="setting-right">
    <div class="setting-right-wrap wrap-boxes settings">
      <div class="formBox">
        <div id="setting-profile" class="setting-wrap setting-profile">
          <div class="common-title">
            个人信息
            <a href="javascript: void(0);" class="pull-right js-edit-info"><i class="el-icon-edit"></i>编辑</a>
          </div>
          <div class="line"></div>
          <div class="info-wapper">
            <div class="info-box clearfix">
              <label class="pull-left">昵称</label>
              <div class="pull-left" v-if="store.state.user.username">{{ store.state.user.username }}</div>
              <div class="pull-left" v-else>None</div>
            </div>
            <div class="info-box clearfix">
              <label class="pull-left">邮箱</label>
              <div class="pull-left" v-if="store.state.user.email">{{ store.state.user.email }}</div>
              <div class="pull-left" v-else>None</div>
            </div>
            <div class="info-box clearfix">
              <label class="pull-left">手机号</label>
              <div class="pull-left" v-if="store.state.user.mobile">{{ store.state.user.mobile }}</div>
              <div class="pull-left" v-else>None</div>
            </div>
            <div class="info-box clearfix">
              <label class="pull-left">最后登录时间</label>
              <div class="pull-left" v-if="store.state.user.last_login">{{ store.state.user.last_login }}</div>
              <div class="pull-left" v-else>None</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import store from "../../store/index.js";

// import user from "../../api/user.js"
// 获取用户的个人信息
// const get_user_info = () => {
//   let token = sessionStorage.token || localStorage.token;
//   user.get_user_info(token).then(response => {
//     store.state.user = response.data.data; // 我的课程列表
//     console.log(store.state.user);
//   })
// }
// get_user_info();
</script>

<style scoped>
.clearfix:after {
  content: '\0020';
  display: block;
  height: 0;
  clear: both;
  visibility: hidden;
}

.setting-right {
  float: left;
  width: 1284px;
  box-sizing: border-box;
  background-color: #fff
}

.setting-right-wrap {
  min-height: 550px
}

.pull-left {
  float: left;
}

.pull-right {
  float: right;
}

.common-title {
  line-height: 32px;
  font-size: 16px;
  font-weight: 700;
}

.common-title a {
  color: #93999f;
  font-weight: 400;
}

.common-title a:hover {
  color: #008cc8;
}

.common-title a i {
  color: #008cc8;
  margin-right: 4px;
  vertical-align: middle;
}

.line {
  height: 1px;
  background-color: #d0d6d9;
  margin-top: 12px;
}

.setting-profile {
  padding: 0 !important
}

.setting-profile .info-wapper {
  margin: 24px auto 24px 40px
}

.setting-profile .info-box {
  margin-bottom: 12px
}

.setting-profile .info-box label {
  width: 180px;
  line-height: 20px;
  padding: 20px 0;
  text-align: center;
  background-color: #f3f5f7;
  color: #07111b;
  font-weight: 700
}

.setting-profile .info-box div {
  width: 1034px;
  margin-left: 8px;
  line-height: 20px;
  padding: 20px 0 20px 22px;
  border-bottom: 1px solid #d9dde1
}

.edit-info .wlfg-wrap textarea {
  height: 70px
}

.edit-info .wlfg-wrap input {
  font-size: 14px
}

</style>