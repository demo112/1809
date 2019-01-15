from django.conf.urls import url
from . import views


urlpatterns = [
    # 匹配首页
    url(r'^$', views.index),
    # 匹配　login/
    url(r'^signin/$', views.signin),
    url(r'^signup/$', views.signup),
]
