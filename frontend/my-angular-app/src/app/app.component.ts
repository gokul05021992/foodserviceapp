import { Component, OnInit } from '@angular/core';
import { AppService } from '../services/food.service';
import { Router, RouterModule } from '@angular/router'; // Import RouterModule

// import { Router } from '@angular/router';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule,RouterModule],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent implements OnInit {
  foodItems: any[] = [];

  constructor(private foodService: AppService, private router: Router) {}

  ngOnInit() {
    this.foodService.getAvailableFoods().subscribe({
      next: (data) => {
        this.foodItems = data;
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