from django.db import models

# Create your models here.


# 网站发展流程设置
class DevelopmentProcess(models.Model):
    time = models.DateField(blank=True, verbose_name="时间")
    description = models.CharField(max_length=200, verbose_name='描述')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='数据创建时间')
    index = models.IntegerField(default=999, verbose_name='排列顺序(从小到大)')

    class Meta:
        verbose_name = '网站发展流程设置'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __str__(self):
        return self.description


# 导航分类
class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='分类名称')
    index = models.IntegerField(default=999, verbose_name='分类排序(从小到大)')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
        # ordering = ['index', 'id']

    def __str__(self):
        return self.name


# 发布导航
class Guide(models.Model):
    title = models.CharField(max_length=50, verbose_name='标题')
    callback_url = models.URLField(verbose_name='URL地址')
    description = models.CharField(max_length=200, verbose_name='链接描述')
    img = models.ImageField(upload_to='gateway/%Y/%m/%d',
                            default='avatar/default.jpg',
                            max_length=200, blank=True,
                            null=True,
                            verbose_name='图标')
    category = models.ForeignKey(Category, blank=True, null=True, verbose_name='分类', on_delete=models.CASCADE)
    date_publish = models.DateTimeField(auto_now=True, verbose_name='发布时间')
    index = models.IntegerField(default=999, verbose_name='排列顺序(从小到大)')

    class Meta:
        verbose_name = '导航页设置'
        verbose_name_plural = verbose_name
        # ordering = ['index', 'id']

    def __str__(self):
        return self.title
