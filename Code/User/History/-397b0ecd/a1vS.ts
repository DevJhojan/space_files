import { Component } from '@angular/core';
import IUComponent from '../i-u/i-u.component';
import INuComponent from '../i-nu/i-nu.component';
import NiNuComponent from '../ni-nu/ni-nu.component';
import NiUComponent from '../ni-u/ni-u.component';

@Component({
  selector: 'app-task',
  standalone: true,
  imports: [IUComponent,INuComponent,NiNuComponent,NiUComponent],
  templateUrl: './task.component.html',
  styleUrl: './task.component.css'
})
export default class TaskComponent {

}
