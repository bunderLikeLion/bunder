# Generated by Django 4.0.5 on 2022-06-24 21:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book_report', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrap',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='book_report',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='book_report.bookreport'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bookreport',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='유저'),
        ),
    ]
