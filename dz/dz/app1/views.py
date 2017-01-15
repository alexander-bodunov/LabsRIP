from django.shortcuts import render
from . import models
from . import forms
from django.views.generic import View
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib import auth
from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.


#b=models.Department.objects.get(pk=1)


data={
            'departments':[]
        }


def get_department(id_chosen):
    return models.Department.objects.filter(pk=id_chosen)#get()#pk=id_chosen | number_of_members < 10)

def get_workers(id_chosen):
    return models.Worker.objects.filter(department=id_chosen).values()

def get_single_worker(id_chosen):
    return models.Worker.objects.filter(id=id_chosen).values()

class DepartmentsView(View):
    def get(self,request):
        allDepartments=self.get_all_departments()
        for department in allDepartments:
            data['departments'].append(department)
        #data['user_name']=user.
        return render(request,'departments.html',data)

    def get_all_departments(self):
        return models.Department.objects.all()

class SingleDepartmentView(TemplateView):
    template_name='single_department.html'
    '''def get_department(self,id_choosen):
        return models.Department.objects(id=id_choosen)'''
    '''def get_essential(self, **kwargs):
        context=super(SingleDepartmentView, self).get_context_data(**kwargs)
        return context["department_id"]'''
    def get_context_data(self, **kwargs):
        context=super(SingleDepartmentView, self).get_context_data(**kwargs)
        '''
        #context1=context
        #con=context1['department_id']
        context1= models.Department.objects.get(pk=context['department_id'])'''
        context_copy=get_department(context['department_id'])
        context_worker=get_workers(context['department_id'])
        a=context_copy[0]
        context['name']=a.name
        context['leader']=a.leader
        context['main_speciality']=a.main_speciality
        context['number_of_members']=a.number_of_members
        context['workers']=context_worker
        return context

class WorkerView(TemplateView):
    template_name='worker.html'
    def get_context_data(self, **kwargs):
        context=super(WorkerView, self).get_context_data(**kwargs)
        context_worker=get_single_worker(context['worker_id'])
        context_worker=context_worker[0]
        context['name']= context_worker['name']
        context['gift']=context_worker['gift']
        context['photo']=context_worker['photo']
        return context





def login(request):
    redirect_url = '/'
    if request.method == 'POST':
        redirect_url = '/'
        form = forms.FormAuth(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data['username'],
                                     password=form.cleaned_data['password'])
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect(redirect_url)
            else:
                form.add_error(None, 'invalid login/password')
    else:
        form=forms.FormAuth()
    return render(request, 'login.html', {'form':form, 'continue': redirect_url})


def register(request):
    redirect_url = '/'
    if request.method == 'POST':
        form = forms.FormRegister(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/autenfication/')
    else:
        form = forms.FormRegister()
    return render(request, 'register.html', {'form': form,'continue': redirect_url})

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




#class DepartmentCreate(TemplateView):

    #def post(self,request, *args, **kwargs):