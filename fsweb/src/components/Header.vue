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
            <el-badge type="danger" :value="store.state.cart_total" class="item">
              <span><router-link to="/cart">购物车</router-link></span>
            </el-badge>
          </div>
          <div class="login-box ">
            <router-link to="/user/course">我的课堂</router-link>
            <el-dropdown>
                <span class="el-dropdown-link">
                  <router-link to="/user">
                  <el-avatar class="avatar" size="50" :src="settings.host + store.state.user.avatar"></el-avatar>
                  </router-link>
                </span>
              <template #dropdown>
                <el-dropdown-menu>
                  <el-dropdown-item :icon="UserFilled">
                    <router-link to="/user">个人中心</router-link>
                  </el-dropdown-item>
                  <el-dropdown-item :icon="List" to="/user/order">订单列表</el-dropdown-item>
                  <el-dropdown-item :icon="Setting" to="/user">个人设置</el-dropdown-item>
                  <el-dropdown-item :icon="Position" @click="logout">注销登录</el-dropdown-item>
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
            <router-link to="/register">注册</router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
  <el-dialog :width="600" v-model="state.show_login">
    <Login @login_success="login_success"></Login>
  </el-dialog>
</template>


<script setup>
import nav from "../api/nav";
import Login from "./Login.vue";
import {reactive} from "vue";
import {UserFilled, List, Setting, Position} from '@element-plus/icons-vue'
import settings from "../settings.js";
import {useStore} from "vuex"

const store = useStore()

const state = reactive({
  show_login: false,
})


// 请求头部导航列表
nav.get_header_nav().then(response => {
  nav.header_nav_list = response.data.data.results;
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


<style scoped>

/* 登陆后状态栏 */
.logined-bar {
  margin-top: 0;
  height: 72px;
  line-height: 72px;
}

.header .logined-bar .shop-cart {
  height: 32px;
  line-height: 32px;
}

.logined-bar .login-box {
  height: 72px;
  line-height: 72px;
  position: relative;
}

.logined-bar .el-avatar {
  float: right;
  width: 50px;
  height: 50px;
  position: absolute;
  top: -10px;
  left: 10px;
  transition: transform .5s ease-in .1s;
}

.logined-bar .el-avatar:hover {
  transform: scale(1.3);
}


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
  box-sizing: border-box;
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