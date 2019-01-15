"""djangodemo03 URL Configuration

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
from django.conf.urls import url

from index import views

urlpatterns = [
    # url(r'^index/', views.index),
    url(r'^01-add-author/$', views.add_author),
    url(r'^02-add-book/$', views.add_book),
    url(r'^03-add-publisher/$', views.add_publisher),
    url(r'^02-query/$', views.query),
    url(r'^03-queryall/$', views.queryall),
    url(r'^04-filter/$', views.filter_views),
    url(r'^05-lookup/$', views.filed_lookup),
    url(r'^06-exclude/$', views.exclud),
    url(r'^05-update/(\d+)/$', views.update),
]
