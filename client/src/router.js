import { createRouter, createWebHistory } from 'vue-router'

const routes = [
    { path: '/', redirect: '/newPassword'},
    { path: '/statistics', name: 'Statistics', component: () => import('./components/Pages/StatisticsPage.vue')},
    { path: '/start', name: 'Auth', component: () => import('./components/Auth.vue')},
    { path: '/newPassword', name: 'NotFound', component: () => import('./components/NotFound.vue')}
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router