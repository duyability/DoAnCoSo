from django.db import models
from django.conf import settings
from python_job.utils import get_unique_slug

User = settings.AUTH_USER_MODEL


# Create your models here.
class NganhNghe(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    title = models.CharField(max_length=255, default='')
    slug = models.SlugField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'title', 'slug')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class ThanhPho(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    title = models.CharField(max_length=255, default='')
    slug = models.SlugField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'title', 'slug')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class KyNang(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    title = models.CharField(max_length=255, default='')
    slug = models.SlugField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'title', 'slug')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


# Viec theo du an - Minh Duc
class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, default='')
    title = models.CharField(max_length=300, default='')
    description = models.TextField(default='')
    skill = models.TextField(max_length=300, default='')
    Nganh_Nghe = models.ForeignKey(NganhNghe, on_delete=models.CASCADE, verbose_name="Chọn Nganh Nghe", default='')
    Thanh_Pho = models.ForeignKey(ThanhPho, on_delete=models.CASCADE, verbose_name="Chọn Thành Phố", default='')
    last_date = models.DateTimeField()
    NS_tu = models.DecimalField("Ngân sách từ",decimal_places=3, max_digits=50, default='')
    NS_den = models.DecimalField("Ngân sách đến",decimal_places=3, max_digits=50, default='')
    file = models.FileField("File đính kèm", default='')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    filled = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'title', 'slug')
        super().save(*args, **kwargs)


# Viec theo PartTime
class JobPartTime(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)  # Ngày tạo Job(auto)
    slug = models.SlugField(max_length=255, default='')
    title = models.CharField(max_length=300, default='')
    description = models.TextField(default='')
    skill = models.TextField(max_length=300, default='')
    Nganh_Nghe = models.ForeignKey(NganhNghe, on_delete=models.CASCADE, verbose_name="Chọn Nganh Nghe", default='')
    Thanh_Pho = models.ForeignKey(ThanhPho, on_delete=models.CASCADE, verbose_name="Chọn Thành Phố", default='')
    date_begin = models.DateTimeField()  # ngay bat dau lam
    duration = models.CharField(max_length=100, default='')  # Thoi han lam
    NS_tu = models.IntegerField("Ngân sách từ ", default='')
    NS_den = models.IntegerField("Ngân sách đến", default='')
    year_exp = models.CharField("Số Năm Kinh Nghiệm", max_length=300, default='')
    location = models.CharField("Hình thức làm việc", max_length=300, default='')  # Hinh thuc - vi tri lam viec
    file = models.FileField("File đính kèm", upload_to='uploads/ViecLamPartTime/file/%Y/%m/%d/', default='')
    company_name = models.CharField("Tên Công Ty", max_length=300, default='')
    hinh = models.ImageField("Logo Công Ty", upload_to='uploads/ViecLamPartTime/logo/%Y/%m/%d/', default='')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'title', 'slug')
        super().save(*args, **kwargs)


# Gui Bao Gia
class Applicant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applicants')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    baogia = models.CharField(max_length=300, default='')
    time = models.CharField(max_length=300, default='')
    exp_info = models.TextField(max_length=400, default='')
    dudinh_info = models.TextField(max_length=400, default='')
    hotline = models.CharField(max_length=15, default='')
    email = models.CharField(max_length=55, default='')
    file = models.FileField("File đính kèm", upload_to='uploads/baogia/file/%Y/%m/%d/', default='')

    def __str__(self):
        return self.user.get_full_name()


# Nop CV partTime
class CVonsite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    jobpt = models.ForeignKey(JobPartTime, on_delete=models.CASCADE, related_name='CVonsites')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    baogia = models.CharField(max_length=300, default='')
    exp_info = models.TextField(max_length=400, default='')
    dudinh_info = models.TextField(max_length=400, default='')
    hotline = models.CharField(max_length=15, default='')
    email = models.CharField(max_length=55, default='')
    file = models.FileField("File đính kèm", upload_to='uploads/CVonsite/file/%Y/%m/%d/', default='')

    def __str__(self):
        return self.user.get_full_name()
