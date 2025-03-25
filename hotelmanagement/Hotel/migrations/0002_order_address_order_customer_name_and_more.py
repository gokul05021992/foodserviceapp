# Generated by Django 5.1.6 on 2025-02-26 08:40

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.TextField(default='123 Default St.', max_length=255),
        ),
        migrations.AddField(
            model_name='order',
            name='customer_name',
            field=models.CharField(default='Anonymous', max_length=255),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
