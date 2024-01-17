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
