"""britecore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$',TemplateView.as_view(template_name='ticket/index.html')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', views.login, {'template_name': 'ticket/login.html'}),
    url(r'^client/add$', TemplateView.as_view(template_name='ticket/client/client_add.html'), name="client_add"),
    url(r'^client/edit$', TemplateView.as_view(template_name='ticket/client/client_edit.html'), name="client_edit"),
    url(r'^client/list$', TemplateView.as_view(template_name='ticket/client/client_list.html'), name="client_list"),
    url(r'^feature/add$', TemplateView.as_view(template_name='ticket/feature/client_add.html')),
    url(r'^feature/edit$', TemplateView.as_view(template_name='ticket/feature/client_edit.html')),
    url(r'^feature/list$', TemplateView.as_view(template_name='ticket/feature/client_list.html')),
    url(r'^user/add$', TemplateView.as_view(template_name='ticket/user/user_add.html')),
    url(r'^user/edit$', TemplateView.as_view(template_name='ticket/user/user_edit.html')),
    url(r'^user/list$', TemplateView.as_view(template_name='ticket/user/user_list.html')),
    url(r'^user/register$', TemplateView.as_view(template_name='ticket/user/user_register.html')),
]
