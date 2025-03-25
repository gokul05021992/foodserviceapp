from django.db import models
from django.utils import timezone

# Create your models here.


class Food(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='food_images/',null=True,blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    foods = models.ManyToManyField(Food, related_name="orders")
    customer_name = models.CharField(max_length=255, default="Anonymous")
    address = models.TextField(max_length=255, default="123 Default St.") 
    order_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Order {self.id} - {self.order_date}"


