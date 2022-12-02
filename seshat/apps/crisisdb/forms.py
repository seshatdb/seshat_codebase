from .models import Human_sacrifice, External_conflict, Internal_conflict, External_conflict_side, Agricultural_population, Arable_land, Arable_land_per_farmer, Gross_grain_shared_per_agricultural_population, Net_grain_shared_per_agricultural_population, Surplus, Military_expense, Silver_inflow, Silver_stock, Total_population, Gdp_per_capita, Drought_event, Locust_event, Socioeconomic_turmoil_event, Crop_failure_event, Famine_event, Disease_outbreak
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

class Human_sacrificeForm(forms.ModelForm):
    class Meta:
        model = Human_sacrifice
        fields = commonfields.copy()
        fields.append('human_sacrifice')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['human_sacrifice'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class External_conflictForm(forms.ModelForm):
    class Meta:
        model = External_conflict
        fields = commonfields.copy()
        fields.append('conflict_name')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['conflict_name'] = forms.TextInput(attrs={'class': 'form-control  mb-3', })
        

class Internal_conflictForm(forms.ModelForm):
    class Meta:
        model = Internal_conflict
        fields = commonfields.copy()
        fields.append('conflict')
        fields.append('expenditure')
        fields.append('leader')
        fields.append('casualty')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['conflict'] = forms.TextInput(attrs={'class': 'form-control  mb-3', })
        widgets['expenditure'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        widgets['leader'] = forms.TextInput(attrs={'class': 'form-control  mb-3', })
        widgets['casualty'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class External_conflict_sideForm(forms.ModelForm):
    class Meta:
        model = External_conflict_side
        fields = commonfields.copy()
        fields.append('conflict_id')
        fields.append('expenditure')
        fields.append('leader')
        fields.append('casualty')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['conflict_id'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        widgets['expenditure'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        widgets['leader'] = forms.TextInput(attrs={'class': 'form-control  mb-3', })
        widgets['casualty'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Agricultural_populationForm(forms.ModelForm):
    class Meta:
        model = Agricultural_population
        fields = commonfields.copy()
        fields.append('agricultural_population')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['agricultural_population'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Arable_landForm(forms.ModelForm):
    class Meta:
        model = Arable_land
        fields = commonfields.copy()
        fields.append('arable_land')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['arable_land'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Arable_land_per_farmerForm(forms.ModelForm):
    class Meta:
        model = Arable_land_per_farmer
        fields = commonfields.copy()
        fields.append('arable_land_per_farmer')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['arable_land_per_farmer'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Gross_grain_shared_per_agricultural_populationForm(forms.ModelForm):
    class Meta:
        model = Gross_grain_shared_per_agricultural_population
        fields = commonfields.copy()
        fields.append('gross_grain_shared_per_agricultural_population')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['gross_grain_shared_per_agricultural_population'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Net_grain_shared_per_agricultural_populationForm(forms.ModelForm):
    class Meta:
        model = Net_grain_shared_per_agricultural_population
        fields = commonfields.copy()
        fields.append('net_grain_shared_per_agricultural_population')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['net_grain_shared_per_agricultural_population'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class SurplusForm(forms.ModelForm):
    class Meta:
        model = Surplus
        fields = commonfields.copy()
        fields.append('surplus')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['surplus'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Military_expenseForm(forms.ModelForm):
    class Meta:
        model = Military_expense
        fields = commonfields.copy()
        fields.append('conflict')
        fields.append('expenditure')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['conflict'] = forms.TextInput(attrs={'class': 'form-control  mb-3', })
        widgets['expenditure'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Silver_inflowForm(forms.ModelForm):
    class Meta:
        model = Silver_inflow
        fields = commonfields.copy()
        fields.append('silver_inflow')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['silver_inflow'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Silver_stockForm(forms.ModelForm):
    class Meta:
        model = Silver_stock
        fields = commonfields.copy()
        fields.append('silver_stock')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['silver_stock'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Total_populationForm(forms.ModelForm):
    class Meta:
        model = Total_population
        fields = commonfields.copy()
        fields.append('total_population')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['total_population'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Gdp_per_capitaForm(forms.ModelForm):
    class Meta:
        model = Gdp_per_capita
        fields = commonfields.copy()
        fields.append('gdp_per_capita')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['gdp_per_capita'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Drought_eventForm(forms.ModelForm):
    class Meta:
        model = Drought_event
        fields = commonfields.copy()
        fields.append('drought_event')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['drought_event'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Locust_eventForm(forms.ModelForm):
    class Meta:
        model = Locust_event
        fields = commonfields.copy()
        fields.append('locust_event')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['locust_event'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Socioeconomic_turmoil_eventForm(forms.ModelForm):
    class Meta:
        model = Socioeconomic_turmoil_event
        fields = commonfields.copy()
        fields.append('socioeconomic_turmoil_event')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['socioeconomic_turmoil_event'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Crop_failure_eventForm(forms.ModelForm):
    class Meta:
        model = Crop_failure_event
        fields = commonfields.copy()
        fields.append('crop_failure_event')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['crop_failure_event'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Famine_eventForm(forms.ModelForm):
    class Meta:
        model = Famine_event
        fields = commonfields.copy()
        fields.append('famine_event')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['famine_event'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

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
        widgets['longitude'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        widgets['latitude'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        widgets['elevation'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        widgets['sub_category'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        widgets['magnitude'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        widgets['duration'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        