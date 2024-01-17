import { Routes } from '@angular/router';

export const routes: Routes = [

  {
    path: 'home',
    loadComponent: () => import('./home/home.component'),
    children:[
      {
        path:'task',
        title: 'task',
        loadComponent:()=> import('./home/task/task.component')
      },
      {
        path:'task-constans',
        title: 'Task Constants',
        loadComponent:()=> import('./home/tasks-constans/tasks-constans.component')
      },
      {
        path:'time-bomb',
        title: 'Time Bomb',
        loadComponent:()=> import('./home/time-bomb/time-bomb.component')
      },
      {
        path:'ni-u',
        title: 'No important but Urgent',
        loadComponent:()=> import('./home/ni-u/ni-u.component')
      },
      {
        path:'ni-nu',
        title: 'No important No Urgent',
        loadComponent:()=> import('./home/ni-nu/ni-nu.component')
      },
      {
        path:'i-u',
        title: 'Important & Urgent',
        loadComponent:()=> import('./home/i-u/i-u.component')
      },
      {
        path:'i-nu',
        title: 'Important Not Urgent',
        loadComponent:()=> import('./home/task/task.component')
      },
      {
        path:'task',
        title: 'task',
        loadComponent:()=> import('./home/task/task.component')
      },

      {
        path:'',
        redirectTo: '/task',
        pathMatch:'full'
      }
    ]
  },
  { path: '', redirectTo:'/home', pathMatch:'full'  }
];
