<template>
  <div class="login box">
    <img src="../assets/Loginbg.3377d0c.jpg" alt="">
    <div class="login">
      <div class="login-title">
        <img src="../assets/logo.png" alt="logo">
        <p>帮助有志向的年轻人通过努力学习获得体面的工作和生活!</p>
      </div>
      <div class="login_box">
        <div class="title">
          <span class="active">用户注册</span>
        </div>
        <div class="inp">
          <input v-model="user.mobile" type="text" placeholder="手机号码" class="user">
          <input v-model="user.password" type="password" placeholder="登录密码" class="user">
          <input v-model="user.re_password" type="password" placeholder="确认密码" class="user">
          <input v-model="user.code" type="text" class="code" placeholder="短信验证码">
          <el-button id="get_code" type="primary">获取验证码</el-button>
          <button class="login_btn" @click="registerhandler">注册</button>
          <p class="go_login">已有账号
            <router-link to="/login">立即登录</router-link>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import {reactive, defineEmits, watch} from "vue"
import {ElMessage} from 'element-plus'
import {useStore} from "vuex"
import user from "../api/user";
import {useRouter} from "vue-router"

const router = useRouter()
const store = useStore()


// 监听数据mobile是否发生变化
watch(() => user.mobile, (mobile, prevMobile) => {
  if (/1[3-9]\d{9}/.test(user.mobile)) {
    // 发送ajax验证手机号是否已经注册
    user.check_mobile().then(response => {
      ElMessage.success(response.data.message);
    })
  }
})

const registerhandler = (res) => {
  // 注册处理
  if (!/^1[3-9]\d{9}$/.test(user.mobile)) {
    // 错误提示
    ElMessage.error('手机号格式不正确.');
    return false // 阻止代码继续往下执行
  }
  if (user.password.length < 8 || user.password.length > 18) {
    ElMessage.error('密码必须在8~18个字符之间.');
    return false
  }

  if (user.password !== user.re_password) {
    ElMessage.error('密码和确认密码不一致.');
    return false
  }

  if (!user.code) {
    ElMessage.error('请输入验证码.');
    return false
  }

  // 发送请求
  user.register({}).then(response => {
    // 保存token，并根据用户的选择，是否记住密码
    localStorage.removeItem("token");
    sessionStorage.removeItem("token");

    // 默认不需要记住登录
    sessionStorage.token = response.data.data.token;

    // vuex存储用户登录信息
    let payload = response.data.data.token.split(".")[1]  // 载荷
    let payload_data = JSON.parse(atob(payload)) // 用户信息
    store.commit("login", payload_data)
    // 清空表单信息
    user.mobile = ""
    user.password = ""
    user.re_password = ""
    user.code = ""
    user.remember = false
    //  成功提示
    ElMessage.success("注册成功.");
    // 路由跳转到首页
    router.push("/");
  })
}


</script>

<style scoped>
.box {
  width: 100%;
  height: 100%;
  position: relative;
  overflow: hidden;
}

.box img {
  width: 100%;
  min-height: 100%;
}

.box .login {
  position: absolute;
  width: 500px;
  height: 400px;
  left: 0;
  margin: auto;
  right: 0;
  bottom: 0;
  top: -438px;
}

.login-title {
  width: 100%;
  text-align: center;
}

.login-title img {
  width: 190px;
  height: auto;
}

.login-title p {
  font-size: 18px;
  color: #fff;
  letter-spacing: .29px;
  padding-top: 10px;
  padding-bottom: 50px;
}

.login_box {
  width: 400px;
  height: auto;
  background: #fff;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, .5);
  border-radius: 4px;
  margin: 0 auto;
  padding-bottom: 40px;
  padding-top: 50px;
}

.title {
  font-size: 20px;
  color: #9b9b9b;
  letter-spacing: .32px;
  border-bottom: 1px solid #e6e6e6;
  display: flex;
  justify-content: space-around;
  padding: 0px 60px 0 60px;
  margin-bottom: 20px;
  cursor: pointer;
}

.title span.active {
  color: #4a4a4a;
}

.inp {
  width: 350px;
  margin: 0 auto;
}

.inp .code {
  width: 190px;
  margin-right: 56px;
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
  width: 30px;
  height: 45px;
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