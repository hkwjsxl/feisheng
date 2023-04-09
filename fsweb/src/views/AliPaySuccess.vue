<template>
  <div class="success" v-if="order.is_show">
    <Header/>
    <div class="main">
      <div class="title">
        <i class="el-icon-chat-dot-round"></i>
        <div class="success-tips">
          <p class="tips1">您已成功购买 {{ order.course_list?.length }} 门课程！</p>
          <p class="tips2">你还可以加入QQ群 <span>747556033</span> 学习交流</p>
        </div>
      </div>
      <div class="order-info">
        <p class="info1"><b>付款时间：</b><span>{{ order.pay_time }}</span></p>
        <p class="info2"><b>付款金额：</b><span>{{ order.real_price?.toFixed(2) }}</span></p>
        <p class="info3"><b>课程信息：</b>
          <span v-for="course in order.course_list">《{{ course.name }}》</span>
        </p>
      </div>
      <div class="wechat-code">
        <img src="../assets/wechat.jpg" alt="" class="er">
        <p><i class="el-icon-warning"></i>重要！微信扫码关注获得学习通知&amp;课程更新提醒！否则将严重影响学习进度和课程体验！</p>
      </div>
      <div class="study">
        <router-link to="/user/study"><span>立即学习</span></router-link>
      </div>
    </div>
    <Footer/>
  </div>
</template>

<script setup>
import Header from "../components/Header.vue"
import Footer from "../components/Footer.vue"
import {ElMessage} from "element-plus";
import order from "../api/order";
import {useRouter} from "vue-router";

const router = useRouter()

let query_string = location.search; // 获取查询字符串的支付结果参数
order.relay_alipay_result(query_string).then(response => {
  order.is_show = true;
  let result_data = response.data.data;
  console.log("result_data", result_data)
  order.course_list = result_data.course_list;
  order.real_price = result_data.real_price;
  order.pay_time = result_data.pay_time;
}).catch(error => {
  console.log(error)
  ElMessage.error(error.message);
  router.push("/");
})

</script>

<style>
.success {
  padding-top: 80px;
}

.main {
  height: 100%;
  padding-top: 25px;
  padding-bottom: 25px;
  margin: 0 auto;
  width: 1200px;
  background: #fff;
}

.main .title {
  display: flex;
  -ms-flex-align: center;
  align-items: center;
  padding: 25px 40px;
  border-bottom: 1px solid #f2f2f2;
}

.main .title .success-tips {
  box-sizing: border-box;
}

.title img {
  vertical-align: middle;
  width: 60px;
  height: 60px;
  margin-right: 40px;
}

.title .success-tips {
  box-sizing: border-box;
}

.title .tips1 {
  font-size: 22px;
  color: #000;
}

.title .tips2 {
  font-size: 16px;
  color: #4a4a4a;
  letter-spacing: 0;
  text-align: center;
  margin-top: 10px;
}

.title .tips2 span {
  color: #ec6730;
}

.order-info {
  padding: 25px 48px;
  padding-bottom: 15px;
  border-bottom: 1px solid #f2f2f2;
}

.order-info p {
  display: -ms-flexbox;
  display: flex;
  margin-bottom: 10px;
  font-size: 16px;
}

.order-info p b {
  font-weight: 400;
  color: #9d9d9d;
  white-space: nowrap;
}

.wechat-code {
  display: flex;
  -ms-flex-align: center;
  align-items: center;
  padding: 25px 40px;
  border-bottom: 1px solid #f2f2f2;
}

.wechat-code > img {
  width: 180px;
  height: 180px;
  margin-right: 15px;
}

.wechat-code p {
  font-size: 14px;
  color: #d0021b;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
}

.wechat-code p > img {
  width: 16px;
  height: 16px;
  margin-right: 10px;
}

.study {
  padding: 25px 52px;
}

.study span {
  display: block;
  width: 140px;
  height: 42px;
  text-align: center;
  line-height: 42px;
  cursor: pointer;
  background: #ffc210;
  border-radius: 6px;
  font-size: 16px;
  color: #fff;
}

.el-icon-warning {
  font-size: 22px;
  margin-right: 5px;
}

.el-icon-chat-dot-round {
  font-size: 122px;
  margin-right: 10px;
}
</style>