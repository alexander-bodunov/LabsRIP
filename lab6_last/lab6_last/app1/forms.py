__author__ = 'Work'
from django import forms
from . import models

class FormAdd(forms.Form):
    id=forms.IntegerField()
    name=forms.CharField()
    author=forms.CharField()
    description=forms.CharField()
    def save(self):
        con = models.Connection("root","toshiba19","lab6")
        db_connection=con.connect()
        b=models.Book(db_connection,self.cleaned_data['id'],
                      self.cleaned_data['name'],
                      self.cleaned_data['author'],
                      self.cleaned_data['description'])
        b.save()
