
from seshat.utils.utils import adder, dic_of_all_vars, list_of_all_Polities, dic_of_all_vars_in_sections, dic_of_all_vars_with_varhier
from django.db.models.base import Model
# from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.safestring import mark_safe
from django.views.generic.list import ListView

from django.contrib.contenttypes.models import ContentType

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.http import HttpResponseRedirect, response, JsonResponse
from ..core.models import Citation, Reference, Polity, Section, Subsection, Country, Variablehierarchy

# from .mycodes import *
from django.conf import settings

from django.urls import reverse, reverse_lazy

from django.views import generic
import csv
import datetime

from django.core.paginator import Paginator

from django.http import HttpResponse

import requests
from requests.structures import CaseInsensitiveDict



from .models import Agricultural_population, Arable_land, Arable_land_per_farmer, Gross_grain_shared_per_agricultural_population, Net_grain_shared_per_agricultural_population, Surplus, Military_expense, Silver_inflow, Silver_stock, Total_population, Gdp_per_capita, Drought_event, Locust_event, Socioeconomic_turmoil_event, Crop_failure_event, Famine_event, Disease_outbreak


from .forms import Agricultural_populationForm, Arable_landForm, Arable_land_per_farmerForm, Gross_grain_shared_per_agricultural_populationForm, Net_grain_shared_per_agricultural_populationForm, SurplusForm, Military_expenseForm, Silver_inflowForm, Silver_stockForm, Total_populationForm, Gdp_per_capitaForm, Drought_eventForm, Locust_eventForm, Socioeconomic_turmoil_eventForm, Crop_failure_eventForm, Famine_eventForm, Disease_outbreakForm

class Agricultural_populationCreate(PermissionRequiredMixin, CreateView):
    model = Agricultural_population
    form_class = Agricultural_populationForm
    template_name = "crisisdb/agricultural_population/agricultural_population_form.html"
    #permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('agricultural_population-create')
    def get_context_data(self, **kwargs):
        # get the explanattion:
        all_var_hiers = Variablehierarchy.objects.all()
        for item in all_var_hiers:
            if item.name == "Agricultural Population":
                my_exp = item.explanation
                my_sec = item.section.name
                my_subsec = item.subsection.name
                my_name = item.name
                break
            else:
                my_exp = "No_Explanations"
                my_sec = "No_SECTION"
                my_subsec = "NO_SUBSECTION"
                my_name = "NO_NAME"
        context = super().get_context_data(**kwargs)
        context["mysection"] = my_sec
        context["mysubsection"] = my_subsec
        context["myvar"] = my_name
        context["my_exp"] = my_exp

        return context


class Agricultural_populationUpdate(PermissionRequiredMixin, UpdateView):
    model = Agricultural_population
    form_class = Agricultural_populationForm
    template_name = "crisisdb/agricultural_population/agricultural_population_update.html"
    #permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Agricultural Population"

        return context

class Agricultural_populationDelete(PermissionRequiredMixin, DeleteView):
    model = Agricultural_population
    success_url = reverse_lazy('agricultural_populations')
    template_name = "core/delete_general.html"
    #permission_required = 'catalog.can_mark_returned'


class Agricultural_populationListView(generic.ListView):
    model = Agricultural_population
    template_name = "crisisdb/agricultural_population/agricultural_population_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('agricultural_populations')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Agricultural Population"

        return context
        
class Agricultural_populationDetailView(generic.DetailView):
    model = Agricultural_population
    template_name = "crisisdb/agricultural_population/agricultural_population_detail.html"


#@permission_required('admin.can_add_log_entry')
def agricultural_population_download(request):
    items = Agricultural_population.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="agricultural_populations.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'agricultural_population', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.agricultural_population, ])

    return response

        

class Arable_landCreate(PermissionRequiredMixin, CreateView):
    model = Arable_land
    form_class = Arable_landForm
    template_name = "crisisdb/arable_land/arable_land_form.html"
    #permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('arable_land-create')
    def get_context_data(self, **kwargs):
        # get the explanattion:
        all_var_hiers = Variablehierarchy.objects.all()
        for item in all_var_hiers:
            if item.name == "Arable Land":
                my_exp = item.explanation
                my_sec = item.section.name
                my_subsec = item.subsection.name
                my_name = item.name
                break
            else:
                my_exp = "No_Explanations"
                my_sec = "No_SECTION"
                my_subsec = "NO_SUBSECTION"
                my_name = "NO_NAME"
        context = super().get_context_data(**kwargs)
        context["mysection"] = my_sec
        context["mysubsection"] = my_subsec
        context["myvar"] = my_name
        context["my_exp"] = my_exp

        return context


class Arable_landUpdate(PermissionRequiredMixin, UpdateView):
    model = Arable_land
    form_class = Arable_landForm
    template_name = "crisisdb/arable_land/arable_land_update.html"
    #permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Arable Land"

        return context

class Arable_landDelete(PermissionRequiredMixin, DeleteView):
    model = Arable_land
    success_url = reverse_lazy('arable_lands')
    template_name = "core/delete_general.html"
    #permission_required = 'catalog.can_mark_returned'


class Arable_landListView(generic.ListView):
    model = Arable_land
    template_name = "crisisdb/arable_land/arable_land_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('arable_lands')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Arable Land"

        return context
        
class Arable_landDetailView(generic.DetailView):
    model = Arable_land
    template_name = "crisisdb/arable_land/arable_land_detail.html"


