from django.conf.urls import url
from . import views


urlpatterns = [
    # 匹配首页
    url(r'^index/$', views.index),
    url(r'^guoyuan/$', views.index),
    # 匹配　login/
    url(r'^signup/$', views.signup),
    url(r'^login/$', views.login),
    url(r'^', views.index),
]
