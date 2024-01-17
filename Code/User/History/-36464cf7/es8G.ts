import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';
import { NavBarComponent } from './shared';

@Component({
  selector: 'app-root',
  standalone: true,/** todo sera standalone */
  imports: [CommonModule, RouterOutlet, NavBarComponentBarComponent, HabitsComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'TodoBull';
}