#@permission_required('admin.can_add_log_entry')
def arable_land_download(request):
    items = Arable_land.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="arable_lands.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'arable_land', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.arable_land, ])

    return response

        

class Arable_land_per_farmerCreate(PermissionRequiredMixin, CreateView):
    model = Arable_land_per_farmer
    form_class = Arable_land_per_farmerForm
    template_name = "crisisdb/arable_land_per_farmer/arable_land_per_farmer_form.html"
    #permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('arable_land_per_farmer-create')
    def get_context_data(self, **kwargs):
        # get the explanattion:
        all_var_hiers = Variablehierarchy.objects.all()
        for item in all_var_hiers:
            if item.name == "Arable Land Per Farmer":
                my_exp = item.explanation
                my_sec = item.section.name
                my_subsec = item.subsection.name
                my_name = item.name
                break
            else:
                my_exp = "No_Explanations"
                my_sec = "No_SECTION"
                my_subsec = "NO_SUBSECTION"
                my_name = "NO_NAME"
        context = super().get_context_data(**kwargs)
        context["mysection"] = my_sec
        context["mysubsection"] = my_subsec
        context["myvar"] = my_name
        context["my_exp"] = my_exp

        return context


class Arable_land_per_farmerUpdate(PermissionRequiredMixin, UpdateView):
    model = Arable_land_per_farmer
    form_class = Arable_land_per_farmerForm
    template_name = "crisisdb/arable_land_per_farmer/arable_land_per_farmer_update.html"
    #permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Arable Land Per Farmer"

        return context

class Arable_land_per_farmerDelete(PermissionRequiredMixin, DeleteView):
    model = Arable_land_per_farmer
    success_url = reverse_lazy('arable_land_per_farmers')
    template_name = "core/delete_general.html"
    #permission_required = 'catalog.can_mark_returned'


class Arable_land_per_farmerListView(generic.ListView):
    model = Arable_land_per_farmer
    template_name = "crisisdb/arable_land_per_farmer/arable_land_per_farmer_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('arable_land_per_farmers')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Arable Land Per Farmer"

        return context
        
class Arable_land_per_farmerDetailView(generic.DetailView):
    model = Arable_land_per_farmer
    template_name = "crisisdb/arable_land_per_farmer/arable_land_per_farmer_detail.html"


#@permission_required('admin.can_add_log_entry')
def arable_land_per_farmer_download(request):
    items = Arable_land_per_farmer.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="arable_land_per_farmers.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'arable_land_per_farmer', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.arable_land_per_farmer, ])

    return response

        

class Gross_grain_shared_per_agricultural_populationCreate(PermissionRequiredMixin, CreateView):
    model = Gross_grain_shared_per_agricultural_population
    form_class = Gross_grain_shared_per_agricultural_populationForm
    template_name = "crisisdb/gross_grain_shared_per_agricultural_population/gross_grain_shared_per_agricultural_population_form.html"
    #permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('gross_grain_shared_per_agricultural_population-create')
    def get_context_data(self, **kwargs):
        # get the explanattion:
        all_var_hiers = Variablehierarchy.objects.all()
        for item in all_var_hiers:
            if item.name == "Gross Grain Shared Per Agricultural Population":
                my_exp = item.explanation
                my_sec = item.section.name
                my_subsec = item.subsection.name
                my_name = item.name
                break
            else:
                my_exp = "No_Explanations"
                my_sec = "No_SECTION"
                my_subsec = "NO_SUBSECTION"
                my_name = "NO_NAME"
        context = super().get_context_data(**kwargs)
        context["mysection"] = my_sec
        context["mysubsection"] = my_subsec
        context["myvar"] = my_name
        context["my_exp"] = my_exp

        return context


class Gross_grain_shared_per_agricultural_populationUpdate(PermissionRequiredMixin, UpdateView):
    model = Gross_grain_shared_per_agricultural_population
    form_class = Gross_grain_shared_per_agricultural_populationForm
    template_name = "crisisdb/gross_grain_shared_per_agricultural_population/gross_grain_shared_per_agricultural_population_update.html"
    #permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Gross Grain Shared Per Agricultural Population"

        return context

class Gross_grain_shared_per_agricultural_populationDelete(PermissionRequiredMixin, DeleteView):
    model = Gross_grain_shared_per_agricultural_population
    success_url = reverse_lazy('gross_grain_shared_per_agricultural_populations')
    template_name = "core/delete_general.html"
    #permission_required = 'catalog.can_mark_returned'


class Gross_grain_shared_per_agricultural_populationListView(generic.ListView):
    model = Gross_grain_shared_per_agricultural_population
    template_name = "crisisdb/gross_grain_shared_per_agricultural_population/gross_grain_shared_per_agricultural_population_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('gross_grain_shared_per_agricultural_populations')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Gross Grain Shared Per Agricultural Population"

        return context
        
class Gross_grain_shared_per_agricultural_populationDetailView(generic.DetailView):
    model = Gross_grain_shared_per_agricultural_population
    template_name = "crisisdb/gross_grain_shared_per_agricultural_population/gross_grain_shared_per_agricultural_population_detail.html"


#@permission_required('admin.can_add_log_entry')
def gross_grain_shared_per_agricultural_population_download(request):
    items = Gross_grain_shared_per_agricultural_population.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="gross_grain_shared_per_agricultural_populations.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'gross_grain_shared_per_agricultural_population', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.gross_grain_shared_per_agricultural_population, ])

    return response

        

