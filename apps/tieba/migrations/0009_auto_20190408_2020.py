# Generated by Django 2.1.7 on 2019-04-08 20:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tieba', '0008_auto_20190408_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signconfig',
            name='user',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True, verbose_name='用户'),
        ),
    ]
