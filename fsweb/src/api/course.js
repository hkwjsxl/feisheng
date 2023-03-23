import http from "../utils/http";
import {reactive, ref} from "vue"


const course = reactive({
    current_direction: 0,  // 当前选中的学习方向，0表示所有方向
    current_category: 0,  // 当前选中的课程分类，0表示不限分类
    direction_list: [],    // 学习方向列表
    category_list: [],    // 课程分类列表
    course_list: [],       // 课程列表数据
    ordering: "-id",       // 课程排序条件
    page: 1,               // 当前页码，默认为1
    size: 5,               // 当前页数据量
    count: 0,         // 课程信息列表的数量
    has_perv: false,  // 是否有上一页
    has_next: false,  // 是否有下一页
    timer: null,      // 课程相关数据的定时器
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
    get_course_list() {
        let params = {
            page: this.page,
            size: this.size,
        }
        if (this.ordering) {
            params.ordering = this.ordering;
        }
        // 方向和分类都为全部时获取全部的课程列表
        if (this.current_direction === 0 && this.current_category === 0) {
            return http.get(`/course/`, {
                params
            })
        }
        // 方向未动，直接点击分类时发出请求
        if (this.current_direction === 0 && this.current_category !== 0) {
            return http.get(`/course/?category=${this.current_category}`, {
                params
            })
        }
        // 分类为全部时发出请求
        if (this.current_category === 0) {
            return http.get(`/course/?direction=${this.current_direction}`, {
                params
            })
        }
        // 获取课程列表信息
        return http.get(`/course/?direction=${this.current_direction}&category=${this.current_category}`, {
            params
        })
    },
    start_timer() {
        // 课程相关的优惠活动倒计时
        clearInterval(this.timer); // 保证整个页面只有一个倒计时对优惠活动的倒计时进行时间
        this.timer = setInterval(() => {
            this.course_list.forEach((course) => {
                // js的对象和python里面的字典/列表一样， 是属于引用类型的。所以修改了成员的值也会影响自身的。
                if (course.discount.expire && course.discount.expire > 0) {
                    // 时间不断自减
                    course.discount.expire--
                }
            })
        }, 1000)
    }
})

export default course;