class Net_grain_shared_per_agricultural_populationCreate(PermissionRequiredMixin, CreateView):
    model = Net_grain_shared_per_agricultural_population
    form_class = Net_grain_shared_per_agricultural_populationForm
    template_name = "crisisdb/net_grain_shared_per_agricultural_population/net_grain_shared_per_agricultural_population_form.html"
    #permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('net_grain_shared_per_agricultural_population-create')
    def get_context_data(self, **kwargs):
        # get the explanattion:
        all_var_hiers = Variablehierarchy.objects.all()
        for item in all_var_hiers:
            if item.name == "Net Grain Shared Per Agricultural Population":
                my_exp = item.explanation
                my_sec = item.section.name
                my_subsec = item.subsection.name
                my_name = item.name
                break
            else:
                my_exp = "No_Explanations"
                my_sec = "No_SECTION"
                my_subsec = "NO_SUBSECTION"
                my_name = "NO_NAME"
        context = super().get_context_data(**kwargs)
        context["mysection"] = my_sec
        context["mysubsection"] = my_subsec
        context["myvar"] = my_name
        context["my_exp"] = my_exp

        return context


class Net_grain_shared_per_agricultural_populationUpdate(PermissionRequiredMixin, UpdateView):
    model = Net_grain_shared_per_agricultural_population
    form_class = Net_grain_shared_per_agricultural_populationForm
    template_name = "crisisdb/net_grain_shared_per_agricultural_population/net_grain_shared_per_agricultural_population_update.html"
    #permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Net Grain Shared Per Agricultural Population"

        return context

class Net_grain_shared_per_agricultural_populationDelete(PermissionRequiredMixin, DeleteView):
    model = Net_grain_shared_per_agricultural_population
    success_url = reverse_lazy('net_grain_shared_per_agricultural_populations')
    template_name = "core/delete_general.html"
    #permission_required = 'catalog.can_mark_returned'


class Net_grain_shared_per_agricultural_populationListView(generic.ListView):
    model = Net_grain_shared_per_agricultural_population
    template_name = "crisisdb/net_grain_shared_per_agricultural_population/net_grain_shared_per_agricultural_population_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('net_grain_shared_per_agricultural_populations')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Net Grain Shared Per Agricultural Population"

        return context
        
class Net_grain_shared_per_agricultural_populationDetailView(generic.DetailView):
    model = Net_grain_shared_per_agricultural_population
    template_name = "crisisdb/net_grain_shared_per_agricultural_population/net_grain_shared_per_agricultural_population_detail.html"


#@permission_required('admin.can_add_log_entry')
def net_grain_shared_per_agricultural_population_download(request):
    items = Net_grain_shared_per_agricultural_population.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="net_grain_shared_per_agricultural_populations.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'net_grain_shared_per_agricultural_population', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.net_grain_shared_per_agricultural_population, ])

    return response

        

class SurplusCreate(PermissionRequiredMixin, CreateView):
    model = Surplus
    form_class = SurplusForm
    template_name = "crisisdb/surplus/surplus_form.html"
    #permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('surplus-create')
    def get_context_data(self, **kwargs):
        # get the explanattion:
        all_var_hiers = Variablehierarchy.objects.all()
        for item in all_var_hiers:
            if item.name == "Surplus":
                my_exp = item.explanation
                my_sec = item.section.name
                my_subsec = item.subsection.name
                my_name = item.name
                break
            else:
                my_exp = "No_Explanations"
                my_sec = "No_SECTION"
                my_subsec = "NO_SUBSECTION"
                my_name = "NO_NAME"
        context = super().get_context_data(**kwargs)
        context["mysection"] = my_sec
        context["mysubsection"] = my_subsec
        context["myvar"] = my_name
        context["my_exp"] = my_exp

        return context


class SurplusUpdate(PermissionRequiredMixin, UpdateView):
    model = Surplus
    form_class = SurplusForm
    template_name = "crisisdb/surplus/surplus_update.html"
    #permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Surplus"

        return context

class SurplusDelete(PermissionRequiredMixin, DeleteView):
    model = Surplus
    success_url = reverse_lazy('surplus')
    template_name = "core/delete_general.html"
    #permission_required = 'catalog.can_mark_returned'


class SurplusListView(generic.ListView):
    model = Surplus
    template_name = "crisisdb/surplus/surplus_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('surplus')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Surplus"

        return context
        
class SurplusDetailView(generic.DetailView):
    model = Surplus
    template_name = "crisisdb/surplus/surplus_detail.html"


#@permission_required('admin.can_add_log_entry')
def surplus_download(request):
    items = Surplus.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="surplus.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'surplus', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.surplus, ])

    return response

        

class Military_expenseCreate(PermissionRequiredMixin, CreateView):
    model = Military_expense
    form_class = Military_expenseForm
    template_name = "crisisdb/military_expense/military_expense_form.html"
    #permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('military_expense-create')
    def get_context_data(self, **kwargs):
        # get the explanattion:
        all_var_hiers = Variablehierarchy.objects.all()
        for item in all_var_hiers:
            if item.name == "Conflict":
                my_exp = item.explanation
                my_sec = item.section.name
                my_subsec = item.subsection.name
                my_name = item.name
                break
            else:
                my_exp = "No_Explanations"
                my_sec = "No_SECTION"
                my_subsec = "NO_SUBSECTION"
                my_name = "NO_NAME"
        context = super().get_context_data(**kwargs)
        context["mysection"] = my_sec
        context["mysubsection"] = my_subsec
        context["myvar"] = my_name
        context["my_exp"] = my_exp

        return context


