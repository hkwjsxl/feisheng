<template>
  <div class="cart">
    <Header/>
    <div class="cart-main">
      <div class="cart-header">
        <div class="cart-header-warp">
          <div class="cart-title left">
            <h1 class="left">确认订单</h1>
          </div>
          <div class="right">
            <div class="">
              <span class="left"><router-link class="myorder-history" to="/cart">返回购物车</router-link></span>
            </div>
          </div>
        </div>
      </div>
      <div class="cart-body" id="cartBody">
        <div class="cart-body-title"><p class="item-1 l">课程信息</p></div>
        <div class="cart-body-table">
          <div class="item" v-for="course_info in cart.select_course_list">
            <div class="item-2">
              <router-link :to="`/project/${course_info.id}`" class="img-box l">
                <img :src="settings.host + course_info.course_cover" alt="">
              </router-link>
              <dl class="l has-package">
                <dt>【{{ course_info.course_type }}】 {{ course_info.name }}</dt>
                <p class="package-item" v-if="course_info.discount.type">{{ course_info.discount.type }}</p>
                <p class="package-item" v-if="course_info.credit>0">{{ course_info.credit }}积分抵扣</p>
              </dl>
            </div>
            <div class="item-3">
              <div class="price">
                <p class="discount-price" v-if="course_info.discount.price>=0">
                  <em>￥</em><span>{{ course_info.discount.price.toFixed(2) }}</span></p>
                <p :class="{'original-price': course_info.discount.price>=0}">
                  <em>￥</em><span>{{ course_info.price.toFixed(2) }}</span></p>
              </div>
            </div>
          </div>
        </div>
        <div class="coupons-box">
          <div class="coupon-title-box">
            <p class="coupon-title">
              使用优惠券/积分
              <span v-if="order.use_coupon" @click="order.use_coupon=!order.use_coupon"><svg
                  xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" data-v-394d1fd8=""><path
                  fill="currentColor"
                  d="M831.872 340.864 512 652.672 192.128 340.864a30.592 30.592 0 0 0-42.752 0 29.12 29.12 0 0 0 0 41.6L489.664 714.24a32 32 0 0 0 44.672 0l340.288-331.712a29.12 29.12 0 0 0 0-41.728 30.592 30.592 0 0 0-42.752 0z"></path></svg></span>
              <span v-else @click="order.use_coupon=!order.use_coupon"><svg xmlns="http://www.w3.org/2000/svg"
                                                                            viewBox="0 0 1024 1024" data-v-394d1fd8=""><path
                  fill="currentColor"
                  d="m488.832 344.32-339.84 356.672a32 32 0 0 0 0 44.16l.384.384a29.44 29.44 0 0 0 42.688 0l320-335.872 319.872 335.872a29.44 29.44 0 0 0 42.688 0l.384-.384a32 32 0 0 0 0-44.16L535.168 344.32a32 32 0 0 0-46.336 0z"></path></svg></span>
            </p>
          </div>
          <transition name="el-zoom-in-top">
            <div class="coupon-del-box" v-if="order.use_coupon">
              <div class="coupon-switch-box">
                <div class="switch-btn ticket" :class="{'checked': order.discount_type===0}"
                     @click="order.discount_type=0">优惠券 (4)<em><i class="imv2-check"></i></em></div>
                <div class="switch-btn code" :class="{'checked': order.discount_type===1}"
                     @click="order.discount_type=1">积分<em><i class="imv2-check"></i></em></div>
              </div>
              <div class="coupon-content ticket" v-if="order.discount_type===0">
                <p class="no-coupons" v-if="order.coupon_list.length<1">暂无可用优惠券</p>
                <div class="coupons-box" v-else>
                  <div class="content-box">
                    <ul class="nouse-box">
                      <li class="l" :class="{select: order.select === key}"
                          @click="order.select = (order.select === key?-1:key)"
                          v-for="(coupon,key) in order.coupon_list" :key="key">
                        <div class="detail-box more-del-box">
                          <div class="price-box">
                            <p class="coupon-price l" v-if="coupon.discount === '1'"> ￥{{ Math.abs(coupon.sale) }} </p>
                            <p class="coupon-price l" v-if="coupon.discount === '2'">
                              {{ coupon.sale.replace("*0.", "") }}折 </p>
                            <p class="use-inst l" v-if="coupon.condition>0">满{{ coupon.condition }}元可用</p>
                            <p class="use-inst l" v-else>任意使用</p>
                          </div>
                          <div class="use-detail-box">
                            <div class="use-ajust-box">适用于：{{ coupon.name }}</div>
                            <div class="use-ajust-box">
                              有效期：{{
                                coupon.start_time.split(" ")[0].replaceAll("-", ".")
                              }}-{{ coupon.end_time.split(" ")[0].replaceAll("-", ".") }}
                            </div>
                          </div>
                        </div>
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
              <div class="coupon-content code" v-else>
                <div class="input-box">
                  <el-input-number v-model="order.credit" :step="1" :min="0"
                                   :max="order.max_use_credit"></el-input-number>
                  <a class="convert-btn" @click="conver_credit">兑换</a>
                  <a class="convert-btn" @click="max_conver_credit">最大积分兑换</a>
                </div>
                <div class="converted-box">
                  <p class="course-title" v-for="course in order.credit_course_list">
                    课程:<span class="c_name">{{ course.name }}</span>
                    <span class="discount-cash">{{ course.credit }}积分抵扣：<em>{{
                        (course.credit / order.credit_to_money).toFixed(2)
                      }}</em>元</span>
                  </p>
                </div>
                <p class="error-msg">
                  本次订单最多可以使用{{ order.max_use_credit }}积分，您当前拥有{{ order.has_credit }}积分。({{
                    order.credit_to_money
                  }}积分=1元)</p>
                <p class="tip">说明：每笔订单只能使用一次积分，并只有在部分允许使用积分兑换的课程中才能使用。</p>
              </div>
            </div>
          </transition>
        </div>
        <div class="pay-type">
          <p class="title">选择支付方式</p>
          <div class="list">
            <img :src="order.pay_type===0?'/src/assets/alipay2.png':'/src/assets/alipay1.png'" @click="order.pay_type=0"
                 alt="支付宝">
            <img :src="order.pay_type===1?'/src/assets/wechat2.png':'/src/assets/wechat1.png'" @click="order.pay_type=1"
                 alt="微信">
            <img :src="order.pay_type===2?'/src/assets/yue2.png':'/src/assets/yue1.png'" @click="order.pay_type=2"
                 alt="余额">
          </div>
        </div>
        <div class="pay-box" :class="{fixed:order.fixed}">
          <div class="row-bottom">
            <div class="row">
              <div class="goods-total-price-box">
                <p class="r rw price-num"><em>￥</em><span>{{ cart.total_price.toFixed(2) }}</span></p>
                <p class="r price-text"><span>共<span>{{ cart.select_course_list?.length }}</span>件商品，</span>商品总金额：</p>
              </div>
            </div>
            <div class="coupons-discount-box">
              <p class="r rw price-num">-<em>￥</em><span>{{ order.discount_price.toFixed(2) }}</span></p>
              <p class="r price-text">优惠券/积分抵扣：</p>
            </div>
            <div class="pay-price-box clearfix">
              <p class="r rw price"><em>￥</em><span
                  id="js-pay-price">{{ (cart.total_price - order.discount_price).toFixed(2) }}</span></p>
              <p class="r price-text">应付：</p>
            </div>
            <span class="r btn btn-red submit-btn" @click="commit_order">提交订单</span>
          </div>
          <div class="pay-add-sign">
            <ul class="clearfix">
              <li>支持花呗</li>
              <li>可开发票</li>
              <li class="drawback">7天可退款</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
    <div class="loadding" v-if="order.loading" @click="check_order">
      <div class="box">
        <p class="time">{{ fill0(parseInt(order.timeout / 60)) }}:{{ fill0(order.timeout % 60) }}</p>
        <i class="el-icon-loading"></i><br>
        <p>支付完成！点击关闭当前页面</p>
      </div>
    </div>
    <Footer/>
  </div>
