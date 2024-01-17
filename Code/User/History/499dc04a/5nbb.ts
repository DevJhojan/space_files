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
        loadComponent:()=> import('./home/)
      },
      {
        path:'task',
        title: 'task',
        loadComponent:()=> import('./home/task/task.component')
      },
      {
        path:'task',
        title: 'task',
        loadComponent:()=> import('./home/task/task.component')
      },
      {
        path:'task',
        title: 'task',
        loadComponent:()=> import('./home/task/task.component')
      },
      {
        path:'task',
        title: 'task',
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
