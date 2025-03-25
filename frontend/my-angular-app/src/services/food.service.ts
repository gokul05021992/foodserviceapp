import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../environment/environment';

@Injectable({
  providedIn: 'root',
})
export class AppService {
  private http = inject(HttpClient);
  private apiUrl = environment.apiUrl; // Base API URL from environment

  constructor() {}

  // ✅ Get Available Foods
  getAvailableFoods(): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}/available-food/`);
  }

  // ✅ Send OTP
  sendOtp(email: string): Observable<any> {
    return this.http.post(`${this.apiUrl}/send-otp/`, { email });
  }

  // ✅ Verify OTP
  verifyOtp(email: string, otp: string): Observable<any> {
    return this.http.post(`${this.apiUrl}/verify-otp/`, { email, otp });
  }
}