class Military_expenseUpdate(PermissionRequiredMixin, UpdateView):
    model = Military_expense
    form_class = Military_expenseForm
    template_name = "crisisdb/military_expense/military_expense_update.html"
    #permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Conflict"

        return context

class Military_expenseDelete(PermissionRequiredMixin, DeleteView):
    model = Military_expense
    success_url = reverse_lazy('military_expenses')
    template_name = "core/delete_general.html"
    #permission_required = 'catalog.can_mark_returned'


class Military_expenseListView(generic.ListView):
    model = Military_expense
    template_name = "crisisdb/military_expense/military_expense_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('military_expenses')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Conflict"

        return context
        
class Military_expenseDetailView(generic.DetailView):
    model = Military_expense
    template_name = "crisisdb/military_expense/military_expense_detail.html"


#@permission_required('admin.can_add_log_entry')
def military_expense_download(request):
    items = Military_expense.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="military_expenses.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'conflict', 'expenditure', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.conflict, obj.expenditure, ])

    return response

        

class Silver_inflowCreate(PermissionRequiredMixin, CreateView):
    model = Silver_inflow
    form_class = Silver_inflowForm
    template_name = "crisisdb/silver_inflow/silver_inflow_form.html"
    #permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('silver_inflow-create')
    def get_context_data(self, **kwargs):
        # get the explanattion:
        all_var_hiers = Variablehierarchy.objects.all()
        for item in all_var_hiers:
            if item.name == "Silver Inflow":
                my_exp = item.explanation
                my_sec = item.section.name
                my_subsec = item.subsection.name
                my_name = item.name
                break
            else:
                my_exp = "No_Explanations"
                my_sec = "No_SECTION"
                my_subsec = "NO_SUBSECTION"
                my_name = "NO_NAME"
        context = super().get_context_data(**kwargs)
        context["mysection"] = my_sec
        context["mysubsection"] = my_subsec
        context["myvar"] = my_name
        context["my_exp"] = my_exp

        return context


class Silver_inflowUpdate(PermissionRequiredMixin, UpdateView):
    model = Silver_inflow
    form_class = Silver_inflowForm
    template_name = "crisisdb/silver_inflow/silver_inflow_update.html"
    #permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Silver Inflow"

        return context

class Silver_inflowDelete(PermissionRequiredMixin, DeleteView):
    model = Silver_inflow
    success_url = reverse_lazy('silver_inflows')
    template_name = "core/delete_general.html"
    #permission_required = 'catalog.can_mark_returned'


class Silver_inflowListView(generic.ListView):
    model = Silver_inflow
    template_name = "crisisdb/silver_inflow/silver_inflow_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('silver_inflows')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Silver Inflow"

        return context
        
class Silver_inflowDetailView(generic.DetailView):
    model = Silver_inflow
    template_name = "crisisdb/silver_inflow/silver_inflow_detail.html"


#@permission_required('admin.can_add_log_entry')
def silver_inflow_download(request):
    items = Silver_inflow.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="silver_inflows.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'silver_inflow', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.silver_inflow, ])

    return response

        

class Silver_stockCreate(PermissionRequiredMixin, CreateView):
    model = Silver_stock
    form_class = Silver_stockForm
    template_name = "crisisdb/silver_stock/silver_stock_form.html"
    #permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('silver_stock-create')
    def get_context_data(self, **kwargs):
        # get the explanattion:
        all_var_hiers = Variablehierarchy.objects.all()
        for item in all_var_hiers:
            if item.name == "Silver Stock":
                my_exp = item.explanation
                my_sec = item.section.name
                my_subsec = item.subsection.name
                my_name = item.name
                break
            else:
                my_exp = "No_Explanations"
                my_sec = "No_SECTION"
                my_subsec = "NO_SUBSECTION"
                my_name = "NO_NAME"
        context = super().get_context_data(**kwargs)
        context["mysection"] = my_sec
        context["mysubsection"] = my_subsec
        context["myvar"] = my_name
        context["my_exp"] = my_exp

        return context


class Silver_stockUpdate(PermissionRequiredMixin, UpdateView):
    model = Silver_stock
    form_class = Silver_stockForm
    template_name = "crisisdb/silver_stock/silver_stock_update.html"
    #permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Silver Stock"

        return context

class Silver_stockDelete(PermissionRequiredMixin, DeleteView):
    model = Silver_stock
    success_url = reverse_lazy('silver_stocks')
    template_name = "core/delete_general.html"
    #permission_required = 'catalog.can_mark_returned'


class Silver_stockListView(generic.ListView):
    model = Silver_stock
    template_name = "crisisdb/silver_stock/silver_stock_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('silver_stocks')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Silver Stock"

        return context
        
class Silver_stockDetailView(generic.DetailView):
    model = Silver_stock
    template_name = "crisisdb/silver_stock/silver_stock_detail.html"


#@permission_required('admin.can_add_log_entry')
def silver_stock_download(request):
    items = Silver_stock.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="silver_stocks.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'silver_stock', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.silver_stock, ])

    return response

        

