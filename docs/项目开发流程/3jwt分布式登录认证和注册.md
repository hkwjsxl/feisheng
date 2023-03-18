# 用户的登陆认证

接下来，因为是新开发一个功能模块，那么我们可以在新的分支下进行开发，将来方便对这部分代码进行单独管理，等开发完成了以后再合并分支到develop也是可以的。

```bash
git checkout -b feature/user
```



## 前端显示登陆页面

### 登录页组件

components/Login.vue

```vue
<template>
  <div class="title">
    <span :class="{active:state.login_type===0}" @click="state.login_type=0">密码登录</span>
    <span :class="{active:state.login_type===1}" @click="state.login_type=1">短信登录</span>
  </div>
  <div class="inp" v-if="state.login_type===0">
    <input v-model="state.username" type="text" placeholder="用户名 / 手机号码" class="user">
    <input v-model="state.password" type="password" class="pwd" placeholder="密码">
    <div id="geetest1"></div>
    <div class="rember">
      <label>
        <input type="checkbox" class="no" name="a"/>
        <span>记住密码</span>
      </label>
      <p>忘记密码</p>
    </div>
    <button class="login_btn">登录</button>
    <p class="go_login" >没有账号 <span>立即注册</span></p>
  </div>
  <div class="inp" v-show="state.login_type===1">
    <input v-model="state.username" type="text" placeholder="手机号码" class="user">
    <input v-model="state.password"  type="text" class="code" placeholder="短信验证码">
    <el-button id="get_code" type="primary">获取验证码</el-button>
    <button class="login_btn">登录</button>
    <p class="go_login" >没有账号 <span>立即注册</span></p>
  </div>
</template>

<script setup>
import {reactive} from "vue";

const state = reactive({
  login_type: 0,
  username:"",
  password:"",
})
</script>

<style scoped>
.title{
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
.title span.active{
	color: #4a4a4a;
    border-bottom: 2px solid #84cc39;
}

.inp{
	width: 350px;
	margin: 0 auto;
}
.inp .code{
    width: 220px;
    margin-right: 26px;
}
#get_code{
   margin-top: 6px;
}
.inp input{
    outline: 0;
    width: 100%;
    height: 45px;
    border-radius: 4px;
    border: 1px solid #d9d9d9;
    text-indent: 20px;
    font-size: 14px;
    background: #fff !important;
}
.inp input.user{
    margin-bottom: 16px;
}
.inp .rember{
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: relative;
    margin-top: 10px;
}
.inp .rember p:first-of-type{
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
.inp .rember p:nth-of-type(2){
    font-size: 14px;
    color: #9b9b9b;
    letter-spacing: .19px;
    cursor: pointer;
}

.inp .rember input{
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

.inp .rember p span{
    display: inline-block;
    font-size: 12px;
    width: 100px;
}
.login_btn{
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
.inp .go_login{
    text-align: center;
    font-size: 14px;
    color: #9b9b9b;
    letter-spacing: .26px;
    padding-top: 20px;
}
.inp .go_login span{
    color: #84cc39;
    cursor: pointer;
}
</style>
```

components/Header.vue，代码：

```vue
<template>
  <div class="header-box">
    <div class="header">
      <div class="content">
        <div class="logo">
          <router-link to="/"><img src="../assets/logo.png" alt=""></router-link>
        </div>
        <ul class="nav">
          <li v-for="nav in nav.header_nav_list">
            <a :href="nav.link" v-if="nav.is_http">{{ nav.name }}</a>
            <router-link :to="nav.link" v-else>{{ nav.name }}</router-link>
          </li>
        </ul>
        <div class="search-warp">
          <div class="search-area">
            <input class="search-input" placeholder="请输入关键字..." type="text" autocomplete="off">
            <div class="hotTags">
              <router-link to="/search/?words=Vue" target="_blank" class="">Vue</router-link>
              <router-link to="/search/?words=Python" target="_blank" class="last">Python</router-link>
            </div>
          </div>
          <div class="showhide-search" data-show="no">
            <img class="imv2-search2" src="../assets/search.svg" alt="search"/>
          </div>
        </div>
        <div class="login-bar">
          <div class="shop-cart full-left">
            <img src="../assets/cart.svg" alt="cart"/>
            <span><router-link to="/cart">购物车</router-link></span>
          </div>
          <div class="login-box full-left">
            <span @click="state.show_login=true">登录</span>
            &nbsp;/&nbsp;
            <span>注册</span>
          </div>
        </div>
      </div>
    </div>
  </div>
  <el-dialog :width="600" v-model="state.show_login">
    <Login></Login>
  </el-dialog>
</template>


<script setup>
import nav from "../api/nav";
import Login from "./Login.vue";
import {reactive} from "vue";

const state = reactive({
  show_login: false,
})


// 请求头部导航列表
nav.get_header_nav().then(response => {
  nav.header_nav_list = response.data.data
})

</script>


<style scoped>
.header-box {
  height: 72px;
}

.header {
  width: 100%;
  height: 72px;
  box-shadow: 0 0.5px 0.5px 0 #c9c9c9;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  margin: auto;
  z-index: 99;
  background: #fff;
}

.header .content {
  max-width: 1366px;
  width: 100%;
  margin: 0 auto;
}

.header .content .logo a {
}

.header .content .logo {
  width: 140px;
  height: 72px;
  line-height: 72px;
  margin: 0 20px;
  float: left;
  cursor: pointer; /* 设置光标的形状为爪子 */
}

.header .content .logo img {
  vertical-align: middle;
  margin: -40px;
}

.header .nav li {
  float: left;
  height: 80px;
  line-height: 80px;
  margin-right: 30px;
  font-size: 16px;
  color: #4a4a4a;
  cursor: pointer;
}

.header .nav li span {
  padding-bottom: 16px;
  padding-left: 5px;
  padding-right: 5px;
}

.header .nav li span a {
  display: inline-block;
}

.header .nav li .this {
  color: #4a4a4a;
  border-bottom: 4px solid #ffc210;
}

.header .nav li:hover span {
  color: #000;
}

/*首页导航全局搜索*/
.search-warp {
  position: relative;
  float: left;
  margin-left: 24px;
}

.search-warp .showhide-search {
  width: 20px;
  height: 24px;
  text-align: right;
  position: absolute;
  display: inline-block;
  right: 0;
  bottom: 24px;
  padding: 0 8px;
  border-radius: 18px;
}

.search-warp .showhide-search i {
  display: block;
  height: 24px;
  color: #545C63;
  cursor: pointer;
  font-size: 18px;
  line-height: 24px;
  width: 20px;
}

.search-area {
  float: right;
  position: relative;
  height: 40px;
  padding-right: 36px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.4);
  zoom: 1;
  background: #F3F5F6;
  border-radius: 4px;
  margin: 16px 0;
  width: 324px;
  box-sizing: border-box;
  font-size: 0;
  -webkit-transition: width 0.3s;
  -moz-transition: width 0.3s;
  transition: width 0.3s;
}

.search-area .search-input {
  padding: 8px 12px;
  font-size: 14px;
  color: #9199A1;
  line-height: 24px;
  height: 40px;
  width: 100%;
  float: left;
  border: 0;
  -webkit-transition: background-color 0.3s;
  -moz-transition: background-color 0.3s;
  transition: background-color 0.3s;
  background-color: transparent;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  -ms-box-sizing: border-box;
  box-sizing: border-box;.inp .code
}

.search-area .search-input.w100 {
  width: 100%;
}

.search-area .hotTags {
  display: inline-block;
  position: absolute;
  top: 0;
  right: 32px;
}

.search-area .hotTags a {
  display: inline-block;
  padding: 4px 8px;
  height: 16px;
  font-size: 14px;
  color: #9199A1;
  line-height: 16px;
  margin-top: 8px;
  max-width: 60px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.search-area .hotTags a:hover {
  color: #F21F1F;
}

.search-area input::-webkit-input-placeholder {
  color: #A6A6A6;
}

.search-area input::-moz-placeholder {
  /* Mozilla Firefox 19+ */
  color: #A6A6A6;
}

.search-area input:-moz-placeholder {
  /* Mozilla Firefox 4 to 18 */
  color: #A6A6A6;
}

.search-area input:-ms-input-placeholder {
  /* Internet Explorer 10-11 */
  color: #A6A6A6;
}

.search-area .btn_search {
  float: left;
  cursor: pointer;
  width: 30px;
  height: 38px;
  text-align: center;
  -webkit-transition: background-color 0.3s;
  -moz-transition: background-color 0.3s;
  transition: background-color 0.3s;
}

.search-area .search-area-result {
  position: absolute;
  left: 0;
  top: 57px;
  width: 300px;
  margin-bottom: 20px;
  border-top: none;
  background-color: #fff;
  box-shadow: 0 8px 16px 0 rgba(7, 17, 27, 0.2);
  font-size: 12px;
  overflow: hidden;
  display: none;
  z-index: 800;
  border-bottom-right-radius: 8px;
  border-bottom-left-radius: 8px;
}

.search-area .search-area-result.hot-hide {
  top: 47px;
}

.search-area .search-area-result.hot-hide .hot {
  display: none;
}

.search-area .search-area-result.hot-hide .history {
  border-top: 0;
}

.search-area .search-area-result h2 {
  font-size: 12px;
  color: #1c1f21;
  line-height: 12px;
  margin-bottom: 8px;
  font-weight: 700;
}

.search-area .search-area-result .hot {
  padding: 12px 0 8px 12px;
  box-sizing: border-box;
}

.search-area .search-area-result .hot .hot-item {
  background: rgba(84, 92, 99, 0.1);
  border-radius: 12px;
  padding: 4px 12px;
  line-height: 16px;
  margin-right: 4px;
  margin-bottom: 4px;
  display: inline-block;
  cursor: pointer;
  font-size: 12px;
  color: #545c63;
}

.search-area .search-area-result .history {
  border-top: 1px solid rgba(28, 31, 33, 0.1);
  box-sizing: border-box;
}

.search-area .search-area-result .history li {
  height: 40px;
  line-height: 40px;
  padding: 0 10px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  color: #787d82;
  cursor: pointer;
}

.search-area .search-area-result .history li:hover,
.search-area .search-area-result .history li .light {
  color: #1c1f21;
  background-color: #edf0f2;
}


.header .login-bar {
  margin-top: 20px;
  height: 80px;
  float: right;
}

.header .login-bar .shop-cart {
  float: left;
  margin-right: 20px;
  border-radius: 17px;
  background: #f7f7f7;
  cursor: pointer;
  font-size: 14px;
  height: 28px;
  width: 88px;
  line-height: 32px;
  text-align: center;
}

.header .login-bar .shop-cart:hover {
  background: #f0f0f0;
}

.header .login-bar .shop-cart img {
  width: 15px;
  margin-right: 4px;
  margin-left: 6px;
}

.header .login-bar .shop-cart span {
  margin-right: 6px;
}

.header .login-bar .login-box {
  float: left;
  height: 28px;
  line-height: 30px;
}

.header .login-bar .login-box span {
  color: #4a4a4a;
  cursor: pointer;
}

.header .login-bar .login-box span:hover {
  color: #000000;
}
</style>
```

`views/Login.vue`，代码：

```vue
<template>
  <div class="login box">
    <img src="../assets/Loginbg.3377d0c.jpg" alt="login_background">
    <div class="login">
      <div class="login-title">
        <img src="../assets/logo.png" alt="">
        <p>帮助有志向的年轻人通过努力学习获得体面的工作和生活!</p>
      </div>
      <div class="login_box">
        <Login></Login>
      </div>
    </div>
  </div>
</template>

<script setup>
import Login from "../components/Login.vue"

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
  /*top: -438px;*/
  top: -250px;
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
```



### 绑定登陆页面路由地址

src/router/index.js，代码：

```javascript
import {createRouter, createWebHistory} from 'vue-router'
// 路由列表
const routes = [
    {
        meta: {
            title: "飞升在线教育-站点首页",
            keepAlive: true
        },
        path: '/',
        name: "Home",
        component: () => import("../views/Home.vue")
    },
    {
        meta: {
            title: "飞升在线教育-用户登录",
            keepAlive: true
        },
        path: '/login',
        name: "Login",
        component: () => import("../views/Login.vue")
    }
]
// 路由对象实例化
const router = createRouter({
    // history, 指定路由的模式
    history: createWebHistory(),
    // 路由列表
    routes,
});
// 暴露路由对象
export default router
```

### BUG修复

`BUG:` `login.vue`背景图显示不占满整个屏幕

`src/style.css`全局样式更改

~~~css
:root {
  font-family: Inter, system-ui, Avenir, Helvetica, Arial, sans-serif;
  line-height: 1.5;
  font-weight: 400;

  color-scheme: light dark;
  color: rgba(255, 255, 255, 0.87);
  background-color: #242424;

  font-synthesis: none;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  -webkit-text-size-adjust: 100%;
}

a {
  font-weight: 500;
  color: #646cff;
  text-decoration: inherit;
}
a:hover {
  color: #535bf2;
}

