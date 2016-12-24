__author__ = 'Work'
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import View
from django.contrib import auth
from django import forms
from django.contrib.auth.models import User
from . import models

class FormAuth(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class FormRegister(forms.Form):
    username=forms.CharField()
    password=forms.CharField()
    def save(self):
        user = User.objects.create_user(username=self.cleaned_data['username'],
                                        password=self.cleaned_data['password'],
                                        )
        return user

class FormAdd(forms.Form):
    name=forms.CharField()
    leader=forms.CharField()
    main_speciality=forms.CharField()
    number_of_members=forms.IntegerField()
    def save(self):
        user = models.Department.objects.create(name=self.cleaned_data['name'],
                                        leader=self.cleaned_data['leader'],
                                        main_speciality=self.cleaned_data['main_speciality'],
                                        number_of_members=self.cleaned_data['number_of_members'],
                                        )
        return user



class FormAddWorker(forms.Form):
    name=forms.CharField()
    gift=forms.IntegerField()
    def save(self,department_id):
        worker = models.Department.objects.create(name=self.cleaned_data['name'],
                                        gift=self.cleaned_data['leader'],
                                        department=department_id
                                        )
        return worker


'''class RegisterFormView(FormView):
    form_class = FormAuth
    success_url = "/"
    template_name = "register.html"
    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)
'''



# Функция для установки сессионного ключа.
# По нему django будет определять, выполнил ли вход пользователь.
from django.contrib.auth import login

'''class LoginFormView(FormView):
    form_class = AuthenticationForm
    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "login.html"
    # В случае успеха перенаправим на главную.
    success_url = "/"
    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()
        # Выполняем аутентификацию пользователя.
        auth.login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)
        '''

