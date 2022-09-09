from .models import Agricultural_population, Arable_land, Arable_land_per_farmer, Gross_grain_shared_per_agricultural_population, Net_grain_shared_per_agricultural_population, Surplus, Military_expense, Silver_inflow, Silver_stock, Total_population, Gdp_per_capita, Drought_event, Locust_event, Socioeconomic_turmoil_event, Crop_failure_event, Famine_event, Disease_outbreak
import datetime

from django import forms
from django.db.models.base import Model
from django.forms import ModelForm
from django.forms.widgets import Textarea

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.admin.widgets import FilteredSelectMultiple

from django.template.defaulttags import register

commonlabels = {
    'year_from': 'Start Year',
    'year_to': 'End Year',
    'tag': 'Certainty',
    'citations': 'Add one or more Citations',
    'finalized': 'This piece of data is verified.',
}

commonfields = ['polity', 'year_from', 'year_to',
                'description', 'tag', 'finalized', 'citations']

commonwidgets = {
    'polity': forms.Select(attrs={'class': 'form-control  mb-3', }),
    'year_from': forms.NumberInput(attrs={'class': 'form-control  mb-3', 'placeholder':'Ex: 1897, -24, +100'}),
    'year_to': forms.NumberInput(attrs={'class': 'form-control  mb-3', 'placeholder':'Ex: 1897, -24, +100'}),
    'description': Textarea(attrs={'class': 'form-control  mb-3', 'style': 'height: 140px', 'placeholder':'Add a meaningful description (optional)'}),
    'citations': forms.SelectMultiple(attrs={'class': 'form-control mb-3 js-states js-example-basic-multiple', 'text':'citations[]' , 'style': 'height: 340px', 'multiple': 'multiple'}),
    'tag': forms.Select(attrs={'class': 'form-control  mb-3', }),
    'finalized': forms.CheckboxInput(attrs={'class': ' mb-3', 'checked': True, }),
}

class Agricultural_populationForm(forms.ModelForm):
    class Meta:
        model = Agricultural_population
        fields = commonfields.copy()
        fields.append('agricultural_population')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['agricultural_population'] = forms.NumberInputwidgets['agricultural_population'] = forms.NumberInput
        

class Arable_landForm(forms.ModelForm):
    class Meta:
        model = Arable_land
        fields = commonfields.copy()
        fields.append('arable_land')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['arable_land'] = forms.NumberInputwidgets['arable_land'] = forms.NumberInput
        

class Arable_land_per_farmerForm(forms.ModelForm):
    class Meta:
        model = Arable_land_per_farmer
        fields = commonfields.copy()
        fields.append('arable_land_per_farmer')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['arable_land_per_farmer'] = forms.NumberInputwidgets['arable_land_per_farmer'] = forms.NumberInput
        

class Gross_grain_shared_per_agricultural_populationForm(forms.ModelForm):
    class Meta:
        model = Gross_grain_shared_per_agricultural_population
        fields = commonfields.copy()
        fields.append('gross_grain_shared_per_agricultural_population')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['gross_grain_shared_per_agricultural_population'] = forms.NumberInputwidgets['gross_grain_shared_per_agricultural_population'] = forms.NumberInput
        

class Net_grain_shared_per_agricultural_populationForm(forms.ModelForm):
    class Meta:
        model = Net_grain_shared_per_agricultural_population
        fields = commonfields.copy()
        fields.append('net_grain_shared_per_agricultural_population')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['net_grain_shared_per_agricultural_population'] = forms.NumberInputwidgets['net_grain_shared_per_agricultural_population'] = forms.NumberInput
        

class SurplusForm(forms.ModelForm):
    class Meta:
        model = Surplus
        fields = commonfields.copy()
        fields.append('surplus')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['surplus'] = forms.NumberInputwidgets['surplus'] = forms.NumberInput
        

class Military_expenseForm(forms.ModelForm):
    class Meta:
        model = Military_expense
        fields = commonfields.copy()
        fields.append('conflict')
        fields.append('expenditure')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['conflict'] = forms.TextInputwidgets['conflict'] = forms.TextInput
        widgets['expenditure'] = forms.NumberInputwidgets['expenditure'] = forms.NumberInput
        

class Silver_inflowForm(forms.ModelForm):
    class Meta:
        model = Silver_inflow
        fields = commonfields.copy()
        fields.append('silver_inflow')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['silver_inflow'] = forms.NumberInputwidgets['silver_inflow'] = forms.NumberInput
        

class Silver_stockForm(forms.ModelForm):
    class Meta:
        model = Silver_stock
        fields = commonfields.copy()
        fields.append('silver_stock')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['silver_stock'] = forms.NumberInputwidgets['silver_stock'] = forms.NumberInput
        

class Total_populationForm(forms.ModelForm):
    class Meta:
        model = Total_population
        fields = commonfields.copy()
        fields.append('total_population')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['total_population'] = forms.NumberInputwidgets['total_population'] = forms.NumberInput
        

class Gdp_per_capitaForm(forms.ModelForm):
    class Meta:
        model = Gdp_per_capita
        fields = commonfields.copy()
        fields.append('gdp_per_capita')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['gdp_per_capita'] = forms.NumberInputwidgets['gdp_per_capita'] = forms.NumberInput
        

class Drought_eventForm(forms.ModelForm):
    class Meta:
        model = Drought_event
        fields = commonfields.copy()
        fields.append('drought_event')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['drought_event'] = forms.NumberInputwidgets['drought_event'] = forms.NumberInput
        

class Locust_eventForm(forms.ModelForm):
    class Meta:
        model = Locust_event
        fields = commonfields.copy()
        fields.append('locust_event')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['locust_event'] = forms.NumberInputwidgets['locust_event'] = forms.NumberInput
        

class Socioeconomic_turmoil_eventForm(forms.ModelForm):
    class Meta:
        model = Socioeconomic_turmoil_event
        fields = commonfields.copy()
        fields.append('socioeconomic_turmoil_event')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['socioeconomic_turmoil_event'] = forms.NumberInputwidgets['socioeconomic_turmoil_event'] = forms.NumberInput
        

class Crop_failure_eventForm(forms.ModelForm):
    class Meta:
        model = Crop_failure_event
        fields = commonfields.copy()
        fields.append('crop_failure_event')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['crop_failure_event'] = forms.NumberInputwidgets['crop_failure_event'] = forms.NumberInput
        

class Famine_eventForm(forms.ModelForm):
    class Meta:
        model = Famine_event
        fields = commonfields.copy()
        fields.append('famine_event')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['famine_event'] = forms.NumberInputwidgets['famine_event'] = forms.NumberInput
        

class Disease_outbreakForm(forms.ModelForm):
    class Meta:
        model = Disease_outbreak
        fields = commonfields.copy()
        fields.append('longitude')
        fields.append('latitude')
        fields.append('elevation')
        fields.append('sub_category')
        fields.append('magnitude')
        fields.append('duration')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['longitude'] = forms.NumberInputwidgets['longitude'] = forms.NumberInput
        widgets['latitude'] = forms.NumberInputwidgets['latitude'] = forms.NumberInput
        widgets['elevation'] = forms.NumberInputwidgets['elevation'] = forms.NumberInput
        widgets['sub_category'] = forms.Selectwidgets['sub_category'] = forms.Select
        widgets['magnitude'] = forms.Selectwidgets['magnitude'] = forms.Select
        widgets['duration'] = forms.Selectwidgets['duration'] = forms.Select
        