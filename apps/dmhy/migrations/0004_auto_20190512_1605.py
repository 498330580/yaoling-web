# Generated by Django 2.1.7 on 2019-05-12 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dmhy', '0003_auto_20190412_0024'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dmhyall',
            options={'ordering': ['-time'], 'verbose_name': '动漫花园数据', 'verbose_name_plural': '动漫花园数据'},
        ),
    ]