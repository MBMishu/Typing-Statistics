# Generated by Django 3.2.9 on 2023-06-24 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0007_formdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='formdata',
            name='pdf_name',
            field=models.ForeignKey(blank=True, max_length=200, null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_dashboard.pdffile'),
        ),
        migrations.AddField(
            model_name='formdata',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_dashboard.guestuser'),
        ),
    ]