class Total_populationCreate(PermissionRequiredMixin, CreateView):
    model = Total_population
    form_class = Total_populationForm
    template_name = "crisisdb/total_population/total_population_form.html"
    #permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('total_population-create')
    def get_context_data(self, **kwargs):
        # get the explanattion:
        all_var_hiers = Variablehierarchy.objects.all()
        for item in all_var_hiers:
            if item.name == "Total Population":
                my_exp = item.explanation
                my_sec = item.section.name
                my_subsec = item.subsection.name
                my_name = item.name
                break
            else:
                my_exp = "No_Explanations"
                my_sec = "No_SECTION"
                my_subsec = "NO_SUBSECTION"
                my_name = "NO_NAME"
        context = super().get_context_data(**kwargs)
        context["mysection"] = my_sec
        context["mysubsection"] = my_subsec
        context["myvar"] = my_name
        context["my_exp"] = my_exp

        return context


class Total_populationUpdate(PermissionRequiredMixin, UpdateView):
    model = Total_population
    form_class = Total_populationForm
    template_name = "crisisdb/total_population/total_population_update.html"
    #permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Total Population"

        return context

class Total_populationDelete(PermissionRequiredMixin, DeleteView):
    model = Total_population
    success_url = reverse_lazy('total_populations')
    template_name = "core/delete_general.html"
    #permission_required = 'catalog.can_mark_returned'


class Total_populationListView(generic.ListView):
    model = Total_population
    template_name = "crisisdb/total_population/total_population_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('total_populations')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Total Population"

        return context
        
class Total_populationDetailView(generic.DetailView):
    model = Total_population
    template_name = "crisisdb/total_population/total_population_detail.html"


#@permission_required('admin.can_add_log_entry')
def total_population_download(request):
    items = Total_population.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="total_populations.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'total_population', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.total_population, ])

    return response

        

class Gdp_per_capitaCreate(PermissionRequiredMixin, CreateView):
    model = Gdp_per_capita
    form_class = Gdp_per_capitaForm
    template_name = "crisisdb/gdp_per_capita/gdp_per_capita_form.html"
    #permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('gdp_per_capita-create')
    def get_context_data(self, **kwargs):
        # get the explanattion:
        all_var_hiers = Variablehierarchy.objects.all()
        for item in all_var_hiers:
            if item.name == "Gdp Per Capita":
                my_exp = item.explanation
                my_sec = item.section.name
                my_subsec = item.subsection.name
                my_name = item.name
                break
            else:
                my_exp = "No_Explanations"
                my_sec = "No_SECTION"
                my_subsec = "NO_SUBSECTION"
                my_name = "NO_NAME"
        context = super().get_context_data(**kwargs)
        context["mysection"] = my_sec
        context["mysubsection"] = my_subsec
        context["myvar"] = my_name
        context["my_exp"] = my_exp

        return context


class Gdp_per_capitaUpdate(PermissionRequiredMixin, UpdateView):
    model = Gdp_per_capita
    form_class = Gdp_per_capitaForm
    template_name = "crisisdb/gdp_per_capita/gdp_per_capita_update.html"
    #permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Gdp Per Capita"

        return context

class Gdp_per_capitaDelete(PermissionRequiredMixin, DeleteView):
    model = Gdp_per_capita
    success_url = reverse_lazy('gdp_per_capitas')
    template_name = "core/delete_general.html"
    #permission_required = 'catalog.can_mark_returned'


class Gdp_per_capitaListView(generic.ListView):
    model = Gdp_per_capita
    template_name = "crisisdb/gdp_per_capita/gdp_per_capita_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('gdp_per_capitas')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Gdp Per Capita"

        return context
        
class Gdp_per_capitaDetailView(generic.DetailView):
    model = Gdp_per_capita
    template_name = "crisisdb/gdp_per_capita/gdp_per_capita_detail.html"


#@permission_required('admin.can_add_log_entry')
def gdp_per_capita_download(request):
    items = Gdp_per_capita.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="gdp_per_capitas.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'gdp_per_capita', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.gdp_per_capita, ])

    return response

        

class Drought_eventCreate(PermissionRequiredMixin, CreateView):
    model = Drought_event
    form_class = Drought_eventForm
    template_name = "crisisdb/drought_event/drought_event_form.html"
    #permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('drought_event-create')
    def get_context_data(self, **kwargs):
        # get the explanattion:
        all_var_hiers = Variablehierarchy.objects.all()
        for item in all_var_hiers:
            if item.name == "Drought Event":
                my_exp = item.explanation
                my_sec = item.section.name
                my_subsec = item.subsection.name
                my_name = item.name
                break
            else:
                my_exp = "No_Explanations"
                my_sec = "No_SECTION"
                my_subsec = "NO_SUBSECTION"
                my_name = "NO_NAME"
        context = super().get_context_data(**kwargs)
        context["mysection"] = my_sec
        context["mysubsection"] = my_subsec
        context["myvar"] = my_name
        context["my_exp"] = my_exp

        return context


class Drought_eventUpdate(PermissionRequiredMixin, UpdateView):
    model = Drought_event
    form_class = Drought_eventForm
    template_name = "crisisdb/drought_event/drought_event_update.html"
    #permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Drought Event"

        return context

class Drought_eventDelete(PermissionRequiredMixin, DeleteView):
    model = Drought_event
    success_url = reverse_lazy('drought_events')
    template_name = "core/delete_general.html"
    #permission_required = 'catalog.can_mark_returned'


