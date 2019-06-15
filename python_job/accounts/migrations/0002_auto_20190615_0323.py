# Generated by Django 2.2.2 on 2019-06-14 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('vlance', '0001_initial'),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nganh_nghe',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='vlance.NganhNghe', verbose_name='Chọn Nganh Nghe'),
        ),
        migrations.AddField(
            model_name='user',
            name='thanh_pho',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='vlance.ThanhPho', verbose_name='Chọn Thành Phố'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]