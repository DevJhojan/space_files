import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { HabitsComponent } from '@shared/habits/habits.component';
import { NavBarComponent } from '@shared/nav-bar/nav-bar.component';
import TimeBombComponent from './time-bomb/time-bomb.component';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [RouterModule, NavBarComponent, HabitsComponent, TimeBombComponent],
  templateUrl: './home.component.html',
})
export default class HomeComponent {}
