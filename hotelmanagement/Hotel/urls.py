from django.urls import path
from .views import AvailableFood,RevenueAPIView,userFood

urlpatterns = [
    path('available-food/', AvailableFood.as_view(), name='available-food'),
    path('revneue-food/', RevenueAPIView.as_view(), name='available-food'),
    path('user-food/', userFood.as_view(), name='available-food'),
]