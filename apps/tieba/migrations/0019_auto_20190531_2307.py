# Generated by Django 2.1.7 on 2019-05-31 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tieba', '0018_bduss_time_email_send'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bduss_time',
            name='email_send',
            field=models.DateTimeField(editable=False, verbose_name='发送BDUSS失效邮件的时间记录'),
        ),
    ]
