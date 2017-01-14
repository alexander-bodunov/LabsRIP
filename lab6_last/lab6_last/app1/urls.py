__author__ = 'Work'
from django.conf.urls import url
from . import views
from . import models

urlpatterns = [
    url(r'0/0/0/orm',views.ShopsView.as_view(),name="orm"),
    url(r'0/0/clear_all',models.Book(models.Connection("root","toshiba19","lab6").connect())._clear_all,name="delete"),
    url(r'^0/add',views.add,name="add_url"),
    url(r'^book/(?P<id_selected>.)$',views.BookView.as_view(),name="book"),
    url(r'^',views.BooksView.as_view(),name="books")
]