body {
  margin: 0;
  display: flex;
  place-items: center;
  min-width: 320px;
  min-height: 100vh;
}

h1 {
  font-size: 3.2em;
  line-height: 1.1;
}

button {
  border-radius: 8px;
  border: 1px solid transparent;
  padding: 0.6em 1.2em;
  font-size: 1em;
  font-weight: 500;
  font-family: inherit;
  background-color: #1a1a1a;
  cursor: pointer;
  transition: border-color 0.25s;
}
button:hover {
  border-color: #646cff;
}
button:focus,
button:focus-visible {
  outline: 4px auto -webkit-focus-ring-color;
}

.card {
  padding: 2em;
}

#app {
  max-width: 1920px;
  margin: 0 auto;
  /*padding: 2rem;*/
  text-align: center;
}

@media (prefers-color-scheme: light) {
  :root {
    color: #213547;
    background-color: #ffffff;
  }
  a:hover {
    color: #747bff;
  }
  button {
    background-color: #f9f9f9;
  }
}

~~~

`banner.vue`轮播图样式更改

~~~vue

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
  width: 1400px;
  margin: auto;
  border-radius: 8px 8px 0 0;
}
.g-banner .g-banner-content {
  position: relative;
  float: left;
  width: 1142px;
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
  width: 256px;
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
~~~

提交git

```bash
feature:前端登录注册页面;
全局样式更改，解决轮播图显示问题，解决login.vue页面背景图不占满整个屏幕问题；

# 执行 git push 可能会提示如下，跟着执行提示的命令即可。
git push --set-upstream origin feature/user  
# 这句命令表示提交的时候，同步创建线上分支
```



## 后端实现登陆认证



Django默认已经提供了认证系统Auth模块。认证系统包含：

- 用户管理
- 权限管理[RBAC]
- 用户组管理（就是权限里面的角色）
- 密码哈希系统（就是密码加密和验证密码）
- 用户登录或内容显示的表单和视图
- 一个可插拔的后台系统(admin站点)

Django默认用户的认证机制依赖Session机制，但是session认证机制在前后端分离项目中具有一定的局限性。

1. session默认会把session_id 作为cookie保存到客户端。有些客户端的是默认禁用cookie/或者没法使用cookie的。
2. session的数据默认是保存到服务端的，带来一定的存储要求。

所以，基于session的这种现状，我们一般在前后端分离的项目中，一般引入JWT认证机制来实现用户的登录和鉴权（鉴别身份，识别权限），jwt可以将用户的身份凭据存放在一个Token（认证令牌，本质上就是一个经过处理的字符串）中，然后把token发送给客户端，客户端可以选择采用自己的技术来保存这个token。

在django中如果要实现jwt认证，有一个常用的第三方jwt模块，我们可以很方便的去通过jwt对接Django的认证系统，帮助我们来快速实现：

- 用户的数据模型
- 用户密码的加密与验证
- 用户的权限系统



### Django用户模型类

```python
from django.contrib.auth.models import User
```

Django的Auth认证系统中提供了用户模型类User保存用户的数据，默认的User包含以下常见的基本字段：

| 字段名             | 字段描述                                                     |
| ------------------ | ------------------------------------------------------------ |
| `username`         | 必选。150个字符以内。 用户名可能包含字母数字，`_`，`@`，`+` `.` 和`-`个字符。 |
| `first_name`       | 可选（`blank=True`）。 少于等于30个字符。                    |
| `last_name`        | 可选（`blank=True`）。 少于等于30个字符。                    |
| `email`            | 可选（`blank=True`）。 邮箱地址。                            |
| `password`         | 必选。 密码的哈希加密串。 （Django 不保存原始密码）。 原始密码可以无限长而且可以包含任意字符。 |
| `groups`           | 与`Group` 之间的多对多关系。对接权限功能的。                 |
| `user_permissions` | 与`Permission` 之间的多对多关系。对接权限功能的。            |
| `is_staff`         | 布尔值。 设置用户是否可以访问Admin 站点。                    |
| `is_active`        | 布尔值。 指示用户的账号是否激活。 它不是用来控制用户是否能够登录，而是描述一种帐号的使用状态。值为False的时候，是无法登录的。 |
| `is_superuser`     | 是否是超级用户。超级用户具有所有权限。                       |
| `last_login`       | 用户最后一次登录的时间。                                     |
| `date_joined`      | 账户创建的时间。 当账号创建时，默认设置为当前的date/time。   |

### 创建用户模块的子应用

```shell
cd fsapi/apps/
python ../../manage.py startapp user
```

在settings/dev.py文件中注册子应用。

```python
INSTALLED_APPS = [
    ...
  	"user.apps.UserConfig",
]
```

创建`user/urls.py`子路由并在总路由中进行注册。

users/urls.py，代码：

```python
from rest_framework.routers import SimpleRouter
from . import views
router = SimpleRouter()
urlpatterns = [

]
urlpatterns += router.urls
```

`fsapi/urls.py`，总路由

```python
path('user/', include(('user.urls', 'user'), namespace='user')),
```



### 创建自定义的用户模型类

Django认证系统中提供的用户模型类及方法很方便，我们可以使用这个模型类，但是字段有些无法满足项目需求，如本项目中需要保存用户的手机号，需要给模型类添加额外的字段。

Django提供了`django.contrib.auth.models.AbstractUser`用户抽象模型类允许我们继承，扩展字段来使用Django认证系统的用户模型类。

在创建好的应用`models.py`中定义用户的用户模型类。

```python
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserInfo(AbstractUser):
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号')
    money = models.DecimalField(max_digits=9, default=0.0, decimal_places=2, verbose_name="钱包余额")
    credit = models.IntegerField(default=0, verbose_name="积分")
    avatar = models.ImageField(upload_to="avatar/%Y", default="", null=True, blank=True, verbose_name="个人头像")
    nickname = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="用户昵称")

    is_deleted = models.BooleanField(default=False, verbose_name="是否删除")

    class Meta:
        db_table = 'fs_user'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

```

我们自定义的用户模型类还不能直接被Django的认证系统所识别，需要在配置文件中告知Django认证系统使用我们自定义的模型类。

在`settings/dev.py`配置文件中进行设置

```python
AUTH_USER_MODEL = 'user.UserInfo'
```

`AUTH_USER_MODEL` 参数的设置以`点.`来分隔，表示`应用名.模型类名`。

**Django建议我们对于AUTH_USER_MODEL参数的设置一定要在第一次数据库迁移之前就设置好，否则后续使用可能出现未知错误。**

数据库已经迁移过的，再执行`python manage.py makemigrations`会报错。

![image-20230316103622041](https://img2023.cnblogs.com/blog/2570053/202303/2570053-20230316103624531-726162618.png)

这是表示有一个叫admin的子应用使用了原来的废弃的auth.User模型，但是目前数据库已经设置了默认的子应用为`users`的模型了，所以产生了冲突。那么这种冲突，我们需要重置下原来的auth模块的迁移操作，再次迁移就可以解决了。

```
解决步骤：
1. 备份数据库[如果刚开始开发，无需备份。]
   mysqldump -uroot -proot123456 fs > fs.sql

2. 注释掉users.UserInfo代码以及AUTH_USER_MODEL配置项，然后执行数据迁移回滚操作，把冲突的所有表迁移记录全部归零
   # python manage.py migrate <子应用目录> zero
   python manage.py migrate auth zero

3. 恢复users.UserInfo代码以及AUTH_USER_MODEL配置项，执行数据迁移。
   python manage.py makemigrations
   python manage.py migrate
4. 创建管理员查看auth功能是否能正常使用。
   python manage.py createsuperuser
```

提交版本

```bash
feature:后台初始化用户模型表；
```



### 实现jwt认证分布式认证流程

**可以直接过**

在用户注册或登录后，我们想记录用户的登录状态，或者为用户创建身份认证的凭证。我们不再使用Session认证机制，而使用Json Web Token认证机制。

```
Json web token (JWT), 是为了在网络应用环境间传递声明而执行的一种基于JSON的开放标准（(RFC 7519).该token被设计为紧凑且安全的，特别适用于分布式站点的单点登录（SSO）场景。JWT的声明一般被用来在身份提供者（客户端）和服务提供者（服务端）间传递被认证的用户身份信息，以便于从资源服务器获取资源，也可以增加一些额外的其它业务逻辑所必须的声明信息，该token也可直接被用于身份认证，也可被数据加密传输。
```



#### JWT的构成

JWT就一段字符串，由三段信息构成的，将这三段信息文本用`.`拼接一起就构成了Jwt token字符串。就像这样:

```
eyJ0eXAiOiAiand0IiwgImFsZyI6ICJIUzI1NiJ9.eyJzdWIiOiAicm9vdCIsICJleHAiOiAiMTUwMTIzNDU1IiwgImlhdCI6ICIxNTAxMDM0NTUiLCAibmFtZSI6ICJ3YW5neGlhb21pbmciLCAiYWRtaW4iOiB0cnVlLCAiYWNjX3B3ZCI6ICJRaUxDSmhiR2NpT2lKSVV6STFOaUo5UWlMQ0poYkdjaU9pSklVekkxTmlKOVFpTENKaGJHY2lPaUpJVXpJMU5pSjkifQ==.815ce0e4e15fff813c5c9b66cfc3791c35745349f68530bc862f7f63c9553f4b
```

第一部分我们称它为**头部**（header)，第二部分我们称其为**载荷**（payload, 类似于飞机上承载的物品)，第三部分是**签证**（signature).



#### header

jwt的头部承载两部分信息：

- typ: 声明token类型，这里是jwt ，typ的值也可以是：Bear
- alg: 声明签证的加密的算法 通常直接使用 HMAC SHA256

完整的头部就像下面这样的JSON：

```
{
  'typ': 'JWT',
  'alg': 'HS256'
}
```

然后将头部进行base64编码，构成了jwt的第一部分头部

python代码举例：

```python
import base64, json
header_data = {"typ": "jwt", "alg": "HS256"}
header = base64.b64encode( json.dumps(header_data).encode() ).decode()
print(header) # eyJ0eXAiOiAiand0IiwgImFsZyI6ICJIUzI1NiJ9
```



#### payload

载荷就是存放有效信息的地方。这个名字像是特指飞机上承载的货仓，这些有效信息包含三个部分:

- 标准声明
- 公共声明
- 私有声明

**标准声明**指定jwt实现规范中要求的属性。 (官方建议但不强制使用) ：

- iss: jwt签发者
- sub: jwt所面向的用户
- **aud**: 接收jwt的一方
- **exp**: jwt的过期时间，这个过期时间必须要大于签发时间
- **nbf**: 定义在什么时间之后，该jwt才可以使用
- **iat**: jwt的签发时间
- **jti**: jwt的唯一身份标识，主要用来作为一次性token, 从而回避重放攻击。

**公共声明** ： 公共的声明可以添加任何的公开信息，一般添加用户的相关信息或其他业务需要的必要信息.但不建议添加敏感信息，因为该部分在客户端可直接读取.

**私有声明** ： 私有声明是提供者和消费者所共同定义的声明，一般不建议存放敏感信息，里面存放的是一些可以在服务端或者客户端通过秘钥进行加密和解密的加密信息。往往采用的RSA非对称加密算法。

举例，定义一个payload载荷信息，demo/jwtdemo.py：

```python
import base64, json, time

if __name__ == '__main__':
    # 载荷
    iat = int(time.time())
    payload_data = {
        "sub": "root",
        "exp": iat + 3600,  # 假设一小时过期
        "iat": iat,
        "name": "wangxiaoming",
        "avatar": "1.png",
        "user_id": 1,
        "admin": True,
        "acc_pwd": "QiLCJhbGciOiJIUzI1NiJ9QiLCJhbGciOiJIUzI1NiJ9QiLCJhbGciOiJIUzI1NiJ9",
    }
    # 将其进行base64编码，得到JWT的第二部分。
    payload = base64.b64encode(json.dumps(payload_data).encode()).decode()
    print(payload)
```



#### signature

JWT的第三部分是一个签证信息，用于辨真伪，防篡改。这个签证信息由三部分组成：

- header (base64后的头部)
- payload (base64后的载荷)
- secret（保存在服务端的秘钥字符串，不会提供给客户端的，这样可以保证客户端没有签发token的能力）

举例，定义一个完整的jwt token，jwtdemo.py：

