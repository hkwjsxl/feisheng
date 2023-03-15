import http from "../utils/http"
import {reactive, ref} from "vue"

const banner = reactive({
    banner_list: [], // 轮播广告列表
    get_banner_list() {
        // 获取轮播广告
        return http.get("/home/banner/")
    },

})

export default banner;