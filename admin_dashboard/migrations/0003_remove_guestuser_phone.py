# Generated by Django 3.2.9 on 2023-06-24 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0002_guestuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guestuser',
            name='phone',
        ),
    ]