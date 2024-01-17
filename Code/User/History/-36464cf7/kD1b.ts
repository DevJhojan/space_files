import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';
import { NavBarComponent } from '@shared/nav-bar/nav-bar.component';
import { HabitsComponent } from '@shared/habits/habits.component';

@Component({
  selector: 'app-root',
  standalone: true,/** todo sera standalone */
  imports: [CommonModule, RouterOutlet, NavBarComponent, HabitsComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'TodoBull';
}
