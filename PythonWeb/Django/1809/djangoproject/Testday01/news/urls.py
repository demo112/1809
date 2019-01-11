"""
    music中的应用级子路由处理函数
"""
from django.conf.urls import url
from . import views
#进入到此urls.py中说明已经匹配上了localhost:8000/music/
#所以在此文件中只需要匹配具体的资源路径就可以了,不用考虑localhost:8000/music/ 的路径了
urlpatterns = [
    # 匹配localhost:8000/music/show/
    url(r'^index/$', views.index),
]
