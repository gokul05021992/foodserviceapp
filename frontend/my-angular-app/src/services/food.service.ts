import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../environment/environment';
import { catchError } from 'rxjs/operators';


@Injectable({
  providedIn: 'root',
})
export class FoodService {
  private http = inject(HttpClient);
  private apiUrl = `${environment.apiUrl}/available-food/`; // Correct endpoint
  // private apiUrl = `${environment.apiUrl}/available-food/`; // Correct endpoint
  getAvailableFoods(): Observable<any> {
    return this.http.get<any>(this.apiUrl);
  }
}
