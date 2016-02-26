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
from ticket.views import ClientAdd, ClientDelete,ClientEdit, ClientList, UserAdd, FeatureAdd, FeatureDelete, FeatureEdit, FeatureList, UserDelete, UserEdit, UserList

urlpatterns = [
    url(r'^$',TemplateView.as_view(template_name='ticket/base/base.html')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', views.login, {'template_name': 'ticket/login.html'}),
    url(r'^client/add$', ClientAdd.as_view(), name="client_add"),
    url(r'^client/delete/(?P<pk>\d+)/$', ClientDelete.as_view(), name="client_delete"),
    url(r'^client/edit/(?P<pk>\d+)/$', ClientEdit.as_view(), name="client_edit"),
    url(r'^client/list$', ClientList.as_view(), name="client_list"),
    url(r'^feature/add$', FeatureAdd.as_view(), name='feature_add'),
    url(r'^feature/delete/(?P<pk>\d+)/$', FeatureDelete.as_view(), name="feature_delete"),
    url(r'^feature/edit/(?P<pk>\d+)/$', FeatureEdit.as_view(),name='feature_edit'),
    url(r'^feature/list$', FeatureList.as_view(), name='feature_list'),
    url(r'^user/add$', UserAdd.as_view(), name='user_add'),
    url(r'^user/delete/(?P<pk>\d+)/$', UserDelete.as_view(), name='user_delete'),
    url(r'^user/edit/(?P<pk>\d+)/$', UserEdit.as_view(), name='user_edit'),
    url(r'^user/list$', UserList.as_view(), name='user_list'),
    url(r'^user/register$', TemplateView.as_view(template_name='ticket/user/user_register.html')),
]
