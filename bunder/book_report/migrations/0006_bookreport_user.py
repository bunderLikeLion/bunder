# Generated by Django 4.0.5 on 2022-06-22 09:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book_report', '0005_remove_bookreport_book_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookreport',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]