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
from ticket.views import SaleAdd, SaleDelete,SaleEdit, SaleList, UserAdd, ItemAdd,ItemDelete,\
    ItemEdit, ItemList, ItemSearch, StatusAdd, StatusDelete, StatusEdit, StatusList, UserEdit, UserList,\
    UserLogin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',TemplateView.as_view(template_name='ticket/base/base.html')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sale/add$', login_required(SaleAdd.as_view()), name="sale_add"),
    url(r'^sale/delete/(?P<pk>\d+)/$', login_required(SaleDelete.as_view()), name="sale_delete"),
    url(r'^sale/edit/(?P<pk>\d+)/$', login_required(SaleEdit.as_view()), name="sale_edit"),
    url(r'^sale/list$', login_required(SaleList.as_view()), name="sale_list"),
    url(r'^item/add$', login_required(ItemAdd.as_view()), name='item_add'),
    url(r'^item/delete/(?P<pk>\d+)/$', login_required(ItemDelete.as_view()), name="item_delete"),
    url(r'^item/edit/(?P<pk>\d+)/$', login_required(ItemEdit.as_view()),name='item_edit'),
    url(r'^item/list$', login_required(ItemList.as_view()), name='item_list'),
    url(r'^item/search$', login_required(ItemSearch.as_view()), name='item_search'),
    url(r'^status/add$', login_required(StatusAdd.as_view()), name='status_add'),
    url(r'^status/delete/(?P<pk>\d+)/$', login_required(StatusDelete.as_view()), name="status_delete"),
    url(r'^status/edit/(?P<pk>\d+)/$', login_required(StatusEdit.as_view()),name='status_edit'),
    url(r'^status/list$', login_required(StatusList.as_view()), name='status_list'),
    url(r'^user/add$', UserAdd.as_view(), name='user_add'),
    url(r'^user/edit/(?P<pk>\d+)/$', login_required(UserEdit.as_view()), name='user_edit'),
    url(r'^user/list$', UserList.as_view(), name='user_list'),
    url(r'^user/login/$', UserLogin,name="user_login"),
    url(r'^user/logout/$', views.logout ,name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
