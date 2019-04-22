from django.contrib import admin
from .models import *

# Register your models here.


class BdussAdmin(admin.ModelAdmin):
    list_per_page = 10  # 每页显示10条，默认为100条
    list_display = ('username', 'bduss')    # 显示字段

    # 显示当前用户信息
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    # 保存当前用户为默认用户
    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.user = request.user
            print(request.user)
            print(form.cleaned_data['bduss'])
        obj.save()


admin.site.register(Bduss, BdussAdmin)


class TiebaMeListAdmin(admin.ModelAdmin):
    list_display = ('forum_name', 'forum_id', 'user_exp', 'user_level', 'is_sign', 'username', 'note')


admin.site.register(TiebaMeList, TiebaMeListAdmin)


class SignTimeAdmin(admin.ModelAdmin):
    list_display = ('name', 'time')


admin.site.register(SignTime, SignTimeAdmin)

