from django.db import models
from django.conf import settings
from python_job.utils import get_unique_slug

User = settings.AUTH_USER_MODEL


#Create your models here.
class NganhNghe(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    title = models.CharField(max_length=255,default='')
    slug = models.SlugField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'title', 'slug')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ThanhPho(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    title = models.CharField(max_length=255,default='')
    slug = models.SlugField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'title', 'slug')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255,default='')
    title = models.CharField(max_length=300,default='')
    description = models.TextField(default='')
    skill = models.TextField(max_length=300,default='')
    Nganh_Nghe = models.ForeignKey(NganhNghe, on_delete=models.CASCADE, verbose_name="Chọn Nganh Nghe", default='')
    Thanh_Pho = models.ForeignKey(ThanhPho, on_delete=models.CASCADE, verbose_name="Chọn Thành Phố", default='')
    last_date = models.DateTimeField()
    NS_tu = models.IntegerField("Ngân sách từ ", default='')
    NS_den = models.IntegerField("Ngân sách đến", default='')
    file = models.FileField("File đính kèm", default='')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    filled = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'title', 'slug')
        super().save(*args, **kwargs)

class Applicant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applicants')
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.get_full_name()