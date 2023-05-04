import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'auth',
    component: () => import('../components/authorization/mainAuth.vue')
  },
  {
    path: '/user-login',
    name: 'user-login',
    component: () => import('../components/authorization/userLogin.vue')
  },
  {
    path: '/user-register',
    name: 'user-register',
    component: () => import('../components/authorization/userRegister.vue')
  },
  {
    path: '/home',
    name: 'home',
    component: () => import('../components/Home.vue')
  },
  {
    path: '/scanner',
    name: 'scanner',
    component: () => import('../components/QRScanner.vue')
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
