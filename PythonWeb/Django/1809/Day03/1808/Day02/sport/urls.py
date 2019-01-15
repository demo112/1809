from django.conf.urls import url
from .views import *

# http://localhost:8000/sport/xxxx
urlpatterns = [
    #当访问路径是 index/ 的时候,则将请求交给 index_views
    url(r'^index/$',index_views),
]