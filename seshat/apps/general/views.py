
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

from django.apps import apps




from .models import Polity_research_assistant, Polity_utm_zone, Polity_original_name, Polity_alternative_name, Polity_peak_years, Polity_duration, Polity_degree_of_centralization, Polity_suprapolity_relations, Polity_capital, Polity_language, Polity_linguistic_family, Polity_language_genus, Polity_religion_genus, Polity_religion_family, Polity_religion, Polity_relationship_to_preceding_entity, Polity_preceding_entity, Polity_succeeding_entity, Polity_supracultural_entity, Polity_scale_of_supracultural_interaction, Polity_alternate_religion_genus, Polity_alternate_religion_family, Polity_alternate_religion, Polity_expert, Polity_editor, Polity_religious_tradition


from .forms import Polity_research_assistantForm, Polity_utm_zoneForm, Polity_original_nameForm, Polity_alternative_nameForm, Polity_peak_yearsForm, Polity_durationForm, Polity_degree_of_centralizationForm, Polity_suprapolity_relationsForm, Polity_capitalForm, Polity_languageForm, Polity_linguistic_familyForm, Polity_language_genusForm, Polity_religion_genusForm, Polity_religion_familyForm, Polity_religionForm, Polity_relationship_to_preceding_entityForm, Polity_preceding_entityForm, Polity_succeeding_entityForm, Polity_supracultural_entityForm, Polity_scale_of_supracultural_interactionForm, Polity_alternate_religion_genusForm, Polity_alternate_religion_familyForm, Polity_alternate_religionForm, Polity_expertForm, Polity_editorForm, Polity_religious_traditionForm

class Polity_research_assistantCreate(PermissionRequiredMixin, CreateView):
    model = Polity_research_assistant
    form_class = Polity_research_assistantForm
    template_name = "general/polity_research_assistant/polity_research_assistant_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('polity_research_assistant-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Polity Research Assistant"
        context["my_exp"] = "The RA(s) who worked on a polity."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'polity_ra': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The RA of a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Polity_research_assistantUpdate(PermissionRequiredMixin, UpdateView):
    model = Polity_research_assistant
    form_class = Polity_research_assistantForm
    template_name = "general/polity_research_assistant/polity_research_assistant_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Research Assistant"

        return context

