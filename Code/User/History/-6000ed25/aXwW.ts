import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { HabitsComponent } from '@shared/habits/habits.component';
import { NavBarComponent } from '@shared/nav-bar/nav-bar.component';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [RouterModule, NavBarComponent, HabitsComponent],
  templateUrl: './home.component.html',
})
export default class HomeComponent {

}
