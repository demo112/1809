from django.conf.urls import url
from .views import *

# http://localhost:8000/news/xxxx
urlpatterns = [
    # 访问路径是 index/ 的时候,将请求交给 index_views去处理
    url(r'^index/$',index_views),
]