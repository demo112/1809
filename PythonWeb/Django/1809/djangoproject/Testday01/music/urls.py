"""
    music中的应用级子路由处理函数
"""
from django.conf.urls import url
from . import views


# 处理路径从music后开始
urlpatterns = [
    # 匹配localhost:8000/music/show/
    url(r'^show/$', views.show),
]
