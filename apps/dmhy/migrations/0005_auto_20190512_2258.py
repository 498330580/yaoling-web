# Generated by Django 2.1.7 on 2019-05-12 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmhy', '0004_auto_20190512_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dmhyall',
            name='time',
            field=models.DateTimeField(db_index=True, verbose_name='发布时间'),
        ),
    ]