class Drought_eventListView(generic.ListView):
    model = Drought_event
    template_name = "crisisdb/drought_event/drought_event_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('drought_events')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Drought Event"

        return context
        
class Drought_eventDetailView(generic.DetailView):
    model = Drought_event
    template_name = "crisisdb/drought_event/drought_event_detail.html"


#@permission_required('admin.can_add_log_entry')
def drought_event_download(request):
    items = Drought_event.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="drought_events.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'drought_event', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.drought_event, ])

    return response

        

class Locust_eventCreate(PermissionRequiredMixin, CreateView):
    model = Locust_event
    form_class = Locust_eventForm
    template_name = "crisisdb/locust_event/locust_event_form.html"
    #permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('locust_event-create')
    def get_context_data(self, **kwargs):
        # get the explanattion:
        all_var_hiers = Variablehierarchy.objects.all()
        for item in all_var_hiers:
            if item.name == "Locust Event":
                my_exp = item.explanation
                my_sec = item.section.name
                my_subsec = item.subsection.name
                my_name = item.name
                break
            else:
                my_exp = "No_Explanations"
                my_sec = "No_SECTION"
                my_subsec = "NO_SUBSECTION"
                my_name = "NO_NAME"
        context = super().get_context_data(**kwargs)
        context["mysection"] = my_sec
        context["mysubsection"] = my_subsec
        context["myvar"] = my_name
        context["my_exp"] = my_exp

        return context


class Locust_eventUpdate(PermissionRequiredMixin, UpdateView):
    model = Locust_event
    form_class = Locust_eventForm
    template_name = "crisisdb/locust_event/locust_event_update.html"
    #permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Locust Event"

        return context

class Locust_eventDelete(PermissionRequiredMixin, DeleteView):
    model = Locust_event
    success_url = reverse_lazy('locust_events')
    template_name = "core/delete_general.html"
    #permission_required = 'catalog.can_mark_returned'


class Locust_eventListView(generic.ListView):
    model = Locust_event
    template_name = "crisisdb/locust_event/locust_event_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('locust_events')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Locust Event"

        return context
        
class Locust_eventDetailView(generic.DetailView):
    model = Locust_event
    template_name = "crisisdb/locust_event/locust_event_detail.html"


#@permission_required('admin.can_add_log_entry')
def locust_event_download(request):
    items = Locust_event.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="locust_events.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'locust_event', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.locust_event, ])

    return response

        

class Socioeconomic_turmoil_eventCreate(PermissionRequiredMixin, CreateView):
    model = Socioeconomic_turmoil_event
    form_class = Socioeconomic_turmoil_eventForm
    template_name = "crisisdb/socioeconomic_turmoil_event/socioeconomic_turmoil_event_form.html"
    #permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('socioeconomic_turmoil_event-create')
    def get_context_data(self, **kwargs):
        # get the explanattion:
        all_var_hiers = Variablehierarchy.objects.all()
        for item in all_var_hiers:
            if item.name == "Socioeconomic Turmoil Event":
                my_exp = item.explanation
                my_sec = item.section.name
                my_subsec = item.subsection.name
                my_name = item.name
                break
            else:
                my_exp = "No_Explanations"
                my_sec = "No_SECTION"
                my_subsec = "NO_SUBSECTION"
                my_name = "NO_NAME"
        context = super().get_context_data(**kwargs)
        context["mysection"] = my_sec
        context["mysubsection"] = my_subsec
        context["myvar"] = my_name
        context["my_exp"] = my_exp

        return context


class Socioeconomic_turmoil_eventUpdate(PermissionRequiredMixin, UpdateView):
    model = Socioeconomic_turmoil_event
    form_class = Socioeconomic_turmoil_eventForm
    template_name = "crisisdb/socioeconomic_turmoil_event/socioeconomic_turmoil_event_update.html"
    #permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Socioeconomic Turmoil Event"

        return context

class Socioeconomic_turmoil_eventDelete(PermissionRequiredMixin, DeleteView):
    model = Socioeconomic_turmoil_event
    success_url = reverse_lazy('socioeconomic_turmoil_events')
    template_name = "core/delete_general.html"
    #permission_required = 'catalog.can_mark_returned'


class Socioeconomic_turmoil_eventListView(generic.ListView):
    model = Socioeconomic_turmoil_event
    template_name = "crisisdb/socioeconomic_turmoil_event/socioeconomic_turmoil_event_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('socioeconomic_turmoil_events')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Socioeconomic Turmoil Event"

        return context
        
class Socioeconomic_turmoil_eventDetailView(generic.DetailView):
    model = Socioeconomic_turmoil_event
    template_name = "crisisdb/socioeconomic_turmoil_event/socioeconomic_turmoil_event_detail.html"


#@permission_required('admin.can_add_log_entry')
def socioeconomic_turmoil_event_download(request):
    items = Socioeconomic_turmoil_event.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="socioeconomic_turmoil_events.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'socioeconomic_turmoil_event', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.socioeconomic_turmoil_event, ])

    return response

        

