"""Day02 URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #访问路径是以 music/ 做为开始的时候,将请求交给music中的urls.py去处理
    url(r'^music/',include('music.urls')),
    #访问路径是以 sport/ 做为开始的时候,将请求交给sport中的urls.py去处理
    url(r'^sport/',include('sport.urls')),
    #访问路径是以 news/ 做为开始的时候,将请求交给news中的urls.py去处理
    url(r'^news/',include('news.urls')),
    #访问路径中不包含指定的路径时(admin/,music/,sport/,news/),交给index中的urls.py去处理
    url(r'^',include('index.urls')),
]
