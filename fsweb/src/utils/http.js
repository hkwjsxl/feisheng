import axios from "axios"
import settings from "../settings";

const http = axios.create({
    // timeout: 2500,  // 请求超时，有大文件上传需要关闭这个配置
    baseURL: settings.host,  // 设置api服务端的默认地址[如果基于服务端实现的跨域，这里可以填写api服务端的地址，如果基于nodejs客户端测试服务器实现的跨域，则这里不能填写api服务端地址]
    withCredentials: false,  // 是否允许客户端ajax请求时携带cookie
})

// 请求拦截器
http.interceptors.request.use((config) => {
    // console.log("http请求之前");
    return config;
}, (error) => {
    // console.log("http请求错误");
    return Promise.reject(error);
});

// 响应拦截器
http.interceptors.response.use((response) => {
    // console.log("服务端响应数据成功以后，返回结果给客户端的第一时间，执行then之前");
    return response;
}, (error) => {
    // console.log("服务端响应错误内容的时候。...");
    return Promise.reject(error);
});

export default http;