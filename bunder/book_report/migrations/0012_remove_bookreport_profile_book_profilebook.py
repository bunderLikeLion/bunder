# Generated by Django 4.0.5 on 2022-06-25 19:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book_club', '0003_rename_image_book_book_img_alter_book_category'),
        ('book_report', '0011_bookreport_profile_book_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookreport',
            name='profile_book',
        ),
        migrations.CreateModel(
            name='ProfileBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_club.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
