// app.routes.ts
import { Routes } from '@angular/router';
import { FoodOrderComponent } from '../food-order/food-order.component';
import { LayoutComponent } from '../layout/layout.component';
import { UsersComponent } from './users/users.component';
import { LoginComponent } from './login/login.component';

export const routes: Routes = [
    { path: '', component: LayoutComponent },
    { path: 'order/:id', component: FoodOrderComponent, runGuardsAndResolvers: 'always' },
    { path: 'user/:id', component: UsersComponent },
    { path: 'login', component: LoginComponent }
];