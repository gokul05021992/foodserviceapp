import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule], // ✅ Ensure necessary modules are imported
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {
  loginForm: FormGroup;
  isOtpSent = false;
  generatedOtp: string = '';

  constructor(private fb: FormBuilder, private router: Router) {
    this.loginForm = this.fb.group({
      email: ['', [Validators.required, Validators.email]],
      otp: ['', [Validators.required, Validators.minLength(4), Validators.maxLength(6)]]
    });
  }

  sendOtp() {
    if (this.loginForm.get('email')?.valid) {
      this.isOtpSent = true;
      this.generatedOtp = Math.floor(1000 + Math.random() * 9000).toString();
      alert(`OTP Sent: ${this.generatedOtp}`); // Simulate OTP sending
    }
  }

  login() {
    if (this.loginForm.value.otp === this.generatedOtp) {
      localStorage.setItem('isLoggedIn', 'true'); // Store login state
      this.router.navigate(['/user']); // Navigate to user dashboard
    } else {
      alert('Invalid OTP. Please try again.');
    }
  }
}
