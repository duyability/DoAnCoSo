from django.db import models

# Create your models here.
class SEO(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    title = models.CharField(max_length=255, default='')
    description = models.CharField(max_length=255,default='')
    keyword = models.CharField(max_length=255,default='')

    def __str__(self):
        return self.title

