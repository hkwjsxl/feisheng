<template>
  <div class="login box">
    <img src="../assets/Loginbg.3377d0c.jpg" alt="login_background">
    <div class="login">
      <div class="login-title">
        <img src="../assets/logo.png" alt="logo">
        <p>帮助有志向的年轻人通过努力学习获得体面的工作和生活!</p>
      </div>
      <div class="login_box">
        <Login @successhandle="login_success"></Login>
      </div>
    </div>
  </div>
</template>

<script setup>
import Login from "../components/Login.vue"
import {useRouter} from "vue-router"

const router = useRouter()
// 用户登录成功以后的处理
const login_success = () => {
  console.log(123)
  // 跳转到首页
  router.push("/");
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
</style>