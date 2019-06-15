from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.managers import UserManager
from vlance.models import ThanhPho, NganhNghe

GENDER_CHOICES = (
    ('male', 'Nam'),
    ('female', 'Nữ'))


class User(AbstractUser):
    username = None
    role = models.CharField(max_length=12, error_messages={
        'required': "Role must be provided"
    })
    gender = models.CharField(max_length=10, blank=True, null=True, default="")
    hotline = models.CharField(max_length=15,null=False,default='')
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "Email của bạn đã tồn tại.",
                              })


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __unicode__(self):
        return self.email

    objects = UserManager()

class UpUser(models.Model):
    # update
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thanh_pho = models.ForeignKey(ThanhPho, on_delete=models.CASCADE, verbose_name="Chọn Thành Phố", default='')
    nganh_nghe = models.ForeignKey(NganhNghe, on_delete=models.CASCADE, verbose_name="Chọn Nganh Nghe", default='')
    hinh = models.ImageField("Avatar ", upload_to='uploads/User/avatar/%Y/%m/%d/', default='')
    skill = models.TextField("Skill  ", max_length=300, default='')
    sologan = models.CharField(max_length=50, blank=True, null=True, default="")
    description = models.CharField("Mô tả - giới thiệu về bản thân", max_length=300, blank=True, null=True, default="")
    year_exp = models.CharField("Số Năm Kinh Nghiệm", max_length=300, default='')
    # end update