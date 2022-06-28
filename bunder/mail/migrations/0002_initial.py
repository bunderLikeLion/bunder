# Generated by Django 4.0.5 on 2022-06-28 18:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mail', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mail',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receivernick', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mail',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
