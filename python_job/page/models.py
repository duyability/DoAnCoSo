from django.db import models
from python_job.utils import get_unique_slug


class Page(models.Model):
        created_at = models.DateTimeField(auto_now_add=True, null=True)  # Ngày tạo Job(auto)
        slug = models.SlugField(max_length=255, default='')
        title = models.CharField(max_length=300, default='')
        description = models.TextField(default='')

        def __str__(self):
            return self.title

        def save(self, *args, **kwargs):
            if not self.slug:
                self.slug = get_unique_slug(self, 'title', 'slug')
            super().save(*args, **kwargs)
