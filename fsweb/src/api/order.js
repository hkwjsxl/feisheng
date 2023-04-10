import http from "../utils/http";
import {reactive} from "vue";

const order = reactive({
    total_price: 0,      // 勾选商品的总价格
    discount_price: 0,   // 本次下单的优惠抵扣价格
    discount_type: 0,    // 0表示优惠券，1表示积分
    use_coupon: false,   // 用户是否使用优惠
    coupon_list: [], // 用户拥有的可用优惠券列表
    select: -1,          // 当前用户选中的优惠券下标，-1表示没有选择
    credit: 0,           // 当前用户选择抵扣的积分，0表示没有使用积分
    fixed: true,         // 底部订单总价是否固定浮动
    pay_type: 0,         // 支付方式
    credit_to_money: 0,  // 积分兑换现金的比例
    has_credit: 0,       // 用户拥有的积分
    credit_course_list: [], // 可使用积分抵扣的课程列表
    course_list: [],     // 本次购买的商品课程列表
    real_price: 0,       // 付款金额
    pay_time: undefined, // 付款时间
    is_show: false,      // 是否展示支付成功的内容[接收到支付宝的同步处理结果以后，先把结果转发给后端验证成功以后，才把前端的页面内容展示处理]
    order_number: null,  // 订单号
    loading: false,      // 订单支付时的倒计时背景遮罩层
    timeout: 0,          // 订单支付超时倒计时
    timer: 0,            // 订单支付倒计时定时器的标记符

    order_status: -1,    // 个人中心的默认显示的订单状态选项
    order_status_chioces: [], // 个人中心的订单支付状态选项
    page: 1,                 // 个人中心的订单列表对应的页码
    size: 5,                 // 个人中心的订单列表对应的单页数据量
    order_list: [],           // 个人中心的订单列表
    count: 0,                // 个人中心的订单列表的总数据量


    create_order(user_coupon_id, token) {
        // 生成订单
        return http.post("/order/", {
            pay_type: this.pay_type,
            user_coupon_id,
            credit: this.credit,
        }, {
            headers: {
                Authorization: "jwt " + token,
            }
        })
    },
    get_enable_coupon_list(token) {
        // 获取本次下单的可用优惠券列表
        return http.get("/coupon/enable/", {
            headers: {
                Authorization: "jwt " + token,
            }
        })
    },
    alipay_page_pay(order_number) {
        // 获取订单的支付宝支付链接信息
        return http.get(`/payments/alipay/${order_number}/`)
    },
    relay_alipay_result(query_string) {
        // 把地址栏中的查询字符串(支付成功以后的同步回调通知)转发给服务端
        return http.get(`/payments/alipay/result/${query_string}`)
    },
    query_order(token) {
        // 查询订单支付结果
        return http.get(`/payments/alipay/query/${this.order_number}/`, {
            headers: {
                Authorization: "jwt " + token,
            }
        })
    },
    get_order_status() {
        // 获取订单状态选项
        return http.get('/order/pay/status/')
    },
    get_order_list(token) {
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
    },
    order_cancel(order_id, token) {
        // 取消订单操作
        return http.put(`/order/${order_id}/`, {}, {
            headers: {
                Authorization: "jwt " + token,
            }
        })
    }
})

export default order;