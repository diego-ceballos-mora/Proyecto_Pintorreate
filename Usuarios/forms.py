#encoding: utf-8

from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create Users

class MyUserForm(UserCreationForm):
    """A form for creating new users. Includes all the required fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    avatar = models.ImageField(upload_to = 'avatar', blank = True)


    class Meta:
        model = Usuario
        fields = ('first_name', 'last_name', 'username')

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username = username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("Error al crear Usuario.")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1", "")
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            raise forms.ValidationError("Los dos password debe ser iguales.")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_staff = False
        user.is_superuser = False
        if commit:
            user.save()
        return user

class EditUserForm(forms.ModelForm):
    class Meta:
        model=Usuario

        fields=('username','first_name','last_name','email','password','avatar')
        exclude=('password',)



