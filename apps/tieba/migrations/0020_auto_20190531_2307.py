# Generated by Django 2.1.7 on 2019-05-31 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tieba', '0019_auto_20190531_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bduss_time',
            name='email_send',
            field=models.DateTimeField(auto_now_add=True, verbose_name='发送BDUSS失效邮件的时间记录'),
        ),
    ]