</template>

<script setup>
import {reactive, watch} from "vue"
import Header from "../components/Header.vue"
import Footer from "../components/Footer.vue"
import {useStore} from "vuex";
import cart from "../api/cart"
import order from "../api/order";
import settings from "../settings.js";
import {ElMessage} from "element-plus";
import {useRouter} from "vue-router";
import {fill0} from "../utils/func";

let store = useStore()
let router = useRouter()

const get_select_course = () => {
  // 获取购物车中的勾选商品列表
  let token = sessionStorage.token || localStorage.token;
  cart.get_select_course(token).then(response => {
    cart.select_course_list = response.data.data;
    if (cart.select_course_list.length === 0) {
      ElMessage.error("当前购物车中没有下单的商品！请重新重新选择购物车中要购买的商品~");
      router.back();
    }

    // 计算本次下单的总价格
    let sum = 0
    let credit_course_list = [] // 可使用积分抵扣的课程列表
    let max_use_credit = 0     // 本次下单最多可以用于抵扣的积分
    response.data.data?.forEach((course, key) => {
      if (course.discount.price > 0 || course.discount.price === 0) {
        sum += course.discount.price
      } else {
        sum += course.price
      }

      if (course.credit > 0) {
        max_use_credit = max_use_credit + course.credit
        credit_course_list.push(course)
      }

    })
    cart.total_price = sum;
    order.credit_course_list = credit_course_list
    order.max_use_credit = max_use_credit // 本次下单最多可以用于抵扣的积分
    // 本次订单最多可以使用的积分数量
    // 如果用户积分不足，则最多只能用完自己的积分
    if (order.max_use_credit > order.has_credit) {
      order.max_use_credit = order.has_credit
    }
  }).catch(error => {
    if (error?.response?.status === 400) {
      ElMessage.error("登录超时！请重新登录后再继续操作~");
    }
  })
}

get_select_course();


