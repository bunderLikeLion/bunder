# Generated by Django 4.0.5 on 2022-06-27 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_club', '0008_alter_book_category_alter_bookclub_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookclubvote',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
