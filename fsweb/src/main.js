import {createApp} from 'vue'
import './style.css'
import App from './App.vue'
// 注册router对象
import router from "./router/index.js";
// element-plus
import 'element-plus/dist/index.css';
import 'element-plus/theme-chalk/index.css'
// 注册store
import store from "./store"

createApp(App).use(router).use(store).mount('#app')
