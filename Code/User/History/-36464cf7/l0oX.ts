import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';
import { NavBarComponent } from './shared';
import { HabitsComponent } from './shared/habits/habits.component';

@Component({
  selector: 'app-root',
  standalone: true,/** todo sera standalone */
  imports: [CommonModule, RouterOutlet, NavBarComponentBarComponent, HabitsComponentponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'TodoBull';
}
