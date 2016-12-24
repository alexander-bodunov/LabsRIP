__author__ = 'Work'
from django.views.generic.base import TemplateView
from django.core.paginator import Paginator,InvalidPage
from . import models
from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
#from django.errors import InvalidPage,KeyError


data={
            'departments':[],
            'paginator':{
                'has_previous':False,
                'has_next':True,
                'num_pages':1,
                'previous_page_number':0,
                'next_page_number':2
            }
        }


class MyPaginator(View):
    def paginator(self,page_num):
        allDepartments=self.get_all_departments()
        paginator = Paginator(allDepartments, 3,allow_empty_first_page=True)
        data1=paginator.page(page_num)
        page_num=int(page_num)
        if data1 == False:
            return HttpResponse(":( Пустая страница")
        data["departments"]=[]
        for department in data1:
            data['departments'].append(department)
        count=allDepartments.count()
        pages=self.get_num_pages(count,3)
        datapag={}
        datapag['has_previous']=self.has_next(page_num,1)
        datapag['has_next']=self.has_next(page_num,pages)
        datapag['num_pages']=self.pages(pages)
        datapag['previous_page_number']=page_num-1
        datapag['next_page_number']=page_num+1
        datapag['n']=count
        datapag['Is']=True
        data['paginator']=datapag
        #data['user_name']=user.
        return data
    def get_all_departments(self):
        return models.Department.objects.all()
    #def count_all_departments:
        #return models.Department.objects.all.count()
    def has_next(self,x,y):
        if x==y:
            return False
        return True
    def get_num_pages(self,x,y):
        z=(x // y)
        if (x % y)!=0:
            z=z+1
        return z
    def pages(self,x):
        i=1
        while i<x+1:
            yield i
            i=i+1



class DepartmentsListView(TemplateView,MyPaginator):
    template_name="departments.html"
    def get_context_data(self, ** kwargs):
        try:
            page_num=super(DepartmentsListView, self).get_context_data(**kwargs)
        except KeyError:
            page_num=1
        if type(page_num) != int:
            if page_num == "":
                page_num = page_num["page_num"]
            else:
                page_num=page_num["page_num"]#int(page_num)
        return self.paginator(page_num)


class DepartmentsListViewFirst(TemplateView,MyPaginator):
    template_name="departments.html"
    def get_context_data(self, ** kwargs):
        page_num=1
        return self.paginator(page_num)

