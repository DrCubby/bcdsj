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
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.contrib.auth import views
from django.views.generic import TemplateView
from ticket.views import ClientAdd, ClientDelete,ClientEdit, ClientList, UserAdd, FeatureAdd, FeatureDelete,\
    FeatureEdit, FeatureList, ProductAdd, ProductDelete, ProductEdit, ProductList, UserEdit, UserList,\
    UserLogin

urlpatterns = [
    url(r'^$',TemplateView.as_view(template_name='ticket/base/base.html')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^client/add$', login_required(ClientAdd.as_view()), name="client_add"),
    url(r'^client/delete/(?P<pk>\d+)/$', login_required(ClientDelete.as_view()), name="client_delete"),
    url(r'^client/edit/(?P<pk>\d+)/$', login_required(ClientEdit.as_view()), name="client_edit"),
    url(r'^client/list$', login_required(ClientList.as_view()), name="client_list"),
    url(r'^feature/add$', login_required(FeatureAdd.as_view()), name='feature_add'),
    url(r'^feature/delete/(?P<pk>\d+)/$', login_required(FeatureDelete.as_view()), name="feature_delete"),
    url(r'^feature/edit/(?P<pk>\d+)/$', login_required(FeatureEdit.as_view()),name='feature_edit'),
    url(r'^feature/list$', login_required(FeatureList.as_view()), name='feature_list'),
    url(r'^product/add$', login_required(ProductAdd.as_view()), name='product_add'),
    url(r'^product/delete/(?P<pk>\d+)/$', login_required(ProductDelete.as_view()), name="product_delete"),
    url(r'^product/edit/(?P<pk>\d+)/$', login_required(ProductEdit.as_view()),name='product_edit'),
    url(r'^product/list$', login_required(ProductList.as_view()), name='product_list'),
    url(r'^user/add$', UserAdd.as_view(), name='user_add'),
    url(r'^user/edit/(?P<pk>\d+)/$', login_required(UserEdit.as_view()), name='user_edit'),
    url(r'^user/list$', login_required(UserList.as_view()), name='user_list'),
    url(r'^user/login/$', UserLogin,name="user_login"),
    url(r'^user/logout/$', 'django.contrib.auth.views.logout',{'next_page': '/'},name='logout'),
    url(r'^user/register$', TemplateView.as_view(template_name='ticket/user/user_register.html')),
]
