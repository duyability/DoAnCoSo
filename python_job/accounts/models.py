from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.managers import UserManager
from vlance.models import ThanhPho, NganhNghe, KyNang

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
    # update
    thanh_phos = models.ForeignKey(ThanhPho, on_delete=models.CASCADE,null=True, verbose_name="Chọn Thành Phố", default='1')
    nganh_nghes = models.ForeignKey(NganhNghe, on_delete=models.CASCADE,null=True, verbose_name="Chọn Ngành Nghề", default='1')
    hinh = models.ImageField("Avatar ", upload_to='uploads/User/avatar/%Y/%m/%d/',default='uploads/User/unknown.png',null=True,)
    skill = models.ManyToManyField(KyNang, verbose_name="Chọn kỹ năng", default='',null=True,)
    sologan = models.CharField("Chức danh",max_length=50, blank=True, null=True, default='')
    description = models.TextField("Giới Thiệu", max_length=300, blank=True, null=True, default="")
    year_exp = models.CharField("Trình Độ", max_length=300, default='',null=True)
    # end update

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __unicode__(self):
        return self.email

    objects = UserManager()

class UpUser(models.Model):
    # update
    created_at = models.DateTimeField(auto_now_add=True, null=True)  # Ngày tạo Job(auto)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    # thanh_pho = models.ForeignKey(ThanhPho, on_delete=models.CASCADE, verbose_name="Chọn Thành Phố", default='')
    # nganh_nghe = models.ForeignKey(NganhNghe, on_delete=models.CASCADE, verbose_name="Chọn Nganh Nghe", default='')
    # hinh = models.ImageField("Avatar ", upload_to='uploads/User/avatar/%Y/%m/%d/', default='')
    # skill = models.ManyToManyField(KyNang,verbose_name="Chọn kỹ năng", default='')
    # sologan = models.CharField(max_length=50, blank=True, null=True, default="")
    # description = models.TextField("Mô tả - giới thiệu về bản thân", max_length=300, blank=True, null=True, default="")
    # year_exp = models.CharField("Số Năm Kinh Nghiệm", max_length=300, default='')
    # end update