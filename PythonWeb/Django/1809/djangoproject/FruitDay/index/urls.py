from django.conf.urls import url
from . import views


urlpatterns = [
    # 匹配首页
    url(r'^index/$', views.index),
    url(r'^guoyuan/$', views.index),
    # 匹配　login/
    url(r'^signup/$', views.signup),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^$', views.index),
]


urlpatterns += [
    url(r'^check_login/$', views.check_login),
    url(r'^check_uphone/$', views.check_uphone),
    url(r'^type_goods/$', views.type_goods),
]
