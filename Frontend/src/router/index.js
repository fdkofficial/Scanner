import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
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
    component: () => import('../components/pages/Home.vue')
  },
  {
    path: '/collect',
    name: 'collect',
    component: () => import('../components/pages/Collect.vue')
  },
  {
    path: '/drop',
    name: 'drop',
    component: () => import('../components/pages/Drop.vue')
  },
  {
    path: '/collect-unit-scanner',
    name: 'collect-unit-scanner',
    component: () => import('../components/pages/CollectUnitScanner.vue')
  },
  {
    path: '/drop-unit-scanner',
    name: 'drop-unit-scanner',
    component: () => import('../components/pages/DropUnitScanner.vue')
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
