import { createRouter, createWebHashHistory } from 'vue-router'
import Main from "./components/Main"
import NotFound from "./components/NotFound"
const routes = [
{ path: '/main', name: 'Main', component: Main },
{ path: '/', name: 'Auth', component: () => import('./components/Auth.vue')},
{ path: '/:pathMatch(.*)*', name: 'NotFound', component: NotFound }
]
const router = createRouter({history: createWebHashHistory(), routes})
export default router