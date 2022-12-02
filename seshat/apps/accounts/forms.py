from django import forms
from django.db.models.base import Model
from django.forms import ModelForm
from django.forms.widgets import Textarea

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.admin.widgets import FilteredSelectMultiple

from django.template.defaulttags import register
from .models import Seshat_Task, Seshat_Expert


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