from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.views.generic import ListView
from taggit.managers import TaggableManager

from python_job.utils import get_unique_slug


class Page(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)  # Ngày tạo Job(auto)
    slug = models.SlugField(max_length=255, default='')
    title = models.CharField(max_length=300, default='')
    des_cut = models.TextField("Mô tả ngắn",max_length=300, default='')
    description = RichTextUploadingField(default='')
    thum = models.ImageField("Hình đại diện", upload_to='uploads/Blog/logo/%Y/%m/%d/', default='')
    tags = TaggableManager("Từ khóa",help_text='Các từ khóa đươc phân cách bằng dấu phẩy (,)')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'title', 'slug')
        super().save(*args, **kwargs)
