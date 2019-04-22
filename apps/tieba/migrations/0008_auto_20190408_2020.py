# Generated by Django 2.1.7 on 2019-04-08 20:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tieba', '0007_signconfig_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signconfig',
            name='user',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
    ]