const commit_order = () => {
  // 生成订单
  let token = sessionStorage.token || localStorage.token

  // 当用户选择了优惠券，则需要获取当前选择的优惠券发放记录的id
  let user_coupon_id = -1;
  if (order.select !== -1) {
    user_coupon_id = order.coupon_list[order.select].user_coupon_id;
  }

  order.create_order(user_coupon_id, token).then(response => {
    if (response.data.code === 500) {
      ElMessage.error("报错了~")
    } else {

      // 支付倒计时提示
      order.order_number = response.data.data.order_number;  // 订单号
      order.loading = true                             // 显示遮罩层
      order.timeout = response.data.data.order_timeout;      // 订单超时的时间，为15分钟
      clearInterval(order.timer)  // 先清除原有定时器，保证整个页面中timer对应的定时器是唯一的。
      order.timer = setInterval(() => {
        if (order.timeout > 1) {
          order.timeout = order.timeout - 1;
        } else {
          ElMessage.error("订单超时！如果您已经支付成功！请点击关闭当前弹窗！当前页面15秒后关闭！");
          clearInterval(order.timer);
          // 发送一个订单查询
          check_order();
          // 关闭页面
          setTimeout(() => {
            // 跳转到用户的订单用心
            router.push("/user/order");
          }, 1500);
        }
      }, 3000);

      // 成功提示
      ElMessage.success("下单成功！马上跳转到支付页面，请稍候~")
      // 扣除掉被下单的商品数量，更新购物车中的商品数量
      store.commit("cart_total", store.state.cart_total - cart.select_course_list.length);
      // 订单生成以后，先扣除临时用户积分
      order.has_credit = order.has_credit - order.credit
      // 根据订单号到服务端获取支付链接，并打开支付页面。
      order.alipay_page_pay(response.data.data.order_number).then(response => {
        window.open(response.data.data.link, "_blank");
      })

    }
  }).catch(error => {
    if (error?.response?.status === 400) {
      ElMessage.success("登录超时！请重新登录后再继续操作~");
    }
  })
}


// 获取本次下单的可用优惠券
const get_enable_coupon_list = () => {
  let token = sessionStorage.token || localStorage.token;
  order.get_enable_coupon_list(token).then(response => {
    order.coupon_list = response.data.data.coupon_list;
    // 获取积分相关信息
    order.credit_to_money = response.data.data.credit_to_money;
    order.has_credit = response.data.data.has_credit;
    // 订单生成后，扣除用户积分
    // order.has_credit = order.has_credit - order.credit;
  })
}
get_enable_coupon_list()

// 积分兑换抵扣
const conver_credit = () => {
  order.discount_price = parseFloat((order.credit / order.credit_to_money).toFixed(2))
}

// 本次下单的最大兑换积分
const max_conver_credit = () => {
  order.credit = order.max_use_credit
  conver_credit();
}


// 查询订单状态
const check_order = () => {
  let token = sessionStorage.token || localStorage.token;
  order.query_order(token).then(response => {
    order.loading = false;
    router.push("/user/order");
  }).catch(error => {
    console.log(error);
    ElMessage.error(error.response.data.errmsg);
  })
}

// 监听用户选择的支付方式
watch(
    () => order.pay_type,
    () => {
      console.log(order.pay_type)
    }
)

// 监听用户选择的优惠券
watch(
    () => order.select,
    () => {
      order.discount_price = 0;
      // 如果没有选择任何的优惠券，则select 为-1，那么不用进行计算优惠券折扣的价格了
      if (order.select === -1) {
        return // 阻止代码继续往下执行
      }

      // 根据下标select，获取当前选中的优惠券信息
      let current_coupon = order.coupon_list[order.select]

      // 针对折扣优惠券，找到最大优惠的课程
      let max_discount = -1;
      for (let course of cart.select_course_list) {  // 循环本次下单的勾选商品
        // 找到当前优惠券的可用课程
        if (current_coupon.enable_course === "__all__") { // 如果当前优惠券是通用优惠券
          if (max_discount !== -1) {
            if (course.price > max_discount.price) {  // 在每次循环中，那当前循环的课程的价格与之前循环中得到的最大优惠课程的价格进行比较
              max_discount = course
            }
          } else {
            max_discount = course
          }
        } else if ((current_coupon.enable_course.indexOf(course.id) > -1) && (course.price >= parseFloat(current_coupon.condition))) {
          // 判断 当前优惠券如果包含了当前课程， 并 课程的价格 > 当前优惠券的使用门槛
          // 只允许没有参与其他优惠券活动的课程使用优惠券，基本所有的平台都不存在折上折的。
          if (course.discount.price === undefined) {
            if (max_discount !== -1) {
              if (course.price > max_discount.price) {
                max_discount = course
              }
            } else {
              max_discount = course
            }
          }
        }
      }

      if (max_discount !== -1) {
        if (current_coupon.discount === '1') { // 抵扣优惠券[抵扣的价格就是当前优惠券的价格]
          order.discount_price = parseFloat(Math.abs(current_coupon.sale))
        } else if (current_coupon.discount === '2') { // 折扣优惠券]抵扣的价格就是(1-折扣百分比) * 课程原价]
          order.discount_price = parseFloat(max_discount.price * (1 - parseFloat(current_coupon.sale.replace("*", ""))))
        }
      } else {
        order.select = -1
        order.discount_price = 0
        ElMessage.error("当前课程商品已经参与了其他优惠活动，无法再次使用当前优惠券！")
      }

    }
)

// 在切换不同的优惠类型，重置积分和优惠券信息
watch(
    () => order.discount_type,
    () => {
      order.select = -1
      order.credit = 0
      order.discount_price = 0
    }
)
// 底部订单总价信息固定浮动效果
window.onscroll = () => {
  let cart_body_table = document.querySelector(".cart-body-table")
  let offsetY = window.scrollY
  console.log("cart_body_table", cart_body_table)
  console.log("offsetY", offsetY)
  let maxY = 0
  if (cart_body_table) {
    maxY = cart_body_table.offsetTop + cart_body_table.offsetHeight;
  }
  order.fixed = offsetY < maxY
}
</script>

<style scoped>
.cart-header {
  height: 160px;
  background-color: #e3e6e9;
  background: url("/src/assets/cart-header-bg.jpeg") repeat-x;
  background-size: 38%;
}

.cart-header .cart-header-warp {
  width: 1500px;
  height: 120px;
  line-height: 120px;
  margin-left: auto;
  margin-right: auto;
  font-size: 14px
}

