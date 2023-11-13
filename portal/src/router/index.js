import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
const REGISTER_URL = import.meta.env.VITE_REGISTER_URL

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/services',
      name: 'services',
      component: () => import('../views/ServicesView.vue')
    },
    {
      path: '/requests',
      name: 'requests',
      component: () => import('../views/RequestsView.vue')
    },
    {
      path: '/stats',
      name: 'stats',
      component: () => import('../views/StatsView.vue')
    },
    {
      path: '/profile',
      name: 'profile',
      component: () => import('../views/ProfileView.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue')
    },
    {
      path: '/service',
      name: 'service',
      component: () => import('../views/ServiceView.vue')
    },
    {
      path: '/register',
      name: 'register',
      beforeEnter: (to, from, next) => {
        window.location.href = REGISTER_URL; // Redirect to register URL
        next(false); // Avoid Vue Router navigation
      }
    }
  ]
})

export default router
