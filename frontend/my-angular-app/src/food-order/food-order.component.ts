import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FoodService } from '../services/food.service';

@Component({
  selector: 'app-food-order',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './food-order.component.html',
  styleUrl: './food-order.component.css',
})
export class FoodOrderComponent implements OnInit {
  orderId: number | null = null;
  foodDetails: any;

  constructor(private route: ActivatedRoute, private foodService: FoodService) {}

  ngOnInit(): void {
    this.route.paramMap.subscribe((params) => {
      this.orderId = parseInt(params.get('id')!, 10);
      if (this.orderId) {
        this.foodService.getAvailableFoods().subscribe({
          next: (data) => {
            this.foodDetails = data.find((item: any) => item.id === this.orderId);
          },
          error: (error) => {
            console.error('Error fetching food items:', error);
          },
        });
      }
    });
  }
}