.cart-header .cart-header-warp .myorder-history {
  font-weight: 200
}

.cart-header .left {
  float: left
}

.cart-header .right {
  float: right
}

.cart-header .cart-title {
  color: #4d555d;
  font-weight: 200;
  font-size: 14px
}

.cart-header .cart-title h1 {
  font-size: 32px;
  line-height: 115px;
  margin-right: 25px;
  color: #07111b;
  font-weight: 200
}

.cart-header .cart-title span {
  margin: 0 4px
}

.l {
  float: left;
}

.r {
  float: right;
}

.cart-body {
  width: 1500px;
  padding: 0 36px 32px;
  background-color: #fff;
  margin-top: -40px;
  margin-left: auto;
  margin-right: auto;
  box-shadow: 0 8px 16px 0 rgba(7, 17, 27, .1);
  border-radius: 8px;
  box-sizing: border-box
}

.cart-body .left {
  float: left !important
}

.cart-body .right {
  float: right !important
}

.cart-body .cart-body-title {
  min-height: 88px;
  line-height: 88px;
  border-bottom: 1px solid #b7bbbf;
  box-sizing: border-box
}

body {
  background: #f8fafc
}

.cart-body .cart-body-title span {
  font-size: 14px
}

.cart-body .cart-body-title .item-1 > span,
.cart-body .cart-body-title .item-2 > span,
.cart-body .cart-body-title .item-3 > span {
  display: inline-block;
  font-size: 14px;
  line-height: 24px;
  color: #4d555d
}

.cart-body .cart-body-title .item-1 > span {
  color: #93999f
}

.cart-body .cart-body-title .item-2 > span {
  margin-left: 40px
}

.cart-body .item {
  height: 88px;
  padding: 24px 0;
  background: #f3f5f7;
}

.cart-body .cart-body-table {
  padding-bottom: 36px;
  border-bottom: 1px solid #d9dde1;
}

.cart-body .item > div {
  float: left
}

.cart-body .item .item-1 {
  padding-top: 34px;
  position: relative;
  z-index: 1
}

.cart-body .item:last-child > .item-1::after {
  display: none
}

.cart-body .item-1 {
  width: 120px
}

.cart-body .item-1 i {
  margin-left: 12px;
  margin-right: 8px;
  font-size: 24px
}

.cart-body .item-2 {
  width: 1020px;
  position: relative;
}

.cart-body .item-2 > span {
  line-height: 88px;
}

.cart-body .item-2 dl {
  width: 464px;
  margin-left: 24px;
  padding-top: 12px
}

.cart-body .item-2 dl a {
  display: block;
}

.cart-body .item-2 dl.has-package {
  padding-top: 4px;
}

.cart-body .item-2 dl.has-package .package-item {
  display: inline-block;
  padding: 0 12px;
  margin-top: 4px;
  font-size: 12px;
  color: rgba(240, 20, 20, .6);
  line-height: 24px;
  background: rgba(240, 20, 20, .08);
  border-radius: 12px;
  cursor: pointer
}

.cart-body .item-2 dl.has-package .package-item:hover {
  color: #fff;
  background: rgba(240, 20, 20, .2)
}

.cart-body .item-2 dt {
  font-size: 16px;
  color: #07111b;
  line-height: 24px;
  margin-bottom: 4px
}

.cart-body .item-2 .img-box {
  display: block;
  margin-left: 42px;
}

.cart-body .item-2 .img-box img {
  height: 94px;
}

.cart-body .item-2 dd {
  font-size: 12px;
  color: #93999f;
  line-height: 24px;
  font-weight: 200
}

.cart-body .item-2 dd a {
  display: inline-block;
  margin-left: 12px;
  color: rgba(240, 20, 20, .4)
}

.cart-body .item-2 dd a:hover {
  color: #f01414
}

.cart-body .item-3 {
  width: 280px;
  margin-left: 48px;
  position: relative;
}

.cart-body .item-3 .price {
  display: inline-block;
  height: 46px;
  width: 96px;
  padding-top: 24px;
  padding-bottom: 24px;
  color: #f01414;
}

.cart-body .item-3 .price em,
.cart-body .item-3 .price span {
  font-size: 18px;
}

.cart-body .item-3 .price .original-price em,
.cart-body .item-3 .price .original-price span {
  font-size: 15px;
  color: #aaa;
  text-decoration: line-through;
}

.cart-body .cart-body-bot li {
  float: left
}

.cart-body .cart-body-bot .li-1 em,
.cart-body .cart-body-bot .li-3 em {
  font-style: normal;
  color: red
}

.cart-body .cart-body-bot .li-2 .price {
  font-size: 16px;
  color: #f01414;
  line-height: 24px;
  font-weight: 700
}

.coupons-box::after {
  display: block;
  content: "";
  overflow: hidden;
  clear: both;
}

.coupons-box .coupon-title-box {
  margin: 27px 0 0 12px
}

.coupons-box .coupon-title-box .coupon-title {
  color: #07111b;
  font-size: 16px;
  line-height: 34px
}

.coupons-box .coupon-title-box .coupon-title svg {
  position: relative;
  width: 26px;
  height: 26px;
  top: 5px;
  margin-left: 12px;
  font-size: 24px;
  color: #999;
  cursor: pointer
}


.coupons-box .coupon-del-box {
  width: 100%;
  padding-top: 24px;
  box-sizing: border-box
}

.coupons-box .coupon-del-box .coupon-switch-box {
  margin-bottom: 16px
}

