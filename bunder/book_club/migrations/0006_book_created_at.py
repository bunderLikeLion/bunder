# Generated by Django 4.0.5 on 2022-06-26 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_club', '0005_alter_book_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]