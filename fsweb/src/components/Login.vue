<template>
  <div class="title">
    <span :class="{active:user.login_type===0}" @click="user.login_type=0">密码登录</span>
    <span :class="{active:user.login_type===1}" @click="user.login_type=1">短信登录</span>
  </div>
  <div class="inp" v-if="user.login_type===0">
    <input v-model="user.account" type="text" placeholder="用户名 / 手机号码" class="user">
    <input v-model="user.password" type="password" class="pwd" placeholder="密码">
    <div id="geetest1"></div>
    <div class="rember">
      <label>
        <input type="checkbox" class="no" v-model="user.remember"/>
        <span>记住密码</span>
      </label>
      <p>忘记密码</p>
    </div>
    <button class="login_btn" @click="loginhandler">登录</button>
    <p class="go_login">没有账号
      <router-link to="/register">立即注册</router-link>
    </p>
  </div>
  <div class="inp" v-show="user.login_type===1">
    <input v-model="user.mobile" type="text" placeholder="手机号码" class="user">
    <input v-model="user.code" type="text" class="code" placeholder="短信验证码">
    <el-button id="get_code" type="primary">点击获取验证码</el-button>
    <button class="login_btn">登录</button>
    <p class="go_login">没有账号 <span>立即注册</span></p>
  </div>
</template>

<script setup>
import user from "../api/user"
import {ElMessage} from 'element-plus'

const emit = defineEmits(["login_success",])

import {useStore} from "vuex"

const store = useStore()


const loginhandler = () => {
  // 登录处理
  if (user.account.length < 1 || user.password.length < 1) {
    // 错误提示
    ElMessage.error('用户名或密码不能为空.');
    return false // 在函数/方法中，可以阻止代码继续往下执行
  }

  // 发送请求
  user.login().then(response => {
    // 保存token，并根据用户的选择，是否记住密码
    localStorage.removeItem("token")
    sessionStorage.removeItem("token")
    if (user.remember) { // 判断是否记住登录状态
      // 记住登录
      localStorage.token = response.data.token
    } else {
      // 不记住登录，关闭浏览器以后就删除状态
      sessionStorage.token = response.data.token
    }

    // vuex存储用户登录信息，保存token，并根据用户的选择，是否记住密码
    let payload = response.data.token.split(".")[1]  // 载荷
    let payload_data = JSON.parse(atob(payload)) // 用户信息
    console.log(payload_data)
    store.commit("login", payload_data)

    // 成功提示
    ElMessage.success("登录成功.")
    // 关闭登录弹窗，对外发送一个登录成功的信息
    user.account = ""
    user.password = ""
    user.re_password = ""
    user.mobile = ""
    user.code = ""
    user.remember = false
    emit("login_success")

  }).catch(error => {
    ElMessage.error("登录异常.")
  })
}

</script>

<style scoped>
.title {
  font-size: 20px;
  color: #9b9b9b;
  letter-spacing: .32px;
  border-bottom: 1px solid #e6e6e6;
  display: flex;
  justify-content: space-around;
  padding: 0 60px 0 60px;
  margin-bottom: 20px;
  cursor: pointer;
}

.title span.active {
  color: #4a4a4a;
  border-bottom: 2px solid #84cc39;
}

.inp {
  width: 350px;
  margin: 0 auto;
}

.inp .code {
  width: 190px;
  margin-right: 16px;
}

#get_code {
  margin-top: 6px;
}

.inp input {
  outline: 0;
  width: 100%;
  height: 45px;
  border-radius: 4px;
  border: 1px solid #d9d9d9;
  text-indent: 20px;
  font-size: 14px;
  background: #fff !important;
}

.inp input.user {
  margin-bottom: 16px;
}

.inp .rember {
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: relative;
  margin-top: 10px;
}

.inp .rember p:first-of-type {
  font-size: 12px;
  color: #4a4a4a;
  letter-spacing: .19px;
  margin-left: 22px;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
  /*position: relative;*/
}

.inp .rember p:nth-of-type(2) {
  font-size: 14px;
  color: #9b9b9b;
  letter-spacing: .19px;
  cursor: pointer;
}

.inp .rember input {
  outline: 0;
  width: 15px;
  height: 30px;
  border-radius: 4px;
  border: 1px solid #d9d9d9;
  text-indent: 20px;
  font-size: 14px;
  background: #fff !important;
  vertical-align: middle;
  margin-right: 4px;
}

.inp .rember p span {
  display: inline-block;
  font-size: 12px;
  width: 100px;
}

.login_btn {
  cursor: pointer;
  width: 100%;
  height: 45px;
  background: #84cc39;
  border-radius: 5px;
  font-size: 16px;
  color: #fff;
  letter-spacing: .26px;
  margin-top: 30px;
  border: none;
  outline: none;
}

.inp .go_login {
  text-align: center;
  font-size: 14px;
  color: #9b9b9b;
  letter-spacing: .26px;
  padding-top: 20px;
}

.inp .go_login span {
  color: #84cc39;
  cursor: pointer;
}
</style>