__author__ = 'Work'
from django.conf.urls import url, include
from django.contrib import admin
from . import views
from . import twviews
from . import forms
from django.contrib.auth.views import login as my_login
from django.views.generic.base import TemplateView


urlpatterns = [
    #url(r'^autenfication/$',forms.LoginFormView.as_view(),name="autenfication_url"),
    #url(r'^register/$',forms.RegisterFormView.as_view(),name="login_url"),
    url(r'^autenfication/$',views.login,name="autenfication_url"),
    url(r'^register/$',views.register,name="login_url"),
    #url(r'^/0/0/0/(?P<department_id>.)$',views.add_worker,name="worker_add"),
    url(r'^add/$',views.add,name="add_url"),
    #url(r'^addworker',views.addworker,name="add_worker"),
    url(r'^0/0/(?P<page_num>.)$',twviews.DepartmentsListView.as_view(),name='departments_url_pag'),
    url(r'^0/(?P<worker_id>.)$',views.WorkerView.as_view(),name='worker_url'),
    url(r'(?P<department_id>.)',views.SingleDepartmentView.as_view(),name='single_department_url'),
    #url(r'^',views.DepartmentsView.as_view(),name='departments_url'),
    url(r'',twviews.DepartmentsListViewFirst.as_view(),name='departments_url'),
        ]


#(?P<page_num>.)?