class Crop_failure_eventCreate(PermissionRequiredMixin, CreateView):
    model = Crop_failure_event
    form_class = Crop_failure_eventForm
    template_name = "crisisdb/crop_failure_event/crop_failure_event_form.html"
    #permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('crop_failure_event-create')
    def get_context_data(self, **kwargs):
        # get the explanattion:
        all_var_hiers = Variablehierarchy.objects.all()
        for item in all_var_hiers:
            if item.name == "Crop Failure Event":
                my_exp = item.explanation
                my_sec = item.section.name
                my_subsec = item.subsection.name
                my_name = item.name
                break
            else:
                my_exp = "No_Explanations"
                my_sec = "No_SECTION"
                my_subsec = "NO_SUBSECTION"
                my_name = "NO_NAME"
        context = super().get_context_data(**kwargs)
        context["mysection"] = my_sec
        context["mysubsection"] = my_subsec
        context["myvar"] = my_name
        context["my_exp"] = my_exp

        return context


class Crop_failure_eventUpdate(PermissionRequiredMixin, UpdateView):
    model = Crop_failure_event
    form_class = Crop_failure_eventForm
    template_name = "crisisdb/crop_failure_event/crop_failure_event_update.html"
    #permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Crop Failure Event"

        return context

class Crop_failure_eventDelete(PermissionRequiredMixin, DeleteView):
    model = Crop_failure_event
    success_url = reverse_lazy('crop_failure_events')
    template_name = "core/delete_general.html"
    #permission_required = 'catalog.can_mark_returned'


class Crop_failure_eventListView(generic.ListView):
    model = Crop_failure_event
    template_name = "crisisdb/crop_failure_event/crop_failure_event_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('crop_failure_events')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Crop Failure Event"

        return context
        
class Crop_failure_eventDetailView(generic.DetailView):
    model = Crop_failure_event
    template_name = "crisisdb/crop_failure_event/crop_failure_event_detail.html"


#@permission_required('admin.can_add_log_entry')
def crop_failure_event_download(request):
    items = Crop_failure_event.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="crop_failure_events.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'crop_failure_event', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.crop_failure_event, ])

    return response

        

class Famine_eventCreate(PermissionRequiredMixin, CreateView):
    model = Famine_event
    form_class = Famine_eventForm
    template_name = "crisisdb/famine_event/famine_event_form.html"
    #permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('famine_event-create')
    def get_context_data(self, **kwargs):
        # get the explanattion:
        all_var_hiers = Variablehierarchy.objects.all()
        for item in all_var_hiers:
            if item.name == "Famine Event":
                my_exp = item.explanation
                my_sec = item.section.name
                my_subsec = item.subsection.name
                my_name = item.name
                break
            else:
                my_exp = "No_Explanations"
                my_sec = "No_SECTION"
                my_subsec = "NO_SUBSECTION"
                my_name = "NO_NAME"
        context = super().get_context_data(**kwargs)
        context["mysection"] = my_sec
        context["mysubsection"] = my_subsec
        context["myvar"] = my_name
        context["my_exp"] = my_exp

        return context


class Famine_eventUpdate(PermissionRequiredMixin, UpdateView):
    model = Famine_event
    form_class = Famine_eventForm
    template_name = "crisisdb/famine_event/famine_event_update.html"
    #permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Famine Event"

        return context

class Famine_eventDelete(PermissionRequiredMixin, DeleteView):
    model = Famine_event
    success_url = reverse_lazy('famine_events')
    template_name = "core/delete_general.html"
    #permission_required = 'catalog.can_mark_returned'


class Famine_eventListView(generic.ListView):
    model = Famine_event
    template_name = "crisisdb/famine_event/famine_event_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('famine_events')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Famine Event"

        return context
        
class Famine_eventDetailView(generic.DetailView):
    model = Famine_event
    template_name = "crisisdb/famine_event/famine_event_detail.html"


#@permission_required('admin.can_add_log_entry')
def famine_event_download(request):
    items = Famine_event.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="famine_events.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'famine_event', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.famine_event, ])

    return response

        

class Disease_outbreakCreate(PermissionRequiredMixin, CreateView):
    model = Disease_outbreak
    form_class = Disease_outbreakForm
    template_name = "crisisdb/disease_outbreak/disease_outbreak_form.html"
    #permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('disease_outbreak-create')
    def get_context_data(self, **kwargs):
        # get the explanattion:
        all_var_hiers = Variablehierarchy.objects.all()
        for item in all_var_hiers:
            if item.name == "Longitude":
                my_exp = item.explanation
                my_sec = item.section.name
                my_subsec = item.subsection.name
                my_name = item.name
                break
            else:
                my_exp = "No_Explanations"
                my_sec = "No_SECTION"
                my_subsec = "NO_SUBSECTION"
                my_name = "NO_NAME"
        context = super().get_context_data(**kwargs)
        context["mysection"] = my_sec
        context["mysubsection"] = my_subsec
        context["myvar"] = my_name
        context["my_exp"] = my_exp

        return context


class Disease_outbreakUpdate(PermissionRequiredMixin, UpdateView):
    model = Disease_outbreak
    form_class = Disease_outbreakForm
    template_name = "crisisdb/disease_outbreak/disease_outbreak_update.html"
    #permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Longitude"

        return context

class Disease_outbreakDelete(PermissionRequiredMixin, DeleteView):
    model = Disease_outbreak
    success_url = reverse_lazy('disease_outbreaks')
    template_name = "core/delete_general.html"
    #permission_required = 'catalog.can_mark_returned'


class Disease_outbreakListView(generic.ListView):
    model = Disease_outbreak
    template_name = "crisisdb/disease_outbreak/disease_outbreak_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('disease_outbreaks')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Longitude"

        return context
        
