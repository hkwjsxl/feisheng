<template>
  <div class="cart">
    <Header/>
    <div class="cart-main">
      <div class="cart-header">
        <div class="cart-header-warp">
          <div class="cart-title left">
            <h1 class="left">我的购物车</h1>
            <div class="left">
              共<span>5</span>门，已选择<span>5</span>门
            </div>
          </div>
          <div class="right">
            <div class="">
              <span class="left"><router-link class="myorder-history" to="/myorder">我的订单列表</router-link></span>
            </div>
          </div>
        </div>
      </div>
      <div class="cart-body" id="cartBody">
        <div class="cart-body-title">
          <div class="item-1 l">
            <el-checkbox v-model="state.checked">全选</el-checkbox>
          </div>
          <div class="item-2 l"><span class="course">课程</span></div>
          <div class="item-3 l"><span>金额</span></div>
          <div class="item-4 l"><span>操作</span></div>
        </div>
        <div class="cart-body-table">
          <div class="item">
            <div class="item-1">
              <el-checkbox v-model="state.checked"></el-checkbox>
            </div>
            <div class="item-2">
              <a href="" class="img-box l">
                <img src="/src/assets/course-7.png">
              </a>
              <dl class="l has-package">
                <dt>【实战课 移动端UI设置入门与实战</dt>
                <p class="package-item">优惠价</p>
              </dl>
            </div>

            <div class="item-3">
              <div class="price">
                <span class="discount-price"><em>￥</em><span>588.00</span></span><br>
                <span class="original-price"><em>￥</em><span>1988.00</span></span>
              </div>
            </div>
            <div class="item-4">
              <el-icon :size="26" class="close">
                <Close/>
              </el-icon>
            </div>
          </div>
          <div class="item">
            <div class="item-1">
              <el-checkbox v-model="state.checked"></el-checkbox>
            </div>
            <div class="item-2">
              <a href="" class="img-box l"><img src="/src/assets/course-1.png"></a>
              <dl class="l has-package">
                <dt>【实战课】算法与数据结构</dt>
                <p class="package-item">限时优惠</p>
              </dl>
            </div>
            <div class="item-3">
              <div class="price"><em>￥</em><span>299.00</span></div>
            </div>
            <div class="item-4">
              <el-icon :size="26" class="close">
                <Close/>
              </el-icon>
            </div>
          </div>
          <div class="cart-body-bot fixed">
            <div class=" cart-body-bot-box">
              <div class="right">
                <div class="add-coupon-box">
                  <div class="li-left">
                    <div class="li-2">
                      <span class="topdiv w70">总计金额：</span>
                      <span class="price price-red w100">
                        <em>￥</em>
                        <span>1751.00</span>
                      </span>
                    </div>
                  </div>
                  <div class="li-3"><span class="btn">去结算</span></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <Footer/>
  </div>
</template>

<script setup>
import {Close} from '@element-plus/icons-vue'
import {reactive} from "vue"
import Header from "../components/Header.vue"
import Footer from "../components/Footer.vue"
import {} from "../api/cart"
import {ElMessage} from 'element-plus'

let state = reactive({
  checked: false,
})
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

.cart-header .cart-title .js-number-box-cart {
  line-height: 115px
}

.cart-header .num {
  display: none;
  padding: 4px 5px;
  background-color: #f01414;
  color: #fff;
  border-radius: 50%;
  text-align: center;
  font-size: 12px;
  line-height: 10px;
  margin-top: 51px;
  margin-left: 5px
}

.l {
  float: left;
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

.cart-body .priceprice i {
  float: left
}

body {
  background: #f8fafc
}

.cart-body .cart-body-title span {
  font-size: 14px
}

.cart-body .cart-body-title .item-1 > span,
.cart-body .cart-body-title .item-2 > span,
.cart-body .cart-body-title .item-3 > span,
.cart-body .cart-body-title .item-4 > span {
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

.cart-body .cart-body-title .item-2 .course {
  line-height: 88px;
}

.cart-body .cart-body-title .item-4 > span {
  margin-right: 32px
}

.cart-body .cart-body-table .title .title-content span {
  margin-right: 9px;
  position: relative
}

.cart-body .cart-body-table .title .title-content span::after {
  content: "/";
  position: absolute;
  right: -9px
}

.cart-body .cart-body-table .title .title-content span:last-child::after {
  content: ''
}

.cart-body .item {
  height: 88px;
  padding: 24px 0;
  border-bottom: 1px solid #d9dde1
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

.cart-body .item.disabled .price, .cart-body .item.disabled dt {
  color: #93999f !important
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
  width: 820px;
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
  color: #1c1f21;
  height: 46px;
  width: 96px;
  padding-top: 24px;
  padding-bottom: 24px;
  font-size: 18px;
}

.cart-body .item-3 .price .original-price {
  color: #aaa;
  text-decoration: line-through;
}

.cart-body .item-4 {
  margin-left: 74px;
}

.cart-body .item-4 .close {
  font-size: 40px;
  height: 90px;
  color: #b7bbbf;
  line-height: 90px;
  cursor: pointer
}

.cart-body .item-4 .close:hover {
  color: #ff0000;
}

.cart-body .cart-body-bot.fixed {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  background-color: #fff;
  z-index: 300;
  box-shadow: 10px -2px 12px rgba(7, 17, 27, .2)
}

.cart-body .cart-body-bot.fixed .cart-body-bot-box {
  padding-bottom: 70px;
  width: 1500px;
  height: 20px;
  padding-top: 40px;
}

.cart-body .cart-body-bot.fixed .cart-body-bot-box .li-3 {
  margin-right: 36px
}

.cart-body .cart-body-bot .cart-body-bot-box {
  margin-left: auto;
  margin-right: auto;
  display: block;
  padding-top: 24px
}

.cart-body .cart-body-bot .cart-body-bot-box .add-coupon-box {
  display: flex;
  flex-direction: row;
  align-items: center
}

.cart-body .cart-body-bot li {
  float: left
}

.cart-body .cart-body-bot .li-left {
  text-align: right
}

.cart-body .cart-body-bot .li-3 {
  font-size: 12px;
  color: #07111b;
  line-height: 24px
}

.cart-body .cart-body-bot .li-1 em, .cart-body .cart-body-bot .li-3 em {
  font-style: normal;
  color: red
}

.cart-body .cart-body-bot .li-2 {
  font-size: 0
}

.cart-body .cart-body-bot .li-2 .topdiv {
  font-size: 14px;
  color: #07111b;
  line-height: 28px
}

.cart-body .cart-body-bot .li-2 .price {
  font-size: 16px;
  color: #f01414;
  line-height: 24px;
  font-weight: 700
}

.cart-body .cart-body-bot .li-3 .btn {
  margin-left: 38px;
  float: right;
  padding: 13px 32px;
  color: #fff;
  font-size: 16px;
  color: #fff;
  cursor: pointer;
  font-weight: 200;
  background: #f01414;
  border-radius: 4px
}

.cart-body .cart-body-bot .w70 {
  display: inline-block;
  width: 120px;
  text-align: right
}

.cart-body .cart-body-bot .w100 {
  display: inline-block;
  width: 100px;
  text-align: right
}
</style>