import { Routes } from '@angular/router';

export const routes: Routes = [
  {
    path: 'home',
    loadComponent: () => import('./home/home.component'),
    children: [
      {
        path: 'tasks',
        title: 'Normal Task',
        loadComponent: () => import('./home/task/task.component'),
      },
      {
        path: 'task-constans',
        title: 'Task Constants',
        loadComponent: () =>
          import('./home/tasks-constans/tasks-constans.component'),
      },

      {
        path: '',
        redirectTo: 'tasks',
        pathMatch: 'full',
      },
    ],
  },
  {
    path: 'time-bomb',
    title: 'Time Bomb',
    loadComponent: () => import('./home/time-bomb/time-bomb.component'),
  },
  {
    path: 'ni-u',
    title: 'No important but Urgent',
    loadComponent: () => import('./home/ni-u/ni-u.component'),
  },
  {
    path: 'ni-nu',
    title: 'No important No Urgent',
    loadComponent: () => import('./home/ni-nu/ni-nu.component'),
  },
  {
    path: 'i-u',
    title: 'Important & Urgent',
    loadComponent: () => import('./home/i-u/i-u.component'),
  },
  {
    path: 'i-nu',
    title: 'Important Not Urgent',
    loadComponent: () => import('./home/i-nu/i-nu.component'),
  },
  { path: '', redirectTo: '/home', pathMatch: 'full' },
];