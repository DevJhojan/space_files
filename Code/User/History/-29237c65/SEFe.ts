import { CommonModule } from '@angular/common';
import { ChangeDetectionStrategy, Component } from '@angular/core';

@Component({
  selector: 'app-shared',
  standalone: true,
  imports: [
    CommonModule,
  ],
  templateurl: './shared.component.html',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class SharedComponent { }
