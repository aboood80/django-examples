from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        # User : is built in class and its attribuites are:
        # username, email, first_name, last_name, password
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        # UserProfileInfo : is model we created. 
        model = UserProfileInfo 
        # used to refer to User model with the same name"attributes"
        fields = ('portfolio_site', 'profile_pic')
