import http from "../utils/http";
import {reactive, ref} from "vue"

const cart = reactive({
    course_list: [], // 购物车商品列表
    total_price: 0,  // 购物车中的商品总价格
    selected_course_total: 0, // 购物车中被勾选商品的数量
    checked: false,  // 购物车中是否全选商品了
    // 添加课程到购物车
    add_course_to_cart(course_id, token) {
        return http.post("/cart/", {
            course_id: course_id
        }, {
            // 因为当前课程端添加课程商品到购物车必须登录，所以接口操作时必须发送jwt
            headers: {
                Authorization: "JWT " + token,
            }
        })
    },
    get_course_from_cart(token) {
        // 获取购物车的商品课程列表
        return http.get("/cart/", {
            headers: {
                Authorization: "JWT " + token,
            }
        })
    }
})

export default cart;