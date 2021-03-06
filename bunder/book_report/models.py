from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import FileExtensionValidator

User = settings.AUTH_USER_MODEL


# Create your models here.

class BookReport(models.Model):
    class Meta:
        db_table = "BookReport"

    report_name = models.CharField(max_length=200, verbose_name="독후감 제목", blank=False)
    book_name = models.CharField(max_length=200, verbose_name="책 제목", blank=False)
    book_author = models.CharField(max_length=200, verbose_name="책 글쓴이", blank=False, default="")
    book_category = models.CharField(max_length=200, verbose_name="책 카테고리", blank=False)
    content = models.TextField(help_text="독후감을 적어주세요", verbose_name="독후감 내용", blank=False)
    book_img = models.CharField(max_length=500, verbose_name="책 사진", default="")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='', verbose_name="유저")
    like = models.ManyToManyField(User, related_name='likes', blank=True)
    likes = models.IntegerField(verbose_name='likes_counter', default=0)
    image_upload = models.ImageField(upload_to='book_report_images', blank=True, null=True)

    def __str__(self):
        return self.report_name


class Scrap(models.Model):
    class Meta:
        db_table = "scrap"

    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    book_report = models.ForeignKey(BookReport, on_delete=models.CASCADE, default='')
    created_at = models.DateTimeField(verbose_name='created_at', default=timezone.now)


class Comment(models.Model):
    class Meta:
        db_table = 'report_comment'

    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    book_report = models.ForeignKey(BookReport, on_delete=models.CASCADE, default="")
    content = models.CharField(max_length=120, verbose_name='content')
    created_at = models.DateTimeField(verbose_name='created at', default=timezone.now)
