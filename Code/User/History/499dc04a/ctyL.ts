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
      }
      
    ]
  },
  { path: '', redirectTo:'/home', pathMatch:'full'  }
];
