from django.contrib import admin
from .models import *

# Register your models here.


class GuideAdmin(admin.ModelAdmin):
    list_display = ('title', 'callback_url', 'description', 'category', 'date_publish', 'index')


admin.site.register(Guide, GuideAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Category, CategoryAdmin)