```python
import base64, json, hashlib

if __name__ == '__main__':
    """jwt 头部的生成"""
    header_data = {"typ": "jwt", "alg": "HS256"}
    header = base64.b64encode( json.dumps(header_data).encode() ).decode()
    print(header) # eyJ0eXAiOiAiand0IiwgImFsZyI6ICJIUzI1NiJ9

    """jwt 载荷的生成"""
    payload_data = {
        "sub": "root",
        "exp": "150123455",
        "iat": "150103455",
        "name": "wangxiaoming",
        "admin": True,
        "acc_pwd": "QiLCJhbGciOiJIUzI1NiJ9QiLCJhbGciOiJIUzI1NiJ9QiLCJhbGciOiJIUzI1NiJ9",
    }
    # 将其进行base64编码，得到JWT的第二部分。
    payload = base64.b64encode(json.dumps(payload_data).encode()).decode()
    print(payload) # eyJzdWIiOiAicm9vdCIsICJleHAiOiAiMTUwMTIzNDU1IiwgImlhdCI6ICIxNTAxMDM0NTUiLCAibmFtZSI6ICJ3YW5neGlhb21pbmciLCAiYWRtaW4iOiB0cnVlLCAiYWNjX3B3ZCI6ICJRaUxDSmhiR2NpT2lKSVV6STFOaUo5UWlMQ0poYkdjaU9pSklVekkxTmlKOVFpTENKaGJHY2lPaUpJVXpJMU5pSjkifQ==

    # from django.conf import settings
    # secret = settings.SECRET_KEY
    secret = 'django-insecure-hbcv-y9ux0&8qhtkgmh1skvw#v7ru%t(z-#chw#9g5x1r3z=$p'
    data = header + payload + secret  # 秘钥绝对不能提供给客户端。
    HS256 = hashlib.sha256()
    HS256.update(data.encode('utf-8'))
    signature = HS256.hexdigest()
    print(signature) # 815ce0e4e15fff813c5c9b66cfc3791c35745349f68530bc862f7f63c9553f4b

    # jwt 最终的生成
    token = f"{header}.{payload}.{signature}"
    print(token)
    # eyJ0eXAiOiAiand0IiwgImFsZyI6ICJIUzI1NiJ9.eyJzdWIiOiAicm9vdCIsICJleHAiOiAiMTUwMTIzNDU1IiwgImlhdCI6ICIxNTAxMDM0NTUiLCAibmFtZSI6ICJ3YW5neGlhb21pbmciLCAiYWRtaW4iOiB0cnVlLCAiYWNjX3B3ZCI6ICJRaUxDSmhiR2NpT2lKSVV6STFOaUo5UWlMQ0poYkdjaU9pSklVekkxTmlKOVFpTENKaGJHY2lPaUpJVXpJMU5pSjkifQ==.815ce0e4e15fff813c5c9b66cfc3791c35745349f68530bc862f7f63c9553f4b
```

**注意：secret是保存在服务器端的，jwt的签发生成也是在服务器端的，secret就是用来进行jwt的签发和jwt的验证，所以，它就是你服务端的私钥，在任何场景都不应该流露出去。一旦客户端得知这个secret, 那就意味着客户端是可以自我签发jwt了。**



举例，定义一个完整的jwt token，并认证token，demo/jwtdemo.py：

```python
import base64, json, hashlib
from datetime import datetime

if __name__ == '__main__':
    # 头部生成原理
    header_data = {
        "typ": "jwt",
        "alg": "HS256"
    }
    # print( json.dumps(header_data).encode() )
    # json转成字符串，接着base64编码处理
    header = base64.b64encode(json.dumps(header_data).encode()).decode()
    print(header)  # eyJ0eXAiOiAiand0IiwgImFsZyI6ICJIUzI1NiJ9


    # 载荷生成原理
    iat = int(datetime.now().timestamp()) # 签发时间
    payload_data = {
        "sub": "root",
        "exp": iat + 3600,  # 假设一小时过期
        "iat": iat,
        "name": "wangxiaoming",
        "admin": True,
        "acc_pwd": "QiLCJhbGciOiJIUzI1NiJ9QiLCJhbGciOiJIUzI1NiJ9QiLCJhbGciOiJIUzI1NiJ9",
    }

    payload = base64.b64encode(json.dumps(payload_data).encode()).decode()
    print(payload)
    # eyJzdWIiOiAicm9vdCIsICJleHAiOiAxNjM2NTk3OTAzLCAiaWF0IjogMTYzNjU5NDMwMywgIm5hbWUiOiAid2FuZ3hpYW9taW5nIiwgImFkbWluIjogdHJ1ZSwgImFjY19wd2QiOiAiUWlMQ0poYkdjaU9pSklVekkxTmlKOVFpTENKaGJHY2lPaUpJVXpJMU5pSjlRaUxDSmhiR2NpT2lKSVV6STFOaUo5In0=

    # from django.conf import settings
    # secret = settings.SECRET_KEY
    secret = 'django-insecure-hbcv-y9ux0&8qhtkgmh1skvw#v7ru%t(z-#chw#9g5x1r3z=$p'

    data = header + payload + secret  # 秘钥绝对不能提供给客户端。

    HS256 = hashlib.sha256()
    HS256.update(data.encode('utf-8'))
    signature = HS256.hexdigest()
    print(signature) # ce46f9d350be6b72287beb4f5f9b1bc4c42fc1a1f8c8db006e9e99fd46961156

    # jwt 最终的生成
    token = f"{header}.{payload}.{signature}"
    print(token)
    # eyJ0eXAiOiAiand0IiwgImFsZyI6ICJIUzI1NiJ9.eyJzdWIiOiAicm9vdCIsICJleHAiOiAxNjM2NTk3OTAzLCAiaWF0IjogMTYzNjU5NDMwMywgIm5hbWUiOiAid2FuZ3hpYW9taW5nIiwgImFkbWluIjogdHJ1ZSwgImFjY19wd2QiOiAiUWlMQ0poYkdjaU9pSklVekkxTmlKOVFpTENKaGJHY2lPaUpJVXpJMU5pSjlRaUxDSmhiR2NpT2lKSVV6STFOaUo5In0=.ce46f9d350be6b72287beb4f5f9b1bc4c42fc1a1f8c8db006e9e99fd46961156


    # 认证环节
    token = "eyJ0eXAiOiAiand0IiwgImFsZyI6ICJIUzI1NiJ9.eyJzdWIiOiAicm9vdCIsICJleHAiOiAxNjM2NTk3OTAzLCAiaWF0IjogMTYzNjU5NDMwMywgIm5hbWUiOiAid2FuZ3hpYW9taW5nIiwgImFkbWluIjogdHJ1ZSwgImFjY19wd2QiOiAiUWlMQ0poYkdjaU9pSklVekkxTmlKOVFpTENKaGJHY2lPaUpJVXpJMU5pSjlRaUxDSmhiR2NpT2lKSVV6STFOaUo5In0=.ce46f9d350be6b72287beb4f5f9b1bc4c42fc1a1f8c8db006e9e99fd46961156"
    header, payload, signature = token.split(".")

    # 验证是否过期了
    # 先基于base64，接着使用json解码
    payload_data = json.loads( base64.b64decode(payload.encode()) )
    print(payload_data)
    exp = payload_data.get("exp", None)
    if exp is not None and int(exp) < int(datetime.now().timestamp()):
        print("token过期！！！")
    else:
        print("没有过期")

    # 验证token是否有效，是否被篡改
    # from django.conf import settings
    # secret = settings.SECRET_KEY
    secret = 'django-insecure-hbcv-y9ux0&8qhtkgmh1skvw#v7ru%t(z-#chw#9g5x1r3z=$p'
    data = header + payload + secret  # 秘钥绝对不能提供给客户端。
    HS256 = hashlib.sha256()
    HS256.update(data.encode('utf-8'))
    new_signature = HS256.hexdigest()

    if new_signature != signature:
        print("认证失败")
    else:
        print("认证通过")

```

关于签发和核验JWT，python中提供了一个PyJWT模块帮我们实现jwt的整体流程。我们可以使用Django REST framework JWT扩展来完成。

文档网站：https://jpadilla.github.io/django-rest-framework-jwt/



### 安装配置JWT

安装

```shell
pip install djangorestframework-jwt
```

settings/dev.py，配置jwt

```python
# drf配置
REST_FRAMEWORK = {
    # 自定义异常处理
    'EXCEPTION_HANDLER': 'fsapi.extension.exceptions.custom_exception_handler',
    # 自定义认证（从上到下挨个认证）
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',  # jwt认证
        'rest_framework.authentication.SessionAuthentication',  # session认证
        'rest_framework.authentication.BasicAuthentication',
    ),
}

# jwt认证相关配置项
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(weeks=1),  # 设置jwt的有效期，一周有效
}
```



### 生成jwt

Django REST framework JWT 扩展的说明文档中提供了手动签发JWT的方法

官方文档：https://jpadilla.github.io/django-rest-framework-jwt/#creating-a-new-token-manually

```python
# 可以进入到django的终端下测试生成token的逻辑
python manage.py shell

# 引入jwt配置
from rest_framework_jwt.settings import api_settings
# 获取载荷生成函数
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
# 获取token生成函数
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

# 示例
from user.models import UserInfo
user = UserInfo.objects.first()
payload = jwt_payload_handler(user)  # user用户模型对象
# 生成token
token = jwt_encode_handler(payload)
```

在用户注册或登录成功后，在序列化器中返回用户信息以后同时返回token即可。



### 后端实现登陆认证接口

Django REST framework-JWT为了方便开发者使用jwt提供了登录获取token的视图，开发者可以直接使用它绑定一个url地址即可。

在users/urls.py中绑定登陆视图

```python
from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_jwt.views import obtain_jwt_token

from . import views

router = SimpleRouter()
# router.register('', views.)

urlpatterns = [
    path("login/", obtain_jwt_token, name="login"),
]

urlpatterns += router.urls

# from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
# obtain_jwt_token实际上就是 rest_framework_jwt.views.ObtainJSONWebToken.as_view()
# 登录视图，获取access_token
# obtain_jwt_token = ObtainJSONWebToken.as_view()
# 刷新token视图，依靠旧的access_token生成新的access_token
# refresh_jwt_token = RefreshJSONWebToken.as_view()
# 验证现有的access_token是否有效
# verify_jwt_token = VerifyJSONWebToken.as_view()

```

接下来，我们可以通过postman来测试下功能，可以发送form表单，也可以发送json，username和password是必填字段

~~~json
{
    "username":"root",
    "password":"root123456"
}
~~~

