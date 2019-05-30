from django.db import models
from python_job.utils import get_unique_slug


# Create your models here.
class DichVu(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    title = models.CharField(max_length=255,default='')
    slug = models.SlugField(max_length=255)
    text = models.TextField(default='')
    img = models.ImageField(null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'title', 'slug')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class LinhVuc(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    title = models.CharField(max_length=255,default='')
    slug = models.SlugField(max_length=255)
    text = models.TextField(default='')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'title', 'slug')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
class KyNang(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    title = models.CharField(max_length=255, default='',null=False)
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


class ViecTheoDuAn(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    title = models.CharField("Tiêu đề",max_length=255,default='')
    slug = models.SlugField(max_length=255)
    Linh_Vuc = models.ForeignKey(LinhVuc, on_delete=models.CASCADE,verbose_name="Lĩnh vực",default='')
    Ky_nang = models.ManyToManyField(KyNang, verbose_name="Kỹ Năng",default='')
    Dich_Vu = models.ForeignKey(DichVu, on_delete=models.CASCADE,verbose_name="Dịch Vụ ",default='')
    infojob = models.TextField("Mô tả công việc",max_length=500, default='')
    time_ex = models.DateField("Hạn chào giá",default='')
    Thanh_Pho = models.ForeignKey(ThanhPho, on_delete=models.CASCADE,verbose_name="Chọn Thành Phố",default='')
    NStu = models.IntegerField("Ngân sách từ ", default="")
    NSden = models.IntegerField("Ngân sách đến", default="")
    hinh = models.ImageField("Hình ảnh đính kèm",default='')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'title', 'slug')
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title