.coupons-box .coupon-del-box .coupon-switch-box .switch-btn {
  position: relative;
  display: inline-block;
  width: 138px;
  height: 58px;
  line-height: 20px;
  border: 1px solid #d9dde1;
  border-radius: 8px;
  padding: 18px 0;
  color: #1c1f21;
  text-align: center;
  font-size: 16px;
  margin-right: 16px;
  box-sizing: border-box;
  cursor: pointer
}

.coupons-box .coupon-del-box .coupon-switch-box .switch-btn em {
  display: none;
  position: absolute;
  bottom: 0;
  right: 0;
  width: 0;
  height: 0;
  line-height: 54px;
  border-left-width: 20px;
  border-left-style: solid;
  border-left-color: transparent;
  border-bottom-width: 20px;
  border-bottom-style: solid;
  border-bottom-color: #f01414
}

.coupons-box .coupon-del-box .coupon-switch-box .switch-btn em i {
  color: #fff;
  position: absolute;
  bottom: -20px;
  right: 0;
  font-size: 12px
}

.coupons-box .coupon-del-box .coupon-switch-box .switch-btn.checked {
  border: 2px solid #f01414
}

.coupons-box .coupon-del-box .coupon-switch-box .switch-btn.checked em {
  display: block
}

.coupons-box .coupon-del-box .coupon-content {
  position: relative;
  background: #f3f5f7;
  border-radius: 8px;
  padding: 24px
}

.coupons-box .coupon-del-box .coupon-content:before {
  content: "";
  display: block;
  position: absolute;
  top: -7px;
  left: 62px;
  border-left: 12px solid transparent;
  border-right: 12px solid transparent;
  border-bottom: 7px solid #f3f5f7
}

.coupons-box .coupon-del-box .coupon-content.ticket li {
  padding-top: 8px;
  box-sizing: border-box;
  width: 320px;
  background-color: #fff6f0;
  cursor: pointer;
  margin: 12px
}

.coupons-box .coupon-del-box .coupon-content.ticket li .more-del-box {
  padding: 16px 22px 24px 22px;
  width: 100%;
  box-sizing: border-box;
  background-repeat: no-repeat
}

.coupons-box .coupon-del-box .coupon-content.ticket li .price-box {
  height: 32px;
  line-height: 32px
}

.coupons-box .coupon-del-box .coupon-content.ticket li .price-box .price {
  font-size: 30px;
  margin-right: 4px
}

.coupons-box .coupon-del-box .coupon-content.ticket li .price-box .price sub {
  font-size: 24px;
  letter-spacing: -5px
}

.coupons-box .coupon-del-box .coupon-content.ticket li .price-box .use-inst {
  font-size: 12px;
  margin-top: 5px;
}

.coupons-box .coupon-del-box .coupon-content.ticket .active .price,
.coupons-box .coupon-del-box .coupon-content.ticket .active .use-inst {
  color: #fff
}

.coupons-box .coupon-del-box .coupon-content.ticket .active i {
  position: absolute;
  top: 12px;
  right: 12px;
  color: #fff;
  font-size: 24px
}

.coupons-box .coupon-del-box .coupon-content.ticket .no-coupons {
  font-size: 14px;
  color: #4d555d;
  line-height: 14px
}

.coupons-box .coupon-del-box .coupon-content.code {
  padding-left: 38px
}

.coupons-box .coupon-del-box .coupon-content.code:before {
  left: 216px
}

.coupons-box .coupon-del-box .coupon-content.code .input-box {
  position: relative;
  left: -12px;
  margin-top: 12px
}

.coupons-box .coupon-del-box .coupon-content.code .input-box .convert-input {
  background: #fff;
  border: 1px solid #9199a1;
  width: 356px;
  height: 48px;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 600;
  color: #07111b;
  letter-spacing: 2px;
  line-height: 24px;
  padding: 12px 16px;
  box-sizing: border-box;
  vertical-align: middle
}

.coupons-box .coupon-del-box .coupon-content.code .input-box .convert-btn {
  display: inline-block;
  width: 124px;
  height: 48px;
  line-height: 22px;
  font-size: 16px;
  color: #fff;
  padding: 12px;
  background: #f01414;
  border-radius: 8px;
  margin-left: 24px;
  box-sizing: border-box;
  text-align: center;
  cursor: pointer
}

.coupons-box .coupon-del-box .coupon-content.code .converted-box p {
  line-height: 24px;
  font-size: 16px;
  color: #07111b;
  margin-top: 10px;
}

.coupons-box .coupon-del-box .coupon-content.code .converted-box .c_name,
.coupons-box .coupon-del-box .coupon-content.code .converted-box .code-num {
  padding-left: 8px
}

.coupons-box .coupon-del-box .coupon-content.code .converted-box .cancel-btn {
  background: #fff;
  border: 1px solid #d9dde1;
  line-height: 20px;
  padding: 2px 12px;
  text-align: center;
  border-radius: 4px;
  color: #f01414;
  font-size: 14px;
  margin-left: 16px;
  cursor: pointer
}

.coupons-box .coupon-del-box .coupon-content.code .converted-box .course-title {
  font-size: 14px;
  color: #07111b;
  font-weight: 600;
  margin-top: 12px
}

.coupons-box .coupon-del-box .coupon-content.code .converted-box .course-title .discount-cash {
  margin-left: 12px;
  color: #f01414
}

.coupons-box .coupon-del-box .coupon-content.code .error-msg {
  font-size: 14px;
  color: #f01414;
  margin-top: 8px;
  line-height: 20px;
  height: 20px
}

