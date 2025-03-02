import Vue from 'vue'
import VueRouter from 'vue-router'
import Baseline from '../views/baseline.vue'
import Bug from '../views/bug.vue'
import LLM from '../views/llm.vue'
import Baselinerepair from '../views/baselinerepair.vue'
import Bugrepair from '../views/bugrepair.vue'
Vue.use(VueRouter)

const routes = [
    {
        path: '/baseline',
        name: 'Baseline',
        component: Baseline,
        meta: { name: '基线检测'}
    },
    {
        path: '/bug',
        name: 'Scene',
        component: Bug,
        meta: { name: '漏洞扫描' }
    }, 
    {
        path: '/llm',
        name: 'LLM',
        component: LLM,
        meta: { name: "AI大模型问答" }
    },
]
const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router