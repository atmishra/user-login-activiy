from django.contrib import admin

from .models import UserLoginActivity
# Register your models here.
class UserLoginActivityAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserLoginActivity, UserLoginActivityAdmin)
