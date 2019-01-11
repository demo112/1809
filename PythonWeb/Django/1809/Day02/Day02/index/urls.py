from django.conf.urls import url
from .views import *

#http://localhost:8000/
urlpatterns = [
    #如果访问路径是 login/ 的时候,则交给login_views去处理
    url(r'^login/$',login_views),
    #如果访问路径是 register/ 的时候,则交给register_vivews去处理
    url(r'^register/$',register_views),
    #如果访问路径是  的时候,则交给index_views去处理
    url(r'^$',index_views),

    url(r'^01-temp/$',temp_views),
    url(r'^02-temp/$',temp02_views),
    url(r'^03-var/$',var_views),
]