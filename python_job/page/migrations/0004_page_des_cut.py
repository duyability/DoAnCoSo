# Generated by Django 2.2.2 on 2019-06-21 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_page_thum'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='des_cut',
            field=models.TextField(default='', max_length=300),
        ),
    ]
