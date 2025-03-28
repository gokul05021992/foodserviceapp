import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { AppService } from '../../services/food.service';
import { ToastrService } from 'ngx-toastr';
import { NgxSpinnerModule, NgxSpinnerService } from 'ngx-spinner';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule,NgxSpinnerModule], // ✅ Ensure necessary modules are imported
  providers: [NgxSpinnerService],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {
  loginForm: FormGroup;
  isOtpSent = false;
  generatedOtp: string = '';

  constructor(private fb: FormBuilder, private router: Router,private otpService: AppService, private toastr: ToastrService,
    private spinner: NgxSpinnerService) {
    this.loginForm = this.fb.group({
      email: ['', [Validators.required, Validators.email]],
      otp: ['', [Validators.required, Validators.minLength(4), Validators.maxLength(6)]]
    });
  }

  sendOtp() {
    const email = this.loginForm.get('email')?.value;
    this.spinner.show();
    this.otpService.sendOtp(email).subscribe(
      response => {
        this.spinner.hide();
        this.toastr.success('OTP sent successfully!', 'Success');
        this.isOtpSent = true;
      },
      error => {
        this.spinner.hide();
        this.toastr.error('Error sending OTP', 'Error');
      }
    );
  }

  login() {
    const email = this.loginForm.get('email')?.value;
    const otp = this.loginForm.get('otp')?.value;
    this.otpService.verifyOtp(email, otp).subscribe(
      response => {
        // alert('Login successful!');
        this.router.navigate(['/']);
      },
      error => {
        alert('Invalid OTP');
      }
    );
  }
}
