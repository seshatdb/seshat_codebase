from seshat.utils.utils import adder, dic_of_all_vars, list_of_all_Polities, dic_of_all_vars_in_sections

from django import forms
from django.forms import formset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from seshat.apps.core.models import Section, Subsection, Variablehierarchy
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


# class VariablehierarchyForm(forms.ModelForm):
#     my_vars = dic_of_all_vars()
#     my_vars_tuple = [(key, key) for key in my_vars.keys()]
#     print(my_vars_tuple)
#     name = forms.ChoiceField(
#         label="Variable Name",
#         widget=forms.Select(attrs={'class': 'form-control  mb-3', }), choices=my_vars_tuple)

#     class Meta:
#         model = Variablehierarchy
#         fields = ('name', 'section', 'subsection')
#         widgets = {
#             'section': forms.Select(attrs={'class': 'form-control  mb-3', }),
#             'subsection': forms.Select(attrs={'class': 'form-control  mb-3', }),
#         }

class VariablehierarchyFormNew(forms.Form):
    my_vars = dic_of_all_vars()
    my_vars_tuple = [('', ' -- Select Variable -- ')]
    # print(my_vars_tuple)
    all_sections = Section.objects.all()
    all_sections_tuple = [('', ' -- Select Section -- ')]
    for section in all_sections:
        my_section = section.name
        my_section_tuple = (my_section, my_section)
        all_sections_tuple.append(my_section_tuple)
    # subsections
    all_subsections = Subsection.objects.all()
    all_subsections_tuple = [('', ' -- Select Section First -- ')]
    for subsection in all_subsections:
        my_subsection = subsection.name
        my_subsection_tuple = (my_subsection, my_subsection)
        all_subsections_tuple.append(my_subsection_tuple)
    variable_name = forms.ChoiceField(
        label="Variable Name",
        widget=forms.Select(attrs={'class': 'form-control form-select mb-3', }), choices=my_vars_tuple)
    section_name = forms.ChoiceField(
        label="Section Name",
        widget=forms.Select(attrs={'class': 'form-control form-select mb-3 required-entry',
                                'name': "section",
                                'id': "section",
                                'onchange': "javascript: dynamicdropdown(this.options[this.selectedIndex].value);"
                                }), choices=all_sections_tuple)
    subsection_name = forms.ChoiceField(
        label="Subsection Name",
        widget=forms.Select(attrs={'class': 'form-control form-select mb-3',
                                'name': "subsection",
                                'id': "subsection", }), choices=all_subsections_tuple)
    # forms.CheckboxInput(attrs={'class': 'form-control mb-3', })
    is_verified = forms.BooleanField(
        label=" Verified?", required=False, widget=forms.CheckboxInput(attrs={'type': 'checkbox', 'class': 'form-control form-check-input align-middle'}))

# VarHierFormSet = formset_factory(VariablehierarchyForm, extra=10)
