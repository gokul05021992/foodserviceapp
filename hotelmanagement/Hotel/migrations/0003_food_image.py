# Generated by Django 5.1.6 on 2025-03-07 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel', '0002_order_address_order_customer_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='food_images/'),
        ),
    ]
