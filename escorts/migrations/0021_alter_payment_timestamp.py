# Generated by Django 5.2 on 2025-04-29 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escorts', '0020_remove_payment_date_payment_timestamp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='timestamp',
            field=models.IntegerField(null=True),
        ),
    ]
