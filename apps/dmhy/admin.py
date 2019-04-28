from django.contrib import admin

# Register your models here.


from .models import *


class DmhyAllAdmin(admin.ModelAdmin):
    list_display = ('name', 'time', 'zimuzu', 'fenlei', 'faburen', 'xiazai_url')


admin.site.register(DmhyAll, DmhyAllAdmin)
