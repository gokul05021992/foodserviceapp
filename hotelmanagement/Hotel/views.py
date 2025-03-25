from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
import time  
from .models import Food  # Import your Food model
from .serializers import FoodSerializer  # Import serializer

class AvailableFood(APIView):
    
    def get(self, request):
        start_time = time.time() 
        foods = Food.objects.all()  # Fetch all food items
        serializer = FoodSerializer(foods, many=True,context={'request': request})  # Serialize data
        total_foods = foods.count()
        execution_time = time.time() - start_time
        return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response(
        #     {
        #         # "total_foods": total_foods,
        #         "foods": serializer.data,
        #         # "execution_time": f"{execution_time:.6f} seconds"
        #     }, 
        #     status=status.HTTP_200_OK
        # )


class RevenueAPIView(APIView):
    def get(self, request):
        # Get filter type from query parameters (default to 'daily')
        filter_type = request.GET.get('filter', 'daily')  
        today = timezone.now().date()

        # Filter orders based on filter_type
        if filter_type == 'daily':
            revenue = Order.objects.filter(order_date__date=today).aggregate(total_revenue=Sum('foods__price'))['total_revenue']
        elif filter_type == 'monthly':
            revenue = Order.objects.filter(order_date__year=today.year, order_date__month=today.month).aggregate(total_revenue=Sum('foods__price'))['total_revenue']
        elif filter_type == 'yearly':
            revenue = Order.objects.filter(order_date__year=today.year).aggregate(total_revenue=Sum('foods__price'))['total_revenue']
        else:
            return Response({"error": "Invalid filter type. Use 'daily', 'monthly', or 'yearly'."}, status=status.HTTP_400_BAD_REQUEST)

        return Response(
            {"filter": filter_type, "revenue": revenue or 0}, 
            status=status.HTTP_200_OK
        )