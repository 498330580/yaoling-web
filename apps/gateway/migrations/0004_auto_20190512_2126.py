# Generated by Django 2.1.7 on 2019-05-12 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gateway', '0003_auto_20190511_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guide',
            name='callback_url',
            field=models.CharField(max_length=600, verbose_name='URL地址'),
        ),
    ]
