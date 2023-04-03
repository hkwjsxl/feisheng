import http from "../utils/http";
import {reactive, ref} from "vue"

const cart = reactive({
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
    }
})

export default cart;