# Generated by Django 4.0.5 on 2022-06-25 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_club', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='image',
            new_name='book_img',
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('문학', '문학'), ('경제/경영', '경제/경영'), ('자기계발', '자기계발'), ('인문', '인문'), ('정치/사회', '정치/사회'), ('예술', '예술'), ('과학', '과학'), ('기술/IT', '기술/IT'), ('기타/기타', '기타/기타')], max_length=64),
        ),
    ]
