# Generated by Django 2.1.7 on 2019-05-21 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tieba', '0010_auto_20190408_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='bduss',
            name='usernames',
            field=models.CharField(default='', editable=False, max_length=250, verbose_name='百度用户名(验证用)'),
        ),
    ]