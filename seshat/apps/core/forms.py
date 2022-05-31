from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from seshat.apps.core.models import VariableHierarchy


class SignUpForm(UserCreationForm):
    # first_name = forms.CharField(
    #     max_length=30, required=False, help_text='Optional.')
    # last_name = forms.CharField(
    #     max_length=30, required=False, help_text='Optional.')
    # email = forms.EmailField(
    #     max_length=254, help_text='Required. Inform a valid email address.')
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'type': 'password', 'align': 'center', 'placeholder': 'password'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'type': 'password', 'align': 'center', 'placeholder': 'password'}),
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', )
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control mb-3', }),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control mb-3', }),
            'username': forms.TextInput(
                attrs={'class': 'form-control mb-3', }),
            'email': forms.EmailInput(
                attrs={'class': 'form-control mb-3', }),
        }


class VariableHierarchyForm(forms.ModelForm):
    class Meta:
        model = VariableHierarchy
        fields = ('name', 'section', 'subsection')
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control  mb-3', }),
            'section': forms.Select(attrs={'class': 'form-control  mb-3', }),
            'subsection': forms.Select(attrs={'class': 'form-control  mb-3', }),
        }
