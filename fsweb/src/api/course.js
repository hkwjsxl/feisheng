import http from "../utils/http";
import {reactive, ref} from "vue"


const course = reactive({
    current_direction: 0,  // 当前选中的学习方向，0表示所有方向
    current_category: 0,  // 当前选中的课程分类，0表示不限分类
    direction_list: [],    // 学习方向列表
    category_list: [],    // 课程分类列表
    get_course_direction() {
        // 获取学习方向信息
        return http.get("/course/direction/")
    },
    get_course_category() {
        // 获取课程分类信息
        if (this.current_direction === 0) {
            return http.get('/course/category/')
        } else {
            return http.get(`/course/category/?direction=${this.current_direction}`)
        }
    },
})

export default course;