.coupons-box .coupon-del-box .coupon-content.code .tip {
  font-size: 14px;
  color: #93999f;
  margin-top: 8px;
  line-height: 20px
}


.coupons-box .content-box ul {
  width: 100%
}

.coupons-box .content-box .nouse-box::after,
.coupons-box .content-box .overdue-box::after,
.coupons-box .content-box .use-box::after {
  display: block;
  content: "";
  overflow: hidden;
  clear: both;
}

.coupons-box .content-box .nouse-box li,
.coupons-box .content-box .overdue-box li,
.coupons-box .content-box .use-box li {
  position: relative;
  padding: 24px 32px;
  margin-right: 16px;
  margin-bottom: 16px;
  width: 320px;
  height: 144px;
  border-radius: 8px;
  box-sizing: border-box;
  background-color: #fff;
  box-shadow: 0 8px 16px 0 rgba(7, 17, 27, .2);
  background-repeat: no-repeat;
  background-size: 320px 144px;
}

.coupons-box .content-box .nouse-box li.select {
  background-color: orangered;
}

.coupons-box .content-box .nouse-box li .detail-box,
.coupons-box .content-box .overdue-box li .detail-box,
.coupons-box .content-box .use-box li .detail-box {
  width: 100%;
  height: 100%
}

.coupons-box .content-box .nouse-box li .detail-box .price-box,
.coupons-box .content-box .overdue-box li .detail-box .price-box,
.coupons-box .content-box .use-box li .detail-box .price-box {
  margin-bottom: 8px;
  height: 40px;
  color: #93999f;
  line-height: 40px;
  font-weight: 700
}

.coupons-box .content-box .nouse-box li .detail-box .price-box .coupon-price,
.coupons-box .content-box .overdue-box li .detail-box .price-box .coupon-price,
.coupons-box .content-box .use-box li .detail-box .price-box .coupon-price {
  margin-right: 12px;
  font-size: 36px;
  margin-top: 5px;
}

.coupons-box .content-box .nouse-box li .detail-box .price-box .use-inst,
.coupons-box .content-box .overdue-box li .detail-box .price-box .use-inst,
.coupons-box .content-box .use-box li .detail-box .price-box .use-inst {
  font-size: 14px
}

.coupons-box .content-box .nouse-box li .detail-box .use-detail-box,
.coupons-box .content-box .overdue-box li .detail-box .use-detail-box,
.coupons-box .content-box .use-box li .detail-box .use-detail-box {
  font-size: 12px;
  color: #93999f;
  line-height: 24px
}

.coupons-box .content-box .nouse-box li .detail-box .use-detail-box .use-ajust-box,
.coupons-box .content-box .overdue-box li .detail-box .use-detail-box .use-ajust-box,
.coupons-box .content-box .use-box li .detail-box .use-detail-box .use-ajust-box {
  position: relative
}

.coupons-box .content-box .nouse-box li .detail-box .use-detail-box .use-ajust-box i,
.coupons-box .content-box .overdue-box li .detail-box .use-detail-box .use-ajust-box i,
.coupons-box .content-box .use-box li .detail-box .use-detail-box .use-ajust-box i {
  position: relative;
  top: 3px;
  left: 0;
  font-size: 16px;
  color: #93999f;
  line-height: 24px;
  cursor: pointer
}

.coupons-box .content-box .nouse-box li .detail-box .use-detail-box .use-ajust-box .use-course a,
.coupons-box .content-box .overdue-box li .detail-box .use-detail-box .use-ajust-box .use-course a,
.coupons-box .content-box .use-box li .detail-box .use-detail-box .use-ajust-box .use-course a {
  padding: 16px 0;
  width: 100%;
  display: block;
  font-size: 12px;
  color: #4d555d;
  line-height: 20px;
  border-bottom: 1px solid #d9dde1;
  box-sizing: border-box
}

.coupons-box .content-box .nouse-box li .detail-box .use-detail-box .use-ajust-box .use-course a:hover,
.coupons-box .content-box .overdue-box li .detail-box .use-detail-box .use-ajust-box .use-course a:hover,
.coupons-box .content-box .use-box li .detail-box .use-detail-box .use-ajust-box .use-course a:hover {
  color: #07111b
}

.coupons-box .content-box .nouse-box li .detail-box .use-detail-box .use-ajust-box .use-course a:last-child,
.coupons-box .content-box .overdue-box li .detail-box .use-detail-box .use-ajust-box .use-course a:last-child,
.coupons-box .content-box .use-box li .detail-box .use-detail-box .use-ajust-box .use-course a:last-child {
  border-bottom: none
}

.coupons-box .content-box li {
  background-image: url(/src/assets/coupons_bg.png)
}

.coupons-box .content-box .nouse-box li .detail-box .price-box .coupon-price {
  color: #f01414
}

.coupons-box .content-box .nouse-box li .detail-box .price-box .use-inst {
  color: #f01414
}

.coupons-box .content-box .nouse-box li .detail-box .use-detail-box {
  color: #07111b
}

.coupons-box .content-box .nouse-box li .detail-box .use-detail-box .use-ajust-box i {
  color: #4d555d
}

.coupons-box .content-box .nouse-box li.wait-use {
  background-image: url(/src/assets/coupon_start_bg.png)
}

.coupons-box .content-box .use-box li {
  background-image: url(/src/assets/coupons_used_bg.png)
}

.coupons-box .content-box .use-box li.useing {
  background-image: url(/src/assets/coupon_useing_bg.png)
}

