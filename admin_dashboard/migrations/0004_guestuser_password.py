# Generated by Django 3.2.9 on 2023-06-24 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0003_remove_guestuser_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='guestuser',
            name='password',
            field=models.CharField(max_length=200, null=True),
        ),
    ]