# Generated by Django 4.0.5 on 2022-06-28 17:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_name', models.CharField(max_length=200, verbose_name='독후감 제목')),
                ('book_name', models.CharField(max_length=200, verbose_name='책 제목')),
                ('book_author', models.CharField(default='', max_length=200, verbose_name='책 글쓴이')),
                ('book_category', models.CharField(max_length=200, verbose_name='책 카테고리')),
                ('content', models.TextField(help_text='독후감을 적어주세요', verbose_name='독후감 내용')),
                ('book_img', models.CharField(default='', max_length=500, verbose_name='책 사진')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('likes', models.IntegerField(default=0, verbose_name='likes_counter')),
                ('image_upload', models.ImageField(blank=True, null=True, upload_to='book_report_images')),
            ],
            options={
                'db_table': 'BookReport',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500, verbose_name='content')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created at')),
            ],
            options={
                'db_table': 'report_comment',
            },
        ),
        migrations.CreateModel(
            name='Scrap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created_at')),
                ('book_report', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='book_report.bookreport')),
            ],
            options={
                'db_table': 'scrap',
            },
        ),
    ]
