import { createRouter, createWebHistory } from 'vue-router'

import InformationView from '../views/InformationView.vue';
import ValidateView from '../views/ValidateView.vue';
import DashboardView from '../views/DashboardView.vue';
import PlacesView from '../views/PlacesView.vue';
import CalendarView from '../views/CalendarView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Information',
      component: InformationView,
      meta: { sidebar: false }
    },
    {
      path: '/validate',
      name: 'Validate',
      component: ValidateView,
      meta: { sidebar: false }
    },
    {
      path: '/dashboard',
      name: 'Dashboard',
      component: DashboardView,
      meta: { title: 'Places', description: "Places for buildings yours storages.", sidebar: true }
    },
    {
      path: '/places',
      name: 'Places',
      component: PlacesView,
      meta: { title: 'Places', description: "Places for buildings yours storages.", sidebar: true }
    },
    {
      path: '/calendar',
      name: 'Calendar',
      component: CalendarView,
      meta: { title: 'Calendar', sidebar: true }
    },
  ]
})

export default router
