import {createApp} from 'vue'
import './style.css'
import App from './App.vue'
// 注册router对象
import router from "./router/index.js";

createApp(App).use(router).mount('#app')
