import {createApp} from 'vue'
import './style.css'
import App from './App.vue'
// 注册router对象
import router from "./router/index.js";
import 'element-plus/dist/index.css';

createApp(App).use(router).mount('#app')
