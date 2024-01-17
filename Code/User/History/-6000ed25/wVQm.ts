import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [RouterModule, NavBarComponent, HabitsComponent],
  templateUrl: './home.component.html',
})
export default class HomeComponent {

}
