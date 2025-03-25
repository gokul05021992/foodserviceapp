from django.urls import path
from .views import AvailableFood,RevenueAPIView

urlpatterns = [
    path('available-food/', AvailableFood.as_view(), name='available-food'),
    path('revneue-food/', RevenueAPIView.as_view(), name='available-food'),
]