.coupons-box .content-box .overdue-box li {
  background-image: url(/src/assets/coupons_overdue.png)
}

.tip-box ol {
  margin-top: 16px;
  width: 100%;
  list-style: decimal;
  margin-left: 14px;
  box-sizing: border-box
}

.tip-box ol li {
  font-size: 12px
}

.pay-box {
  margin-top: 36px;
  position: relative
}

.pay-box::after,
.goods-total-price-box::after,
.package-discount-box::after,
.pay-price-box::after,
.coupons-discount-box::after {
  display: block;
  content: "";
  clear: both;
  overflow: hidden;
}

.pay-box .rw {
  width: 140px;
  box-sizing: border-box;
  text-align: right
}

.pay-box .bargain-discount-box, .pay-box .coupons-discount-box, .pay-box .goods-total-price-box, .pay-box .package-discount-box, .pay-box .redpackage-discount-box, .pay-box .student-discount-box {
  margin-bottom: 12px;
  line-height: 26px
}

.pay-box .bargain-discount-box .price-num, .pay-box .coupons-discount-box .price-num, .pay-box .goods-total-price-box .price-num, .pay-box .package-discount-box .price-num, .pay-box .redpackage-discount-box .price-num, .pay-box .student-discount-box .price-num {
  position: relative;
  font-size: 14px;
  color: #07111b
}

.pay-box .bargain-discount-box .price-text, .pay-box .coupons-discount-box .price-text, .pay-box .goods-total-price-box .price-text, .pay-box .package-discount-box .price-text, .pay-box .redpackage-discount-box .price-text, .pay-box .student-discount-box .price-text {
  text-align: right;
  font-size: 14px;
  color: #07111b
}

.pay-box .bargain-discount-box .price-text span, .pay-box .coupons-discount-box .price-text span, .pay-box .goods-total-price-box .price-text span, .pay-box .package-discount-box .price-text span, .pay-box .redpackage-discount-box .price-text span, .pay-box .student-discount-box .price-text span {
  margin-left: 4px;
  margin-right: 4px
}

.pay-box .pay-add-sign {
  text-align: right;
  position: absolute;
  top: -10px
}

.pay-box .pay-add-sign li {
  float: left;
  padding: 0 12px;
  height: 26px;
  line-height: 26px;
  border: 1px solid #f01414;
  border-radius: 18px;
  font-size: 12px;
  color: #f01414;
  margin-right: 15px
}

.pay-box .pay-add-sign li.drawback {
  position: relative
}

.pay-box .pay-add-sign li.drawback .imv2-ques {
  position: absolute;
  top: -4px;
  right: -2px;
  background: #fff;
  color: #d7dbdf;
  font-size: 14px;
  display: inline-block;
  width: 14px;
  height: 14px;
  cursor: pointer
}

.pay-box .pay-add-sign li.drawback .imv2-ques:hover {
  color: #f20d0d
}

.pay-box .pay-add-sign a.checkbackbtn {
  display: none;
  color: #fff;
  font-size: 12px;
  text-align: center;
  border-radius: 8px;
  vertical-align: top;
  position: absolute;
  left: 100%;
  top: -12px;
  background: rgba(28, 31, 33, .25);
  width: 100px;
  height: 26px;
  line-height: 26px;
  margin-left: 8px
}

.pay-box .pay-add-sign a.checkbackbtn i.arrow {
  width: 0;
  height: 0;
  border-top: 5px solid transparent;
  border-right: 5px solid;
  border-bottom: 5px solid transparent;
  position: absolute;
  left: -5px;
  top: 8px;
  border-right-color: rgba(28, 31, 33, .25)
}

.pay-box .pay-price-box {
  color: #07111b
}

.pay-box .pay-price-box .price {
  position: relative;
  color: #f01414;
  font-size: 24px;
  font-weight: 700;
  line-height: 36px;
  height: 36px;
}

.pay-box .pay-price-box .price-text {
  line-height: 36px;
  height: 36px;
}

.pay-box .pay-price-box .price span {
  float: none;
  font-weight: 700
}

.pay-box .pay-account {
  font-size: 12px;
  color: #93999f;
  line-height: 24px;
  margin-bottom: 20px;
  margin-top: 15px
}

.pay-box .submit-btn {
  padding: 0;
  width: 140px;
  height: 40px;
  margin-top: 12px;
  text-align: center;
  font-size: 14px;
  line-height: 40px;
  border-radius: 24px
}

.pay-box .disabled {
  background: #ccc;
  cursor: not-allowed;
  border: none
}

.pay-box .presale-wrap {
  text-align: right
}

.pay-box .presale-wrap .submit-btn {
  margin-top: 24px
}

.pay-box .presale-box {
  display: inline-block;
  font-size: 0;
  text-align: left
}

.pay-box .presale-box .step {
  width: 213px;
  padding-bottom: 10px;
  position: relative
}

.pay-box .presale-box .step .title {
  font-size: 14px;
  color: #07111b;
  line-height: 26px
}

.pay-box .presale-box .step .title .price {
  color: #93999f;
  float: right
}

.pay-box .presale-box .step .title .price.active {
  color: #f01414
}

.pay-box .presale-box .step .desc {
  font-size: 12px;
  color: #93999f;
  line-height: 16px
}

.pay-box .presale-box .step:nth-child(3) .price {
  color: #f01414;
  font-size: 24px;
  font-weight: 700
}

.pay-box .presale-box .step .step-line {
  position: absolute;
  top: 8px;
  left: -16px;
  width: 9px;
  display: flex;
  flex-direction: column;
  align-items: center
}

