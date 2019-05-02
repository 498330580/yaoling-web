from django.db import models

# Create your models here.


from django.contrib.auth.models import AbstractUser


# 用户模型.
class MyUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d',
                               default='avatar/default.jpg',
                               max_length=200, blank=True,
                               null=True,
                               verbose_name='用户头像')
    qq = models.CharField(max_length=20, blank=True, null=True, verbose_name='QQ号码', default='')
    mobile = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name='手机号码', default='')
    url = models.URLField(max_length=100, blank=True, null=True, verbose_name='个人网页地址')
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    gender = models.CharField(max_length=12,
                              choices=(("male", "男"), ("female", "女"), ("secrecy", "保密"),),
                              default="secrecy",
                              verbose_name="性别")
    nation = models.CharField(null=True, blank=True, max_length=15, verbose_name="民族", default='')
    education = models.CharField(max_length=15,
                                 choices=(
                                     ("xx", "小学"),
                                     ("cz", "初中"),
                                     ("gz", "高中"),
                                     ('dz', '大专'),
                                     ('bk', '本科'),
                                     ('qt', '其他')
                                 ),
                                 default="",
                                 verbose_name="学历")
    id_number = models.CharField(null=True, blank=True, max_length=15, verbose_name="身份证", help_text="如果最后一位为X请大写", default='')
    address = models.CharField(null=True, blank=True, max_length=50, verbose_name="家庭地址", default='')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.username
