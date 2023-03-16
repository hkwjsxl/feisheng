import {createStore} from "vuex"
import createPersistedState from "vuex-persistedstate"
// 实例化一个vuex存储库
export default createStore({
    // 调用永久存储vuex数据的插件，localstorage里会多一个名叫vuex的Key，里面就是vuex的数据
    plugins: [createPersistedState()],
    state() {  // 相当于组件中的data，用于保存全局状态数据
        return {
            user: {}
        }
    },
    getters: {
        getUserInfo(state) {
            // 从jwt的载荷中提取用户信息
            let now = parseInt((new Date() - 0) / 1000);
            if (state.user.exp === undefined) {
                // 没登录
                state.user = {}
                localStorage.token = null;
                sessionStorage.token = null;
                return null
            }

            if (parseInt(state.user.exp) < now) {
                // 过期处理
                state.user = {}
                localStorage.token = null;
                sessionStorage.token = null;
                return null
            }
            return state.user;
        }
    },
    mutations: { // 相当于组件中的methods，用于操作state全局数据
        login(state, payload) {
            state.user = payload; // state.user 就是上面声明的user
        },
        logout(state) { // 退出登录
            state.user = {}
            localStorage.token = null;
            sessionStorage.token = null;
        }
    }
})