import { Component } from '@angular/core';
import { routes } from '../../app.routes';

@Component({
  selector: 'app-nav-bar',
  standalone: true,
  imports: [],
  templateUrl: './nav-bar.component.html',
})

export class NavBarComponent {
  public menuNav = routes
  .map((router)=> router.children ?? [])
  .flat()
  .filter((route)=> route && route.path)
  .filter((route)=> !route.path?.includes(':'));
}
