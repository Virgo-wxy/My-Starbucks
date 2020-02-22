# -- coding: utf-8 --
from django import forms


class UserForm(forms.Form):
    username=forms.CharField(label='user name',max_length=200)
    password=forms.CharField(label='user password',widget=forms.PasswordInput)