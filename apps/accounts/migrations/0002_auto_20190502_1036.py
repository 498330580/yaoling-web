# Generated by Django 2.1.7 on 2019-05-02 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='address',
            field=models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='家庭地址'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='education',
            field=models.CharField(choices=[('xx', '小学'), ('cz', '初中'), ('gz', '高中'), ('dz', '大专'), ('bk', '本科'), ('qt', '其他')], default='', max_length=15, verbose_name='学历'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='id_number',
            field=models.CharField(blank=True, default='', help_text='如果最后一位为X请大写', max_length=15, null=True, verbose_name='身份证'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='mobile',
            field=models.CharField(blank=True, default='', max_length=11, null=True, unique=True, verbose_name='手机号码'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='nation',
            field=models.CharField(blank=True, default='', max_length=15, null=True, verbose_name='民族'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='qq',
            field=models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='QQ号码'),
        ),
    ]
