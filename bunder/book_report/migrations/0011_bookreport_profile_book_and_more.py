# Generated by Django 4.0.5 on 2022-06-25 18:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book_report', '0010_merge_20220625_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookreport',
            name='profile_book',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile_book', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bookreport',
            name='image_upload',
            field=models.ImageField(blank=True, null=True, upload_to='book_report_images'),
        ),
    ]
