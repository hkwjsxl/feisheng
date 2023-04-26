# 订单管理

![image-20210929180934491](https://img2023.cnblogs.com/blog/2570053/202304/2570053-20230410204952378-1890773106.png)

上面的效果，可以使用vue-router的嵌套路由来实现，根据不同的子路径，来指定部分内容改变，不会切换公共部分内容。

## 个人中心

订单列表位于用户中心页面，所以我们接下来先完善头部子组件中的跳转链接。

设置好用户的头像

components/login.vue

~~~vue
const loginhandler = () => {
// ...
	// vuex存储用户登录信息，保存token，并根据用户的选择，是否记住密码
    let payload = response.data.token.split(".")[1]  // 载荷
    let payload_data = JSON.parse(atob(payload)) // 用户信息
    store.commit("login", payload_data)
    store.commit("cart_total", response.data.cart_total)
    // 设置用户头像
    store.state.user.avatar = payload_data.avatar;
// ...
~~~

`src/components/Header.vue`，代码：

```vue
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
    <el-dropdown-item :icon="List">订单列表</el-dropdown-item>
    <el-dropdown-item :icon="Setting">个人设置</el-dropdown-item>
    <el-dropdown-item :icon="Position" @click="logout">注销登录</el-dropdown-item>
        </el-dropdown-menu>
    </template>
</el-dropdown>
```

个人中心主页面，`src/views/User.vue`，代码：

```vue
<template>
  <Header></Header>
  <main class="clearfix">
    <div class="bg-other user-head-info">
      <div class="user-info clearfix">
        <div class="user-pic" data-is-fans="0" data-is-follows="">
            <div class="user-pic-bg"><img class="img" :src="settings.host + store.state.user.avatar" alt=""></div>
        </div>
        <div class="user-info-right">
          <h3 class="user-name clearfix"><span>墨落</span></h3>
          <p class="about-info">
            <span>男</span>
            <span>CG影视动画师</span>
          </p>
        </div>
        <div class="user-sign hide">
          <p class="user-desc">这位同学很懒，木有签名的说～</p>
        </div>
        <div class="study-info clearfix">
          <div class="item follows">
            <div class="u-info-learn" title="学习时长16分" style="cursor:pointer;">
              <em>0.28h</em>
              <span>学习时长 </span>
            </div>
          </div>
          <div class="item follows">
            <router-link to="/u/index/credit"><em>0</em></router-link>
            <span>积分</span>
          </div>
          <div class="item follows">
            <router-link to="/u/index/follows"><em>12</em></router-link>
            <span>关注</span>
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
main{
  margin-bottom: 40px;
}
.bg-other {
	background: url("../assets/user_bg.png") no-repeat center top #000;
	background-size: cover;
}
.user-head-info{
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
	box-shadow: 0 4px 8px 0 rgba(7,17,27,.1);
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
	color: rgba(255,255,255,.8);
	line-height: 28px
}

.user-head-info .study-info .item span {
	display: block;
	text-align: center;
	font-size: 14px;
	color: rgba(255,255,255,.8);
	line-height: 20px;
	margin-top: 4px
}

.user-head-info .study-info .follows {
	margin-right: 24px
}

.user-head-info .study-info .set-btn {
	padding: 8px 16px;
	border: 1px solid rgba(255,255,255,.4);
	border-radius: 18px;
	font-size: 14px;
	color: rgba(255,255,255,.8);
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

.main{
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
```

个人信息页面效果展示

`src/components/user/Info.vue`，代码：

```vue
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
        <div class="pull-left">墨落</div>
       </div>
       <div class="info-box clearfix">
        <label class="pull-left">职位</label>
        <div class="pull-left">CG影视动画师</div>
       </div>
       <div class="info-box clearfix">
        <label class="pull-left">城市</label>
        <div class="pull-left">未设置</div>
       </div>
       <div class="info-box clearfix">
        <label class="pull-left">性别</label>
        <div class="pull-left">男</div>
       </div>
       <div class="info-box clearfix">
        <label class="pull-left">个性签名</label>
        <div class="pull-left">未设置</div>
       </div>
      </div>
     </div>
    </div>
   </div>
  </div>
</template>

<script setup>

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
	padding: 0!important
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
```

我的订单页面展示

`src/components/user/Order.vue`，代码：

```vue
<template>
      <div class="right-container l">
        <div class="right-title">
          <h2>我的订单</h2>
          <ul>
            <li class="action"><router-link to="/user/order">全部<i class="js-all-num">3</i></router-link></li>
            <li><router-link to="/user/order?type=unpaid">未支付</router-link></li>
            <li><router-link to="/user/order?type=paid">已完成</router-link></li>
            <li><router-link to="/user/order?type=invalid">已废弃</router-link></li>
          </ul>
        </div>
        <div class="myOrder">
          <ul class="myOrder-list">
            <li data-flag="2107312249236254">
              <p class="myOrder-number">
                <i class="imv2-receipt"></i>订单编号：2107312249236254
                <span class="date">2021-07-31 22:49:23</span>
                <i class="imv2-delete js-order-del" title="删除订单"></i>
                <router-link to="/user/help" target="_blank" class="myfeedback r">售后帮助</router-link>
              </p>
              <div class="myOrder-course clearfix">
                <dl class="course-del l">
                  <dd class="clearfix">
                    <router-link to="" class="l"><img class="l" src="" width="160" height="90"></router-link>
                    <div class="del-box l">
                      <!-- type为类型 1实战购买 2实战续费 4就业班购买 5就业班续费 -->
                      <!-- cate 订单类型 0无优惠 1组合套餐 2学生优惠 -->
                      <router-link to="/course/525"><p class="course-name">晋级TypeScript高手，成为抢手的前端开发人才</p></router-link>
                      <p class="price-btn-box clearfix">
                        <!-- 如果有优惠券 -->
                        <span class="l truepay-text">实付</span>
                        <span class="l course-little-price">￥358.00</span>
                      </p>
                    </div>
                  </dd>
                  <dd class="clearfix">
                    <router-link to="" class="l"><img class="l" src="" width="160" height="90"></router-link>
                    <div class="del-box l">
                      <!-- type为类型 1实战购买 2实战续费 4就业班购买 5就业班续费 -->
                      <!-- cate 订单类型 0无优惠 1组合套餐 2学生优惠 -->
                      <router-link to="/course/525"><p class="course-name">晋级TypeScript高手，成为抢手的前端开发人才</p></router-link>
                      <p class="price-btn-box clearfix">
                        <!-- 如果有优惠券 -->
                        <span class="l truepay-text">实付</span>
                        <span class="l course-little-price">￥358.00</span>
                      </p>
                    </div>
                  </dd>
                </dl>
                <!-- 使用优惠券 -->
                <div class="course-money l pt15">
                  <div class="wrap">
                    <div class="type-box clearfix mb10">
                      <p class="type-text l">原价</p>
                      <p class="type-price l line-though"><span class="RMB">¥</span>399.00</p>
                    </div>
                    <div class="type-box clearfix mb10">
                      <p class="type-text l">折扣</p>
                      <p class="type-price l">-<span class="RMB">¥</span>41.00</p>
                    </div>
                    <div class="total-box clearfix">
                      <p class="type-text l">实付</p>
                      <p class="type-price l"><span class="RMB">¥</span>358.00</p>
                    </div>
                  </div>
                </div>
                <div class="course-action l">
                  <a class="pay-now" href="/pay/cashier?trade_number=2108100232047715">立即支付</a>
                  <a class="order-cancel" href="javascript:void(0);">取消订单</a>
                </div>
              </div>
            </li>
            <li data-flag="2107312108465190">
              <p class="myOrder-number">
                <i class="imv2-receipt"></i>订单编号：2107312108465190
                <span class="date">2021-07-31 21:08:46</span>
                <i class="imv2-delete js-order-del" title="删除订单"></i>
                <router-link to="/user/help" target="_blank" class="myfeedback r">售后帮助</router-link>
              </p>
              <div class="myOrder-course clearfix">
                <dl class="course-del l">
                  <dd class="clearfix">
                    <router-link to="/course/301" class="l">
                      <img class="l" src="" width="160" height="90">
                    </router-link>
                    <div class="del-box l">
                      <!-- type为类型 1实战购买 2实战续费 4就业班购买 5就业班续费 -->
                      <!-- cate 订单类型 0无优惠 1组合套餐 2学生优惠 -->
                      <router-link to="/course/301"><p class="course-name">Hadoop 系统入门+核心精讲</p></router-link>
                      <p class="price-btn-box clearfix">
                        <!-- 如果有优惠券 -->
                        <span class="l truepay-text">实付</span>
                        <span class="l course-little-price">￥288.00</span>
                      </p>
                    </div>
                  </dd>
                  <dd class="clearfix">
                    <router-link to="/course/464" class="l">
                      <img class="l" src="" width="160" height="90">
                    </router-link>
                    <div class="del-box l">
                      <!-- type为类型 1实战购买 2实战续费 4就业班购买 5就业班续费 -->
                      <!-- cate 订单类型 0无优惠 1组合套餐 2学生优惠 -->
                      <router-link to="/course/464"><p class="course-name">Kubernetes 入门到进阶实战，系统性掌握 K8s 生产实践</p></router-link>
                      <p class="price-btn-box clearfix">
                        <!-- 如果有优惠券 -->
                        <span class="l truepay-text">实付</span>
                        <span class="l course-little-price">￥299.00</span>
                      </p>
                    </div>
                  </dd>
                  <dd class="clearfix">
                    <router-link to="/course/501" class="l">
                      <img class="l" src="" width="160" height="90">
                    </router-link>
                    <div class="del-box l">
                      <!-- type为类型 1实战购买 2实战续费 4就业班购买 5就业班续费 -->
                      <!-- cate 订单类型 0无优惠 1组合套餐 2学生优惠 -->
                      <router-link to="/course/501"><p class="course-name">2021必修  CSS架构系统精讲 理论+实战玩转蘑菇街</p></router-link>
                      <p class="price-btn-box clearfix">
                        <!-- 如果有优惠券 -->
                        <span class="l truepay-text">实付</span>
                        <span class="l course-little-price">￥288.00</span>
                      </p>
                    </div>
                  </dd>
                  <dd class="clearfix">
                    <router-link to="/course/503" class="l">
                      <img class="l" src="" width="160" height="90">
                    </router-link>
                    <div class="del-box l">
                      <!-- type为类型 1实战购买 2实战续费 4就业班购买 5就业班续费 -->
                      <!-- cate 订单类型 0无优惠 1组合套餐 2学生优惠 -->
                      <router-link to="/course/503"><p class="course-name">Vue3开发企业级音乐Web App 明星讲师带你学习大厂高质量代码</p></router-link>
                      <p class="price-btn-box clearfix">
                        <!-- 如果有优惠券 -->
                        <span class="l truepay-text">实付</span>
                        <span class="l course-little-price">￥448.00</span>
                      </p>
                    </div>
                  </dd>
                  <dd class="clearfix">
                    <router-link to="/course/522" class="l">
                      <img class="l" src="" width="160" height="90">
                    </router-link>
                    <div class="del-box l">
                      <!-- type为类型 1实战购买 2实战续费 4就业班购买 5就业班续费 -->
                      <!-- cate 订单类型 0无优惠 1组合套餐 2学生优惠 -->
                      <router-link to="/course/522"><p class="course-name"> Spring Cloud / Alibaba 微服务架构实战，从架构设计到开发实践，手把手实现</p></router-link>
                      <p class="price-btn-box clearfix">
                        <!-- 如果有优惠券 -->
                        <span class="l truepay-text">实付</span>
                        <span class="l course-little-price">￥428.00</span>
                      </p>
                    </div>
                  </dd>
                </dl>
                <!-- 使用优惠券 -->
                <div class="course-money l pt15">
                  <div class="wrap">
                    <div class="type-box clearfix mb10">
                      <p class="type-text l">原价</p>
                      <p class="type-price l line-though">
                        <span class="RMB">¥</span>
                        1811.00
                      </p>
                    </div>
                    <div class="type-box clearfix mb10">
                      <p class="type-text l">折扣</p>
                      <p class="type-price l">
                        -
                        <span class="RMB">¥</span>
                        60.00
                      </p>
                    </div>
                    <div class="total-box clearfix">
                      <p class="type-text l">实付</p>
                      <p class="type-price l">
                        <span class="RMB">¥</span>
                        1751.00
                      </p>
                    </div>
                  </div>
                </div>
                <div class="course-action l">
                  <p class="order-close">已过期</p>
                </div>
              </div>
            </li>
          </ul>
        </div>
        <div class="page" style="text-align: center">
          <el-pagination background layout="prev, pager, next" :total="1000"></el-pagination>
        </div>
      </div>
</template>

<script setup>

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

.myOrder {
	width: 100%
}

.myOrder-list li {
	padding: 32px;
	padding-top: 0;
	box-shadow: 0 2px 8px 2px rgba(0,0,0,.1);
	margin-bottom: 24px;
	background: #fff;
	border-radius: 8px;
	position: relative
}

.myOrder-list li dd {
	margin-top: 24px;
	padding-top: 24px;
	position: relative;
	box-sizing: border-box;
	border-top: 1px solid #d9dde1
}

.myOrder-list li dd a {
	display: block
}

.myOrder-list li dd:first-child {
	border-top: none;
	margin-top: 0;
	padding-top: 0
}

.myOrder-list li:hover {
	-webkit-box-shadow: 0 2px 16px 2px rgba(0,0,0,.1);
	-moz-box-shadow: 0 2px 16px 2px rgba(0,0,0,.1);
	box-shadow: 0 2px 16px 2px rgba(0,0,0,.1)
}

.myOrder-list li:hover .myOrder-number a,.myOrder-list li:hover i.imv2-delete {
	display: block
}

.del-box {
	margin-left: 16px;
	width: 510px
}

.del-box .course-name {
	word-break: break-word;
	color: #07111b;
	font-size: 16px;
	margin-bottom: 8px;
	line-height: 22px
}

.del-box .price-btn-box {
	font-size: 14px;
	line-height: 14px
}

.del-box .price-btn-box .truepay-text {
	color: #93999f;
	margin-right: 5px
}

.del-box .price-btn-box .course-little-price {
	color: #f01414
}

.myOrder-number {
	padding: 28px 0 19px;
	font-weight: 700;
	color: #4d555d;
	border-bottom: 1px solid #b7bbbf;
	font-size: 14px;
	line-height: 14px;
	box-sizing: border-box
}

.myOrder-number a,.myOrder-number span {
	color: #93999f;
	font-weight: 500;
	margin-left: 24px
}

.myOrder-number a {
	display: none
}

.myOrder-number a:hover {
	color: #4d555d
}

.myOrder-number i.imv2-delete,.myOrder-number i.imv2-receipt {
	float: left;
	margin-top: -2px;
	margin-right: 10px;
	font-size: 16px;
	color: #f01414
}

.myOrder-number i.imv2-delete {
	float: right;
	margin-left: 28px;
	color: #93999f;
	cursor: pointer;
	display: none
}

.myOrder-number i.imv2-delete:hover {
	color: #4d555d
}

.myOrder-course {
	position: relative;
	margin-top: 25px
}

.course-money {
	width: 250px;
	height: 100%;
	text-align: center;
	color: #93999f;
	font-size: 16px;
	box-sizing: border-box;
	line-height: 16px
}

.course-money .wrap {
	display: inline-block
}

.course-money .RMB {
	font-size: 14px;
	vertical-align: top;
	line-height: 14px
}

.course-money .type-box {
	line-height: 14px;
	text-align: left
}

.course-money .type-box .type-price,.course-money .type-box .type-text {
	font-size: 16px;
	color: #93999f
}

.course-money .type-box .type-price .RMB,.course-money .type-box .type-text .RMB {
	font-size: 14px;
	display: inline-block;
	position: relative;
	top: -1px;
	vertical-align: top;
	line-height: 14px
}

.course-money .type-box .line-though {
	text-decoration: line-through
}

.course-money .type-box .type-text {
	margin-right: 5px
}

.course-money .total-box .type-text {
	font-size: 14px;
	color: #93999f;
	margin-right: 5px
}

.course-money .total-box .type-price {
	color: #f01414
}

.course-money .mb10 {
	margin-bottom: 10px
}

.course-money.presale .type-box {
	line-height: 18px;
	margin-bottom: 4px
}

.course-money.presale .type-box .type-text {
	color: #1c1f21
}

.course-money.presale .type-box .type-price .RMB {
	vertical-align: baseline
}

.course-action {
	position: absolute;
	top: 0;
	width: 180px;
	height: 100%;
	border-left: 1px solid #d9dde1;
	right: 0;
	text-align: center
}

.course-action .pay-now {
	margin: 12px auto;
	display: block;
	width: 120px;
	height: 36px;
	color: #fff;
	background: rgba(240,20,20,.8);
	border-radius: 18px;
	line-height: 36px
}

.course-action .pay-now:hover {
	background-color: #f01414
}

.course-action .order-cancel {
	color: #93999f;
	display: block;
	font-size: 14px;
	line-height: 14px
}

.course-action .order-cancel:hover {
	color: #4d555d
}

.course-action .order-close {
	color: #93999f;
	margin-top: 36px;
	line-height: 14px
}

.course-action.order-recover .order-close {
	margin-top: 22px
}

.course-del {
	width: 740px;
	border-right: 1px solid #d9dde1;
	position: relative
}

</style>
```

路由，`src/router/index.js`，代码：

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
            authorization: true,
        },
        path: '/user',
        name: "User",
        component: () => import("../views/User.vue"),
        children: [
            {
                meta: {
                    title: "飞升在线教育-个人信息",
                    keepAlive: true,
                    authorization: true,
                },
                path: '',
                name: "UserInfo",
                component: () => import("../components/user/Info.vue"),
            },
            {
                meta: {
                    title: "飞升在线教育--我的订单",
                    keepAlive: true,
                    authorization: true,
                },
                path: 'order',
                name: "UserOrder",
                component: () => import("../components/user/Order.vue"),
            },
        ]
    }, {
        meta: {
            title: "飞升在线教育-课程列表",
            keepAlive: true,
        },
        path: '/project',
        name: "Course",
        component: () => import("../views/Course.vue"),
    }, {
        meta: {
            title: "飞升在线教育-课程详情",
            keepAlive: true
        },
        path: '/project/:id',     // :id vue的路径参数，代表了课程的ID
        name: "Info",
        component: () => import("../views/Info.vue"),
    }, {
        meta: {
            title: "飞升在线教育-购物车",
            keepAlive: true,
            authorization: true,
        },
        path: '/cart',
        name: "Cart",
        component: () => import("../views/Cart.vue"),
    }, {
        meta: {
            title: "飞升在线教育-确认下单",
            keepAlive: true,
            authorization: true,
        },
        path: '/order',
        name: "Order",
        component: () => import("../views/Order.vue"),
    }, {
        meta: {
            title: "支付成功",
            keepAlive: true
        },
        path: '/alipay',
        name: "PaySuccess",
        component: () => import("../views/AliPaySuccess.vue"),
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

提交git

~~~python
feature: 个人中心页面展示
~~~





## 我的订单

### 服务端提供当前用户的订单列表api接口

`orders/views.py`，代码：

```python
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Order
from .serializers import OrderModelSerializer, OrderListModelSerializer
from mixins import ReCreateModelMixin, ReListModelMixin
from response import APIResponse
from paginations import RePageNumberPagination


# 中间代码省略。。。。
# 中间代码省略。。。。


class OrderPayChoicesAPIView(APIView):
    def get(self, request):
        """返回订单状态"""
        return APIResponse(data=Order.status_choices)


class OrderListAPIView(ReListModelMixin, GenericViewSet):
    """当前登录用户的订单列表"""
    permission_classes = [IsAuthenticated]
    pagination_class = RePageNumberPagination

    serializer_class = OrderListModelSerializer

    def get_queryset(self):
        user = self.request.user  # 获取当前登录用户
        query = Order.objects.filter(user=user, is_deleted=False, is_show=True)
        order_status = int(self.request.query_params.get("status", -1))
        status_list = [item[0] for item in Order.status_choices]
        if order_status in status_list:
            query = query.filter(order_status=order_status)
        else:
            # 订单状态传入不正确时，返回所有的订单
            query = query.all()
        return query.order_by("-id").all()
```

`orders/serializers.py`，代码：

```python
class OrderDetailMdoelSerializer(serializers.ModelSerializer):
    """订单详情序列化器"""
    # 通过source修改数据源，可以把需要调用的部分外键字段提取到当前序列化器中
    course_id = serializers.IntegerField(source="course.id")
    course_name = serializers.CharField(source="course.name")
    course_cover = serializers.ImageField(source="course.course_cover")

    class Meta:
        model = OrderDetail
        fields = ["id", "price", "real_price", "discount_name", "course_id", "course_name", "course_cover"]


class OrderListModelSerializer(serializers.ModelSerializer):
    """订单列表序列化器"""
    order_courses = OrderDetailMdoelSerializer(many=True)
    
    class Meta:
        model = Order
        fields = ["id", "order_number", "total_price", "real_price", "pay_time", "created_time", "credit", "coupon",
                  "pay_type", "order_status", "order_courses"]

```

`orders/models.py`，代码：

```python
class Order(BaseModel):
    """订单基本信息模型"""
    # //.... 中间代码省略
    # //.... 中间代码省略
    # //.... 中间代码省略
    def coupon(self):
        """当前订单关联的优惠券信息"""
        coupon_related = self.to_coupon.first()
        if coupon_related:
            return {
                "id": coupon_related.coupon.id,
                "name": coupon_related.coupon.name,
                "sale": coupon_related.coupon.sale,
                "discount": coupon_related.coupon.discount,
                "condition": coupon_related.coupon.condition,
            }
        return {}

```

`orders/urls.py`，代码：

```python
from django.urls import path

from . import views

urlpatterns = [
    # 创建订单
    path("", views.OrderCreateAPIView.as_view({"post": "create"})),
    # 查看订单状态
    path("pay/status/", views.OrderPayChoicesAPIView.as_view()),
    # 获取订单详情
    path("list/", views.OrderListAPIView.as_view({"get": "list"})),
]

```



### 客户端展示订单列表

`api/order.js`，代码：

```javascript
import http from "../utils/http";
import {reactive} from "vue";

const order = reactive({
    // ... 中间代码省略
    // ... 中间代码省略
    // ... 中间代码省略
    order_status: -1,    // 个人中心的默认显示的订单状态选项
    order_status_chioces:[], // 个人中心的订单支付状态选项
    page: 1,                 // 个人中心的订单列表对应的页码
    size: 5,                 // 个人中心的订单列表对应的单页数据量
    order_list:[],           // 个人中心的订单列表
    count: 0,                // 个人中心的订单列表的总数据量
    // ... 中间代码省略
    // ... 中间代码省略
    // ... 中间代码省略
    get_order_status(){
        // 获取订单状态选项
        return http.get('/order/pay/status/')
    },
    get_order_list(token){
        // 获取当前登录用户的订单列表[分页显示]
        return http.get('/order/list/', {
            params: {
                page: this.page,
                size: this.size,
                status: this.order_status,
            },
            headers: {
                Authorization: "jwt " + token,
            }
        })
    }
});

export default order;
```

`src/components/user/Order.vue`，代码：

```vue
<template>
      <div class="right-container l">
        <div class="right-title">
          <h2>我的订单</h2>
          <ul>
            <li :class="{action: order.order_status===-1}"><a href="" @click.prevent="order.order_status=-1">全部<i class="js-all-num" v-if="order.order_status===-1">{{order.count}}</i></a></li>
            <li :class="{action: order.order_status===status[0]}" v-for="status in order.order_status_chioces">
              <a href="" @click.prevent="order.order_status=status[0]">{{status[1]}}<i class="js-all-num" v-if="order.order_status===status[0]">{{order.count}}</i></a>
            </li>
          </ul>
        </div>
        <div class="myOrder">
          <ul class="myOrder-list">
            <li v-for="order_info in order.order_list">
              <p class="myOrder-number">
                <i class="imv2-receipt"></i>订单编号：{{order_info.order_number}}
                <span class="date">{{order_info.created_time.replace("T", " ").split(".")[0]}}</span>
                <span class="imv2-delete js-order-del">删除订单</span>
                <router-link to="/user/help" target="_blank" class="myfeedback r">售后帮助</router-link>
              </p>
              <div class="myOrder-course clearfix">
                <dl class="course-del l"  v-for="course_info in order_info.order_courses">
                  <dd class="clearfix">
                    <router-link :to="`/project/${course_info.course_id}`" class="l"><img class="l" :src="course_info.course_cover" width="160" height="90"></router-link>
                    <div class="del-box l">
                      <router-link :to="`/project/${course_info.course_id}`"><p class="course-name">{{course_info.course_name}}</p></router-link>
                      <p class="price-btn-box clearfix">
                        <!-- 如果有优惠券 -->
                        <span class="l truepay-text" v-if="course_info.price > course_info.real_price">原价</span>
                        <span class="l line-though clearfix" style="float: none" v-if="course_info.price > course_info.real_price">￥{{course_info.price}}</span>
                        <span class="l truepay-text" v-if="course_info.price > course_info.real_price">折扣</span>
                        <span class="l line-though clearfix" style="float: none" v-if="course_info.price > course_info.real_price">￥{{parseFloat(course_info.price - course_info.real_price).toFixed(2)}}</span>
                        <span class="l truepay-text">实付</span>
                        <span class="l course-little-price">￥{{course_info.real_price}}</span>
                      </p>
                    </div>
                  </dd>
                </dl>
                <!-- 使用优惠券 -->
                <div class="course-money l pt15">
                  <div class="wrap">
                    <div class="type-box clearfix mb10">
                      <p class="type-text l">订单总价</p>
                      <p class="type-price l line-though"><span class="RMB">¥</span>{{order_info.total_price}}</p>
                    </div>
                    <div class="type-box clearfix mb10" v-if="order_info.total_price > order_info.real_price">
                      <p class="type-text l" v-if="order_info.credit>0">积分折扣</p>
                      <p class="type-text l" v-if="order_info.coupon.id">优惠券折扣</p>
                      <p class="type-price l">-<span class="RMB">¥</span>{{parseFloat(order_info.total_price - order_info.real_price).toFixed(2)}}</p>
                    </div>
                    <div class="total-box clearfix">
                      <p class="type-text l">订单实付</p>
                      <p class="type-price l"><span class="RMB">¥</span>{{order_info.real_price}}</p>
                    </div>
                  </div>
                </div>
                <div class="course-action l" v-if="order_info.order_status === 0">
                  <a class="pay-now" href="" @click.prevent="pay_now(order_info)">立即支付</a>
                  <a class="order-cancel" href="" @click.prevent="pay_cancel(order_info)">取消订单</a>
                </div>
                <div class="course-action l" v-else-if="order_info.order_status === 1">
                  <a class="pay-now" href="" @click.prevent="evaluate_now(order_info)">立即评价</a>
                  <a class="order-cancel" href="" @click.prevent="order_refund(order_info)">申请退款</a>
                </div>
                <div class="course-action l" v-else-if="order_info.order_status === 2">
                  <a class="pay-now" href="" @click.prevent="delete_order(order_info)">删除订单</a>
                </div>
                <div class="course-action l" v-else-if="order_info.order_status === 3">
                  <a class="pay-now" href="" @click.prevent="recovery_now(order_info)">订单恢复</a>
                  <a class="pay-now" href="" @click.prevent="delete_order(order_info)">删除订单</a>
                </div>
              </div>
            </li>
          </ul>
        </div>
        <div class="page" style="text-align: center">
          <el-pagination
              background
              layout="sizes, prev, pager, next, jumper"
              :total="order.count"
              :page-sizes="[5, 10, 15, 20]"
              :page-size="order.size"
              @current-change="current_page"
              @size-change="current_size"
          ></el-pagination>
        </div>
      </div>
</template>
```

```vue
<script setup>
import {watch} from "vue";
import order from "../../api/order"

const getOrderStatus = () => {
  // 获取订单状态选项
  order.get_order_status().then(response => {
    order.order_status_chioces = response.data.data;
  })
}
getOrderStatus()


const getOrderList = () => {
  // 获取当前登录用户的订单列表
  let token = sessionStorage.token || localStorage.token;
  order.get_order_list(token).then(response => {
    order.order_list = response.data.data.results
    order.count = response.data.data.count
  })
}
getOrderList()

let pay_now = (order_info) => {
  // 订单继续支付
}
let pay_cancel = (order_info) => {
  // 取消订单
}

let evaluate_now = (order_info) => {
  // 订单评价
}

let order_refund = (order_info) => {
  // 申请退款
}

let delete_order = (order_info) => {
  // 删除订单
}

let recovery_now = (order) => {
  // 恢复订单
}

// 切换页码
let current_page = (page) => {
  order.page = page;
}

// 切换分页数据量
let current_size = (size) => {
  order.size = size;
}

// 监听页码
watch(
    () => order.page,
    () => {
      getOrderList()
    }
)

// 监听页面数据量大小
watch(
    () => order.size,
    () => {
      order.page = 1;
      getOrderList()
    }
)

// 监听订单状态选项
watch(
    () => order.order_status,
    () => {
      order.page = 1;
      getOrderList()
    }
)

</script>
```

提交代码版本

```bash
feature: 用户中心展示当前用户的订单列表
```



### 订单状态切换

#### 取消订单

服务端提供取消订单的API接口

`order/views.py`

```python
from django.db import transaction

from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Order
from .serializers import OrderModelSerializer, OrderListModelSerializer

from logger import log
from mixins import ReCreateModelMixin, ReListModelMixin
from response import APIResponse
from paginations import RePageNumberPagination
from return_code import HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR
from coupon.services import add_coupon_to_redis


class OrderCreateAPIView(ReCreateModelMixin, GenericViewSet):
    """创建订单"""
    permission_classes = (IsAuthenticated,)

    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer


class OrderPayChoicesAPIView(APIView):
    def get(self, request):
        """返回订单状态"""
        return APIResponse(data=Order.status_choices)


class OrderListAPIView(ReListModelMixin, GenericViewSet):
    """当前登录用户的订单列表"""
    permission_classes = [IsAuthenticated]
    pagination_class = RePageNumberPagination

    serializer_class = OrderListModelSerializer

    def get_queryset(self):
        user = self.request.user  # 获取当前登录用户
        query = Order.objects.filter(user=user, is_deleted=False, is_show=True)
        order_status = int(self.request.query_params.get("status", -1))
        status_list = [item[0] for item in Order.status_choices]
        if order_status in status_list:
            query = query.filter(order_status=order_status)
        else:
            # 订单状态传入不正确时，返回所有的订单
            query = query.all()
        return query.order_by("-id").all()


class OrderViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def pay_cancel(self, request, pk):
        """取消订单"""
        try:
            order = Order.objects.get(pk=pk, order_status=0)
        except Exception as e:
            log.error("当前订单记录不存在或不能取消---%s", str(e))
            return APIResponse(HTTP_400_BAD_REQUEST, "当前订单记录不存在或不能取消.")

        with transaction.atomic():
            save_id = transaction.savepoint()
            try:
                # 1. 查询当前订单是否使用了积分，如果有则恢复
                if order.credit > 0:
                    order.user.credit += order.credit
                    order.user.save()

                # 2. 查询当前订单是否使用了优惠券，如果有则恢复
                obj = order.to_coupon.first()
                if obj:
                    add_coupon_to_redis(obj)

                # 3. 切换当前订单为取消状态
                order.order_status = 2
                order.save()

                return APIResponse({"error": "当前订单已取消！"})

            except Exception as e:
                transaction.savepoint_rollback(save_id)
                log.error(f"订单无法取消，发生未知错误.---{e}")
                return APIResponse(HTTP_500_INTERNAL_SERVER_ERROR, "当前订单无法取消，请联系客服工作人员.")

```

`coupon/services.py`，代码：

```python
import json
from datetime import datetime

from django_redis import get_redis_connection

from course.models import Course


def get_user_coupon_list(user_id):
    """获取指定用户拥有的所有优惠券列表"""
    redis = get_redis_connection("coupon")
    coupon_list = redis.keys(f"{user_id}:*")
    try:
        coupon_id_list = [item.decode() for item in coupon_list]
    except:
        coupon_id_list = []
    coupon_data = []
    # 遍历redis中所有的优惠券数据并转换数据格式
    for coupon_key in coupon_id_list:
        coupon_item = {"user_coupon_id": int(coupon_key.split(":")[-1])}
        coupon_hash = redis.hgetall(coupon_key)
        for key, value in coupon_hash.items():
            key = key.decode()
            value = value.decode()
            if key in ["to_course", "to_category", "to_direction"]:
                value = json.loads(value)
            coupon_item[key] = value
        coupon_data.append(coupon_item)

    return coupon_data


def get_user_enable_coupon_list(user_id):
    """
    获取指定用户本次下单的可用优惠券列表
    # 根据当前本次客户端购买商品课程进行比较，获取用户的当前可用优惠券。
    """
    redis = get_redis_connection("cart")

    # 先获取所有的优惠券列表
    coupon_data = get_user_coupon_list(user_id)

    # 获取指定用户的购物车中的勾选商品[与优惠券的适用范围进行比对，找出能用的优惠券]
    cart_hash = redis.hgetall(f"cart_{user_id}")

    # 获取被勾选的商品课程的ID列表
    course_id_list = {int(key.decode()) for key, value in cart_hash.items() if value == b'1'}

    # 获取被勾选的商品课程的模型对象列表
    course_list = Course.objects.filter(pk__in=course_id_list, is_deleted=False, is_show=True).all()

    category_id_list = set()
    direction_id_list = set()
    for course in course_list:
        # 获取被勾选的商品课程的父类课程分类id列表，并保证去重
        category_id_list.add(int(course.category.id))
        # # 获取被勾选的商品课程的父类学习方向id列表，并保证去重
        direction_id_list.add(int(course.direction.id))

    # 创建一个列表用于保存所有的可用优惠券
    enable_coupon_list = []
    for item in coupon_data:
        coupon_type = int(item.get("coupon_type"))

        if coupon_type == 0:
            # 通用类型优惠券
            item["enable_course"] = "__all__"
            enable_coupon_list.append(item)

        elif coupon_type == 3:
            # 指定课程优惠券
            coupon_course = {int(course_item["course__id"]) for course_item in item.get("to_course")}
            # 交集处理
            ret = course_id_list & coupon_course
            if len(ret) > 0:
                item["enable_course"] = {int(course.id) for course in course_list if course.id in ret}
                enable_coupon_list.append(item)

        elif coupon_type == 2:
            # 指定课程分配优惠券
            coupon_category = {int(category_item["category__id"]) for category_item in item.get("to_category")}
            # 交集处理
            ret = category_id_list & coupon_category

            if len(ret) > 0:
                item["enable_course"] = {int(course.id) for course in course_list if course.category.id in ret}
                enable_coupon_list.append(item)

        elif coupon_type == 1:
            # 指定学习方向的优惠券
            coupon_direction = {int(direction_item["direction__id"]) for direction_item in item.get("to_direction")}
            # 交集处理
            ret = direction_id_list & coupon_direction

            if len(ret) > 0:
                item["enable_course"] = {int(course.id) for course in course_list if course.direction.id in ret}
                enable_coupon_list.append(item)

    return enable_coupon_list


def add_coupon_to_redis(obj):
    """
    添加优惠券使用记录到redis中
    """
    redis = get_redis_connection("coupon")
    # 记录优惠券信息到redis中
    pipe = redis.pipeline()
    pipe.multi()
    pipe.hset(f"{obj.user.id}:{obj.id}", "coupon_id", obj.coupon.id)
    pipe.hset(f"{obj.user.id}:{obj.id}", "name", obj.coupon.name)
    pipe.hset(f"{obj.user.id}:{obj.id}", "discount", obj.coupon.discount)
    pipe.hset(f"{obj.user.id}:{obj.id}", "get_discount_display", obj.coupon.get_discount_display())

    pipe.hset(f"{obj.user.id}:{obj.id}", "coupon_type", obj.coupon.coupon_type)
    pipe.hset(f"{obj.user.id}:{obj.id}", "get_coupon_type_display", obj.coupon.get_coupon_type_display())

    pipe.hset(f"{obj.user.id}:{obj.id}", "start_time", obj.coupon.start_time.strftime("%Y-%m-%d %H:%M:%S"))
    pipe.hset(f"{obj.user.id}:{obj.id}", "end_time", obj.coupon.end_time.strftime("%Y-%m-%d %H:%M:%S"))

    pipe.hset(f"{obj.user.id}:{obj.id}", "get_type", obj.coupon.get_type)
    pipe.hset(f"{obj.user.id}:{obj.id}", "get_get_type_display", obj.coupon.get_get_type_display())

    pipe.hset(f"{obj.user.id}:{obj.id}", "condition", obj.coupon.condition)
    pipe.hset(f"{obj.user.id}:{obj.id}", "sale", obj.coupon.sale)

    pipe.hset(f"{obj.user.id}:{obj.id}", "to_direction",
              json.dumps(list(obj.coupon.to_direction.values("direction__id", "direction__name"))))
    pipe.hset(f"{obj.user.id}:{obj.id}", "to_category",
              json.dumps(list(obj.coupon.to_category.values("category__id", "category__name"))))
    pipe.hset(f"{obj.user.id}:{obj.id}", "to_course",
              json.dumps(list(obj.coupon.to_course.values("course__id", "course__name"))))

    # 设置当前优惠券的有效期
    pipe.expire(f"{obj.user.id}:{obj.id}", int(obj.coupon.end_time.timestamp() - datetime.now().timestamp()))
    pipe.execute()

```

对于之前在admin站点中保存优惠券使用都redis中的操作，也可以调用上面的代码，`coupon/admin.py`，代码：

```python
import json

from django.contrib import admin
from django.utils import timezone as datetime

from django_redis import get_redis_connection

from .models import Coupon, CouponDirection, CouponCourseCat, CouponCourse, CouponLog
from logger import log
from coupon.services import add_coupon_to_redis


class CouponDirectionInLine(admin.TabularInline):  # admin.StackedInline
    """学习方向的内嵌类"""
    model = CouponDirection
    fields = ["id", "direction"]


class CouponCourseCatInLine(admin.TabularInline):  # admin.StackedInline
    """课程分类的内嵌类"""
    model = CouponCourseCat
    fields = ["id", "category"]


class CouponCourseInLine(admin.TabularInline):  # admin.StackedInline
    """课程信息的内嵌类"""
    model = CouponCourse
    fields = ["id", "course"]


class CouponModelAdmin(admin.ModelAdmin):
    """优惠券的模型管理器"""
    list_display = ["id", "name", "start_time", "end_time", "total", "has_total", "coupon_type", "get_type", ]
    inlines = [CouponDirectionInLine, CouponCourseCatInLine, CouponCourseInLine]


admin.site.register(Coupon, CouponModelAdmin)


class CouponLogModelAdmin(admin.ModelAdmin):
    """优惠券发放和使用日志"""
    list_display = ["id", "user", "coupon", "order", "use_time", "use_status"]

    def save_model(self, request, obj, form, change):
        """
        保存或更新记录时自动执行的钩子
        request: 本次客户端提交的请求对象
        obj: 本次操作的模型实例对象
        form: 本次客户端提交的表单数据
        change: 值为True，表示更新数据，值为False，表示添加数据
        """
        obj.save()

        # 同步记录到redis中
        redis = get_redis_connection("coupon")
        if obj.use_status == 0 and obj.use_time == None:
            # 未使用过的 记录优惠券信息到redis中
            add_coupon_to_redis(obj)
        else:
            # 使用过的优惠直接删除
            redis.delete(f"{obj.user.id}:{obj.id}")

    def delete_model(self, request, obj):
        """
        删除记录时自动执行的钩子
        详情页中删除一个记录时执行
        如果系统后台管理员删除当前优惠券记录，则redis中的对应记录也被删除
        """
        log.info(f"详情页中删除一个记录---{obj}")
        redis = get_redis_connection("coupon")
        redis.delete(f"{obj.user.id}:{obj.id}")
        obj.delete()

    def delete_queryset(self, request, queryset):
        """
        删除记录时自动执行的钩子
        列表页中删除多个记录时执行
        在列表页中进行删除优惠券记录时，也要同步删除容redis中的记录
        """
        log.info(f"列表页中删除多个记录---{queryset}")
        redis = get_redis_connection("coupon")
        for obj in queryset:
            redis.delete(f"{obj.user.id}:{obj.id}")
        queryset.delete()


admin.site.register(CouponLog, CouponLogModelAdmin)

```

`order/urls.py`，代码：

```python
from django.urls import path,re_path
from . import views

urlpatterns = [
    path("", views.OrderCreateAPIView.as_view()),
    path("pay/choices/", views.OrderPayChoicesAPIView.as_view()),
    path("list/", views.OrderListAPIView.as_view()),
    re_path("^(?P<pk>\d+)/$", views.OrderViewSet.as_view({"put": "pay_cancel"})),
]

```



##### 客户端实现取消订单功能

`api/order.js`，代码：

```javascript
import http from "../utils/http";
import {reactive} from "vue";

const order = reactive({
  // 中间代码省略....
  // 中间代码省略....
  order_cancel(order_id,token){
    // 取消订单操作
    return http.put(`/order/${order_id}/`, {},{
        headers:{
            Authorization: "jwt " + token,
        }
    })
  }
})

export default order;
```

`components/user/Order.vue`，代码：

```vue

<script setup>
// ...

let pay_cancel = (order_info) => {
  // 取消订单
  let token = sessionStorage.token || localStorage.token;
  order.order_cancel(order_info.id, token).then(response => {
    order_info.order_status = 2;
  })
}
</script>
```



#### 再次支付

`components/user/Order.vue`，代码：

```vue
<script setup>

let pay_now = (order_info) => {
  // 订单继续支付
  order.order_number = order_info.order_number;
  let token = sessionStorage.token || localStorage.token;
  if (order.pay_type === 0) {
    // 如果当前订单的支付方式属于支付宝，发起支付宝支付
    order.alipay_page_pay(order_info.order_number, token).then(response => {
      // 新开浏览器窗口，跳转到支付页面
      window.open(response.data.data.link, "_blank");
      // 新建定时器，每隔5秒到服务端查询一次当前订单的支付结果
      let max_query_timer = 180;
      clearInterval(order.timer);
      order.timer = setInterval(() => {
        max_query_timer--;
        if (max_query_timer > 0) {
          order.query_order(token).then(response => {
            order_info.order_status = 1;
            clearInterval(order.timer);
          })
        } else {
          clearInterval(order.timer);
        }
      }, 5000);
    })
  }
}

</script>
```

提交代码版本

```bash
feature: 订单状态切换-取消订单与再次支付
```



#### 订单超时

用户下单在15分钟以后自动判断订单状态如果是0, 则直接改成3，恢复当前订单的优惠券和用户积分。

##### 使用Celery的定时任务来完成订单超时功能

```
定时任务[async_tasks]，主要是依靠操作系统的计划任务或者第三方软件的定时执行
定时任务的常见场景：
   1. 订单超时取消
   2. 生日邮件[例如，每天凌晨检查当天有没有用户生日，有则发送一份祝福邮件]
   3. 财务统计[例如，每个月的1号，把当月的订单进行统计，生成一个财务记录，保存到数据库中]
   4. 页面缓存[例如，把首页设置为每隔5分钟生成一次缓存]

在django中要实现订单的超时取消，有以下2种类型，4种方式：
   1. 通过计划任务来实现定时多次
      计划任务，是celery提供给开发者设置周期任务的，可以定时多次，例如：每周一次，每分钟一次
      1.1 Celery本身提供了计划任务的schedules执行
      1.2 安装并配置django的第三方模块django-crontab[依靠系统本身的计划任务来完成，与celery无关]
   2. 通过定时任务来实现定时一次
      2.1 celery提供的apply_async来完成
      2.2 redis值空间值事件，实际上就是基于redis的发布订阅的特性来完成
```

在实现订单超时的定时任务之前，我们需要先简单使用一下定时任务。`orders/tasks.py`，代码：

```python
from celery import shared_task


@shared_task(name="order_timeout")
def order_timeout(order_id):
    print(order_id)
    return True

```

终端下重启celery。并进入django内置的终端进行异步定时任务的测试。

```bash
# 第一个终端
celery -A fsapi worker -l info
# windows如果没有执行，用下面的命令
celery -A fsapi worker --pool=solo -l info
# 第二个终端
# 进入项目根目录
python manage.py shell
from orders.tasks import order_timeout
order_timeout.apply_async(kwargs={"order_id": 3}, countdown=5)  # countdown为定时时间，单位：秒
```

在此之前，我们已经在文件`extension/constants.py`中，对定时任务的定时时间设置了一个常量

```python
# 订单超时的时间(单位：秒)
ORDER_TIMEOUT = 15 * 60
```

在用户下单成功时，设置订单超时的定时任务。

`orders/tasks.py`，代码：

```python
from celery import shared_task
from django.db import transaction
from .models import Order
from coupon.services import add_coupon_to_redis

from logger import log


@shared_task(name="order_timeout")
def order_timeout(order_id):
    print(f"要超时取消的订单ID={order_id}")
    try:
        order = Order.objects.get(pk=order_id)
    except Exception as e:
        log.warning(f"订单不存在！order_id:{order_id}: {e}")
        return

    if order.order_status == 0:
        """只针对未支付的订单进行超时取消"""
        with transaction.atomic():
            save_id = transaction.savepoint()
            try:
                # 1. 查询当前订单是否使用了积分，如果有则恢复
                if order.credit > 0:
                    order.user.credit += order.credit
                    order.user.save()

                # 2. 查询当前订单是否使用了优惠券，如果有则恢复
                obj = order.to_coupon.first()
                if obj:
                    add_coupon_to_redis(obj)

                # 3. 切换当前订单为取消状态
                order.order_status = 3
                order.save()

                return {"order_id": order.id, "status": True, "errmsg": f"订单超时取消成功！"}

            except Exception as e:
                transaction.savepoint_rollback(save_id)
                log.warning(f"过期订单无法处理！order_id:{order_id}: {e}")
                return {"order_id": order.id, "status": False, "errmsg": f"{e}"}

```

在用户下单的时候，设置定时任务，`orders/serializers.py`的create创建订单时，代码：

```python
from datetime import datetime

from django.db import transaction

from rest_framework import serializers
from rest_framework import exceptions
from django_redis import get_redis_connection

from .models import Order, OrderDetail, Course
from .tasks import order_timeout

from logger import log
from coupon.models import CouponLog
from constants import CREDIT_TO_MONEY, ORDER_TIMEOUT


class OrderModelSerializer(serializers.ModelSerializer):
    user_coupon_id = serializers.IntegerField(write_only=True, default=-1)
    order_timeout = serializers.IntegerField(read_only=True)

    class Meta:
        model = Order
        fields = ["pay_type", "id", "order_number", "user_coupon_id", "credit", "order_timeout"]
        read_only_fields = ["id", "order_number", "order_timeout"]
        extra_kwargs = {
            "pay_type": {"write_only": True},
            "credit": {"write_only": True},
        }

    def get_validated_data(self, validated_data):
        user = self.context["request"].user
        user_id = user.id
        # 用户支付方式
        pay_type = validated_data.get("pay_type", 0)
        # 判断用户如果使用了优惠券，则优惠券需要判断验证
        user_coupon_id = validated_data.get("user_coupon_id")

        # 本次下单时，用户使用的优惠券
        user_coupon = None
        if user_coupon_id != -1:
            user_coupon = CouponLog.objects.filter(
                pk=user_coupon_id, user_id=user_id, is_deleted=False, is_show=True
            ).first()

        # 本次下单时使用的积分数量
        use_credit = validated_data.get("credit", 0)
        if use_credit > 0 and use_credit > user.credit:
            raise serializers.ValidationError(detail="您拥有的积分不足以抵扣本次下单的积分，请重新下单！")

        return user, user_id, pay_type, user_coupon_id, user_coupon, use_credit

    def create_order(self, redis, user_id, pay_type):
        # 创建订单记录
        order = Order.objects.create(
            name="购买课程",  # 订单标题
            user_id=user_id,  # 当前下单的用户ID
            order_number=datetime.now().strftime("%Y%m%d") + ("%08d" % user_id) + "%08d" % redis.incr(
                "order_number"),  # 基于redis生成分布式唯一订单号
            pay_type=pay_type,  # 支付方式,默认是支付宝支付
        )

        # 记录本次下单的商品列表
        cart_hash = redis.hgetall(f"cart_{user_id}")
        if len(cart_hash) < 1:
            raise serializers.ValidationError(detail="购物车没有要下单的商品")

        return order, cart_hash

    def discount_credit(self, cart_hash, order, user_coupon, use_credit, user):
        # 提取购物车中所有勾选状态为b'1'的商品
        course_id_list = [int(key.decode()) for key, value in cart_hash.items() if value == b'1']

        # 筛选出要购买的所有课程
        course_list = Course.objects.filter(pk__in=course_id_list, is_deleted=False, is_show=True).all()

        detail_list = []
        total_price = 0  # 本次订单的总价格
        real_price = 0  # 本次订单的实付总价

        # 用户使用优惠券或积分以后，需要在服务端计算本次使用优惠券或积分的最大优惠额度
        total_discount_price = 0  # 总优惠价格
        max_discount_course = None  # 享受最大优惠的课程

        # 本次下单最多可以抵扣的积分
        max_use_credit = 0

        for course in course_list:
            discount_price = course.discount.get("price", None)  # 获取课程原价
            discount_name = course.discount.get("type", "")
            detail_list.append(OrderDetail(
                order=order,
                course=course,
                name=course.name,
                price=course.price,
                real_price=float(course.price if discount_price is None else discount_price),
                discount_name=discount_name,
            ))

            # 统计订单的总价和实付总价
            total_price += float(course.price)
            real_price += float(course.price if discount_price is None else discount_price)

            # 在用户使用了优惠券，并且当前课程没有参与其他优惠活动时，找到最佳优惠课程
            if user_coupon and discount_price is None:
                if max_discount_course is None:
                    max_discount_course = course
                else:
                    if course.price >= max_discount_course.price:
                        max_discount_course = course

            # 添加每个课程的可用积分
            if use_credit > 0 and course.credit > 0:
                max_use_credit += course.credit

        # 在用户使用了优惠券以后，根据循环中得到的最佳优惠课程进行计算最终抵扣金额
        if user_coupon:
            # 优惠公式
            sale = float(user_coupon.coupon.sale[1:])
            if user_coupon.coupon.discount == 1:
                """减免优惠券"""
                total_discount_price = sale
            elif user_coupon.coupon.discount == 2:
                """折扣优惠券"""
                total_discount_price = float(max_discount_course.price) * (1 - sale)
            else:
                raise exceptions.ValidationError("优惠方式错误.")

        if use_credit > 0:
            if max_use_credit < use_credit:
                raise exceptions.ValidationError("本次使用的抵扣积分数额超过了限制.")

            # 当前订单添加积分抵扣的数量
            order.credit = use_credit
            total_discount_price = float(use_credit / CREDIT_TO_MONEY)

            # todo 扣除用户拥有的积分，后续在订单超时未支付，则返还订单中对应数量的积分给用户。如果订单成功支付，则添加一个积分流水记录。
            user.credit = user.credit - use_credit
            user.save()

        # 一次性批量添加本次下单的商品记录
        OrderDetail.objects.bulk_create(detail_list)

        # 保存订单的总价格和实付价格
        order.total_price = total_price
        order.real_price = float(real_price - total_discount_price)
        order.save()

    def delete_cart(self, redis, user_id, cart_hash):
        # 删除购物车中被勾选的商品，保留没有被勾选的商品信息
        cart_no_selectd = {key: value for key, value in cart_hash.items() if value == b'0'}
        pipe = redis.pipeline()
        pipe.multi()
        # 删除原来的购物车
        pipe.delete(f"cart_{user_id}")
        # 重新把未勾选的商品记录到购物车中
        # hmset不能设置空值
        if cart_no_selectd:
            pipe.hmset(f"cart_{user_id}", cart_no_selectd)
        # hset 在新版本的redis中实际上hmset已经被废弃了，改用hset替代hmset
        pipe.execute()

    def bind_discount_and_order(self, user_coupon, order, user_id, user_coupon_id):
        # 如果有使用了优惠券，则把优惠券和当前订单进行绑定
        if user_coupon:
            user_coupon.order = order
            user_coupon.save()
            # 使用过后，把优惠券从redis中移除
            redis = get_redis_connection("coupon")
            redis.delete(f"{user_id}:{user_coupon_id}")

    def handle_order(self, order):
        # 将来订单状态发生改变，再修改优惠券的使用状态，如果订单过期，则再次还原优惠券到redis中
        order_timeout.apply_async(kwargs={"order_id": order.id}, countdown=ORDER_TIMEOUT)
        # 返回订单超时时间
        order.order_timeout = ORDER_TIMEOUT

    def create(self, validated_data):
        """创建订单"""
        redis = get_redis_connection("cart")
        # 获取数据
        user, user_id, pay_type, user_coupon_id, user_coupon, use_credit = self.get_validated_data(validated_data)
        # 开始事务
        with transaction.atomic():
            # 设置事务回滚的标记点,一个事物中可以设置多个回滚标记
            transaction_start = transaction.savepoint()
            try:
                # 创建订单
                order, cart_hash = self.create_order(redis, user_id, pay_type)
                # 订单折扣和积分优惠
                self.discount_credit(cart_hash, order, user_coupon, use_credit, user)
                # 删除购物车中被勾选的商品，保留没有被勾选的商品信息
                self.delete_cart(redis, user_id, cart_hash)
                # 把优惠券和当前订单进行绑定
                self.bind_discount_and_order(user_coupon, order, user_id, user_coupon_id)
                # 处理订单其余的操作
                self.handle_order(order)
                return order

            except Exception as e:
                log.error(f"订单创建失败：{e}")
                transaction.savepoint_rollback(transaction_start)
                raise exceptions.ValidationError("订单创建失败.")


class OrderDetailMdoelSerializer(serializers.ModelSerializer):
    """订单详情序列化器"""
    # 通过source修改数据源，可以把需要调用的部分外键字段提取到当前序列化器中
    course_id = serializers.IntegerField(source="course.id")
    course_name = serializers.CharField(source="course.name")
    course_cover = serializers.ImageField(source="course.course_cover")

    class Meta:
        model = OrderDetail
        fields = ["id", "price", "real_price", "discount_name", "course_id", "course_name", "course_cover"]


class OrderListModelSerializer(serializers.ModelSerializer):
    """订单列表序列化器"""
    order_courses = OrderDetailMdoelSerializer(many=True)

    class Meta:
        model = Order
        fields = ["id", "order_number", "total_price", "real_price", "pay_time", "created_time", "credit", "coupon",
                  "pay_type", "order_status", "order_courses"]

```

接下来，我们就可以重启Celery即可。运行celery

~~~python
celery -A fsapi worker --pool=solo -l info
~~~

提交代码版本

```bash
feature: 订单状态切换-订单超时处理
```

