# Generated by Django 4.0.5 on 2022-06-25 06:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('book_report', '0004_alter_comment_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='created at'),
        ),
    ]
