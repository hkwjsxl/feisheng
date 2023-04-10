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