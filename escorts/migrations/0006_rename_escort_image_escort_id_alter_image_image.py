# Generated by Django 5.2 on 2025-04-12 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escorts', '0005_remove_escort_agency_remove_escort_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='escort',
            new_name='escort_id',
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='media/images/'),
        ),
    ]
