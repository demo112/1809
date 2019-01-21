# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *


# 定义高级管理类
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'email']
    list_display_links = ['age', 'email']
    list_editable = ["name"]
    search_fields = ['name', "age", 'email']
    list_filter = ['name', 'email']
    fields = ['name', 'age', 'email']


class BookAdmin(admin.ModelAdmin):
    list_display = ["title", 'publicate_date']
    list_editable = ['publicate_date']
    date_hierarchy = 'publicate_date'


class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'city']
    list_editable = ["address", 'city']
    list_filter = ['city']
    search_fields = ['name', 'website']
    fieldsets = [
        # 分组一
        ['信息', {
            "fields": ['name', 'website'],
            "classes": ["collapse"]}],
        # 分组二
        ['位置信息', {  # 组名
            "fields": ['country', 'city', 'address'],  # 字段名
            "classes": ["collapse"]}],  # 展示效果
    ]


# Register your models here.
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Wife)































