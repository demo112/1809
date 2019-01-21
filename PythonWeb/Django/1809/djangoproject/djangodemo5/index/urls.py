"""djangodemo5 URL Configuration

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
from . import views


urlpatterns = [
    url(r"^show_index/$", views.show_index),
    url(r"^02-post/$", views.post_views),
    url(r"^03-form/$", views.form),
    url(r"^04-register/$", views.register),
    url(r"^05-login/$", views.login),
    url(r"^06-widget/$", views.widget),
    url(r"^07-set_cookie/$", views.set_cookie),
    url(r"^08-get_cookie/$", views.get_cookie),
    url(r"^09-set_session/$", views.set_session),
    url(r"^10-get_session/$", views.get_session),

]


urlpatterns += [
    url(r"^$", views.request_views),
]
