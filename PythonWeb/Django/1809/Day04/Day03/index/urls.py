from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^01-addBook/$',addbook_views),
    url(r'^02-query/$',query_views),
]