"""test01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import index.views as index_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]


urlpatterns += [
    url(r'^music/', include('music.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^sport/', include('sport.urls')),
    url(r'^index/', include('index.urls')),
]


urlpatterns += [
    # 方法一：
    # 通过主路由配文件直接进入到应用中数的视图处理，跨国应用中的路由
    url(r'^$', index_views.index),
    url(r'^login/$', index_views.login),
    url(r'^register/$', index_views.register),
    # 方法二：
    # 当访问路径不是admin/XXX之类的时候，一律要交给index应用中处理
    # 处理所有之前没有匹配到的路由，交给index应用处理
    url(r'^', include('index.urls')),
]
