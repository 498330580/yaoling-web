# Generated by Django 2.1.7 on 2019-04-12 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmhy', '0002_auto_20190409_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dmhyall',
            name='name_url',
            field=models.CharField(db_index=True, max_length=250, verbose_name='链接'),
        ),
    ]
