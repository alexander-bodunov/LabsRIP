__author__ = 'Work'


from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views
from . import views



urlpatterns=[
    url(r'^admin/', admin.site.urls),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^login/', views.login_hand, name='login'),
    ##url(r'', views.logout_view, name='index'),
    url(r'',views.InitView.as_view(), name= 'init')
]
