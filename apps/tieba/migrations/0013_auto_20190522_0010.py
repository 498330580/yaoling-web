# Generated by Django 2.1.7 on 2019-05-22 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tieba', '0012_auto_20190521_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bduss',
            name='usernames',
            field=models.CharField(default='', editable=False, max_length=250, verbose_name='百度用户名(验证用)'),
        ),
    ]
