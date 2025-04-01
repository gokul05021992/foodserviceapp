import { Component } from '@angular/core';
import { Router, RouterModule,NavigationEnd } from '@angular/router'; // Import RouterModule
import { CommonModule } from '@angular/common';
import { AppComponent } from '../app/app.component';
import { AppService } from '../services/food.service';
import { filter } from 'rxjs';


@Component({
  selector: 'app-layout',
  standalone: true,
  imports: [CommonModule,RouterModule],
  templateUrl: './layout.component.html',
  styleUrl: './layout.component.css'
})
export class LayoutComponent {
foodItems: any[] = [];


  constructor(private foodService: AppService, private router: Router) {}

  ngOnInit() {
    this.foodService.getAvailableFoods().subscribe({
      next: (data) => {
        this.foodItems = data.foods;
      },
      error: (error) => {
        console.error('Error fetching food items:', error);
      },
    });
  }

  orderFood(foodId: number) {
    this.router.navigate(['/order', foodId]);
  }
}

