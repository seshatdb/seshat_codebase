from django import forms
from django.db.models.base import Model
from django.forms import ModelForm
from django.forms.widgets import Textarea

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.admin.widgets import FilteredSelectMultiple

from django.template.defaulttags import register
from .models import Seshat_Task, Seshat_Expert, Profile, User


class Seshat_TaskForm(forms.ModelForm):
    class Meta:
        model = Seshat_Task
        fields = ["giver", "taker", "task_description", "task_url"]
        labels = {
            'giver': 'Who are You? ',
            'taker': '<h5>Who needs to take the task?</h5><h6 class="text-secondary mt-1">Hold <kbd class="bg-success">Ctrl</kbd> to select multiple task-takers.</h6>',
            'task_description': '<h6>What is the task?</h6>',
            "task_url" : "Task URL"
        }
                
        widgets = {
        'giver': forms.Select(attrs={'class': 'form-control  mb-3', }),
        'taker': forms.SelectMultiple(attrs={'class': 'form-group mt-3 px-2', }),
        'task_description': forms.Textarea(attrs={'class': 'form-control  mb-3', }),
        'task_url': forms.TextInput(attrs={'class': 'form-control  mb-3', })
}

        
# class EditProfileForm(ModelForm):
#     class Meta:
#         model = User
#         fields = (
#                  'email',
#                  'first_name',
#                  'last_name'
#                 )
        
#         widgets = {
#         'email': forms.Textarea(attrs={'class': 'form-control  mb-3', }),
#         'first_name': forms.TextInput(attrs={'class': 'form-control  mb-3', }),
#         'last_name': forms.TextInput(attrs={'class': 'form-control  mb-3', }),
# }

class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=32)
    last_name = forms.CharField(max_length=32)
    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "role", "location", "bio", ]
        labels = {
            'first_name': "first_name",
            'last_name': "last_name",
            'role': 'role',
            'location': 'location',
            'bio': 'Bio',
        }
                
        widgets = {
         'bio': forms.Textarea(attrs={'class': 'form-control  mb-3', }),
#         'role': forms.TextInput(attrs={'class': 'form-control  mb-3', }),
#         'location': forms.TextInput(attrs={'class': 'form-control  mb-3', }),
#         'last_name': forms.TextInput(attrs={'class': 'form-control  mb-3', }),
#         'first_name': forms.TextInput(attrs={'class': 'form-control  mb-3', }),

}