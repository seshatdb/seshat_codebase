from seshat.utils.utils import adder, dic_of_all_vars, list_of_all_Polities, dic_of_all_vars_in_sections

from django import forms
from django.forms import formset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from seshat.apps.core.models import Section, VariableHierarchy
from django.core.exceptions import NON_FIELD_ERRORS
from crispy_forms.helper import FormHelper


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


# class VariableHierarchyForm(forms.ModelForm):
#     my_vars = dic_of_all_vars()
#     my_vars_tuple = [(key, key) for key in my_vars.keys()]
#     print(my_vars_tuple)
#     name = forms.ChoiceField(
#         label="Variable Name",
#         widget=forms.Select(attrs={'class': 'form-control  mb-3', }), choices=my_vars_tuple)

#     class Meta:
#         model = VariableHierarchy
#         fields = ('name', 'section', 'subsection')
#         widgets = {
#             'section': forms.Select(attrs={'class': 'form-control  mb-3', }),
#             'subsection': forms.Select(attrs={'class': 'form-control  mb-3', }),
#         }


class VariableHierarchyForm(forms.ModelForm):
    my_vars = dic_of_all_vars()
    my_vars_tuple = [(key, key) for key in my_vars.keys()]
    # print(my_vars_tuple)
    all_sections = Section.objects.all()
    my_sections_tuple = [(key.id, key.name) for key in all_sections]
    name = forms.ChoiceField(
        label="Variable Name",
        widget=forms.Select(attrs={'class': 'form-control form-select mb-3', }), choices=my_vars_tuple)

    class Meta:
        model = VariableHierarchy
        fields = ('name', 'section', 'subsection', 'is_verified')
        widgets = {
            'section': forms.Select(attrs={
                'class': 'form-control form-select mb-3 required-entry',
                'name': "section",
                'id': "section",
                'onchange': "javascript: dynamicdropdown(this.options[this.selectedIndex].value);"}),
            'subsection': forms.Select(attrs={
                'class': 'form-control form-select mb-3',
                'name': "subsection",
                'id': "subsection", },),
            'is_verified': forms.CheckboxInput(attrs={'class': 'form-control mb-3', }),
        }
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }

    def __init__(self, *args, **kwargs):
        super(VariableHierarchyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = True

# VarHierFormSet = formset_factory(VariableHierarchyForm, extra=10)
