import http from "../utils/http"
import {reactive, ref} from "vue"

const user = reactive({
    login_type: 0, // 登录方式，0，密码登录，1，短信登录
    account: "",  // 登录账号/手机号/邮箱
    password: "", // 登录密码
    re_password: "", // 登录密码
    remember: false, // 是否记住登录状态
    mobile: "",      // 登录手机号码
    code: "",        // 短信验证码
    sms_btn_text: "点击获取验证码",  // 短信按钮提示信息
    is_send: false,  // 短信发送的标记
    sms_interval: 60,// 间隔时间
    interval: null,  // 定时器的标记
    login() {
        // 用户登录
        return http.post("/user/login/", {
            "username": this.account,
            "password": this.password,
        })
    },
    check_mobile() {
        // 验证手机号
        return http.get(`/user/mobile/${this.mobile}/`)
    },
    register(data) {
        data.mobile = this.mobile
        data.re_password = this.re_password
        data.password = this.password
        data.sms_code = this.code
        // 用户注册请求
        return http.post("/user/register/", data)
    },
    get_sms_code() {
        return http.get(`/user/sms/${this.mobile}/`)
    },
    login_mobile() {
        // 用户登录
        return http.post("/user/login/sms/", {
            "mobile": this.mobile,
            "sms_code": this.code,
        })
    },
    get_user_info(token) {
        // 获取用户个人信息
        return http.get("/user/info/", {
            headers: {
                Authorization: "jwt " + token,
            }
        })
    },
})

export default user;