class Polity_research_assistantDelete(PermissionRequiredMixin, DeleteView):
    model = Polity_research_assistant
    success_url = reverse_lazy('polity_research_assistants')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Polity_research_assistantListView(generic.ListView):
    model = Polity_research_assistant
    template_name = "general/polity_research_assistant/polity_research_assistant_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('polity_research_assistants')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Research Assistant"
        context["var_main_desc"] = "The ra(s) who worked on a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "Staff"
        context["inner_vars"] = {'polity_ra': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The RA of a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Polity_research_assistantListViewAll(generic.ListView):
    model = Polity_research_assistant
    template_name = "general/polity_research_assistant/polity_research_assistant_list_all.html"

    def get_absolute_url(self):
        return reverse('polity_research_assistants_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Polity_research_assistant.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Research Assistant"
        context["var_main_desc"] = "The ra(s) who worked on a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "Staff"
        context["inner_vars"] = {'polity_ra': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The RA of a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Polity_research_assistantDetailView(generic.DetailView):
    model = Polity_research_assistant
    template_name = "general/polity_research_assistant/polity_research_assistant_detail.html"


@permission_required('core.view_capital')
def polity_research_assistant_download(request):
    items = Polity_research_assistant.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_research_assistants.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'polity_ra', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.polity_ra, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def polity_research_assistant_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_research_assistants.csv"'
    
    my_meta_data_dic = {'notes': None, 'main_desc': 'The RA(s) who worked on a polity.', 'main_desc_source': None, 'section': 'General Variables', 'subsection': 'Staff'}
    my_meta_data_dic_inner_vars = {'polity_ra': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The RA of a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Polity_utm_zoneCreate(PermissionRequiredMixin, CreateView):
    model = Polity_utm_zone
    form_class = Polity_utm_zoneForm
    template_name = "general/polity_utm_zone/polity_utm_zone_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('polity_utm_zone-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Polity Utm Zone"
        context["my_exp"] = "The UTM Zone of a polity."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'utm_zone': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The details of UTM_ZONE.', 'units': None, 'choices': None, 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}}
        context["potential_cols"] = []
        return context


class Polity_utm_zoneUpdate(PermissionRequiredMixin, UpdateView):
    model = Polity_utm_zone
    form_class = Polity_utm_zoneForm
    template_name = "general/polity_utm_zone/polity_utm_zone_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Utm Zone"

        return context

class Polity_utm_zoneDelete(PermissionRequiredMixin, DeleteView):
    model = Polity_utm_zone
    success_url = reverse_lazy('polity_utm_zones')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Polity_utm_zoneListView(generic.ListView):
    model = Polity_utm_zone
    template_name = "general/polity_utm_zone/polity_utm_zone_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('polity_utm_zones')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Utm Zone"
        context["var_main_desc"] = "The utm zone of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'utm_zone': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The details of UTM_ZONE.', 'units': None, 'choices': None, 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}}
        context["potential_cols"] = []

        return context


class Polity_utm_zoneListViewAll(generic.ListView):
    model = Polity_utm_zone
    template_name = "general/polity_utm_zone/polity_utm_zone_list_all.html"

    def get_absolute_url(self):
        return reverse('polity_utm_zones_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Polity_utm_zone.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Utm Zone"
        context["var_main_desc"] = "The utm zone of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'utm_zone': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The details of UTM_ZONE.', 'units': None, 'choices': None, 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Polity_utm_zoneDetailView(generic.DetailView):
    model = Polity_utm_zone
    template_name = "general/polity_utm_zone/polity_utm_zone_detail.html"


@permission_required('core.view_capital')
def polity_utm_zone_download(request):
    items = Polity_utm_zone.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_utm_zones.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'utm_zone', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.utm_zone, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def polity_utm_zone_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_utm_zones.csv"'
    
    my_meta_data_dic = {'notes': None, 'main_desc': 'The UTM Zone of a polity.', 'main_desc_source': None, 'section': 'General Variables', 'subsection': 'General'}
    my_meta_data_dic_inner_vars = {'utm_zone': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The details of UTM_ZONE.', 'units': None, 'choices': None, 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Polity_original_nameCreate(PermissionRequiredMixin, CreateView):
    model = Polity_original_name
    form_class = Polity_original_nameForm
    template_name = "general/polity_original_name/polity_original_name_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('polity_original_name-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Polity Original Name"
        context["my_exp"] = "The original name of a polity."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'original_name': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The details of original_name.', 'units': None, 'choices': None, 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}}
        context["potential_cols"] = []
        return context


class Polity_original_nameUpdate(PermissionRequiredMixin, UpdateView):
    model = Polity_original_name
    form_class = Polity_original_nameForm
    template_name = "general/polity_original_name/polity_original_name_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Original Name"

        return context

class Polity_original_nameDelete(PermissionRequiredMixin, DeleteView):
    model = Polity_original_name
    success_url = reverse_lazy('polity_original_names')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Polity_original_nameListView(generic.ListView):
    model = Polity_original_name
    template_name = "general/polity_original_name/polity_original_name_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('polity_original_names')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Original Name"
        context["var_main_desc"] = "The original name of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'original_name': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The details of original_name.', 'units': None, 'choices': None, 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}}
        context["potential_cols"] = []

        return context


class Polity_original_nameListViewAll(generic.ListView):
    model = Polity_original_name
    template_name = "general/polity_original_name/polity_original_name_list_all.html"

    def get_absolute_url(self):
        return reverse('polity_original_names_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Polity_original_name.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Original Name"
        context["var_main_desc"] = "The original name of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'original_name': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The details of original_name.', 'units': None, 'choices': None, 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Polity_original_nameDetailView(generic.DetailView):
    model = Polity_original_name
    template_name = "general/polity_original_name/polity_original_name_detail.html"


@permission_required('core.view_capital')
def polity_original_name_download(request):
    items = Polity_original_name.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_original_names.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'original_name', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.original_name, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def polity_original_name_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_original_names.csv"'
    
    my_meta_data_dic = {'notes': None, 'main_desc': 'The original name of a polity.', 'main_desc_source': None, 'section': 'General Variables', 'subsection': 'General'}
    my_meta_data_dic_inner_vars = {'original_name': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The details of original_name.', 'units': None, 'choices': None, 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Polity_alternative_nameCreate(PermissionRequiredMixin, CreateView):
    model = Polity_alternative_name
    form_class = Polity_alternative_nameForm
    template_name = "general/polity_alternative_name/polity_alternative_name_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('polity_alternative_name-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Polity Alternative Name"
        context["my_exp"] = "The alternative name of a polity."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'alternative_name': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The details of alternative_name.', 'units': None, 'choices': None, 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}}
        context["potential_cols"] = []
        return context


class Polity_alternative_nameUpdate(PermissionRequiredMixin, UpdateView):
    model = Polity_alternative_name
    form_class = Polity_alternative_nameForm
    template_name = "general/polity_alternative_name/polity_alternative_name_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Alternative Name"

        return context

class Polity_alternative_nameDelete(PermissionRequiredMixin, DeleteView):
    model = Polity_alternative_name
    success_url = reverse_lazy('polity_alternative_names')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Polity_alternative_nameListView(generic.ListView):
    model = Polity_alternative_name
    template_name = "general/polity_alternative_name/polity_alternative_name_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('polity_alternative_names')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Alternative Name"
        context["var_main_desc"] = "The alternative name of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'alternative_name': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The details of alternative_name.', 'units': None, 'choices': None, 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}}
        context["potential_cols"] = []

        return context


class Polity_alternative_nameListViewAll(generic.ListView):
    model = Polity_alternative_name
    template_name = "general/polity_alternative_name/polity_alternative_name_list_all.html"

    def get_absolute_url(self):
        return reverse('polity_alternative_names_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Polity_alternative_name.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Alternative Name"
        context["var_main_desc"] = "The alternative name of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'alternative_name': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The details of alternative_name.', 'units': None, 'choices': None, 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Polity_alternative_nameDetailView(generic.DetailView):
    model = Polity_alternative_name
    template_name = "general/polity_alternative_name/polity_alternative_name_detail.html"


@permission_required('core.view_capital')
def polity_alternative_name_download(request):
    items = Polity_alternative_name.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_alternative_names.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'alternative_name', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.alternative_name, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def polity_alternative_name_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_alternative_names.csv"'
    
    my_meta_data_dic = {'notes': None, 'main_desc': 'The alternative name of a polity.', 'main_desc_source': None, 'section': 'General Variables', 'subsection': 'General'}
    my_meta_data_dic_inner_vars = {'alternative_name': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The details of alternative_name.', 'units': None, 'choices': None, 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Polity_peak_yearsCreate(PermissionRequiredMixin, CreateView):
    model = Polity_peak_years
    form_class = Polity_peak_yearsForm
    template_name = "general/polity_peak_years/polity_peak_years_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('polity_peak_years-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Polity Peak Years"
        context["my_exp"] = "The peak years of a polity."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'peak_year_from': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The beginning of the peak years for a polity.', 'units': None, 'choices': None, 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}, 'peak_year_to': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The end of the peak years for a polity.', 'units': None, 'choices': None, 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}}
        context["potential_cols"] = []
        return context


class Polity_peak_yearsUpdate(PermissionRequiredMixin, UpdateView):
    model = Polity_peak_years
    form_class = Polity_peak_yearsForm
    template_name = "general/polity_peak_years/polity_peak_years_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Peak Years"

        return context

class Polity_peak_yearsDelete(PermissionRequiredMixin, DeleteView):
    model = Polity_peak_years
    success_url = reverse_lazy('polity_peak_yearss')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Polity_peak_yearsListView(generic.ListView):
    model = Polity_peak_years
    template_name = "general/polity_peak_years/polity_peak_years_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('polity_peak_yearss')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Peak Years"
        context["var_main_desc"] = "The peak years of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'peak_year_from': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The beginning of the peak years for a polity.', 'units': None, 'choices': None, 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}, 'peak_year_to': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The end of the peak years for a polity.', 'units': None, 'choices': None, 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}}
        context["potential_cols"] = []

        return context


class Polity_peak_yearsListViewAll(generic.ListView):
    model = Polity_peak_years
    template_name = "general/polity_peak_years/polity_peak_years_list_all.html"

    def get_absolute_url(self):
        return reverse('polity_peak_yearss_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Polity_peak_years.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Peak Years"
        context["var_main_desc"] = "The peak years of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'peak_year_from': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The beginning of the peak years for a polity.', 'units': None, 'choices': None, 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}, 'peak_year_to': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The end of the peak years for a polity.', 'units': None, 'choices': None, 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Polity_peak_yearsDetailView(generic.DetailView):
    model = Polity_peak_years
    template_name = "general/polity_peak_years/polity_peak_years_detail.html"


@permission_required('core.view_capital')
def polity_peak_years_download(request):
    items = Polity_peak_years.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_peak_yearss.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'peak_year_from', 'peak_year_to', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.peak_year_from, obj.peak_year_to, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def polity_peak_years_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_peak_yearss.csv"'
    
    my_meta_data_dic = {'notes': None, 'main_desc': 'The peak years of a polity.', 'main_desc_source': None, 'section': 'General Variables', 'subsection': 'General'}
    my_meta_data_dic_inner_vars = {'peak_year_from': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The beginning of the peak years for a polity.', 'units': None, 'choices': None, 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}, 'peak_year_to': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The end of the peak years for a polity.', 'units': None, 'choices': None, 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Polity_durationCreate(PermissionRequiredMixin, CreateView):
    model = Polity_duration
    form_class = Polity_durationForm
    template_name = "general/polity_duration/polity_duration_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('polity_duration-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Polity Duration"
        context["my_exp"] = "The lifetime of a polity."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'polity_year_from': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The beginning year for a polity.', 'units': None, 'choices': None, 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}, 'polity_year_to': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The end year for a polity.', 'units': None, 'choices': None, 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}}
        context["potential_cols"] = []
        return context


class Polity_durationUpdate(PermissionRequiredMixin, UpdateView):
    model = Polity_duration
    form_class = Polity_durationForm
    template_name = "general/polity_duration/polity_duration_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Duration"

        return context

class Polity_durationDelete(PermissionRequiredMixin, DeleteView):
    model = Polity_duration
    success_url = reverse_lazy('polity_durations')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Polity_durationListView(generic.ListView):
    model = Polity_duration
    template_name = "general/polity_duration/polity_duration_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('polity_durations')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Duration"
        context["var_main_desc"] = "The lifetime of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'polity_year_from': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The beginning year for a polity.', 'units': None, 'choices': None, 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}, 'polity_year_to': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The end year for a polity.', 'units': None, 'choices': None, 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}}
        context["potential_cols"] = []

        return context


class Polity_durationListViewAll(generic.ListView):
    model = Polity_duration
    template_name = "general/polity_duration/polity_duration_list_all.html"

    def get_absolute_url(self):
        return reverse('polity_durations_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Polity_duration.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Duration"
        context["var_main_desc"] = "The lifetime of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'polity_year_from': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The beginning year for a polity.', 'units': None, 'choices': None, 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}, 'polity_year_to': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The end year for a polity.', 'units': None, 'choices': None, 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Polity_durationDetailView(generic.DetailView):
    model = Polity_duration
    template_name = "general/polity_duration/polity_duration_detail.html"


@permission_required('core.view_capital')
def polity_duration_download(request):
    items = Polity_duration.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_durations.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'polity_year_from', 'polity_year_to', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.polity_year_from, obj.polity_year_to, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def polity_duration_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_durations.csv"'
    
    my_meta_data_dic = {'notes': None, 'main_desc': 'The lifetime of a polity.', 'main_desc_source': None, 'section': 'General Variables', 'subsection': 'General'}
    my_meta_data_dic_inner_vars = {'polity_year_from': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The beginning year for a polity.', 'units': None, 'choices': None, 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}, 'polity_year_to': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The end year for a polity.', 'units': None, 'choices': None, 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Polity_degree_of_centralizationCreate(PermissionRequiredMixin, CreateView):
    model = Polity_degree_of_centralization
    form_class = Polity_degree_of_centralizationForm
    template_name = "general/polity_degree_of_centralization/polity_degree_of_centralization_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('polity_degree_of_centralization-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Polity Degree of Centralization"
        context["my_exp"] = "The degree of centralization of a polity."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'degree_of_centralization': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The details of degree_of_centralization.', 'units': None, 'choices': 'DEGREE_OF_CENTRALIZATION_CHOICES', 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}}
        context["potential_cols"] = []
        return context


class Polity_degree_of_centralizationUpdate(PermissionRequiredMixin, UpdateView):
    model = Polity_degree_of_centralization
    form_class = Polity_degree_of_centralizationForm
    template_name = "general/polity_degree_of_centralization/polity_degree_of_centralization_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Degree of Centralization"

        return context

class Polity_degree_of_centralizationDelete(PermissionRequiredMixin, DeleteView):
    model = Polity_degree_of_centralization
    success_url = reverse_lazy('polity_degree_of_centralizations')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Polity_degree_of_centralizationListView(generic.ListView):
    model = Polity_degree_of_centralization
    template_name = "general/polity_degree_of_centralization/polity_degree_of_centralization_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('polity_degree_of_centralizations')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Degree of Centralization"
        context["var_main_desc"] = "The degree of centralization of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'degree_of_centralization': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The details of degree_of_centralization.', 'units': None, 'choices': 'DEGREE_OF_CENTRALIZATION_CHOICES', 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}}
        context["potential_cols"] = []

        return context


class Polity_degree_of_centralizationListViewAll(generic.ListView):
    model = Polity_degree_of_centralization
    template_name = "general/polity_degree_of_centralization/polity_degree_of_centralization_list_all.html"

    def get_absolute_url(self):
        return reverse('polity_degree_of_centralizations_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Polity_degree_of_centralization.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Degree of Centralization"
        context["var_main_desc"] = "The degree of centralization of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'degree_of_centralization': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The details of degree_of_centralization.', 'units': None, 'choices': 'DEGREE_OF_CENTRALIZATION_CHOICES', 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Polity_degree_of_centralizationDetailView(generic.DetailView):
    model = Polity_degree_of_centralization
    template_name = "general/polity_degree_of_centralization/polity_degree_of_centralization_detail.html"


@permission_required('core.view_capital')
def polity_degree_of_centralization_download(request):
    items = Polity_degree_of_centralization.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_degree_of_centralizations.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'degree_of_centralization', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.degree_of_centralization, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def polity_degree_of_centralization_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_degree_of_centralizations.csv"'
    
    my_meta_data_dic = {'notes': None, 'main_desc': 'The degree of centralization of a polity.', 'main_desc_source': None, 'section': 'General Variables', 'subsection': 'General'}
    my_meta_data_dic_inner_vars = {'degree_of_centralization': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The details of degree_of_centralization.', 'units': None, 'choices': 'DEGREE_OF_CENTRALIZATION_CHOICES', 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Polity_suprapolity_relationsCreate(PermissionRequiredMixin, CreateView):
    model = Polity_suprapolity_relations
    form_class = Polity_suprapolity_relationsForm
    template_name = "general/polity_suprapolity_relations/polity_suprapolity_relations_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('polity_suprapolity_relations-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Polity Suprapolity Relations"
        context["my_exp"] = "The supra polity relations of a polity."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'supra_polity_relations': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The details of supra polity relations.', 'units': None, 'choices': 'SUPRA_POLITY_RELATIONS_CHOICES', 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}}
        context["potential_cols"] = []
        return context


class Polity_suprapolity_relationsUpdate(PermissionRequiredMixin, UpdateView):
    model = Polity_suprapolity_relations
    form_class = Polity_suprapolity_relationsForm
    template_name = "general/polity_suprapolity_relations/polity_suprapolity_relations_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Suprapolity Relations"

        return context

class Polity_suprapolity_relationsDelete(PermissionRequiredMixin, DeleteView):
    model = Polity_suprapolity_relations
    success_url = reverse_lazy('polity_suprapolity_relationss')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Polity_suprapolity_relationsListView(generic.ListView):
    model = Polity_suprapolity_relations
    template_name = "general/polity_suprapolity_relations/polity_suprapolity_relations_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('polity_suprapolity_relationss')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Suprapolity Relations"
        context["var_main_desc"] = "The supra polity relations of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'supra_polity_relations': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The details of supra polity relations.', 'units': None, 'choices': 'SUPRA_POLITY_RELATIONS_CHOICES', 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}}
        context["potential_cols"] = []

        return context


class Polity_suprapolity_relationsListViewAll(generic.ListView):
    model = Polity_suprapolity_relations
    template_name = "general/polity_suprapolity_relations/polity_suprapolity_relations_list_all.html"

    def get_absolute_url(self):
        return reverse('polity_suprapolity_relationss_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Polity_suprapolity_relations.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Suprapolity Relations"
        context["var_main_desc"] = "The supra polity relations of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'supra_polity_relations': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The details of supra polity relations.', 'units': None, 'choices': 'SUPRA_POLITY_RELATIONS_CHOICES', 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Polity_suprapolity_relationsDetailView(generic.DetailView):
    model = Polity_suprapolity_relations
    template_name = "general/polity_suprapolity_relations/polity_suprapolity_relations_detail.html"


@permission_required('core.view_capital')
def polity_suprapolity_relations_download(request):
    items = Polity_suprapolity_relations.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_suprapolity_relationss.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'supra_polity_relations', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.supra_polity_relations, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def polity_suprapolity_relations_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_suprapolity_relationss.csv"'
    
    my_meta_data_dic = {'notes': None, 'main_desc': 'The supra polity relations of a polity.', 'main_desc_source': None, 'section': 'General Variables', 'subsection': 'General'}
    my_meta_data_dic_inner_vars = {'supra_polity_relations': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The details of supra polity relations.', 'units': None, 'choices': 'SUPRA_POLITY_RELATIONS_CHOICES', 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Polity_capitalCreate(PermissionRequiredMixin, CreateView):
    model = Polity_capital
    form_class = Polity_capitalForm
    template_name = "general/polity_capital/polity_capital_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('polity_capital-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Polity Capital"
        context["my_exp"] = "The capital of a polity."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'capital': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The capital of a polity.', 'units': None, 'choices': None, 'null_meaning': 'This polity did not have a capital.'}}
        context["potential_cols"] = []
        return context


class Polity_capitalUpdate(PermissionRequiredMixin, UpdateView):
    model = Polity_capital
    form_class = Polity_capitalForm
    template_name = "general/polity_capital/polity_capital_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Capital"

        return context

class Polity_capitalDelete(PermissionRequiredMixin, DeleteView):
    model = Polity_capital
    success_url = reverse_lazy('polity_capitals')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Polity_capitalListView(generic.ListView):
    model = Polity_capital
    template_name = "general/polity_capital/polity_capital_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('polity_capitals')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Capital"
        context["var_main_desc"] = "The capital of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'capital': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The capital of a polity.', 'units': None, 'choices': None, 'null_meaning': 'This polity did not have a capital.'}}
        context["potential_cols"] = []

        return context


class Polity_capitalListViewAll(generic.ListView):
    model = Polity_capital
    template_name = "general/polity_capital/polity_capital_list_all.html"

    def get_absolute_url(self):
        return reverse('polity_capitals_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Polity_capital.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Capital"
        context["var_main_desc"] = "The capital of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'capital': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The capital of a polity.', 'units': None, 'choices': None, 'null_meaning': 'This polity did not have a capital.'}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Polity_capitalDetailView(generic.DetailView):
    model = Polity_capital
    template_name = "general/polity_capital/polity_capital_detail.html"


@permission_required('core.view_capital')
def polity_capital_download(request):
    items = Polity_capital.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_capitals.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'capital', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.capital, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def polity_capital_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_capitals.csv"'
    
    my_meta_data_dic = {'notes': None, 'main_desc': 'The capital of a polity.', 'main_desc_source': None, 'section': 'General Variables', 'subsection': 'General'}
    my_meta_data_dic_inner_vars = {'capital': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The capital of a polity.', 'units': None, 'choices': None, 'null_meaning': 'This polity did not have a capital.'}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Polity_languageCreate(PermissionRequiredMixin, CreateView):
    model = Polity_language
    form_class = Polity_languageForm
    template_name = "general/polity_language/polity_language_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('polity_language-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Polity Language"
        context["my_exp"] = "The language of a polity."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'language': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The language of a polity.', 'units': None, 'choices': 'LANGUAGE_CHOICES', 'null_meaning': 'This polity did not have a language.'}}
        context["potential_cols"] = []
        return context


class Polity_languageUpdate(PermissionRequiredMixin, UpdateView):
    model = Polity_language
    form_class = Polity_languageForm
    template_name = "general/polity_language/polity_language_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Language"

        return context

class Polity_languageDelete(PermissionRequiredMixin, DeleteView):
    model = Polity_language
    success_url = reverse_lazy('polity_languages')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Polity_languageListView(generic.ListView):
    model = Polity_language
    template_name = "general/polity_language/polity_language_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('polity_languages')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Language"
        context["var_main_desc"] = "The language of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'language': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The language of a polity.', 'units': None, 'choices': 'LANGUAGE_CHOICES', 'null_meaning': 'This polity did not have a language.'}}
        context["potential_cols"] = []

        return context


class Polity_languageListViewAll(generic.ListView):
    model = Polity_language
    template_name = "general/polity_language/polity_language_list_all.html"

    def get_absolute_url(self):
        return reverse('polity_languages_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Polity_language.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Language"
        context["var_main_desc"] = "The language of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'language': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The language of a polity.', 'units': None, 'choices': 'LANGUAGE_CHOICES', 'null_meaning': 'This polity did not have a language.'}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Polity_languageDetailView(generic.DetailView):
    model = Polity_language
    template_name = "general/polity_language/polity_language_detail.html"


@permission_required('core.view_capital')
def polity_language_download(request):
    items = Polity_language.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_languages.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'language', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.language, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def polity_language_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_languages.csv"'
    
    my_meta_data_dic = {'notes': None, 'main_desc': 'The language of a polity.', 'main_desc_source': None, 'section': 'General Variables', 'subsection': 'General'}
    my_meta_data_dic_inner_vars = {'language': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The language of a polity.', 'units': None, 'choices': 'LANGUAGE_CHOICES', 'null_meaning': 'This polity did not have a language.'}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Polity_linguistic_familyCreate(PermissionRequiredMixin, CreateView):
    model = Polity_linguistic_family
    form_class = Polity_linguistic_familyForm
    template_name = "general/polity_linguistic_family/polity_linguistic_family_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('polity_linguistic_family-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Polity Linguistic Family"
        context["my_exp"] = "The linguistic family of a polity."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'linguistic_family': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The linguistic family of a polity.', 'units': None, 'choices': 'LINGUISTIC_FAMILY_CHOICES', 'null_meaning': 'This polity did not have a linguistic family.'}}
        context["potential_cols"] = []
        return context


class Polity_linguistic_familyUpdate(PermissionRequiredMixin, UpdateView):
    model = Polity_linguistic_family
    form_class = Polity_linguistic_familyForm
    template_name = "general/polity_linguistic_family/polity_linguistic_family_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Linguistic Family"

        return context

class Polity_linguistic_familyDelete(PermissionRequiredMixin, DeleteView):
    model = Polity_linguistic_family
    success_url = reverse_lazy('polity_linguistic_familys')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Polity_linguistic_familyListView(generic.ListView):
    model = Polity_linguistic_family
    template_name = "general/polity_linguistic_family/polity_linguistic_family_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('polity_linguistic_familys')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Linguistic Family"
        context["var_main_desc"] = "The linguistic family of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'linguistic_family': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The linguistic family of a polity.', 'units': None, 'choices': 'LINGUISTIC_FAMILY_CHOICES', 'null_meaning': 'This polity did not have a linguistic family.'}}
        context["potential_cols"] = []

        return context


class Polity_linguistic_familyListViewAll(generic.ListView):
    model = Polity_linguistic_family
    template_name = "general/polity_linguistic_family/polity_linguistic_family_list_all.html"

    def get_absolute_url(self):
        return reverse('polity_linguistic_familys_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Polity_linguistic_family.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Linguistic Family"
        context["var_main_desc"] = "The linguistic family of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'linguistic_family': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The linguistic family of a polity.', 'units': None, 'choices': 'LINGUISTIC_FAMILY_CHOICES', 'null_meaning': 'This polity did not have a linguistic family.'}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Polity_linguistic_familyDetailView(generic.DetailView):
    model = Polity_linguistic_family
    template_name = "general/polity_linguistic_family/polity_linguistic_family_detail.html"


@permission_required('core.view_capital')
def polity_linguistic_family_download(request):
    items = Polity_linguistic_family.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_linguistic_familys.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'linguistic_family', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.linguistic_family, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def polity_linguistic_family_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_linguistic_familys.csv"'
    
    my_meta_data_dic = {'notes': None, 'main_desc': 'The linguistic family of a polity.', 'main_desc_source': None, 'section': 'General Variables', 'subsection': 'General'}
    my_meta_data_dic_inner_vars = {'linguistic_family': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The linguistic family of a polity.', 'units': None, 'choices': 'LINGUISTIC_FAMILY_CHOICES', 'null_meaning': 'This polity did not have a linguistic family.'}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Polity_language_genusCreate(PermissionRequiredMixin, CreateView):
    model = Polity_language_genus
    form_class = Polity_language_genusForm
    template_name = "general/polity_language_genus/polity_language_genus_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('polity_language_genus-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Polity Language Genus"
        context["my_exp"] = "The language genus of a polity."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'language_genus': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The language genus of a polity.', 'units': None, 'choices': 'LINGUISTIC_FAMILY_CHOICES', 'null_meaning': 'This polity did not have a language Genus.'}}
        context["potential_cols"] = []
        return context


class Polity_language_genusUpdate(PermissionRequiredMixin, UpdateView):
    model = Polity_language_genus
    form_class = Polity_language_genusForm
    template_name = "general/polity_language_genus/polity_language_genus_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Language Genus"

        return context

class Polity_language_genusDelete(PermissionRequiredMixin, DeleteView):
    model = Polity_language_genus
    success_url = reverse_lazy('polity_language_genuss')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Polity_language_genusListView(generic.ListView):
    model = Polity_language_genus
    template_name = "general/polity_language_genus/polity_language_genus_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('polity_language_genuss')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Language Genus"
        context["var_main_desc"] = "The language genus of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'language_genus': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The language genus of a polity.', 'units': None, 'choices': 'LINGUISTIC_FAMILY_CHOICES', 'null_meaning': 'This polity did not have a language Genus.'}}
        context["potential_cols"] = []

        return context


class Polity_language_genusListViewAll(generic.ListView):
    model = Polity_language_genus
    template_name = "general/polity_language_genus/polity_language_genus_list_all.html"

    def get_absolute_url(self):
        return reverse('polity_language_genuss_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Polity_language_genus.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Language Genus"
        context["var_main_desc"] = "The language genus of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'language_genus': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The language genus of a polity.', 'units': None, 'choices': 'LINGUISTIC_FAMILY_CHOICES', 'null_meaning': 'This polity did not have a language Genus.'}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Polity_language_genusDetailView(generic.DetailView):
    model = Polity_language_genus
    template_name = "general/polity_language_genus/polity_language_genus_detail.html"


@permission_required('core.view_capital')
def polity_language_genus_download(request):
    items = Polity_language_genus.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_language_genuss.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'language_genus', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.language_genus, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def polity_language_genus_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_language_genuss.csv"'
    
    my_meta_data_dic = {'notes': None, 'main_desc': 'The language genus of a polity.', 'main_desc_source': None, 'section': 'General Variables', 'subsection': 'General'}
    my_meta_data_dic_inner_vars = {'language_genus': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The language genus of a polity.', 'units': None, 'choices': 'LINGUISTIC_FAMILY_CHOICES', 'null_meaning': 'This polity did not have a language Genus.'}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Polity_religion_genusCreate(PermissionRequiredMixin, CreateView):
    model = Polity_religion_genus
    form_class = Polity_religion_genusForm
    template_name = "general/polity_religion_genus/polity_religion_genus_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('polity_religion_genus-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Polity Religion Genus"
        context["my_exp"] = "The religion genus of a polity."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'religion_genus': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The religion genus of a polity.', 'units': None, 'choices': 'RELIGION_GENUS_CHOICES', 'null_meaning': 'This polity did not have a religion genus.'}}
        context["potential_cols"] = []
        return context


class Polity_religion_genusUpdate(PermissionRequiredMixin, UpdateView):
    model = Polity_religion_genus
    form_class = Polity_religion_genusForm
    template_name = "general/polity_religion_genus/polity_religion_genus_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Religion Genus"

        return context

class Polity_religion_genusDelete(PermissionRequiredMixin, DeleteView):
    model = Polity_religion_genus
    success_url = reverse_lazy('polity_religion_genuss')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Polity_religion_genusListView(generic.ListView):
    model = Polity_religion_genus
    template_name = "general/polity_religion_genus/polity_religion_genus_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('polity_religion_genuss')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Religion Genus"
        context["var_main_desc"] = "The religion genus of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'religion_genus': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The religion genus of a polity.', 'units': None, 'choices': 'RELIGION_GENUS_CHOICES', 'null_meaning': 'This polity did not have a religion genus.'}}
        context["potential_cols"] = []

        return context


class Polity_religion_genusListViewAll(generic.ListView):
    model = Polity_religion_genus
    template_name = "general/polity_religion_genus/polity_religion_genus_list_all.html"

    def get_absolute_url(self):
        return reverse('polity_religion_genuss_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Polity_religion_genus.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Religion Genus"
        context["var_main_desc"] = "The religion genus of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'religion_genus': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The religion genus of a polity.', 'units': None, 'choices': 'RELIGION_GENUS_CHOICES', 'null_meaning': 'This polity did not have a religion genus.'}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Polity_religion_genusDetailView(generic.DetailView):
    model = Polity_religion_genus
    template_name = "general/polity_religion_genus/polity_religion_genus_detail.html"


@permission_required('core.view_capital')
def polity_religion_genus_download(request):
    items = Polity_religion_genus.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_religion_genuss.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'religion_genus', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.religion_genus, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def polity_religion_genus_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_religion_genuss.csv"'
    
    my_meta_data_dic = {'notes': None, 'main_desc': 'The religion genus of a polity.', 'main_desc_source': None, 'section': 'General Variables', 'subsection': 'General'}
    my_meta_data_dic_inner_vars = {'religion_genus': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The religion genus of a polity.', 'units': None, 'choices': 'RELIGION_GENUS_CHOICES', 'null_meaning': 'This polity did not have a religion genus.'}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Polity_religion_familyCreate(PermissionRequiredMixin, CreateView):
    model = Polity_religion_family
    form_class = Polity_religion_familyForm
    template_name = "general/polity_religion_family/polity_religion_family_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('polity_religion_family-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Polity Religion Family"
        context["my_exp"] = "The religion family of a polity."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'religion_family': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The religion family of a polity.', 'units': None, 'choices': 'RELIGION_FAMILY_CHOICES', 'null_meaning': 'This polity did not have a religion family.'}}
        context["potential_cols"] = []
        return context


class Polity_religion_familyUpdate(PermissionRequiredMixin, UpdateView):
    model = Polity_religion_family
    form_class = Polity_religion_familyForm
    template_name = "general/polity_religion_family/polity_religion_family_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Religion Family"

        return context

class Polity_religion_familyDelete(PermissionRequiredMixin, DeleteView):
    model = Polity_religion_family
    success_url = reverse_lazy('polity_religion_familys')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Polity_religion_familyListView(generic.ListView):
    model = Polity_religion_family
    template_name = "general/polity_religion_family/polity_religion_family_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('polity_religion_familys')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Religion Family"
        context["var_main_desc"] = "The religion family of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'religion_family': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The religion family of a polity.', 'units': None, 'choices': 'RELIGION_FAMILY_CHOICES', 'null_meaning': 'This polity did not have a religion family.'}}
        context["potential_cols"] = []

        return context


class Polity_religion_familyListViewAll(generic.ListView):
    model = Polity_religion_family
    template_name = "general/polity_religion_family/polity_religion_family_list_all.html"

    def get_absolute_url(self):
        return reverse('polity_religion_familys_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Polity_religion_family.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Religion Family"
        context["var_main_desc"] = "The religion family of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'religion_family': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The religion family of a polity.', 'units': None, 'choices': 'RELIGION_FAMILY_CHOICES', 'null_meaning': 'This polity did not have a religion family.'}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Polity_religion_familyDetailView(generic.DetailView):
    model = Polity_religion_family
    template_name = "general/polity_religion_family/polity_religion_family_detail.html"


@permission_required('core.view_capital')
def polity_religion_family_download(request):
    items = Polity_religion_family.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_religion_familys.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'religion_family', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.religion_family, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def polity_religion_family_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_religion_familys.csv"'
    
    my_meta_data_dic = {'notes': None, 'main_desc': 'The religion family of a polity.', 'main_desc_source': None, 'section': 'General Variables', 'subsection': 'General'}
    my_meta_data_dic_inner_vars = {'religion_family': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The religion family of a polity.', 'units': None, 'choices': 'RELIGION_FAMILY_CHOICES', 'null_meaning': 'This polity did not have a religion family.'}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Polity_religionCreate(PermissionRequiredMixin, CreateView):
    model = Polity_religion
    form_class = Polity_religionForm
    template_name = "general/polity_religion/polity_religion_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('polity_religion-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Polity Religion"
        context["my_exp"] = "The religion of a polity."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'religion': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The religion of a polity.', 'units': None, 'choices': 'RELIGION_CHOICES', 'null_meaning': 'This polity did not have a religion.'}}
        context["potential_cols"] = []
        return context


class Polity_religionUpdate(PermissionRequiredMixin, UpdateView):
    model = Polity_religion
    form_class = Polity_religionForm
    template_name = "general/polity_religion/polity_religion_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Religion"

        return context

class Polity_religionDelete(PermissionRequiredMixin, DeleteView):
    model = Polity_religion
    success_url = reverse_lazy('polity_religions')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Polity_religionListView(generic.ListView):
    model = Polity_religion
    template_name = "general/polity_religion/polity_religion_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('polity_religions')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Religion"
        context["var_main_desc"] = "The religion of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'religion': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The religion of a polity.', 'units': None, 'choices': 'RELIGION_CHOICES', 'null_meaning': 'This polity did not have a religion.'}}
        context["potential_cols"] = []

        return context


class Polity_religionListViewAll(generic.ListView):
    model = Polity_religion
    template_name = "general/polity_religion/polity_religion_list_all.html"

    def get_absolute_url(self):
        return reverse('polity_religions_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Polity_religion.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Religion"
        context["var_main_desc"] = "The religion of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'religion': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The religion of a polity.', 'units': None, 'choices': 'RELIGION_CHOICES', 'null_meaning': 'This polity did not have a religion.'}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Polity_religionDetailView(generic.DetailView):
    model = Polity_religion
    template_name = "general/polity_religion/polity_religion_detail.html"


@permission_required('core.view_capital')
def polity_religion_download(request):
    items = Polity_religion.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_religions.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'religion', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.religion, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def polity_religion_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_religions.csv"'
    
    my_meta_data_dic = {'notes': None, 'main_desc': 'The religion of a polity.', 'main_desc_source': None, 'section': 'General Variables', 'subsection': 'General'}
    my_meta_data_dic_inner_vars = {'religion': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The religion of a polity.', 'units': None, 'choices': 'RELIGION_CHOICES', 'null_meaning': 'This polity did not have a religion.'}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Polity_relationship_to_preceding_entityCreate(PermissionRequiredMixin, CreateView):
    model = Polity_relationship_to_preceding_entity
    form_class = Polity_relationship_to_preceding_entityForm
    template_name = "general/polity_relationship_to_preceding_entity/polity_relationship_to_preceding_entity_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('polity_relationship_to_preceding_entity-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Polity Relationship to Preceding Entity"
        context["my_exp"] = "The polity relationship to preceding (quasi)polity"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'relationship_to_preceding_entity': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The polity relationship to preceding (quasi)polity', 'units': None, 'choices': 'RELATIONSHIP_TO_PRECEDING_ENTITY_CHOICES', 'null_meaning': 'This polity did not have a relationship to preceding (quasi)polity'}}
        context["potential_cols"] = []
        return context


class Polity_relationship_to_preceding_entityUpdate(PermissionRequiredMixin, UpdateView):
    model = Polity_relationship_to_preceding_entity
    form_class = Polity_relationship_to_preceding_entityForm
    template_name = "general/polity_relationship_to_preceding_entity/polity_relationship_to_preceding_entity_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Relationship to Preceding Entity"

        return context

class Polity_relationship_to_preceding_entityDelete(PermissionRequiredMixin, DeleteView):
    model = Polity_relationship_to_preceding_entity
    success_url = reverse_lazy('polity_relationship_to_preceding_entitys')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Polity_relationship_to_preceding_entityListView(generic.ListView):
    model = Polity_relationship_to_preceding_entity
    template_name = "general/polity_relationship_to_preceding_entity/polity_relationship_to_preceding_entity_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('polity_relationship_to_preceding_entitys')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Relationship to Preceding Entity"
        context["var_main_desc"] = "The polity relationship to preceding (quasi)polity"
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'relationship_to_preceding_entity': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The polity relationship to preceding (quasi)polity', 'units': None, 'choices': 'RELATIONSHIP_TO_PRECEDING_ENTITY_CHOICES', 'null_meaning': 'This polity did not have a relationship to preceding (quasi)polity'}}
        context["potential_cols"] = []

        return context


class Polity_relationship_to_preceding_entityListViewAll(generic.ListView):
    model = Polity_relationship_to_preceding_entity
    template_name = "general/polity_relationship_to_preceding_entity/polity_relationship_to_preceding_entity_list_all.html"

    def get_absolute_url(self):
        return reverse('polity_relationship_to_preceding_entitys_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Polity_relationship_to_preceding_entity.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Relationship to Preceding Entity"
        context["var_main_desc"] = "The polity relationship to preceding (quasi)polity"
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'relationship_to_preceding_entity': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The polity relationship to preceding (quasi)polity', 'units': None, 'choices': 'RELATIONSHIP_TO_PRECEDING_ENTITY_CHOICES', 'null_meaning': 'This polity did not have a relationship to preceding (quasi)polity'}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Polity_relationship_to_preceding_entityDetailView(generic.DetailView):
    model = Polity_relationship_to_preceding_entity
    template_name = "general/polity_relationship_to_preceding_entity/polity_relationship_to_preceding_entity_detail.html"


@permission_required('core.view_capital')
def polity_relationship_to_preceding_entity_download(request):
    items = Polity_relationship_to_preceding_entity.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_relationship_to_preceding_entitys.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'relationship_to_preceding_entity', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.relationship_to_preceding_entity, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def polity_relationship_to_preceding_entity_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_relationship_to_preceding_entitys.csv"'
    
    my_meta_data_dic = {'notes': None, 'main_desc': 'The polity relationship to preceding (quasi)polity', 'main_desc_source': None, 'section': 'General Variables', 'subsection': 'General'}
    my_meta_data_dic_inner_vars = {'relationship_to_preceding_entity': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The polity relationship to preceding (quasi)polity', 'units': None, 'choices': 'RELATIONSHIP_TO_PRECEDING_ENTITY_CHOICES', 'null_meaning': 'This polity did not have a relationship to preceding (quasi)polity'}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Polity_preceding_entityCreate(PermissionRequiredMixin, CreateView):
    model = Polity_preceding_entity
    form_class = Polity_preceding_entityForm
    template_name = "general/polity_preceding_entity/polity_preceding_entity_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('polity_preceding_entity-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Polity Preceding Entity"
        context["my_exp"] = "The preceding entity of a polity."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'preceding_entity': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The preceding entity (or the largest settlement) of a polity.', 'units': None, 'choices': None, 'null_meaning': 'This polity did not have a preceding entity.'}}
        context["potential_cols"] = []
        return context


class Polity_preceding_entityUpdate(PermissionRequiredMixin, UpdateView):
    model = Polity_preceding_entity
    form_class = Polity_preceding_entityForm
    template_name = "general/polity_preceding_entity/polity_preceding_entity_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Preceding Entity"

        return context

class Polity_preceding_entityDelete(PermissionRequiredMixin, DeleteView):
    model = Polity_preceding_entity
    success_url = reverse_lazy('polity_preceding_entitys')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Polity_preceding_entityListView(generic.ListView):
    model = Polity_preceding_entity
    template_name = "general/polity_preceding_entity/polity_preceding_entity_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('polity_preceding_entitys')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Preceding Entity"
        context["var_main_desc"] = "The preceding entity of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'preceding_entity': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The preceding entity (or the largest settlement) of a polity.', 'units': None, 'choices': None, 'null_meaning': 'This polity did not have a preceding entity.'}}
        context["potential_cols"] = []

        return context


class Polity_preceding_entityListViewAll(generic.ListView):
    model = Polity_preceding_entity
    template_name = "general/polity_preceding_entity/polity_preceding_entity_list_all.html"

    def get_absolute_url(self):
        return reverse('polity_preceding_entitys_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Polity_preceding_entity.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Preceding Entity"
        context["var_main_desc"] = "The preceding entity of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'preceding_entity': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The preceding entity (or the largest settlement) of a polity.', 'units': None, 'choices': None, 'null_meaning': 'This polity did not have a preceding entity.'}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Polity_preceding_entityDetailView(generic.DetailView):
    model = Polity_preceding_entity
    template_name = "general/polity_preceding_entity/polity_preceding_entity_detail.html"


@permission_required('core.view_capital')
def polity_preceding_entity_download(request):
    items = Polity_preceding_entity.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_preceding_entitys.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'preceding_entity', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.preceding_entity, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def polity_preceding_entity_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_preceding_entitys.csv"'
    
    my_meta_data_dic = {'notes': None, 'main_desc': 'The preceding entity of a polity.', 'main_desc_source': None, 'section': 'General Variables', 'subsection': 'General'}
    my_meta_data_dic_inner_vars = {'preceding_entity': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The preceding entity (or the largest settlement) of a polity.', 'units': None, 'choices': None, 'null_meaning': 'This polity did not have a preceding entity.'}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Polity_succeeding_entityCreate(PermissionRequiredMixin, CreateView):
    model = Polity_succeeding_entity
    form_class = Polity_succeeding_entityForm
    template_name = "general/polity_succeeding_entity/polity_succeeding_entity_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('polity_succeeding_entity-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Polity Succeeding Entity"
        context["my_exp"] = "The succeeding entity of a polity."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'succeeding_entity': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The succeeding entity (or the largest settlement) of a polity.', 'units': None, 'choices': None, 'null_meaning': 'This polity did not have a succeeding entity.'}}
        context["potential_cols"] = []
        return context


class Polity_succeeding_entityUpdate(PermissionRequiredMixin, UpdateView):
    model = Polity_succeeding_entity
    form_class = Polity_succeeding_entityForm
    template_name = "general/polity_succeeding_entity/polity_succeeding_entity_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Succeeding Entity"

        return context

class Polity_succeeding_entityDelete(PermissionRequiredMixin, DeleteView):
    model = Polity_succeeding_entity
    success_url = reverse_lazy('polity_succeeding_entitys')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Polity_succeeding_entityListView(generic.ListView):
    model = Polity_succeeding_entity
    template_name = "general/polity_succeeding_entity/polity_succeeding_entity_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('polity_succeeding_entitys')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Succeeding Entity"
        context["var_main_desc"] = "The succeeding entity of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'succeeding_entity': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The succeeding entity (or the largest settlement) of a polity.', 'units': None, 'choices': None, 'null_meaning': 'This polity did not have a succeeding entity.'}}
        context["potential_cols"] = []

        return context


class Polity_succeeding_entityListViewAll(generic.ListView):
    model = Polity_succeeding_entity
    template_name = "general/polity_succeeding_entity/polity_succeeding_entity_list_all.html"

    def get_absolute_url(self):
        return reverse('polity_succeeding_entitys_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Polity_succeeding_entity.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Succeeding Entity"
        context["var_main_desc"] = "The succeeding entity of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'succeeding_entity': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The succeeding entity (or the largest settlement) of a polity.', 'units': None, 'choices': None, 'null_meaning': 'This polity did not have a succeeding entity.'}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Polity_succeeding_entityDetailView(generic.DetailView):
    model = Polity_succeeding_entity
    template_name = "general/polity_succeeding_entity/polity_succeeding_entity_detail.html"


@permission_required('core.view_capital')
def polity_succeeding_entity_download(request):
    items = Polity_succeeding_entity.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_succeeding_entitys.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'succeeding_entity', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.succeeding_entity, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def polity_succeeding_entity_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_succeeding_entitys.csv"'
    
    my_meta_data_dic = {'notes': None, 'main_desc': 'The succeeding entity of a polity.', 'main_desc_source': None, 'section': 'General Variables', 'subsection': 'General'}
    my_meta_data_dic_inner_vars = {'succeeding_entity': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The succeeding entity (or the largest settlement) of a polity.', 'units': None, 'choices': None, 'null_meaning': 'This polity did not have a succeeding entity.'}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Polity_supracultural_entityCreate(PermissionRequiredMixin, CreateView):
    model = Polity_supracultural_entity
    form_class = Polity_supracultural_entityForm
    template_name = "general/polity_supracultural_entity/polity_supracultural_entity_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('polity_supracultural_entity-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Polity Supracultural Entity"
        context["my_exp"] = "The supracultural entity of a polity."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'supracultural_entity': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The supracultural entity (or the largest settlement) of a polity.', 'units': None, 'choices': None, 'null_meaning': 'This polity did not have a supracultural entity.'}}
        context["potential_cols"] = []
        return context


class Polity_supracultural_entityUpdate(PermissionRequiredMixin, UpdateView):
    model = Polity_supracultural_entity
    form_class = Polity_supracultural_entityForm
    template_name = "general/polity_supracultural_entity/polity_supracultural_entity_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Supracultural Entity"

        return context

class Polity_supracultural_entityDelete(PermissionRequiredMixin, DeleteView):
    model = Polity_supracultural_entity
    success_url = reverse_lazy('polity_supracultural_entitys')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Polity_supracultural_entityListView(generic.ListView):
    model = Polity_supracultural_entity
    template_name = "general/polity_supracultural_entity/polity_supracultural_entity_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('polity_supracultural_entitys')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Supracultural Entity"
        context["var_main_desc"] = "The supracultural entity of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'supracultural_entity': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The supracultural entity (or the largest settlement) of a polity.', 'units': None, 'choices': None, 'null_meaning': 'This polity did not have a supracultural entity.'}}
        context["potential_cols"] = []

        return context


class Polity_supracultural_entityListViewAll(generic.ListView):
    model = Polity_supracultural_entity
    template_name = "general/polity_supracultural_entity/polity_supracultural_entity_list_all.html"

    def get_absolute_url(self):
        return reverse('polity_supracultural_entitys_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Polity_supracultural_entity.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Supracultural Entity"
        context["var_main_desc"] = "The supracultural entity of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'supracultural_entity': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The supracultural entity (or the largest settlement) of a polity.', 'units': None, 'choices': None, 'null_meaning': 'This polity did not have a supracultural entity.'}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Polity_supracultural_entityDetailView(generic.DetailView):
    model = Polity_supracultural_entity
    template_name = "general/polity_supracultural_entity/polity_supracultural_entity_detail.html"


@permission_required('core.view_capital')
def polity_supracultural_entity_download(request):
    items = Polity_supracultural_entity.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_supracultural_entitys.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'supracultural_entity', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.supracultural_entity, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def polity_supracultural_entity_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_supracultural_entitys.csv"'
    
    my_meta_data_dic = {'notes': None, 'main_desc': 'The supracultural entity of a polity.', 'main_desc_source': None, 'section': 'General Variables', 'subsection': 'General'}
    my_meta_data_dic_inner_vars = {'supracultural_entity': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The supracultural entity (or the largest settlement) of a polity.', 'units': None, 'choices': None, 'null_meaning': 'This polity did not have a supracultural entity.'}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Polity_scale_of_supracultural_interactionCreate(PermissionRequiredMixin, CreateView):
    model = Polity_scale_of_supracultural_interaction
    form_class = Polity_scale_of_supracultural_interactionForm
    template_name = "general/polity_scale_of_supracultural_interaction/polity_scale_of_supracultural_interaction_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('polity_scale_of_supracultural_interaction-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Polity Scale of Supracultural Interaction"
        context["my_exp"] = "The scale_of_supra_cultural_interaction of a polity."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'scale_from': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower scale of supra cultural interactionfor a polity.', 'units': 'km squared', 'choices': None, 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}, 'scale_to': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The upper scale of supra cultural interactionfor a polity.', 'units': 'km squared', 'choices': None, 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}}
        context["potential_cols"] = []
        return context


class Polity_scale_of_supracultural_interactionUpdate(PermissionRequiredMixin, UpdateView):
    model = Polity_scale_of_supracultural_interaction
    form_class = Polity_scale_of_supracultural_interactionForm
    template_name = "general/polity_scale_of_supracultural_interaction/polity_scale_of_supracultural_interaction_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Scale of Supracultural Interaction"

        return context

class Polity_scale_of_supracultural_interactionDelete(PermissionRequiredMixin, DeleteView):
    model = Polity_scale_of_supracultural_interaction
    success_url = reverse_lazy('polity_scale_of_supracultural_interactions')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Polity_scale_of_supracultural_interactionListView(generic.ListView):
    model = Polity_scale_of_supracultural_interaction
    template_name = "general/polity_scale_of_supracultural_interaction/polity_scale_of_supracultural_interaction_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('polity_scale_of_supracultural_interactions')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Scale of Supracultural Interaction"
        context["var_main_desc"] = "The scale of Supra Cultural Interaction of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'scale_from': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower scale of supra cultural interactionfor a polity.', 'units': 'km squared', 'choices': None, 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}, 'scale_to': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The upper scale of supra cultural interactionfor a polity.', 'units': 'km squared', 'choices': None, 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}}
        context["potential_cols"] = ['Units']

        return context


class Polity_scale_of_supracultural_interactionListViewAll(generic.ListView):
    model = Polity_scale_of_supracultural_interaction
    template_name = "general/polity_scale_of_supracultural_interaction/polity_scale_of_supracultural_interaction_list_all.html"

    def get_absolute_url(self):
        return reverse('polity_scale_of_supracultural_interactions_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Polity_scale_of_supracultural_interaction.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Scale of Supracultural Interaction"
        context["var_main_desc"] = "The scale of Supra Cultural Interaction of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'scale_from': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower scale of supra cultural interactionfor a polity.', 'units': 'km squared', 'choices': None, 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}, 'scale_to': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The upper scale of supra cultural interactionfor a polity.', 'units': 'km squared', 'choices': None, 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}}
        context["potential_cols"] = ['Units']
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Polity_scale_of_supracultural_interactionDetailView(generic.DetailView):
    model = Polity_scale_of_supracultural_interaction
    template_name = "general/polity_scale_of_supracultural_interaction/polity_scale_of_supracultural_interaction_detail.html"


@permission_required('core.view_capital')
def polity_scale_of_supracultural_interaction_download(request):
    items = Polity_scale_of_supracultural_interaction.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_scale_of_supracultural_interactions.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'scale_from', 'scale_to', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.scale_from, obj.scale_to, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def polity_scale_of_supracultural_interaction_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_scale_of_supracultural_interactions.csv"'
    
    my_meta_data_dic = {'notes': None, 'main_desc': 'The scale_of_supra_cultural_interaction of a polity.', 'main_desc_source': None, 'section': 'General Variables', 'subsection': 'General'}
    my_meta_data_dic_inner_vars = {'scale_from': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower scale of supra cultural interactionfor a polity.', 'units': 'km squared', 'choices': None, 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}, 'scale_to': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The upper scale of supra cultural interactionfor a polity.', 'units': 'km squared', 'choices': None, 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Polity_alternate_religion_genusCreate(PermissionRequiredMixin, CreateView):
    model = Polity_alternate_religion_genus
    form_class = Polity_alternate_religion_genusForm
    template_name = "general/polity_alternate_religion_genus/polity_alternate_religion_genus_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('polity_alternate_religion_genus-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Polity Alternate Religion Genus"
        context["my_exp"] = "The alternate religion genus of a polity."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'alternate_religion_genus': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The alternate religion genus of a polity.', 'units': None, 'choices': 'RELIGION_GENUS_CHOICES', 'null_meaning': 'This polity did not have a alternatereligion genus.'}}
        context["potential_cols"] = []
        return context


class Polity_alternate_religion_genusUpdate(PermissionRequiredMixin, UpdateView):
    model = Polity_alternate_religion_genus
    form_class = Polity_alternate_religion_genusForm
    template_name = "general/polity_alternate_religion_genus/polity_alternate_religion_genus_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Alternate Religion Genus"

        return context

class Polity_alternate_religion_genusDelete(PermissionRequiredMixin, DeleteView):
    model = Polity_alternate_religion_genus
    success_url = reverse_lazy('polity_alternate_religion_genuss')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Polity_alternate_religion_genusListView(generic.ListView):
    model = Polity_alternate_religion_genus
    template_name = "general/polity_alternate_religion_genus/polity_alternate_religion_genus_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('polity_alternate_religion_genuss')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Alternate Religion Genus"
        context["var_main_desc"] = "The alternate religion genus of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'alternate_religion_genus': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The alternate religion genus of a polity.', 'units': None, 'choices': 'RELIGION_GENUS_CHOICES', 'null_meaning': 'This polity did not have a alternatereligion genus.'}}
        context["potential_cols"] = []

        return context


class Polity_alternate_religion_genusListViewAll(generic.ListView):
    model = Polity_alternate_religion_genus
    template_name = "general/polity_alternate_religion_genus/polity_alternate_religion_genus_list_all.html"

    def get_absolute_url(self):
        return reverse('polity_alternate_religion_genuss_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Polity_alternate_religion_genus.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Alternate Religion Genus"
        context["var_main_desc"] = "The alternate religion genus of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'alternate_religion_genus': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The alternate religion genus of a polity.', 'units': None, 'choices': 'RELIGION_GENUS_CHOICES', 'null_meaning': 'This polity did not have a alternatereligion genus.'}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Polity_alternate_religion_genusDetailView(generic.DetailView):
    model = Polity_alternate_religion_genus
    template_name = "general/polity_alternate_religion_genus/polity_alternate_religion_genus_detail.html"


@permission_required('core.view_capital')
def polity_alternate_religion_genus_download(request):
    items = Polity_alternate_religion_genus.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_alternate_religion_genuss.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'alternate_religion_genus', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.alternate_religion_genus, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def polity_alternate_religion_genus_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_alternate_religion_genuss.csv"'
    
    my_meta_data_dic = {'notes': None, 'main_desc': 'The alternate religion genus of a polity.', 'main_desc_source': None, 'section': 'General Variables', 'subsection': 'General'}
    my_meta_data_dic_inner_vars = {'alternate_religion_genus': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The alternate religion genus of a polity.', 'units': None, 'choices': 'RELIGION_GENUS_CHOICES', 'null_meaning': 'This polity did not have a alternatereligion genus.'}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Polity_alternate_religion_familyCreate(PermissionRequiredMixin, CreateView):
    model = Polity_alternate_religion_family
    form_class = Polity_alternate_religion_familyForm
    template_name = "general/polity_alternate_religion_family/polity_alternate_religion_family_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('polity_alternate_religion_family-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Polity Alternate Religion Family"
        context["my_exp"] = "The alternate religion family of a polity."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'alternate_religion_family': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The alternate religion family of a polity.', 'units': None, 'choices': 'RELIGION_FAMILY_CHOICES', 'null_meaning': 'This polity did not have a alternate religion family.'}}
        context["potential_cols"] = []
        return context


class Polity_alternate_religion_familyUpdate(PermissionRequiredMixin, UpdateView):
    model = Polity_alternate_religion_family
    form_class = Polity_alternate_religion_familyForm
    template_name = "general/polity_alternate_religion_family/polity_alternate_religion_family_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Alternate Religion Family"

        return context

class Polity_alternate_religion_familyDelete(PermissionRequiredMixin, DeleteView):
    model = Polity_alternate_religion_family
    success_url = reverse_lazy('polity_alternate_religion_familys')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Polity_alternate_religion_familyListView(generic.ListView):
    model = Polity_alternate_religion_family
    template_name = "general/polity_alternate_religion_family/polity_alternate_religion_family_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('polity_alternate_religion_familys')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Alternate Religion Family"
        context["var_main_desc"] = "The alternate religion family of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'alternate_religion_family': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The alternate religion family of a polity.', 'units': None, 'choices': 'RELIGION_FAMILY_CHOICES', 'null_meaning': 'This polity did not have a alternate religion family.'}}
        context["potential_cols"] = []

        return context


class Polity_alternate_religion_familyListViewAll(generic.ListView):
    model = Polity_alternate_religion_family
    template_name = "general/polity_alternate_religion_family/polity_alternate_religion_family_list_all.html"

    def get_absolute_url(self):
        return reverse('polity_alternate_religion_familys_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Polity_alternate_religion_family.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Alternate Religion Family"
        context["var_main_desc"] = "The alternate religion family of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'alternate_religion_family': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The alternate religion family of a polity.', 'units': None, 'choices': 'RELIGION_FAMILY_CHOICES', 'null_meaning': 'This polity did not have a alternate religion family.'}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Polity_alternate_religion_familyDetailView(generic.DetailView):
    model = Polity_alternate_religion_family
    template_name = "general/polity_alternate_religion_family/polity_alternate_religion_family_detail.html"


@permission_required('core.view_capital')
def polity_alternate_religion_family_download(request):
    items = Polity_alternate_religion_family.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_alternate_religion_familys.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'alternate_religion_family', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.alternate_religion_family, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def polity_alternate_religion_family_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_alternate_religion_familys.csv"'
    
    my_meta_data_dic = {'notes': None, 'main_desc': 'The alternate religion family of a polity.', 'main_desc_source': None, 'section': 'General Variables', 'subsection': 'General'}
    my_meta_data_dic_inner_vars = {'alternate_religion_family': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The alternate religion family of a polity.', 'units': None, 'choices': 'RELIGION_FAMILY_CHOICES', 'null_meaning': 'This polity did not have a alternate religion family.'}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Polity_alternate_religionCreate(PermissionRequiredMixin, CreateView):
    model = Polity_alternate_religion
    form_class = Polity_alternate_religionForm
    template_name = "general/polity_alternate_religion/polity_alternate_religion_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('polity_alternate_religion-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Polity Alternate Religion"
        context["my_exp"] = "The alternate religion  of a polity."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'alternate_religion': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The alternate religion of a polity.', 'units': None, 'choices': 'RELIGION_CHOICES', 'null_meaning': 'This polity did not have a alternate religion .'}}
        context["potential_cols"] = []
        return context


class Polity_alternate_religionUpdate(PermissionRequiredMixin, UpdateView):
    model = Polity_alternate_religion
    form_class = Polity_alternate_religionForm
    template_name = "general/polity_alternate_religion/polity_alternate_religion_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Alternate Religion"

        return context

class Polity_alternate_religionDelete(PermissionRequiredMixin, DeleteView):
    model = Polity_alternate_religion
    success_url = reverse_lazy('polity_alternate_religions')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Polity_alternate_religionListView(generic.ListView):
    model = Polity_alternate_religion
    template_name = "general/polity_alternate_religion/polity_alternate_religion_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('polity_alternate_religions')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Alternate Religion"
        context["var_main_desc"] = "The alternate religion  of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'alternate_religion': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The alternate religion of a polity.', 'units': None, 'choices': 'RELIGION_CHOICES', 'null_meaning': 'This polity did not have a alternate religion .'}}
        context["potential_cols"] = []

        return context


class Polity_alternate_religionListViewAll(generic.ListView):
    model = Polity_alternate_religion
    template_name = "general/polity_alternate_religion/polity_alternate_religion_list_all.html"

    def get_absolute_url(self):
        return reverse('polity_alternate_religions_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Polity_alternate_religion.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Alternate Religion"
        context["var_main_desc"] = "The alternate religion  of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'alternate_religion': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The alternate religion of a polity.', 'units': None, 'choices': 'RELIGION_CHOICES', 'null_meaning': 'This polity did not have a alternate religion .'}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Polity_alternate_religionDetailView(generic.DetailView):
    model = Polity_alternate_religion
    template_name = "general/polity_alternate_religion/polity_alternate_religion_detail.html"


@permission_required('core.view_capital')
def polity_alternate_religion_download(request):
    items = Polity_alternate_religion.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_alternate_religions.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'alternate_religion', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.alternate_religion, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def polity_alternate_religion_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_alternate_religions.csv"'
    
    my_meta_data_dic = {'notes': None, 'main_desc': 'The alternate religion  of a polity.', 'main_desc_source': None, 'section': 'General Variables', 'subsection': 'General'}
    my_meta_data_dic_inner_vars = {'alternate_religion': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The alternate religion of a polity.', 'units': None, 'choices': 'RELIGION_CHOICES', 'null_meaning': 'This polity did not have a alternate religion .'}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Polity_expertCreate(PermissionRequiredMixin, CreateView):
    model = Polity_expert
    form_class = Polity_expertForm
    template_name = "general/polity_expert/polity_expert_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('polity_expert-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Polity Expert"
        context["my_exp"] = "The expert of a polity."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'expert': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The expert of a polity.', 'units': None, 'choices': None, 'null_meaning': 'This polity did not have an expert.'}}
        context["potential_cols"] = []
        return context


class Polity_expertUpdate(PermissionRequiredMixin, UpdateView):
    model = Polity_expert
    form_class = Polity_expertForm
    template_name = "general/polity_expert/polity_expert_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Expert"

        return context

class Polity_expertDelete(PermissionRequiredMixin, DeleteView):
    model = Polity_expert
    success_url = reverse_lazy('polity_experts')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Polity_expertListView(generic.ListView):
    model = Polity_expert
    template_name = "general/polity_expert/polity_expert_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('polity_experts')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Expert"
        context["var_main_desc"] = "The expert of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'expert': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The expert of a polity.', 'units': None, 'choices': None, 'null_meaning': 'This polity did not have an expert.'}}
        context["potential_cols"] = []

        return context


class Polity_expertListViewAll(generic.ListView):
    model = Polity_expert
    template_name = "general/polity_expert/polity_expert_list_all.html"

    def get_absolute_url(self):
        return reverse('polity_experts_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Polity_expert.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Expert"
        context["var_main_desc"] = "The expert of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'expert': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The expert of a polity.', 'units': None, 'choices': None, 'null_meaning': 'This polity did not have an expert.'}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Polity_expertDetailView(generic.DetailView):
    model = Polity_expert
    template_name = "general/polity_expert/polity_expert_detail.html"


@permission_required('core.view_capital')
def polity_expert_download(request):
    items = Polity_expert.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_experts.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'expert', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.expert, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def polity_expert_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_experts.csv"'
    
    my_meta_data_dic = {'notes': None, 'main_desc': 'The expert of a polity.', 'main_desc_source': None, 'section': 'General Variables', 'subsection': 'General'}
    my_meta_data_dic_inner_vars = {'expert': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The expert of a polity.', 'units': None, 'choices': None, 'null_meaning': 'This polity did not have an expert.'}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Polity_editorCreate(PermissionRequiredMixin, CreateView):
    model = Polity_editor
    form_class = Polity_editorForm
    template_name = "general/polity_editor/polity_editor_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('polity_editor-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Polity Editor"
        context["my_exp"] = "The editor of a polity."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'editor': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The editor of a polity.', 'units': None, 'choices': None, 'null_meaning': 'This polity did not have an editor.'}}
        context["potential_cols"] = []
        return context


class Polity_editorUpdate(PermissionRequiredMixin, UpdateView):
    model = Polity_editor
    form_class = Polity_editorForm
    template_name = "general/polity_editor/polity_editor_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Editor"

        return context

class Polity_editorDelete(PermissionRequiredMixin, DeleteView):
    model = Polity_editor
    success_url = reverse_lazy('polity_editors')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Polity_editorListView(generic.ListView):
    model = Polity_editor
    template_name = "general/polity_editor/polity_editor_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('polity_editors')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Editor"
        context["var_main_desc"] = "The editor of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'editor': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The editor of a polity.', 'units': None, 'choices': None, 'null_meaning': 'This polity did not have an editor.'}}
        context["potential_cols"] = []

        return context


class Polity_editorListViewAll(generic.ListView):
    model = Polity_editor
    template_name = "general/polity_editor/polity_editor_list_all.html"

    def get_absolute_url(self):
        return reverse('polity_editors_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Polity_editor.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Editor"
        context["var_main_desc"] = "The editor of a polity."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'editor': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The editor of a polity.', 'units': None, 'choices': None, 'null_meaning': 'This polity did not have an editor.'}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Polity_editorDetailView(generic.DetailView):
    model = Polity_editor
    template_name = "general/polity_editor/polity_editor_detail.html"


@permission_required('core.view_capital')
def polity_editor_download(request):
    items = Polity_editor.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_editors.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'editor', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.editor, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def polity_editor_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_editors.csv"'
    
    my_meta_data_dic = {'notes': None, 'main_desc': 'The editor of a polity.', 'main_desc_source': None, 'section': 'General Variables', 'subsection': 'General'}
    my_meta_data_dic_inner_vars = {'editor': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The editor of a polity.', 'units': None, 'choices': None, 'null_meaning': 'This polity did not have an editor.'}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Polity_religious_traditionCreate(PermissionRequiredMixin, CreateView):
    model = Polity_religious_tradition
    form_class = Polity_religious_traditionForm
    template_name = "general/polity_religious_tradition/polity_religious_tradition_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('polity_religious_tradition-create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Polity Religious Tradition"
        context["my_exp"] = "The details of religious traditions."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'religious_tradition': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The details of religious traditions.', 'units': None, 'choices': None, 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}}
        context["potential_cols"] = []
        return context


class Polity_religious_traditionUpdate(PermissionRequiredMixin, UpdateView):
    model = Polity_religious_tradition
    form_class = Polity_religious_traditionForm
    template_name = "general/polity_religious_tradition/polity_religious_tradition_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Religious Tradition"

        return context

class Polity_religious_traditionDelete(PermissionRequiredMixin, DeleteView):
    model = Polity_religious_tradition
    success_url = reverse_lazy('polity_religious_traditions')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Polity_religious_traditionListView(generic.ListView):
    model = Polity_religious_tradition
    template_name = "general/polity_religious_tradition/polity_religious_tradition_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('polity_religious_traditions')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Religious Tradition"
        context["var_main_desc"] = "The details of religious traditions."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'religious_tradition': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The details of religious traditions.', 'units': None, 'choices': None, 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}}
        context["potential_cols"] = []

        return context


class Polity_religious_traditionListViewAll(generic.ListView):
    model = Polity_religious_tradition
    template_name = "general/polity_religious_tradition/polity_religious_tradition_list_all.html"

    def get_absolute_url(self):
        return reverse('polity_religious_traditions_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Polity_religious_tradition.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Religious Tradition"
        context["var_main_desc"] = "The details of religious traditions."
        context["var_main_desc_source"] = "None"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "General"
        context["inner_vars"] = {'religious_tradition': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The details of religious traditions.', 'units': None, 'choices': None, 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Polity_religious_traditionDetailView(generic.DetailView):
    model = Polity_religious_tradition
    template_name = "general/polity_religious_tradition/polity_religious_tradition_detail.html"


@permission_required('core.view_capital')
def polity_religious_tradition_download(request):
    items = Polity_religious_tradition.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_religious_traditions.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'religious_tradition', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity, obj.polity.new_name, obj.polity.name, obj.religious_tradition, obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def polity_religious_tradition_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="polity_religious_traditions.csv"'
    
    my_meta_data_dic = {'notes': None, 'main_desc': 'The details of religious traditions.', 'main_desc_source': None, 'section': 'General Variables', 'subsection': 'General'}
    my_meta_data_dic_inner_vars = {'religious_tradition': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The details of religious traditions.', 'units': None, 'choices': None, 'null_meaning': 'No_Value_Provided_in_Old_Wiki'}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

def generalvars(request):

    app_name = 'general'  # Replace with your app name
    models = apps.get_app_config(app_name).get_models()

    unique_politys = set()
    number_of_all_rows = 0
    number_of_variables = 0
    counts = {}
    for model in models:
        model_name = model.__name__
        count = model.objects.count()
        number_of_all_rows += count
        model_title = model_name.replace("_", " ").title()
        model_create = model_name.lower() + "-create"
        model_download = model_name.lower() + "-download"
        model_metadownload = model_name.lower() + "-metadownload"
        model_all = model_name.lower() + "s_all"
        model_s = model_name.lower() + "s"

        queryset = model.objects.all()
        politys = queryset.values_list('polity', flat=True).distinct()
        unique_politys.update(politys)
        number_of_variables += 1

        counts[model_name] = [model_title, model_s, model_create, model_download, model_metadownload, model_all, count]


    context = {}
    context["my_counts"] = counts
    context["all_polities"] = len(unique_politys)
    context["number_of_all_rows"] = number_of_all_rows

    context["number_of_variables"] = number_of_variables

    return render(request, 'general/generalvars.html', context=context)

    