#create this file

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class SignInForm(forms.Form):
    username=forms.CharField(required=True,label="User Name")
    password=forms.CharField(
        required=True,
        label='Password',
        widget=forms.PasswordInput()
    )

    def clean(self):
        username=self.cleaned_data['username']
        password = self.cleaned_data['password']
        user=authenticate(username=username,password=password)
        if user is None:
            raise forms.ValidationError('username or passwors is incorrect')

class SignUpForm(forms.Form):
    email = forms.EmailField(required=True, label="Email")
    username = forms.CharField(required=True, label="User Name")
    password = forms.CharField(
        required=True,
        label='Password',
        widget=forms.PasswordInput()
    )

#first this methos is called to check whether data is already present or not; internall it filters data based on unique data,here username is kept unique
    def clean(self):
        cleaned_data = self.cleaned_data
        if User.objects.filter(username=cleaned_data.get('username')).exists():                 #it is query set; it creates a query object internally then it is fired on db if present is returns result as list; it aslo implements lazy loading
            raise forms.ValidationError('Looks like a username with that email or password already exists')

        #lazy loading here it will not always fire query on db; it will fire the query only when it is used; e.g--> here we say if user.objects.filter..... so we are using the data hece query is fired