# Generated by Django 2.2.2 on 2019-06-14 20:23

import accounts.managers
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(error_messages={'required': 'Role must be provided'}, max_length=12)),
                ('gender', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('hotline', models.CharField(default='', max_length=15)),
                ('email', models.EmailField(error_messages={'unique': 'Email của bạn đã tồn tại.'}, max_length=254, unique=True)),
                ('hinh', models.ImageField(default='', upload_to='uploads/User/avatar/%Y/%m/%d/', verbose_name='Avatar ')),
                ('skill', models.TextField(default='', max_length=300, verbose_name='Skill  ')),
                ('sologan', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('description', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Mô tả - giới thiệu về bản thân')),
                ('year_exp', models.CharField(default='', max_length=300, verbose_name='Số Năm Kinh Nghiệm')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', accounts.managers.UserManager()),
            ],
        ),
    ]
