# Generated by Django 4.0.5 on 2022-06-27 20:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('book_report', '0013_delete_profilebook'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrap',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='created_at'),
        ),
    ]
