import { bootstrapApplication } from '@angular/platform-browser';
import { provideHttpClient } from '@angular/common/http';
import { provideRouter } from '@angular/router'; // Import provideRouter

import { AppComponent } from './app/app.component';
import { routes } from './app/app.routes'; // Import your routes


bootstrapApplication(AppComponent, {
  providers: [provideHttpClient(),provideRouter(routes),] // ✅ Register HttpClient here
}).catch(err => console.error(err));