![image-20230316124832808](https://img2023.cnblogs.com/blog/2570053/202303/2570053-20230316124834681-1796293459.png)

### 更新异常处理

`extension/exceptions.py`

~~~python
from redis import RedisError
from django.db import DatabaseError

from rest_framework.views import exception_handler
from rest_framework import status

from fsapi.extension.response import APIResponse
from fsapi.extension.logger import log


def custom_exception_handler(exc, context):
    """
    自定义异常处理
    :param exc: 异常类
    :param context: 抛出异常的上下文
    :return: Response响应对象
    """
    # 调用drf框架原生的异常处理方法
    response = exception_handler(exc, context)
    view = context['view']
    if not response:
        if isinstance(exc, DatabaseError):
            # mysql数据库异常
            response = APIResponse(status.HTTP_507_INSUFFICIENT_STORAGE, '[%s] %s' % (view, "MySQL数据库内部错误"))
        elif isinstance(exc, RedisError):
            # redis数据库异常
            response = APIResponse(status.HTTP_507_INSUFFICIENT_STORAGE, '[%s] %s' % (view, "Redis数据库异常"))
        else:
            try:
                if isinstance(response.data, list):
                    response = APIResponse(status.HTTP_500_INTERNAL_SERVER_ERROR, '[%s] %s' % (view, response.data))
                else:
                    response = APIResponse(
                        status.HTTP_500_INTERNAL_SERVER_ERROR,
                        '[%s] %s' % (view, response.data.get('detail') or response.data)
                    )
            except AttributeError:
                # 处理resposne没有data属性的情况
                response = APIResponse(status.HTTP_500_INTERNAL_SERVER_ERROR, '[%s] %s' % (view, exc))
    else:
        response = APIResponse(status.HTTP_500_INTERNAL_SERVER_ERROR, '[%s] %s' % (view, exc))
    log.error('[%s] %s' % (view, exc))
    return response

~~~

提交git

~~~python
feature:后台实现JWT基本登录；
BUG：更新异常处理函数；
~~~





## 前端实现登陆功能

在登陆组件中找到登陆按钮，绑定点击事件，调用登录处理方法loginhandle。

### 基本实现

`components/Login.vue`

```html
<template>
  <div class="title">
    <span :class="{active:user.login_type==0}" @click="user.login_type=0">密码登录</span>
    <span :class="{active:user.login_type==1}" @click="user.login_type=1">短信登录</span>
  </div>
  <div class="inp" v-if="user.login_type==0">
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
    <p class="go_login" >没有账号 <span>立即注册</span></p>
  </div>
  <div class="inp" v-show="user.login_type==1">
    <input v-model="user.mobile" type="text" placeholder="手机号码" class="user">
    <input v-model="user.code"  type="text" class="code" placeholder="短信验证码">
    <el-button id="get_code" type="primary">获取验证码</el-button>
    <button class="login_btn">登录</button>
    <p class="go_login" >没有账号 <span>立即注册</span></p>
  </div>
</template>
```

```vue
<script setup>
import user from "../api/user";
import { ElMessage } from 'element-plus'

// 登录处理
const loginhandler = ()=>{
  // 验证数据
  if(user.account.length<1 || user.password.length<1){
    // 错误提示
    console.log("用户名或密码不能为空！");
    ElMessage.error("用户名或密码不能为空！");
    return ;
  }

  // 登录请求处理
  user.login().then(response=>{
    console.log(response.data);
    ElMessage.success("登录成功！");
  }).catch(error=>{
    ElMessage.error("登录失败！");
  })
}

</script>
```

在api中请求后端，api/user.js，代码：

```javascript
import http from "../utils/http"
import {reactive, ref} from "vue"

const user = reactive({
    login_type: 0, // 登录方式，0，密码登录，1，短信登录
    account: "",  // 登录账号/手机号/邮箱
    password: "", // 登录密码
    remember: false, // 是否记住登录状态
    mobile: "",      // 登录手机号码
    code: "",        // 短信验证码
    login() {
        // 用户登录
        return http.post("/user/login/", {
            "username": this.account,
            "password": this.password,
        })
    }
})

export default user;
```

解决elementplus显示错误提示框没有样式的问题。src/main.js，代码：

```javascript
import {createApp} from 'vue'
import './style.css'
import App from './App.vue'
// 注册router对象
import router from "./router/index.js";
import 'element-plus/dist/index.css';

createApp(App).use(router).mount('#app')
```

提交git版本

```bash
feature:客户端请求登陆功能基本实现；
```



### 前端保存jwt

我们保存在浏览器的HTML5提供的本地存储对象中。

浏览器的本地存储提供了2个全局的js对象，给我们用于保存数据的，分别是sessionStorage 和 localStorage ：

- **sessionStorage** 会话存储，浏览器关闭即数据丢失。
- **localStorage** 永久存储，长期有效，浏览器关闭了也不会丢失。

我们可以通过浏览器提供的F12中的Application调试选项中的界面查看到保存在本地存储的数据。

注意：不同的域名或IP下的数据，互不干扰的，相互独立，也调用或访问不了其他域名下的数据。

sessionStorage和localStorage提供的操作一模一样，基本使用：

```js
// 添加/修改数据
sessionStorage.setItem("变量名","变量值")
// 简写：sessionStorage.变量名 = 变量值

// 读取数据
sessionStorage.getItem("变量名")
// 简写：sessionStorage.变量名

// 删除一条数据
sessionStorage.removeItem("变量名")
// 清空所有数据
sessionStorage.clear()  // 慎用，会清空当前域名下所有的存储在本地的数据



// 添加/修改数据
localStorage.setItem("变量名","变量值")
// 简写：localStorage.变量名 = 变量值

// 读取数据
localStorage.getItem("变量名")
// 简写：localStorage.变量名

// 删除数据
localStorage.removeItem("变量名")
// 清空数据
localStorage.clear()  // 慎用，会清空当前域名下所有的存储在本地的数据
```



登陆子组件，components/Login.vue，代码：

```vue
<script setup>
import user from "../api/user";
import {ElMessage} from 'element-plus'

// 登录处理
const loginhandler = () => {
  if (user.account.length < 1 || user.password.length < 1) {
    // 错误提示
    console.log("用户名或密码不能为空！");
    ElMessage.error('用户名或密码不能为空！');
    return;  // 在函数/方法中，可以阻止代码继续往下执行
  }

  // 发送请求
  user.login({
    username: user.account,
    password: user.password
  }).then(response => {
    // 保存token，并根据用户的选择，是否记住密码
    localStorage.removeItem("token");
    sessionStorage.removeItem("token");
    console.log(response.data.token);
    if (user.remember) { // 判断是否记住登录状态
      // 记住登录
      localStorage.token = response.data.token
    } else {
      // 不记住登录，关闭浏览器以后就删除状态
      sessionStorage.token = response.data.token;
    }
    // 保存token，并根据用户的选择，是否记住密码
    // 成功提示
    ElMessage.success("登录成功！");
    console.log("登录成功！");
    // 关闭登录弹窗
  }).catch(error => {
    console.log(error);
  })
}

</script>
```

提交版本

```bash
feature:客户端使用本地存储保存token；
```



### 首页登录成功以后关闭登录弹窗

在components/Login.vue中，基于emit发送自定义事件通知父组件关闭当前登录窗口。components/Login.vue，代码：

```vue

<script setup>
import user from "../api/user"
import { ElMessage } from 'element-plus'
const emit = defineEmits(["successhandle",])

const loginhandler = ()=>{
  // 登录处理
  if(user.account.length<1 || user.password.length<1){
    // 错误提示
    ElMessage.error('用户名或密码不能为空！');
    return false // 在函数/方法中，可以阻止代码继续往下执行
  }

  // 发送请求
  user.login({
    username: user.account,
    password: user.password
  }).then(response=>{
    // 保存token，并根据用户的选择，是否记住密码
    localStorage.removeItem("token")
    sessionStorage.removeItem("token")
    if(user.remember){ // 判断是否记住登录状态
      // 记住登录
      localStorage.token = response.data.token
    }else{
      // 不记住登录，关闭浏览器以后就删除状态
      sessionStorage.token = response.data.token
    }
    // 保存token，并根据用户的选择，是否记住密码
    // 成功提示
    ElMessage.success("登录成功！")
    // 关闭登录弹窗，对外发送一个登录成功的信息
    user.account = ""
    user.password = ""
    user.mobile = ""
    user.code = ""
    user.remember = false
    emit("successhandle")

  }).catch(error=>{
    ElMessage.error("登录异常！")
  })
}

</script>
```

在首页中是通过Header子组件调用的component/Login.vue，所以我们需要在Header子组件中监听自定义事件login_success并关闭登陆弹窗即可。components/Header.vue，代码：

```vue
<el-dialog :width="600" v-model="state.show_login">
    <Login @successhandle="login_success"></Login>
</el-dialog>
```

```vue
<script setup>
import nav from "../api/nav";
import Login from "./Login.vue";
import {reactive} from "vue";

const state = reactive({
  show_login: false,
})


// 请求头部导航列表
nav.get_header_nav().then(response => {
  nav.header_nav_list = response.data.data
})

// 用户登录成功以后的处理
const login_success = (token) => {
  state.show_login = false
}
</script>
```

views/Login.vue登陆页面中，则监听Login子组件登陆成功的自定义事件以后直接路由跳转到首页即可。`views/Login.vue`，代码：

```vue
<template>
  <div class="login box">
    <img src="../assets/Loginbg.3377d0c.jpg" alt="login_background">
    <div class="login">
      <div class="login-title">
        <img src="../assets/logo.png" alt="">
        <p>帮助有志向的年轻人通过努力学习获得体面的工作和生活!</p>
      </div>
      <div class="login_box">
        <Login @successhandle="login_success"></Login>
      </div>
    </div>
  </div>
</template>
```

```vue
<script setup>
import Login from "../components/Login.vue"
import router from "../router";

// 用户登录成功以后的处理
const login_success = () => {
  // 跳转到首页
  router.push("/");
}

</script>
```

提交版本

```bash
feature:客户端登陆成功以后关闭窗口或登陆页面；
```



### 自定义载荷

默认返回值的token只有username和user_id以及email，我们如果还需在客户端页面中显示当前登陆用户的其他信息(例如：头像)，则可以把额外的用户信息添加到jwt的返回结果中。通过修改该视图的返回值可以完成我们的需求。

在extension/authenticate.py 中，创建jwt_payload_handler函数重写返回值。

```python
from rest_framework_jwt.utils import jwt_payload_handler


def custom_jwt_payload_handler(user):
    """
    自定义载荷信息
    :params user  用户模型实例对象
    """
    # 先让jwt模块生成自己的载荷信息
    payload = jwt_payload_handler(user)
    # 追加自己要返回的内容
    if hasattr(user, 'avatar'):
        payload['avatar'] = user.avatar.url if user.avatar else ""
    if hasattr(user, 'nickname'):
        payload['nickname'] = user.nickname
    if hasattr(user, 'money'):
        payload['money'] = float(user.money)
    if hasattr(user, 'credit'):
        payload['credit'] = user.credit
    return payload

```

修改settings/dev.py配置文件

```python
# jwt认证相关配置项
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(weeks=1),  # 设置jwt的有效期，一周有效
    # 自定义载荷
    'JWT_PAYLOAD_HANDLER': 'fsapi.extension.authenticate.custom_jwt_payload_handler',
}
```

提交git版本

```bash
feature:服务端重写jwt的自定义载荷生成函数增加token载荷信息;
```



### 多条件登录

JWT扩展的登录视图，在收到用户名与密码时，也是调用Django的认证系统中提供的**authenticate()**来检查用户名与密码是否正确。

我们可以通过修改Django认证系统的认证后端（主要是authenticate方法）来支持登录账号既可以是用户名也可以是手机号。

**修改Django认证系统的认证后端需要继承django.contrib.auth.backends.ModelBackend，并重写authenticate方法。**

`authenticate(self, request, username=None, password=None, **kwargs)`方法的参数说明：

- request 本次认证的请求对象
- username 本次认证提供的用户账号
- password 本次认证提供的密码

**我们想要让用户既可以以用户名登录，也可以以手机号登录，那么对于authenticate方法而言，username参数即表示用户名或者手机号。**

重写authenticate方法的思路：

1. 根据username参数查找用户User对象，username参数可能是用户名，也可能是手机号
2. 若查找到User对象，调用User对象的check_password方法检查密码是否正确

在extension/authenticate.py中编写：

```python
from django.db.models import Q
from django.contrib.auth.backends import ModelBackend, UserModel

from rest_framework_jwt.utils import jwt_payload_handler


def custom_jwt_payload_handler(user):
    """
    自定义载荷信息
    :params user  用户模型实例对象
    """
    # 先让jwt模块生成自己的载荷信息
    payload = jwt_payload_handler(user)
    # 追加自己要返回的字段内容
    if hasattr(user, 'avatar'):
        payload['avatar'] = user.avatar.url if user.avatar else ""
    if hasattr(user, 'nickname'):
        payload['nickname'] = user.nickname
    if hasattr(user, 'money'):
        payload['money'] = float(user.money)
    if hasattr(user, 'credit'):
        payload['credit'] = user.credit

    return payload


def get_user_by_account(account):
    """
    根据帐号信息获取user模型实例对象
    :param account: 账号信息，可以是用户名，也可以是手机号，甚至其他的可用于识别用户身份的字段信息
    :return: User对象 或者 None
    """
    user = UserModel.objects.filter(Q(mobile=account) | Q(username=account) | Q(email=account)).first()
    return user


class CustomAuthBackend(ModelBackend):
    """
    自定义用户认证类[实现多条件登录]
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        多条件认证方法
        :param request: 本次客户端的http请求对象
        :param username:  本次客户端提交的用户信息，可以是user，也可以mobile或其他唯一字段
        :param password: 本次客户端提交的用户密码
        :param kwargs: 额外参数
        :return:
        """
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)

        if username is None or password is None:
            return
        # 根据用户名信息useranme获取账户信息
        user = get_user_by_account(username)
        if user and user.check_password(password) and self.user_can_authenticate(user):
            return user

```

在配置文件settings/dev.py中告知Django使用我们自定义的认证后端，注意不是给drf添加设置。

```python
# django自定义认证
AUTHENTICATION_BACKENDS = ['fsapi.extension.authenticate.CustomAuthBackend', ]
```

提交版本

```bash
feature:服务端实现jwt多条件登陆认证;
```



## 客户端实现用户登陆状态的判断

`components/Header.vue`，子组件代码：

```vue
<template>
    <div class="header-box">
      <div class="header">
        <div class="content">
          <div class="logo">
            <router-link to="/"><img src="../assets/logo.svg" alt=""></router-link>
          </div>
          <ul class="nav">
              <li v-for="nav in nav.header_nav_list">
                <a :href="nav.link" v-if="nav.is_http">{{nav.name}}</a>
                <router-link :to="nav.link" v-else>{{nav.name}}</router-link>
              </li>
          </ul>
          <div class="search-warp">
            <div class="search-area">
              <input class="search-input" placeholder="请输入关键字..." type="text" autocomplete="off">
              <div class="hotTags">
                <router-link to="/search/?words=Vue" target="_blank" class="">Vue</router-link>
                <router-link to="/search/?words=Python" target="_blank" class="last">Python</router-link>
              </div>
            </div>
            <div class="showhide-search" data-show="no"><img class="imv2-search2" src="../assets/search.svg" /></div>
          </div>
          <div class="login-bar logined-bar" v-show="state.is_login">
            <div class="shop-cart ">
              <img src="../assets/cart.svg" alt="" />
              <span><router-link to="/cart">购物车</router-link></span>
            </div>
            <div class="login-box ">
              <router-link to="">我的课堂</router-link>
              <el-dropdown>
                <span class="el-dropdown-link">
                  <el-avatar class="avatar" size="50"
                             src="/src/assets/avatar.jpg"></el-avatar>
                </span>
                <template #dropdown>
                  <el-dropdown-menu>
                    <el-dropdown-item :icon="UserFilled">学习中心</el-dropdown-item>
                    <el-dropdown-item :icon="List">订单列表</el-dropdown-item>
                    <el-dropdown-item :icon="Setting">个人设置</el-dropdown-item>
                    <el-dropdown-item :icon="Position">注销登录</el-dropdown-item>
                  </el-dropdown-menu>
                </template>
              </el-dropdown>
            </div>
          </div>
          <div class="login-bar" v-show="!state.is_login">
            <div class="shop-cart full-left">
              <img src="../assets/cart.svg" alt="" />
              <span><router-link to="/cart">购物车</router-link></span>
            </div>
            <div class="login-box full-left">
              <span @click="state.show_login=true">登录</span>
              &nbsp;/&nbsp;
              <span>注册</span>
            </div>
          </div>
        </div>
      </div>
    </div>
    <el-dialog :width="600" v-model="state.show_login">
      <Login @successhandle="login_success"></Login>
    </el-dialog>
</template>
```

```vue
<script setup>
import nav from "../api/nav";
import Login from "./Login.vue";
import {reactive} from "vue";
import {UserFilled, List, Setting, Position} from '@element-plus/icons-vue'

const state = reactive({
  is_login: true,  // 登录状态
  show_login: false,
})


// 请求头部导航列表
nav.get_header_nav().then(response => {
  nav.header_nav_list = response.data.data
})

// 用户登录成功以后的处理
const login_success = (token) => {
  state.show_login = false
}
</script>
```

```vue
// 追加
<style scoped>
/* 登陆后状态栏 */
.logined-bar{
  margin-top: 0;
  height: 72px;
  line-height: 72px;
}
.header .logined-bar .shop-cart{
  height: 32px;
  line-height: 32px;
}
.logined-bar .login-box{
  height: 72px;
  line-height: 72px;
  position: relative;
}
.logined-bar .el-avatar{
  float: right;
  width: 50px;
  height: 50px;
  position: absolute;
  top: -10px;
  left: 10px;
  transition: transform .5s ease-in .1s;
}
.logined-bar .el-avatar:hover{
  transform: scale(1.3);
}
</style>
```

如果图标没有显示，可以采用安装以下组件：

```bash
yarn add @element-plus/icons-vue
```



### 使用Vuex保存用户登录状态并判断是否在登陆栏显示用户信息

Vuex是Vue框架生态的一环，用于实现全局数据状态的统一管理。

官方地址：https://next.vuex.vuejs.org/zh/index.html

```bash
# 在客户端项目根目录下执行安装命令
yarn add vuex@next
```

Vuex初始化，是在src目录下创建store目录，store目录下创建index.js文件对vuex进行初始化：

```javascript
import {createStore} from "vuex"

// 实例化一个vuex存储库
export default createStore({
    state () {  // 数据存储位置，相当于组件中的data
        return {
          user: {

          }
        }
    },
    mutations: { // 操作数据的方法，相当于methods
        login (state, user) {  // state 就是上面的state   state.user 就是上面的数据
          state.user = user
        }
    }
})
```

main.js中注册vuex，代码：

```javascript
import {createApp} from 'vue'
import './style.css'
import App from './App.vue'
// 注册router对象
import router from "./router/index.js";
// element-plus
import 'element-plus/dist/index.css';
import 'element-plus/theme-chalk/index.css'
// 注册store
import store from "./store"

createApp(App).use(router).use(store).mount('#app')
```

在components/Login.vue子组件中登录成功以后，记录用户信息到vuex中。

```vue
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
    ElMessage.error('用户名或密码不能为空！');
    return false // 在函数/方法中，可以阻止代码继续往下执行
  }

  // 发送请求
  user.login({
    username: user.account,
    password: user.password
  }).then(response => {
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
    ElMessage.success("登录成功！")
    // 关闭登录弹窗，对外发送一个登录成功的信息
    user.account = ""
    user.password = ""
    user.mobile = ""
    user.code = ""
    user.remember = false
    emit("login_success")

  }).catch(error => {
    ElMessage.error("登录异常！")
  })
}

</script>
```

记录下来了以后，我们就可以直接components/Header.vue中读取Vuex中的用户信息。

```vue
<template>
  <div class="header-box">
    <div class="header">
      <div class="content">
        <div class="logo">
          <router-link to="/"><img src="../assets/logo.png" alt=""></router-link>
        </div>
        <ul class="nav">
          <li v-for="item in nav.header_nav_list">
            <a v-if="item.is_http" :href="item.link">{{ item.name }}</a>
            <router-link v-else :to="item.link">{{ item.name }}</router-link>
          </li>
        </ul>
        <div class="search-warp">
          <div class="search-area">
            <input class="search-input" placeholder="请输入关键字..." type="text" autocomplete="off">
            <div class="hotTags">
              <router-link to="/search/?words=Vue" target="_blank" class="">Vue</router-link>
              <router-link to="/search/?words=Python" target="_blank" class="last">Python</router-link>
            </div>
          </div>
          <div class="showhide-search" data-show="no"><img class="imv2-search2" src="../assets/search.svg"
                                                           alt="search"/></div>
        </div>
        <div class="login-bar logined-bar" v-if="store.state.user.user_id">
          <div class="shop-cart ">
            <img src="../assets/cart.svg" alt=""/>
            <span><router-link to="/cart">购物车</router-link></span>
          </div>
          <div class="login-box ">
            <router-link to="">我的课堂</router-link>
            <el-dropdown>
                <span class="el-dropdown-link">
                  <el-avatar class="avatar" size="50" src="/src/assets/avatar.jpg"></el-avatar>
                </span>
              <template #dropdown>
                <el-dropdown-menu>
                  <el-dropdown-item icon="el-icon-user">学习中心</el-dropdown-item>
                  <el-dropdown-item icon="el-icon-edit-outline">订单列表</el-dropdown-item>
                  <el-dropdown-item icon="el-icon-setting">个人设置</el-dropdown-item>
                  <el-dropdown-item icon="el-icon-position">注销登录</el-dropdown-item>
                </el-dropdown-menu>
              </template>
            </el-dropdown>
          </div>
        </div>
        <div class="login-bar" v-else>
          <div class="shop-cart full-left">
            <img src="../assets/cart.svg" alt=""/>
            <span><router-link to="/cart">购物车</router-link></span>
          </div>
          <div class="login-box full-left">
            <span @click="state.show_login=true">登录</span>
            &nbsp;/&nbsp;
            <span>注册</span>
          </div>
        </div>
      </div>
    </div>
  </div>
  <el-dialog :width="600" v-model="state.show_login">
    <Login @login_success="login_success"></Login>
  </el-dialog>
</template>
```

```vue
<script setup>
import nav from "../api/nav";
import Login from "./Login.vue";
import {reactive} from "vue";

import {useStore} from "vuex"

const store = useStore()

const state = reactive({
  show_login: false,
})


// 请求头部导航列表
nav.get_header_nav().then(response => {
  nav.header_nav_list = response.data.data
  console.log(response.data.data)
})

// 用户登录成功以后的处理
const login_success = (token) => {
  state.show_login = false
}
</script>
```

因为vuex默认是保存数据在内存中的，所以基于浏览器开发的网页，如果在F5刷新网页时会存在数据丢失的情况。所以我们可以把store数据永久存储到localStorage中。这里就需要使用插件vuex-persistedstate来实现。

在前端项目的根目录下执行安装命令

```bash
yarn add vuex-persistedstate
```

在vuex的store/index.js文件中导入此插件。

```javascript
import {createStore} from "vuex"
import createPersistedState from "vuex-persistedstate"

// 实例化一个vuex存储库
export default createStore({
    // 调用永久存储vuex数据的插件，localstorage里会多一个名叫vuex的Key，里面就是vuex的数据
    plugins: [createPersistedState()],
    state(){  // 相当于组件中的data，用于保存全局状态数据
        return {
            user: {}
        }
    },
    getters: {
        getUserInfo(state){
            // 从jwt的载荷中提取用户信息
            let now = parseInt( (new Date() - 0) / 1000 );
            if(state.user.exp === undefined) {
                // 没登录
                state.user = {}
                localStorage.token = null;
                sessionStorage.token = null;
                return null
            }

            if(parseInt(state.user.exp) < now) {
                // 过期处理
                state.user = {}
                localStorage.token = null;
                sessionStorage.token = null;
                return null
            }
            return state.user;
        }
    },
    mutations: { // 相当于组件中的methods，用于操作state全局数据
        login(state, payload){
            state.user = payload; // state.user 就是上面声明的user
        }
    }
})
```

完成了登录功能以后，我们要防止用户翻墙访问需要认证身份的页面时，可以基于vue-router的导航守卫来完成。

src/router/index.js，代码：

```javascript
import {createRouter, createWebHistory} from 'vue-router'
import store from "../store";
// 路由列表
const routes = [
    {
        meta: {
            title: "飞升在线教育-站点首页",
            keepAlive: true
        },
        path: '/',
        name: "Home",
        component: () => import("../views/Home.vue")
    }, {
        meta: {
            title: "飞升在线教育-用户登录",
            keepAlive: true
        },
        path: '/login',
        name: "Login",
        component: () => import("../views/Login.vue")
    }, {
        meta: {
            title: "飞升在线教育-个人中心",
            keepAlive: true,
        },
        path: '/user',
        name: "User",
        component: () => import("../views/User.vue"),
    },
]
// 路由对象实例化
const router = createRouter({
    // history, 指定路由的模式
    history: createWebHistory(),
    // 路由列表
    routes,
});


// 导航守卫
router.beforeEach((to, from, next) => {
    document.title = to.meta.title
    // 登录状态验证
    if (to.meta.authorization && !store.getters.getUserInfo) {
        next({"name": "Login"})
    } else {
        next()
    }
})


// 暴露路由对象
export default router

```

src/views/User.vue，代码：

```vue
<template>
  <div>用户中心</div>
</template>

<script>
export default {
  name: "User"
}
</script>

<style scoped>

</style>
```

提交版本

```bash
feature:客户端基于vuex存储本地全局数据并判断登陆状态；
```





## 退出登录功能

在vuex的store/index.js中编写一个登录注销的方法logout，代码：

```javascript
import {createStore} from "vuex"
import createPersistedState from "vuex-persistedstate"
// 实例化一个vuex存储库
export default createStore({
    // 调用永久存储vuex数据的插件，localstorage里会多一个名叫vuex的Key，里面就是vuex的数据
    plugins: [createPersistedState()],
    state() {  // 相当于组件中的data，用于保存全局状态数据
        return {
            user: {}
        }
    },
    getters: {
        getUserInfo(state) {
            // 从jwt的载荷中提取用户信息
            let now = parseInt((new Date() - 0) / 1000);
            if (state.user.exp === undefined) {
                // 没登录
                state.user = {}
                localStorage.token = null;
                sessionStorage.token = null;
                return null
            }

            if (parseInt(state.user.exp) < now) {
                // 过期处理
                state.user = {}
                localStorage.token = null;
                sessionStorage.token = null;
                return null
            }
            return state.user;
        }
    },
    mutations: { // 相当于组件中的methods，用于操作state全局数据
        login(state, payload) {
            state.user = payload; // state.user 就是上面声明的user
        },
        logout(state) { // 退出登录
            state.user = {}
            localStorage.token = null;
            sessionStorage.token = null;
        }
    }
})
```

在用户点击头部登录栏的注销登录时绑定登录注销操作。`components/Header.vue`，代码：

```vue
<el-dropdown-item :icon="Position" @click="logout">注销登录</el-dropdown-item>
```

```vue
<script setup>
import nav from "../api/nav";
import Login from "./Login.vue";
import {reactive} from "vue";
import {UserFilled, List, Setting, Position} from '@element-plus/icons-vue'

import {useStore} from "vuex"

const store = useStore()

const state = reactive({
  show_login: false,
})


// 请求头部导航列表
nav.get_header_nav().then(response => {
  nav.header_nav_list = response.data.data
})

// 用户登录成功以后的处理
const login_success = (token) => {
  state.show_login = false
}

// 登录注销的处理
const logout = () => {
  store.commit("logout");
}

</script>
```

提交版本

```bash
feature:客户端注销登录状态；
```



## 在登录认证中接入防水墙验证码（**跳过**）

```bash
验证码:
1. 图形验证码 ---> 一张图片，图片是服务端基于pillow模块生成的，里面的内容就是验证码信息，会生成验证码增加一些雪花，干扰线，采用特殊字体写入图片，内容同时会保存一份到redis中。

2. 滑块验证码 ---> 通过js互动的方式，让用户旋转、拖动图片到达一定的随机的位置。

3. 短信验证码 ---> 通过绑定手机的方式，发送随机验证码到用户手机中，确认用户是真人。
   邮件验证码
   微信验证码[消息模板, 关注公众号]
   谷歌验证码[Authenticator，二段验证]
```

使用腾讯提供的防水墙验证码

官网： https://007.qq.com/

登录腾讯云：https://cloud.tencent.com/login

点击立即选购，使用微信扫码登录以后，选择右上角"控制台"。

云产品中，搜索 验证码即可。

创建验证的应用。

在验证应用的基本配置中记录下我们接下来需要使用的2个重要配置信息.

```python
应用ID   CaptchaAppId    
应用秘钥  AppSecretKey 
```

因为后面要python对接腾讯云服务器，所以通过访问管理，API秘钥管理提取当前腾讯云账号的SecretId和SecretKey。

```bash
SecretId: *
SecretKey: *
```

接下来在应用中心点击右边的系统代码集成，把验证码集成到项目中就可以。

web前端接入文件地址：https://cloud.tencent.com/document/product/1110/36841

python接入文档地址：https://cloud.tencent.com/document/sdk/Python

### 前端获取显示并校验验证码

```javascript
// 需要下载官方提供的核心js文件并在项目导入使用。
https://ssl.captcha.qq.com/TCaptcha.js
```

![image-20230318163116362](https://img2023.cnblogs.com/blog/2570053/202303/2570053-20230318163117545-1964273727.png)

components/Login.vue，代码：

```vue
    <button class="login_btn" @click="show_captcha">登录</button>
```

```vue
<script setup>
import user from "../api/user";
import { ElMessage } from 'element-plus'
import "../utils/TCaptcha"
const emit = defineEmits(["successhandle",])

import {useStore} from "vuex"
const store = useStore()

// 显示验证码
const show_captcha = ()=>{
  var captcha1 = new TencentCaptcha('2059674751', (res)=>{
      // 接收验证结果的回调函数
      /* res（验证成功） = {ret: 0, ticket: "String", randstr: "String"}
         res（客户端出现异常错误 仍返回可用票据） = {ret: 0, ticket: "String", randstr: "String", errorCode: Number, errorMessage: "String"}
         res（用户主动关闭验证码）= {ret: 2}
      */
      console.log(res);
      // 调用登录处理
      loginhandler(res);
  });
  captcha1.show(); // 显示验证码
}

// 登录处理
const loginhandler = (res)=>{
  // 验证数据
  if(user.account.length<1 || user.password.length<1){
    // 错误提示
    console.log("错了哦，用户名或密码不能为空！");
    ElMessage.error("错了哦，用户名或密码不能为空！");
    return ;
  }

  // 登录请求处理
  user.login({
    ticket: res.ticket,
    randstr: res.randstr,
  }).then(response=>{
    // 先删除之前存留的状态
    localStorage.removeItem("token");
    sessionStorage.removeItem("token");
    // 根据用户选择是否记住登录密码，保存token到不同的本地存储中
    if(user.remember){
      // 记录登录状态
      localStorage.token = response.data.token
    }else{
      // 不记录登录状态
      sessionStorage.token = response.data.token
    }
    ElMessage.success("登录成功！");
    // 登录后续处理，通知父组件，当前用户已经登录成功
    user.account = ""
    user.password = ""
    user.mobile = ""
    user.code = ""
    user.remember = false

    // vuex存储用户登录信息，保存token，并根据用户的选择，是否记住密码
    let payload = response.data.token.split(".")[1]  // 载荷
    let payload_data = JSON.parse(atob(payload)) // 用户信息
    console.log("payload_data=", payload_data)
    store.commit("login", payload_data)

    emit("successhandle")
  }).catch(error=>{
    ElMessage.error("登录失败！");
  })
}

</script>
```

src/api/user.js，代码：

```javascript
import http from "../utils/http"
import {reactive, ref} from "vue"

const user = reactive({
    login_type: 0, // 登录方式，0，密码登录，1，短信登录
    account: "",  // 登录账号/手机号/邮箱
    password: "", // 登录密码
    remember: false, // 是否记住登录状态
    mobile: "",      // 登录手机号码
    code: "",        // 短信验证码
    login(res){
        // 用户登录
        return http.post("/users/login/", {
            "ticket": res.ticket,
            "randstr": res.randstr,
            "username": this.account,
            "password": this.password,
        })
    }
})

export default user;
```

提交版本

```bash
客户端集成腾讯云验证码
```



### 服务端登录功能中校验验证码结果

python接入文档地址：https://cloud.tencent.com/document/sdk/Python

安装腾讯云PythonSKD扩展模块到项目中

```bash
pip install --upgrade tencentcloud-sdk-python
```

生成代码的API操作界面：https://console.cloud.tencent.com/api/explorer?Product=captcha&Version=2019-07-22&Action=DescribeCaptchaResult&SignVersion=

utils/tencentcloudapi.py，封装一个操作腾讯云SDK的API工具类，代码：

```python
import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.captcha.v20190722 import captcha_client, models
from django.conf import settings


class TencentCloudAPI(object):
    """腾讯云API操作工具类"""

    def __init__(self):
        self.cred = credential.Credential(settings.TENCENTCLOUD["SecretId"], settings.TENCENTCLOUD["SecretKey"])

    def captcha(self, ticket, randstr, user_ip):
        """
        验证码校验工具方法
        :ticket  客户端验证码操作成功以后得到的临时验证票据
        :randstr 客户端验证码操作成功以后得到的随机字符串
        :user_ip 客户端的IP地址
        """
        try:
            Captcha = settings.TENCENTCLOUD["Captcha"]

            # 实例化http请求工具类
            httpProfile = HttpProfile()
            # 设置API所在服务器域名
            httpProfile.endpoint = Captcha["endpoint"]
            # 实例化客户端工具类
            clientProfile = ClientProfile()
            # 给客户端绑定请求的服务端域名
            clientProfile.httpProfile = httpProfile
            # 实例化验证码服务端请求工具的客户端对象
            client = captcha_client.CaptchaClient(self.cred, "", clientProfile)
            # 客户端请求对象参数的初始化
            req = models.DescribeCaptchaResultRequest()

            params = {
                # 验证码类型固定为9
                "CaptchaType": Captcha["CaptchaType"],
                # 客户端提交的临时票据
                "Ticket": ticket,
                # 客户端ip地址
                "UserIp": user_ip,
                # 随机字符串
                "Randstr": randstr,
                # 验证码应用ID
                "CaptchaAppId": Captcha["CaptchaAppId"],
                # 验证码应用key
                "AppSecretKey": Captcha["AppSecretKey"],
            }
            # 发送请求
            req.from_json_string(json.dumps(params))
            # 获取腾讯云的响应结果
            resp = client.DescribeCaptchaResult(req)
            # 把响应结果转换成json格式数据
            result = json.loads( resp.to_json_string() )
            return result and result.get("CaptchaCode") == 1

        except Exception as err:
            raise TencentCloudSDKException
```

settings/dev.py，保存腾讯云验证码的配置信息，保存代码：

```python
# 腾讯云API接口配置
TENCENTCLOUD = {
    # 腾讯云访问秘钥ID
    "SecretId": "AKIDSggmeI7z2qSUHoaf18zb4JKdZv61PEZf",
    # 腾讯云访问秘钥key
    "SecretKey": "06xbzB7VabOyY3asztbkdIfqlovtLYXG",
    # 验证码API配置
    "Captcha": {
        "endpoint": "captcha.tencentcloudapi.com", # 验证码校验服务端域名
        "CaptchaType": 9,  # 验证码类型，固定为9
        "CaptchaAppId": 2059674751,  # 验证码应用ID
        "AppSecretKey": "04LwtDUlnQxumWnItAw4OPA**", # 验证码应用key
    },
}
```

users/views.py，重写登陆视图，先校验验证码，接着再调用jwt原来提供的视图来校验用户账号信息，代码：

```python
from rest_framework_jwt.views import ObtainJSONWebToken
from luffycityapi.utils.tencentcloudapi import TencentCloudAPI,TencentCloudSDKException
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class LoginAPIView(ObtainJSONWebToken):
    """用户登录视图"""
    def post(self, request, *args, **kwargs):
        # 校验用户操作验证码成功以后的ticket临时票据
        try:
            api = TencentCloudAPI()
            result = api.captcha(
                request.data.get("ticket"),
                request.data.get("randstr"),
                request._request.META.get("REMOTE_ADDR"),
            )
            if result:
                # 验证通过
                print("验证通过")
                # 登录实现代码，调用父类实现的登录视图方法
                return super().post(request, *args, **kwargs)
            else:
                # 如果返回值不是True，则表示验证失败
                raise TencentCloudSDKException
        except TencentCloudSDKException as err:
            return Response({"errmsg": "验证码校验失败！"}, status=status.HTTP_400_BAD_REQUEST)
```

users/urls.py，代码：

```python
from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.LoginAPIView.as_view(), name="login"),
]
```

提交版本

```bash
服务端重写登录视图实现验证码的操作结果验证
```



# 用户的注册认证

前端显示注册页面并调整首页头部和登陆页面的注册按钮的链接。

创建一个注册页面views/Register.vue，主要是通过登录窗口组件进行改成而成，组件代码：

```vue
<template>
  <div class="login box">
    <img src="../assets/Loginbg.3377d0c.jpg" alt="">
    <div class="login">
      <div class="login-title">
        <img src="../assets/logo.png" alt="">
        <p>帮助有志向的年轻人通过努力学习获得体面的工作和生活!</p>
      </div>
      <div class="login_box">
        <div class="title">
          <span class="active">用户注册</span>
        </div>
        <div class="inp">
          <input v-model="state.mobile" type="text" placeholder="手机号码" class="user">
          <input v-model="state.password" type="password" placeholder="登录密码" class="user">
          <input v-model="state.re_password" type="password" placeholder="确认密码" class="user">
          <input v-model="state.code" type="text" class="code" placeholder="短信验证码">
          <el-button id="get_code" type="primary">获取验证码</el-button>
          <button class="login_btn">注册</button>
          <p class="go_login">已有账号
            <router-link to="/login">立即登录</router-link>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import {reactive, defineEmits} from "vue"
import {ElMessage} from 'element-plus'
import {useStore} from "vuex"
import "../utils/TCaptcha"

const store = useStore()

const state = reactive({
  password: "",    // 密码
  re_password: "",// 确认密码
  mobile: "",     // 手机号
  code: "",       // 验证码
})
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
```

客户端注册路由，src/router/index.js，代码：

```javascript
import {createRouter, createWebHistory} from 'vue-router'
import store from "../store";
// 路由列表
const routes = [
    {
        meta: {
            title: "飞升在线教育-站点首页",
            keepAlive: true
        },
        path: '/',
        name: "Home",
        component: () => import("../views/Home.vue")
    }, {
        meta: {
            title: "飞升在线教育-用户登录",
            keepAlive: true
        },
        path: '/login',
        name: "Login",
        component: () => import("../views/Login.vue")
    }, {
        meta: {
            title: "飞升在线教育-用户注册",
            keepAlive: true
        },
        path: '/register',
        name: "Register",            // 路由名称
        component: () => import("../views/Register.vue"),         // uri绑定的组件页面
    }, {
        meta: {
            title: "飞升在线教育-个人中心",
            keepAlive: true,
        },
        path: '/user',
        name: "User",
        component: () => import("../views/User.vue"),
    },
]
// 路由对象实例化
const router = createRouter({
    // history, 指定路由的模式
    history: createWebHistory(),
    // 路由列表
    routes,
});


// 导航守卫
router.beforeEach((to, from, next) => {
    document.title = to.meta.title
    // 登录状态验证
    if (to.meta.authorization && !store.getters.getUserInfo) {
        next({"name": "Login"})
    } else {
        next()
    }
})


// 暴露路由对象
export default router
```

修改首页头部的连接和登录窗口中登录和注册的链接。代码：

```html
# components/Header.vue
<router-link to="/register">注册</router-link>
#components/Login.vue
<p class="go_login" >没有账号 <router-link to="/register">立即注册</router-link></p>
```

提交git

~~~python
feature:客户端实现注册页面；
~~~



## 注册功能的实现流程

![image-20230318103916633](https://img2023.cnblogs.com/blog/2570053/202303/2570053-20230318103918322-1387412724.png)

综合上图所示，我们需要在服务端完成3个接口：

```python
1. 验证手机号是否注册了
2. 发送验证码
3. 校验验证码，并保存用户提交的注册信息
```

所以，除了短信发送功能以外，其他2个接口功能，我们完全不需要依赖第三方，直接可以先实现了。



### 服务端提供验证手机号的api接口

user/views，视图代码：

```python
import re

from rest_framework.views import APIView

from response import APIResponse
from return_code import SUCCESS, AUTH_FAILED
from . import models


class MobileAPIView(APIView):
    def get(self, request, mobile, *args, **kwargs):
        """
        校验手机号是否已注册
        :param request:
        :param mobile: 手机号
        :return:
        """
        # 验证手机号格式
        if not re.match(r'^1(3\d|4[5-9]|5[0-35-9]|6[567]|7[0-8]|8\d|9[0-35-9])\d{8}$', mobile):
            return APIResponse(AUTH_FAILED, "手机号格式错误.")
        # 查看验证码是否注册
        if models.UserInfo.objects.filter(mobile=mobile).exists():
            return APIResponse(AUTH_FAILED, "手机号已注册.")
        else:
            return APIResponse(SUCCESS, "注册成功.")

```

路由：

```python
path('mobile/<str:mobile>/', views.MobileAPIView.as_view(), name='mobile'),
```



### 客户端发送ajax请求验证手机号是否已注册

src/api/user.js，代码：

```javascript
import http from "../utils/http"
import {reactive, ref} from "vue"

const user = reactive({
    login_type: 0, // 登录方式，0，密码登录，1，短信登录
    account: "",  // 登录账号/手机号/邮箱
    password: "", // 登录密码
    re_password: "", // 登录密码
    remember: false, // 是否记住登录状态
    mobile: "",      // 登录手机号码
    code: "",        // 短信验证码
    login() {
        // 用户登录
        return http.post("/user/login/", {
            "username": this.account,
            "password": this.password,
        })
    },
    check_mobile() {
        // 验证手机号
        return http.get(`/user/mobile/${this.mobile}/`)
    }
})

export default user;
```



views/Register.vue，代码：

```vue
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
          <button class="login_btn">注册</button>
          <p class="go_login">已有账号
            <router-link to="/login">立即登录</router-link>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>
```

```vue
<script setup>
import {reactive, defineEmits, watch} from "vue"
import {ElMessage} from 'element-plus'
import {useStore} from "vuex"
import user from "../api/user";

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

</script>
```

提交版本

```bash
cd /home/moluo/Desktop/luffycity
git add .
git commit -m "注册功能实现流程-验证手机号是否已经注册!"
git push
```





## 注册功能的基本实现

### 服务端实现用户注册的api接口

序列化器，`user/serializers`，代码：

```python
import re

from django.conf import settings

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from . import models

from authenticate import generate_jwt_token


class UserRegisterModelSerializer(serializers.ModelSerializer):
    """
    注册功能
    """
    re_password = serializers.CharField(required=True, write_only=True)
    sms_code = serializers.CharField(min_length=4, max_length=6, required=True, write_only=True)
    token = serializers.CharField(read_only=True)

    class Meta:
        model = models.UserInfo
        fields = ("mobile", "password", "re_password", "sms_code", "token")
        extra_kwargs = {
            "mobile": {
                "required": True, "write_only": True
            },
            "password": {
                "required": True, "write_only": True, "min_length": 8, "max_length": 18,
            },
        }

    def validate(self, attrs):
        # 验证手机号格式
        mobile = attrs.get("mobile")
        if not re.match(r'^1(3\d|4[5-9]|5[0-35-9]|6[567]|7[0-8]|8\d|9[0-35-9])\d{8}$', mobile):
            raise ValidationError("手机号格式错误.")

        # 验证码两次密码是否一致
        password = attrs.get("password")
        re_password = attrs.get("re_password")
        if password != re_password:
            raise ValidationError("两次密码不一致.")

        # 查看验证码是否注册
        if models.UserInfo.objects.filter(mobile=mobile).exists():
            raise ValidationError("手机号已注册.")

        # todo 短信验证码

        return attrs

    def create(self, validated_data):
        mobile = validated_data.get("mobile")
        password = validated_data.get("password")
        user = models.UserInfo.objects.create_user(
            username=mobile,
            mobile=mobile,
            password=password,
            avatar=settings.DEFAULT_USER_AVATAR,
        )
        user.token = generate_jwt_token(user)
        return user

```

默认头像配置，`settings.constants`，代码：

```python
# 用户默认头像
DEFAULT_USER_AVATAR = "avatar/2023/avatar.jpg"
```

视图，`users.views`，代码，

```python
import re

from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from . import models
from .serializers import UserRegisterModelSerializer

from response import APIResponse
from return_code import SUCCESS, AUTH_FAILED
from mixins import ReCreateModelMixin

class UserRegisterGenericAPIView(GenericViewSet, ReCreateModelMixin):
    queryset = models.UserInfo.objects.filter(is_deleted=False)
    serializer_class = UserRegisterModelSerializer
```

路由，`users/urls`，代码：

```python
from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_jwt.views import obtain_jwt_token

from . import views

router = SimpleRouter()
router.register('register', views.UserRegisterGenericAPIView)

urlpatterns = [
    path("login/", obtain_jwt_token, name="login"),
    path('mobile/<str:mobile>/', views.MobileAPIView.as_view(), name='mobile'),
]

urlpatterns += router.urls
```

`extension/authticate.py`

~~~python
def generate_jwt_token(user):
    """
    生成jwt token
    @params user: 用户模型实例对象
    """
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    payload = jwt_payload_handler(user)
    return jwt_encode_handler(payload)

~~~

提交git

~~~python
feature:服务端实现注册功能（没有短信验证码）;
~~~



### 客户端提交用户注册信息

`views/Register.vue`，代码：

```vue
<button class="login_btn" @click="registerhandler">注册</button>
```

```vue
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
```

src/api/user.js，代码：

```javascript
import http from "../utils/http"
import {reactive, ref} from "vue"

const user = reactive({
    login_type: 0, // 登录方式，0，密码登录，1，短信登录
    account: "",  // 登录账号/手机号/邮箱
    password: "", // 登录密码
    re_password: "", // 登录密码
    remember: false, // 是否记住登录状态
    mobile: "",      // 登录手机号码
    code: "",        // 短信验证码
    login() {
        // 用户登录
        return http.post("/user/login/", {
            "username": this.account,
            "password": this.password,
        })
    },
    check_mobile() {
        // 验证手机号
        return http.get(`/user/mobile/${this.mobile}/`)
    },
    register(data) {
        data.mobile = this.mobile
        data.re_password = this.re_password
        data.password = this.password
        data.sms_code = this.code
        // 用户注册请求
        return http.post("/user/register/", data)
    }
})

export default user;
```

新增src/settings.js，代码：

```javascript
export default {
    // api服务端所在地址
    host: "http://127.0.0.1:8000", // 服务器地址
}
```

components/Login.vue，登录组件中，把app_id改成settings提供的变量，代码：

```vue
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
```

提交版本

```bash
feature:注册功能实现流程-客户端保存用户注册信息.；
未实现手机号短信登录
```



## 注册功能添加短信验证码

接下来，我们把注册过程中一些注册信息（例如：短信验证码）缓存到redis数据库中。

在django集成redis缓存功能的文档：https://django-redis-chs.readthedocs.io/zh_CN/latest/#

确认settings.dev.py配置中添加了存储短信验证码的配置项，代码：（前面配置过的，就不用配置了）

```python

# 设置redis缓存
CACHES = {
    # 默认缓存
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        # "LOCATION": "redis://:密码@IP地址:端口/库编号",
        "LOCATION": "redis://:%s@%s:%s/0" % (REDIS_PASSWORD, REDIS_HOST, REDIS_PORT),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {"max_connections": 100},
        }
    },
    # 提供给admin运营站点的session存储
    "session": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://:%s@%s:%s/1" % (REDIS_PASSWORD, REDIS_HOST, REDIS_PORT),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {"max_connections": 100},
        }
    },
    # 提供存储短信验证码
    "sms_code": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://:%s@%s:%s/2" % (REDIS_PASSWORD, REDIS_HOST, REDIS_PORT),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {"max_connections": 100},
        }
    }
}

# 设置用户登录admin站点时,记录登录状态的session保存到redis缓存中
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# 设置session保存的位置对应的缓存配置项
SESSION_CACHE_ALIAS = "session"

```



### 使用云通讯发送短信

官网：https://www.yuntongxun.com/

在登录后的平台控制台下获取以下信息：

```
ACCOUNT SID：2c94811c86c00e9b0186f2873a040afa
AUTH TOKEN : *
AppID(默认)：2c94811c86c00e9b0186f2873b0d0b01
Rest URL(生产)： https://app.cloopen.com:8883
```

![image-20230318102532592](https://img2023.cnblogs.com/blog/2570053/202303/2570053-20230318102728377-102093213.png)

查看发送短信的sdk api接口文档。

http://doc.yuntongxun.com/pe/5f029ae7a80948a1006e776e

#### 后端生成短信验证码

安装云通讯的短信SDK扩展模块，终端执行命令：

```bash
pip install ronglian_sms_sdk
```

封装容联云的短信发送功能，`libs/sms/ronglianyunapi`，代码：

```python
import json
from django.conf import settings

from ronglian_sms_sdk import SmsSDK


def send_sms(tid, mobile, datas):
    """
    发送短信
    @params tid: 模板ID，默认测试使用1
    @params mobile: 接收短信的手机号，多个手机号使用都逗号隔开
            单个号码： mobile="13312345678"
            多个号码： mobile="13312345678,13312345679,...."
    @params datas: 短信模板的参数列表
            例如短信模板为： 【云通讯】您的验证码是{1}，请于{2}分钟内正确输入。
            则datas=("123456",5,)
    """
    ronglianyun = settings.RONGLIANYUN
    sdk = SmsSDK(ronglianyun.get("accId"), ronglianyun.get("accToken"), ronglianyun.get("appId"))
    resp = sdk.sendMessage(tid, mobile, datas)
    response = json.loads(resp)
    print(f"response={response}")
    return response.get("statusCode") == "000000"

```

把容联云的配置信息，填写到配置文件中，`settings.dev`，代码：

```python
# 容联云短信
RONGLIANYUN = {
    "accId": '2c94811c86c00e9b0186f2873a040afa',
    "accToken": os.getenv("RONGLIANYUNACCTOKEN"),
    "appId": '2c94811c86c00e9b0186f2873b0d0b01',
    "reg_tid": 1,  # 注册短信验证码的模板ID
    "sms_expire": 300,  # 短信有效期，单位：秒(s)
    "sms_interval": 60,  # 短信发送的冷却时间，单位：秒(s)
}
```

视图，`user/views.py`，代码：

```python
import re
import random

from django.conf import settings
from django_redis import get_redis_connection

from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from . import models
from .serializers import UserRegisterModelSerializer

from response import APIResponse
from return_code import SUCCESS, AUTH_FAILED, TOO_MANY_REQUESTS, SERVER_ERROR
from mixins import ReCreateModelMixin
from sms.ronglianyunapi import send_sms


class MobileAPIView(APIView):
    def get(self, request, mobile, *args, **kwargs):
        """
        校验手机号是否已注册
        :param request:
        :param mobile: 手机号
        :return:
        """
        # 验证手机号格式
        if not re.match(r'^1(3\d|4[5-9]|5[0-35-9]|6[567]|7[0-8]|8\d|9[0-35-9])\d{8}$', mobile):
            return APIResponse(AUTH_FAILED, "手机号格式错误.")
        # 查看验证码是否注册
        if models.UserInfo.objects.filter(mobile=mobile).exists():
            return APIResponse(AUTH_FAILED, "手机号已注册.")
        else:
            return APIResponse(SUCCESS, "手机号尚未注册,请安全注册.")


class UserRegisterGenericAPIView(GenericViewSet, ReCreateModelMixin):
    queryset = models.UserInfo.objects.filter(is_deleted=False)
    serializer_class = UserRegisterModelSerializer


class SMSAPIView(APIView):
    """
    SMS短信接口视图
    """

    def get(self, request, mobile):
        """发送短信验证码"""

        # 验证手机号格式
        if not re.match(r'^1(3\d|4[5-9]|5[0-35-9]|6[567]|7[0-8]|8\d|9[0-35-9])\d{8}$', mobile):
            return APIResponse(AUTH_FAILED, "手机号格式错误.")

        redis = get_redis_connection("sms_code")
        # 判断手机短信是否处于发送冷却中[60秒只能发送一条]
        interval = redis.ttl(f"interval_{mobile}")  # 通过ttl方法可以获取保存在redis中的变量的剩余有效期
        if interval != -2:
            return APIResponse(TOO_MANY_REQUESTS, f"短信发送过于频繁，请{interval}秒后再次点击获取!")

        # 基于随机数生成短信验证码
        code = f"{random.randint(0, 999999):06d}"
        # 获取短信有效期的时间
        time = settings.RONGLIANYUN.get("sms_expire")
        # 短信发送间隔时间
        sms_interval = settings.RONGLIANYUN["sms_interval"]
        # 调用第三方sdk发送短信
        is_ok = send_sms(settings.RONGLIANYUN.get("reg_tid"), mobile, datas=(code, time // 60))
        # 判断验证码是否接入成功
        if not is_ok:
            return APIResponse(SERVER_ERROR, "验证码接入错误.")

        # 记录code到redis中，并以time作为有效期
        # 使用redis提供的管道对象pipeline来优化redis的写入操作[添加/修改/删除]
        pipe = redis.pipeline()
        pipe.multi()  # 开启事务
        pipe.setex(f"sms_{mobile}", time, code)
        pipe.setex(f"interval_{mobile}", sms_interval, "_")
        pipe.execute()  # 提交事务，同时把暂存在pipeline的数据一次性提交给redis

        return APIResponse(message="验证码发送成功.")

```

路由，`user/urls.py`，代码：

```python
path('sms/<str:mobile>/', views.SMSAPIView.as_view(), name='sms'),
```

提交版本

```bash
feature:注册功能实现流程-服务端提供短信发送API接口!;
```



### 客户端请求发送短信

views/Register.vue，注册页面绑定点击发送短信的方法，代码：

```vue
<el-button id="get_code" type="primary" @click="send_sms">{{user.sms_btn_text}}</el-button>
```

```vue

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


// 发送短信
const send_sms = () => {
  if (!/1[3-9]\d{9}/.test(user.mobile)) {
    ElMessage.error("手机号格式有误！")
    return false
  }

  // 判断是否处于短信发送的冷却状态
  if (user.is_send) {
    ElMessage.error("短信发送过于频繁！")
    return false
  }

  let time = user.sms_interval;
  // 发送短信请求
  user.get_sms_code().then(response => {
    ElMessage.success("短信发送中，请留意您的手机！");
    // 发送短信后进入冷却状态
    user.is_send = true;
    // 冷却倒计时
    clearInterval(user.interval);
    user.interval = setInterval(() => {
      if (time < 1) {
        // 退出短信发送的冷却状态
        user.is_send = false
        user.sms_btn_text = "点击获取验证码"
      } else {
        time -= 1;
        user.sms_btn_text = `${time}秒后重新获取`;
      }
    }, 1000)
  }).catch(error => {
    ElMessage.error(error?.response?.data?.message);
    time = error?.response?.data?.interval;
    // 冷却倒计时
    clearInterval(user.interval);
    user.interval = setInterval(() => {
      if (time < 1) {
        // 退出短信发送的冷却状态
        user.is_send = false
        user.sms_btn_text = "点击获取验证码"
      } else {
        time -= 1;
        user.sms_btn_text = `${time}秒后重新获取`;
      }
    }, 1000)

  })
}


</script>
```

src/api/user.js，代码：

```javascript
import http from "../utils/http"
import {reactive, ref} from "vue"

const user = reactive({
    login_type: 0, // 登录方式，0，密码登录，1，短信登录
    account: "",  // 登录账号/手机号/邮箱
    password: "", // 登录密码
    re_password: "", // 登录密码
    remember: false, // 是否记住登录状态
    mobile: "",      // 登录手机号码
    code: "",        // 短信验证码
    sms_btn_text: "点击获取验证码",  // 短信按钮提示信息
    is_send: false,  // 短信发送的标记
    sms_interval: 60,// 间隔时间
    interval: null,  // 定时器的标记
    login() {
        // 用户登录
        return http.post("/user/login/", {
            "username": this.account,
            "password": this.password,
        })
    },
    check_mobile() {
        // 验证手机号
        return http.get(`/user/mobile/${this.mobile}/`)
    },
    register(data) {
        data.mobile = this.mobile
        data.re_password = this.re_password
        data.password = this.password
        data.sms_code = this.code
        // 用户注册请求
        return http.post("/user/register/", data)
    },
    get_sms_code() {
        return http.get(`/user/sms/${this.mobile}/`)
    }
})

export default user;
```

样式更改：`components/Login.vue,views/Register.vue`

~~~css
.inp .code {
  width: 190px;
  margin-right: 16px;
}
~~~

提交版本

```bash
feature:注册功能实现流程-客户端请求发送短信并实现短信倒计时冷却提示；
```



### 服务端校验客户端提交的验证码

`user/serializers.py`，代码：

```python
import re

from django.conf import settings
from django_redis import get_redis_connection

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from . import models

from authenticate import generate_jwt_token


class UserRegisterModelSerializer(serializers.ModelSerializer):
    """
    注册功能
    """
    re_password = serializers.CharField(required=True, write_only=True)
    sms_code = serializers.CharField(min_length=4, max_length=6, required=True, write_only=True)
    token = serializers.CharField(read_only=True)

    class Meta:
        model = models.UserInfo
        fields = ("mobile", "password", "re_password", "sms_code", "token")
        extra_kwargs = {
            "mobile": {
                "required": True, "write_only": True
            },
            "password": {
                "required": True, "write_only": True, "min_length": 8, "max_length": 18,
            },
        }

    def validate(self, attrs):
        # 验证手机号格式
        mobile = attrs.get("mobile")
        if not re.match(r'^1(3\d|4[5-9]|5[0-35-9]|6[567]|7[0-8]|8\d|9[0-35-9])\d{8}$', mobile):
            raise ValidationError("手机号格式错误.")

        # 验证码两次密码是否一致
        password = attrs.get("password")
        re_password = attrs.get("re_password")
        if password != re_password:
            raise ValidationError("两次密码不一致.")

        # 查看验证码是否注册
        if models.UserInfo.objects.filter(mobile=mobile).exists():
            raise ValidationError("手机号已注册.")

        # 从redis中提取短信
        redis = get_redis_connection("sms_code")
        code = redis.get(f"sms_{mobile}")
        if code is None:
            # 获取不到验证码，则表示验证码已经过期了或未发送验证码
            raise ValidationError(detail="验证码不存在或已过期.", code="sms_code")
        # 从redis提取的数据，字符串都是bytes类型，所以decode
        if code.decode() != attrs.get("sms_code"):
            raise ValidationError(detail="短信验证码错误.", code="sms_code")
        # 删除掉redis中的短信和短信失效时间
        redis.delete(f"sms_{mobile}")
        redis.delete(f"interval_{mobile}")

        return attrs

    def create(self, validated_data):
        mobile = validated_data.get("mobile")
        password = validated_data.get("password")
        user = models.UserInfo.objects.create_user(
            username=mobile,
            mobile=mobile,
            password=password,
            avatar=settings.DEFAULT_USER_AVATAR,
        )
        user.token = generate_jwt_token(user)
        return user

```

`Register.vue`

~~~vue
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

    let return_code = response.data.code;
    if (return_code !== 200) {
      ElMessage.error("注册失败.");
      return false;
    }

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


// 发送短信
const send_sms = () => {
  if (!/1[3-9]\d{9}/.test(user.mobile)) {
    ElMessage.error("手机号格式有误！")
    return false
  }

  // 判断是否处于短信发送的冷却状态
  if (user.is_send) {
    ElMessage.error("短信发送过于频繁！")
    return false
  }

  let time = user.sms_interval;
  // 发送短信请求
  user.get_sms_code().then(response => {
    ElMessage.success("短信发送中，请留意您的手机！");
    // 发送短信后进入冷却状态
    user.is_send = true;
    // 冷却倒计时
    clearInterval(user.interval);
    user.interval = setInterval(() => {
      if (time < 1) {
        // 退出短信发送的冷却状态
        user.is_send = false
        user.sms_btn_text = "点击获取验证码"
      } else {
        time -= 1;
        user.sms_btn_text = `${time}秒后重新获取`;
      }
    }, 1000)
  }).catch(error => {
    ElMessage.error(error?.response?.data?.message);
    time = error?.response?.data?.interval;
    // 冷却倒计时
    clearInterval(user.interval);
    user.interval = setInterval(() => {
      if (time < 1) {
        // 退出短信发送的冷却状态
        user.is_send = false
        user.sms_btn_text = "点击获取验证码"
      } else {
        time -= 1;
        user.sms_btn_text = `${time}秒后重新获取`;
      }
    }, 1000)

  })
}
</script>
~~~

提交版本

```bash
feature:注册功能实现流程-服务端校验注册短信验证码；
```



# 手机号短信登录

## 服务端

`urls.py`

~~~python
path('login/sms/', views.UserLoginSMSGenericAPIView.as_view(), name='login_sms'),
~~~

`serializers.py`

~~~python

class UserLoginSMSModelSerializer(serializers.ModelSerializer):
    """
    手机号短信登录
    """
    sms_code = serializers.CharField(min_length=4, max_length=6, required=True, write_only=True)
    token = serializers.CharField(read_only=True)
    mobile = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = models.UserInfo
        fields = ("mobile", "sms_code", "token")

    def validate(self, attrs):
        # 验证手机号格式
        mobile = attrs.get("mobile")
        if not re.match(r'^1(3\d|4[5-9]|5[0-35-9]|6[567]|7[0-8]|8\d|9[0-35-9])\d{8}$', mobile):
            raise ValidationError("手机号格式错误.")

        # 校验验证码
        sms_code = attrs.get("sms_code")
        if not sms_code:
            raise ValidationError("请输入验证码.")

        # 校验手机号是否存在
        user = models.UserInfo.objects.filter(mobile=mobile)
        if not user.exists():
            raise ValidationError("手机号尚未注册.")

        # 从redis中提取短信
        redis = get_redis_connection("sms_code")
        code = redis.get(f"sms_{mobile}")
        if code is None:
            # 获取不到验证码，则表示验证码已经过期了或未发送验证码
            raise ValidationError(detail="验证码不存在或已过期.", code="sms_code")
        # 从redis提取的数据，字符串都是bytes类型，所以decode
        if code.decode() != attrs.get("sms_code"):
            raise ValidationError(detail="短信验证码错误.", code="sms_code")
        # 删除掉redis中的短信和短信失效时间
        redis.delete(f"sms_{mobile}")
        redis.delete(f"interval_{mobile}")

        user = user.first()
        # 返回token
        user.token = generate_jwt_token(user)

        return user
~~~

`views.py`

~~~python
class UserLoginSMSGenericAPIView(APIView):
    """手机号短信验证码登录"""
    authentication_classes = ()
    permission_classes = ()

    def post(self, request, *args, **kwargs):
        serializer = UserLoginSMSModelSerializer(data=request.data)
        if not serializer.is_valid():
            return APIResponse(VALIDATE_ERROR, serializer.errors)
        return APIResponse(data=serializer.data)
~~~

## 客户端

`components/login.vue`

~~~vue

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

const login_mobile_handler = () => {
  // 登录处理
  if (user.mobile.length < 1 || user.code.length < 1) {
    // 错误提示
    ElMessage.error('用户名或密码不能为空.');
    return false // 在函数/方法中，可以阻止代码继续往下执行
  }
  if (!/^1[3-9]\d{9}$/.test(user.mobile)) {
    // 错误提示
    ElMessage.error('手机号格式不正确.');
    return false // 阻止代码继续往下执行
  }
  // 发送请求
  user.login_mobile().then(response => {
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

// 发送短信
const send_sms = () => {
  if (!/1[3-9]\d{9}/.test(user.mobile)) {
    ElMessage.error("手机号格式有误！")
    return false
  }

  // 判断是否处于短信发送的冷却状态
  if (user.is_send) {
    ElMessage.error("短信发送过于频繁！")
    return false
  }

  let time = user.sms_interval;
  // 发送短信请求
  user.get_sms_code().then(response => {
    ElMessage.success("短信发送中，请留意您的手机！");
    // 发送短信后进入冷却状态
    user.is_send = true;
    // 冷却倒计时
    clearInterval(user.interval);
    user.interval = setInterval(() => {
      if (time < 1) {
        // 退出短信发送的冷却状态
        user.is_send = false
        user.sms_btn_text = "点击获取验证码"
      } else {
        time -= 1;
        user.sms_btn_text = `${time}秒后重新获取`;
      }
    }, 1000)
  }).catch(error => {
    ElMessage.error(error?.response?.data?.message);
    time = error?.response?.data?.interval;
    // 冷却倒计时
    clearInterval(user.interval);
    user.interval = setInterval(() => {
      if (time < 1) {
        // 退出短信发送的冷却状态
        user.is_send = false
        user.sms_btn_text = "点击获取验证码"
      } else {
        time -= 1;
        user.sms_btn_text = `${time}秒后重新获取`;
      }
    }, 1000)

  })
}

</script>
~~~

`user.js`

~~~js
import http from "../utils/http"
import {reactive, ref} from "vue"

const user = reactive({
    login_type: 0, // 登录方式，0，密码登录，1，短信登录
    account: "",  // 登录账号/手机号/邮箱
    password: "", // 登录密码
    re_password: "", // 登录密码
    remember: false, // 是否记住登录状态
    mobile: "",      // 登录手机号码
    code: "",        // 短信验证码
    sms_btn_text: "点击获取验证码",  // 短信按钮提示信息
    is_send: false,  // 短信发送的标记
    sms_interval: 60,// 间隔时间
    interval: null,  // 定时器的标记
    login() {
        // 用户登录
        return http.post("/user/login/", {
            "username": this.account,
            "password": this.password,
        })
    },
    check_mobile() {
        // 验证手机号
        return http.get(`/user/mobile/${this.mobile}/`)
    },
    register(data) {
        data.mobile = this.mobile
        data.re_password = this.re_password
        data.password = this.password
        data.sms_code = this.code
        // 用户注册请求
        return http.post("/user/register/", data)
    },
    get_sms_code() {
        return http.get(`/user/sms/${this.mobile}/`)
    },
    login_mobile() {
        // 用户登录
        return http.post("/user/login/sms/", {
            "mobile": this.mobile,
            "sms_code": this.code,
        })
    },
})

export default user;
~~~

