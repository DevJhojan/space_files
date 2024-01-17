import { HabitsComponent } from './../shared/habits/habits.component';
import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { HabitsComponent,HabitsComponent } from '@shared/*';
import { NavBarComponent } from '@shared/nav-bar/nav-bar.component';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [RouterModule, NavBarComponentBarComponent, HabitsComponentitsComponent],
  templateUrl: './home.component.html',
})
export default class HomeComponent {

}
