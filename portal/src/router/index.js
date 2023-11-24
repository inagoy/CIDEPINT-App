import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
const REGISTER_URL = import.meta.env.VITE_REGISTER_URL

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/HomeView.vue')
    },
    {
      path: '/services',
      name: 'services',
      component: () => import('../views/ServicesView.vue')
    },
    {
      path: '/requests',
      name: 'requests',
      beforeEnter: (to, from, next) => {
        // Check if the user is logged in
        if (useAuthStore().user) {
          // User is logged in, allow access to the route
          next()
        } else {
          // User is not logged in, redirect to the login page or another page
          next('/login')
        }
      },
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
      path: '/service/:id',
      name: 'service',
      component: () => import('../views/ServiceView.vue')
    },
    {
      path: '/service-request/:id',
      name: 'serviceRequest',
      beforeEnter: (to, from, next) => {
        // Check if the user is logged in
        if (useAuthStore().user) {
          // User is logged in, allow access to the route
          next()
        } else {
          // User is not logged in, redirect to the login page or another page
          next('/login')
        }
      },
      component: () => import('../views/ServiceRequestView.vue')
    },
    {
      path: '/register',
      name: 'register',
      beforeEnter: (to, from, next) => {
        window.location.href = REGISTER_URL // Redirect to register URL
        next(false) // Avoid Vue Router navigation
      }
    }
  ]
})

export default router
