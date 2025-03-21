import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '../views/HomeView.vue';
import PlacesView from '../views/PlacesView.vue';
import CalendarView from '../views/CalendarView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: HomeView,
      meta: { title: 'Dashboard', description: "A Dashboard for show, analitics for your business." }
    },
    {
      path: '/places',
      name: 'Places',
      component: PlacesView,
      meta: { title: 'Places', description: "Places for buildings yours storages." }
    },
    {
      path: '/calendar',
      name: 'Calendar',
      component: CalendarView,
      meta: { title: 'Calendar' }
    },
  ]
})

export default router