.pay-box .presale-box .step .step-line .circle {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: rgba(147, 153, 159, .3)
}

.pay-box .presale-box .step .step-line .circle.active {
  background: #f01414
}

.pay-box .presale-box .step .step-line .line {
  height: 43px;
  border-left: 1px dashed rgba(147, 153, 159, .3)
}

.pay-box .presale-box .step .step-line .line.short {
  height: 27px
}

.pay-box.fixed {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 80px;
  line-height: 80px;
  background-color: #fff;
  z-index: 300;
  box-shadow: 10px -2px 12px rgba(7, 17, 27, .2);
  padding-top: 10px;
}

.pay-box.fixed .row-bottom {
  max-width: 1500px;
  position: relative;
  margin: 0 auto;
}

.pay-box.fixed .row-bottom .row {
  float: left
}

.pay-box.fixed .row-bottom .bargain-discount-box, .pay-box.fixed .row-bottom .coupons-discount-box, .pay-box.fixed .row-bottom .js-total-hide, .pay-box.fixed .row-bottom .package-discount-box {
  display: none
}

.pay-box.fixed .bargain-discount-box, .pay-box.fixed .coupons-discount-box, .pay-box.fixed .goods-total-price-box, .pay-box.fixed .package-discount-box, .pay-box.fixed .pay-add-sign, .pay-box.fixed .pay-price-box, .pay-box.fixed .redpackage-discount-box {
  float: left;
  margin-bottom: 0
}

.pay-box.fixed .coupons-discount-box, .pay-box.fixed .package-discount-box, .pay-box.fixed .redpackage-discount-box {
  margin-left: 20px
}

.pay-box.fixed .goods-total-price-box {
  width: auto
}

.pay-box.fixed .rw {
  text-align: left;
  width: auto
}

.pay-box.fixed .price, .pay-box.fixed .price-num, .pay-box.fixed .price-text {
  line-height: 80px
}

.pay-box.fixed .pay-add-sign {
  position: static !important;
  margin-left: 20px
}

.pay-box.fixed .pay-add-sign li {
  float: left;
  padding: 0 12px;
  height: 26px;
  line-height: 26px;
  border: 1px solid #f01414;
  border-radius: 18px;
  font-size: 12px;
  color: #f01414;
  margin: 27px 20px 27px 0
}

.pay-box.fixed .pay-price-box {
  width: auto;
  margin-left: 20px
}

.pay-box.fixed .submit-btn {
  margin-top: 16px;
  width: 148px;
  height: 48px;
  line-height: 48px;
  font-size: 16px;
  border-radius: 24px
}

.pay-box.fixed .presale-wrap {
  float: left;
  text-align: left
}

.pay-box.fixed .presale-wrap .presale-box {
  height: 80px;
  display: flex;
  align-items: center
}

.pay-box.fixed .presale-wrap .presale-box .step {
  padding-right: 38px;
  padding-bottom: 0;
  width: auto;
  min-width: 118px;
  height: 45px
}

.pay-box.fixed .presale-wrap .presale-box .step:nth-child(3) {
  height: auto
}

.pay-box.fixed .presale-wrap .presale-box .step .title {
  float: none;
  background: #fff
}

.pay-box.fixed .presale-wrap .presale-box .step .title .price {
  line-height: 26px;
  float: none
}

.pay-box.fixed .presale-wrap .presale-box .step .step-line {
  flex-direction: row;
  width: 100%;
  left: -14px
}

.pay-box.fixed .presale-wrap .presale-box .step .step-line .line {
  border-left: none;
  border-top: 1px dashed rgba(147, 153, 159, .3);
  width: 30px;
  height: 1px;
  position: absolute;
  right: 5px
}

.pay-box.fixed .presale-wrap .presale-box .step .step-line .circle:nth-child(3) {
  position: absolute;
  right: -10px
}

.btn {
  position: relative;
  display: inline-block;
  margin-bottom: 0;
  text-align: center;
  vertical-align: middle;
  touch-action: manipulation;
  text-decoration: none;
  box-sizing: border-box;
  background-image: none;
  -webkit-appearance: none;
  white-space: nowrap;
  outline: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  border-style: solid;
  border-width: 1px;
  cursor: pointer;
  transition: all .3s;
  color: #545c63;
  background-color: transparent;
  border-color: #9199a1;
  opacity: 1;
  padding: 7px 16px;
  font-size: 14px;
  line-height: 1.42857143;
  border-radius: 18px;
}

.btn-red {
  border-style: solid;
  border-width: 1px;
  cursor: pointer;
  -moz-transition: all .3s;
  transition: all .3s;
  color: #fff;
  background-color: #f20d0d;
  border-color: #f20d0d;
  opacity: 1;
}

.btn-red:hover {
  color: #fff;
  border-color: #c20a0a;
  background: #c20a0a;
  opacity: 1;
}

.pay-type {
  margin-top: 28px;
  margin-left: 12px;
}

.pay-type .title {
  margin-top: 28px;
}

.pay-type .list {
  padding-top: 20px;
}

.pay-type .list img {
  margin-right: 10px;
}

.loadding {
  width: 100%;
  height: 100%;
  margin: auto;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 999;
  background-color: rgba(0, 0, 0, .7);
}

.box {
  width: 300px;
  height: 150px;
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  margin: auto;
  font-size: 40px;
  text-align: center;
  padding-top: 50px;
  color: #fff;
}

.box .time {
  font-size: 22px;
}

</style>