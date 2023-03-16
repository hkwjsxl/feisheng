import {createRouter, createWebHistory} from 'vue-router'
// 路由列表
const routes = [
    {
        meta: {
            title: "飞升在线教育-站点首页",
            keepAlive: true
        },
        path: '/',
        name: "Home",
        component: () => import("../views/Home.vue")
    },
    {
        meta: {
            title: "飞升在线教育-用户登录",
            keepAlive: true
        },
        path: '/login',
        name: "Login",
        component: () => import("../views/Login.vue")
    }
]
// 路由对象实例化
const router = createRouter({
    // history, 指定路由的模式
    history: createWebHistory(),
    // 路由列表
    routes,
});
// 暴露路由对象
export default router
