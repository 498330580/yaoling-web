from django.db import models

# Create your models here.

from django.db import models
from django.urls import reverse


class DmhyAll(models.Model):
    name = models.CharField(max_length=500, verbose_name='标题')
    name_url = models.CharField(max_length=250, verbose_name='链接', db_index=True)
    time = models.DateTimeField(verbose_name='发布时间', db_index=True)
    zimuzu = models.TextField(max_length=250, verbose_name='字幕组', null=True)
    zimuzu_url = models.CharField(max_length=250, verbose_name='字幕组链接', null=True)
    fenlei = models.CharField(max_length=250, verbose_name='分类')
    daxiao = models.CharField(max_length=250, verbose_name='大小', null=True)
    faburen = models.CharField(max_length=250, verbose_name='发布人')
    faburen_url = models.CharField(max_length=250, verbose_name='发布人链接')
    xiazai_url = models.TextField(verbose_name='磁链')

    class Meta:
        verbose_name = '动漫花园数据'
        verbose_name_plural = verbose_name
        ordering = ['-time']

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('dmhy:index', args=[self.id])
