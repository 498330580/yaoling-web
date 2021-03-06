# Generated by Django 2.1.7 on 2019-04-09 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmhy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dmhyall',
            name='daxiao',
            field=models.CharField(max_length=250, null=True, verbose_name='大小'),
        ),
        migrations.AlterField(
            model_name='dmhyall',
            name='faburen_url',
            field=models.CharField(max_length=250, verbose_name='发布人链接'),
        ),
        migrations.AlterField(
            model_name='dmhyall',
            name='name',
            field=models.CharField(max_length=500, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='dmhyall',
            name='name_url',
            field=models.CharField(max_length=250, verbose_name='链接'),
        ),
        migrations.AlterField(
            model_name='dmhyall',
            name='zimuzu',
            field=models.TextField(max_length=250, null=True, verbose_name='字幕组'),
        ),
        migrations.AlterField(
            model_name='dmhyall',
            name='zimuzu_url',
            field=models.CharField(max_length=250, null=True, verbose_name='字幕组链接'),
        ),
    ]
