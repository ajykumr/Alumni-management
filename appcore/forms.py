from django.forms import ModelForm, formset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class  AlumniForm(ModelForm):
    class Meta:
        model = Alumni
        fields = '__all__'
        exclude = ['staff','status']
        widgets = {
           'birthdate': forms.DateInput(format=('%d %B, %Y'), attrs={'type':"date"}),
        }


class  EmployerForm(ModelForm):
    class Meta:
        model = Employer
        fields = '__all__'
        exclude = ['alumni']


class  AlumniUpdateForm(ModelForm):
    class Meta:
        model = Alumni
        fields = '__all__'
        widgets = {
           'birthdate': forms.DateInput(format=('%d %B, %Y'), attrs={'type':"date"}),
           'staff': forms.TextInput(attrs={'type': 'hidden'}),
           'usn': forms.TextInput(attrs={'type': 'hidden'})
        }

class CreateStaffForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'email', 'password1', 'password2']

class StaffAccountForm(ModelForm):
    class Meta:
        model = StaffAccount
        fields = '__all__'
        exclude = ['user']


EmployerFormset = formset_factory(EmployerForm ,extra=2)
