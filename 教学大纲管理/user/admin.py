from django.contrib import admin
from .models import MyUserModel
# Register your models here.


class UserAdmin(admin.ModelAdmin):

    pass


# 将用户表在后台界面显示，注册到后台
admin.site.register(MyUserModel, UserAdmin)

