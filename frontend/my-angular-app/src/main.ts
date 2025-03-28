import { bootstrapApplication } from '@angular/platform-browser';
import { provideHttpClient } from '@angular/common/http';
import { provideRouter } from '@angular/router'; // Import provideRouter
import { provideAnimations } from '@angular/platform-browser/animations'; // ✅ Correct way in Angular 16+
import { provideToastr } from 'ngx-toastr'; // ✅ Add this

import { AppComponent } from './app/app.component';
import { routes } from './app/app.routes'; // Import your routes


bootstrapApplication(AppComponent, {
  providers: [provideHttpClient(),provideRouter(routes),provideAnimations(),provideToastr()] // ✅ Register HttpClient here
}).catch(err => console.error(err));
