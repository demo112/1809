from django.contrib import admin
from .models import *
# Register your models here.


class UsersAdmin(admin.ModelAdmin):
    # list_display =
    pass


admin.site.register(Users)
