from django.contrib import admin
from .models import *

#声明 Author 的高级管理类 AuthorAdmin
class AuthorAdmin(admin.ModelAdmin):
    # 1.定义在列表页上显示的属性们
    list_display = ['name','age','email']
    # 2.定义允许被点击的字段们
    list_display_links = ['name','email']
    # 3.定义在列表页上就允许被修改的字段们
    list_editable = ['age']
    # 4. 添加允许被搜索的字段们
    search_fields = ['name','email']
    # 5.右侧增加过滤器
    list_filter = ['name','email']
    # 7.指定在详情页中显示的字段以及排列的顺序
    # fields = ['name','email','age']
    # 8.指定在详情页中的字段分组们
    fieldsets = (
        #分组1 : name,age
        ('基本选项',{
            'fields':('name','age'),
        }),
        #分组2 : email,isActive
        ('高级选项',{
            'fields':('email','isActive'),
            'classes':('collapse',),
        })
    )

class BookAdmin(admin.ModelAdmin):
    list_display = ["title","publicate_date"]
    # 6.顶部增加时间选择器
    date_hierarchy = "publicate_date"

class PublisherAdmin(admin.ModelAdmin):
    #1.列表页中显示name,address,city
    list_display = ['name','address','city']
    #2.address和city可编辑
    list_editable = ['address','city']
    #3.顶部增加筛选:name,city,address,website
    search_fields = ['name','city','address','website']
    #4.分组 : name,address,city 为基本选项,country,website 为高级选项
    fieldsets = (
        ('基本选项',{
            'fields':('name','address','city'),
        }),
        ('高级选项',{
            'fields':('country','website'),
            'classes':('collapse',)
        })
    )


# Register your models here.
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Wife)

