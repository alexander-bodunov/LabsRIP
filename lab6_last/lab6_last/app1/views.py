from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView
from . import models
from . import forms
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

data={
    'books':[]
}

data1={
    'shops':[]
}

class BookView(TemplateView,View):
    template_name = 'book.html'
    def _get(self,id_selected):
        data['books']=[]
        con=models.Connection("root","toshiba19","lab6")
        db_connection=con.connect()
        my_book=models.Book(db_connection)
        my_book1=my_book._get_one(id_selected)
        for book in my_book1:
            data['books'].append(book)
    def get_context_data(self, **kwargs):
        context=super(BookView, self).get_context_data(**kwargs)
        self._get(context['id_selected'])
        context1=data['books'][0]
        context['name']=context1['name']
        context['author']=context1['author']
        context['description']=context1['description']
        return context


class BooksView(View):
    def get(self, request):
        data['books']=[]
        con=models.Connection("root","toshiba19","lab6")
        db_connection=con.connect()
        my_book=models.Book(db_connection)._get_all()
        for book in my_book:
            data['books'].append(book)
        return render(request, 'books.html',data)

def add(request):
    redirect_url = '/'
    if request.method == 'POST':
        form = forms.FormAdd(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/')
    else:
        form = forms.FormAdd()
    return render(request, 'add.html', {'form': form,'continue': redirect_url})

class ShopsView(View):
    def get(self,request):
        data1['shops']=[]
        shops=models.Shop.objects.all()
        for shop in shops:
            data1['shops'].append(shop)
        return render(request,"shop.html",data1)