class Disease_outbreakDetailView(generic.DetailView):
    model = Disease_outbreak
    template_name = "crisisdb/disease_outbreak/disease_outbreak_detail.html"


#@permission_required('admin.can_add_log_entry')
def disease_outbreak_download(request):
    items = Disease_outbreak.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="disease_outbreaks.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'longitude', 'latitude', 'elevation', 'sub_category', 'magnitude', 'duration', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.longitude, obj.latitude, obj.elevation, obj.sub_category, obj.magnitude, obj.duration, ])

    return response

        
def QingVars(request):
    all_sections = Section.objects.all()
    all_subsections = Subsection.objects.all()
    all_varhiers = Variablehierarchy.objects.all()
    meta_data_dict = {}
    for ct in ContentType.objects.all():
        m = ct.model_class()
        #full_name = m.__module__ + m.__name__
        full_name = m.__name__
        meta_data_dict[full_name.lower()] = [full_name.split('.')[-1].replace("_", ' '), m._default_manager.count(), full_name.lower()+"-create",full_name.lower()+"s"]
        print (f".{m.__name__}	{m._default_manager.count()}")
    my_dict = {}
    context = {}
    for sect in all_sections:
        my_dict[sect] = {}
        for subsect in all_subsections:
            list_of_all_varhiers_in_here = []
            for item in all_varhiers:
                #print(item, item.section, item.subsection, sect.name, subsect.name)
                if item.section.name == sect.name and item.subsection.name == subsect.name:
                    print("We hit it")
                    list_of_all_varhiers_in_here.append(meta_data_dict[item.name.lower()])
            if list_of_all_varhiers_in_here:
                my_dict[sect][subsect] = list_of_all_varhiers_in_here
    context["my_dict"] = my_dict
    for ct in ContentType.objects.all():
        m = ct.model_class()
        print (f"{m.__module__}.{m.__name__}	{m._default_manager.count()}")
    return render(request, 'crisisdb/qing-vars.html', context=context)



def playground(request):
    if request.method == "POST":
        print(request.POST.get("selected_pols", 'Hallo'))
    all_pols = list_of_all_Polities()
    all_vars = dic_of_all_vars_with_varhier()
    all_vars_plus = dic_of_all_vars_in_sections()
    context = {'allpols': all_pols, 'all_var_hiers': all_vars, 'crisi': all_vars_plus}
    return render(request, 'crisisdb/playground.html', context=context)


Tags_dic = {
    'TRS': 'Evidenced',
    'DSP': 'Disputed',
    'SSP': 'Suspected',
    'IFR': 'Inferred',
    'UNK': 'Unknown',
}

def playgrounddownload(request):
    # read the data from the previous from
    # make sure you collect all the data from seshat_api
    # sort it out and spit it out
    # small task: download what we have on seshat_api
    checked_pols = request.POST.getlist("selected_pols")
    print("The checked politys are:", checked_pols)

    checked_vars = request.POST.getlist("selected_vars")
    print("The checked vars are:", checked_vars)

    new_checked_vars = ["crisisdb_" + item.lower() + '_related' for item in checked_vars]
    print("The modified checked vars are:", new_checked_vars)

    checked_separator = request.POST.get("SeparatorRadioOptions")
    print("The checked separator are:", checked_separator)

    if checked_separator == "comma":
        checked_sep = ","
    elif checked_separator == "bar":
        checked_sep = "|"
    else:
        print("Bad selection of Separator.")

    url = "http://127.0.0.1:8000/api/politys/"
    #url = "https://www.majidbenam.com/api/politys/"
    print(url)


    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"

    resp = requests.get(url, headers=headers)

    all_my_data = resp.json()['results']

    final_response = HttpResponse(content_type='text/csv')
    now = datetime.datetime.now()
    now_str = now.strftime("%H%M%S")
    myfile_name = 'CrisisDB_data_' + str(request.user) + '_' + now_str
    final_response['Content-Disposition'] = f'attachment; filename="{myfile_name}.csv"'

    # print(all_my_data)
    writer = csv.writer(final_response, delimiter=checked_sep)
    # the top row is the same as Equinox, so no need to read data from user input for that
    writer.writerow(['polity', 'variable_name', 'variable_sub_name', 'value',
                     'year_from', 'year_to', 'certainty', 'references', 'notes'])

    for polity_with_everything in all_my_data:
        if polity_with_everything['name'] not in checked_pols:
            continue
        else:
            for variable in new_checked_vars:
                if variable not in polity_with_everything.keys():
                    continue
                else:
                    # we can get into a list of dictionaries
                    for var_instance in polity_with_everything[variable]:
                        all_inner_keys = var_instance.keys()
                        # print(all_inner_keys)
                        all_used_keys = []
                        for active_key in all_inner_keys:
                            if active_key not in ['year_from', 'year_to', 'tag'] and active_key not in all_used_keys:
                                an_equinox_row = []
                                an_equinox_row.append(
                                    polity_with_everything['name'])
                                an_equinox_row.append(
                                    variable[:-8])
                                an_equinox_row.append(
                                    active_key)
                                an_equinox_row.append(
                                    var_instance[active_key])
                                all_used_keys.append(active_key)
                                an_equinox_row.append(
                                    var_instance['year_from'])
                                an_equinox_row.append(
                                    var_instance['year_to'])
                                full_tag = Tags_dic[var_instance['tag']]
                                an_equinox_row.append(full_tag)
                                writer.writerow(an_equinox_row)

    return final_response

