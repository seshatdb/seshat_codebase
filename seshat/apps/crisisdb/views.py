
from seshat.utils.utils import adder, dic_of_all_vars, list_of_all_Polities, dic_of_all_vars_in_sections, dic_of_all_vars_with_varhier
from django.db.models.base import Model
# from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.safestring import mark_safe
from django.views.generic.list import ListView

from django.contrib.contenttypes.models import ContentType

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.db.models import F, Count, CharField, ExpressionWrapper
from ..general.mixins import PolityIdMixin


from django.http import HttpResponseRedirect, response, JsonResponse, HttpResponseForbidden
from ..core.models import Citation, Reference, Polity, Section, Subsection, Country, Variablehierarchy, SeshatComment, SeshatCommentPart
from seshat.apps.accounts.models import Seshat_Expert

# from .mycodes import *
from django.conf import settings

from django.urls import reverse, reverse_lazy

from django.views import generic
import csv
import datetime

from django.core.paginator import Paginator

from django.http import HttpResponse
from django.template.loader import render_to_string

import requests
from requests.structures import CaseInsensitiveDict

from django.contrib import messages



import re


def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

from .models import Power_transition, Crisis_consequence, Human_sacrifice, External_conflict, Internal_conflict, External_conflict_side, Agricultural_population, Arable_land, Arable_land_per_farmer, Gross_grain_shared_per_agricultural_population, Net_grain_shared_per_agricultural_population, Surplus, Military_expense, Silver_inflow, Silver_stock, Total_population, Gdp_per_capita, Drought_event, Locust_event, Socioeconomic_turmoil_event, Crop_failure_event, Famine_event, Disease_outbreak, Us_location, Us_violence_subtype, Us_violence_data_source, Us_violence


from .forms import Power_transitionForm, Crisis_consequenceForm, Human_sacrificeForm, External_conflictForm, Internal_conflictForm, External_conflict_sideForm, Agricultural_populationForm, Arable_landForm, Arable_land_per_farmerForm, Gross_grain_shared_per_agricultural_populationForm, Net_grain_shared_per_agricultural_populationForm, SurplusForm, Military_expenseForm, Silver_inflowForm, Silver_stockForm, Total_populationForm, Gdp_per_capitaForm, Drought_eventForm, Locust_eventForm, Socioeconomic_turmoil_eventForm, Crop_failure_eventForm, Famine_eventForm, Disease_outbreakForm, Us_locationForm, Us_violence_subtypeForm, Us_violence_data_sourceForm, Us_violenceForm




# Consequences of Crisis:


def get_citations_dropdown(request):
    # get dropdown data here
    all_data = Citation.objects.all()
    data = all_data #{'citations': all_data}
    citations_list = []
    counter = 0
    for item in data:
        if counter <5000:
            citations_list.append({
                'id': item.id,
                'name': item.__str__(),
            }
            )
            counter = counter + 1

    # render dropdown template as string
    #html = render_to_string('crisisdb/crisis_consequence/crisis_citation_dropdown.html', data)

    # return dropdown template as JSON response
    return JsonResponse({'data': citations_list})

class Crisis_consequenceCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    model = Crisis_consequence
    form_class = Crisis_consequenceForm
    success_url = reverse_lazy("crisis_consequences_all")
    template_name = "crisisdb/crisis_consequence/crisis_consequence_form.html"
    permission_required = 'core.add_capital'

    def get_success_url(self):
        polity_id = self.object.polity.id
        return reverse('polity-detail-main', kwargs={'pk': polity_id}) + '#crisis_case_var'

    def get_absolute_url(self):
        return reverse('crisis_consequence-create')
    def get_context_data(self, **kwargs):
        # get the explanattion:
        context = super().get_context_data(**kwargs)
        context["mysection"] = "X"
        context["mysubsection"] = "Y"
        context["myvar"] = "Z"
        context["my_exp"] = "Conequences of Crisis Explanataion"
        context["mytitle"] = "Add a NEW crisis case below:"
        context["mysubtitle"] = "Please complete the form below to submit a new Crisis Case to the database:"

        return context

class Crisis_consequenceUpdate(PermissionRequiredMixin, UpdateView):
    model = Crisis_consequence
    success_url = reverse_lazy('crisis_consequences_all')
    form_class = Crisis_consequenceForm
    template_name = "crisisdb/crisis_consequence/crisis_consequence_form.html"
    permission_required = 'core.add_capital'

    def get_success_url(self):
        polity_id = self.object.polity.id
        return reverse('polity-detail-main', kwargs={'pk': polity_id}) + '#crisis_case_var'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Z"
        context["mytitle"] = "Update the crisis case below:"
        context["mysubtitle"] = "Please complete the form below to update the Crisis Case:"


        return context
    
class Crisis_consequenceCreateHeavy(PermissionRequiredMixin, CreateView):
    model = Crisis_consequence
    form_class = Crisis_consequenceForm
    success_url = reverse_lazy("crisis_consequences_all")
    template_name = "crisisdb/crisis_consequence/crisis_consequence_form_heavy.html"
    permission_required = 'core.add_capital'

    def get_success_url(self):
        polity_id = self.object.polity.id
        return reverse('polity-detail-main', kwargs={'pk': polity_id}) + '#crisis_case_var'

    def get_absolute_url(self):
        return reverse('crisis_consequence-create')
    def get_context_data(self, **kwargs):
        # get the explanattion:
        context = super().get_context_data(**kwargs)
        context["mysection"] = "X"
        context["mysubsection"] = "Y"
        context["myvar"] = "Z"
        context["my_exp"] = "Conequences of Crisis Explanataion"
        context["mytitle"] = "Add a NEW crisis case below:"
        context["mysubtitle"] = "Please complete the form below to create a new Crisis Case:"
        return context

class Crisis_consequenceUpdateHeavy(PermissionRequiredMixin, UpdateView):
    model = Crisis_consequence
    success_url = reverse_lazy('crisis_consequences_all')
    form_class = Crisis_consequenceForm
    template_name = "crisisdb/crisis_consequence/crisis_consequence_form_heavy.html"
    permission_required = 'core.add_capital'

    def get_success_url(self):
        polity_id = self.object.polity.id
        return reverse('polity-detail-main', kwargs={'pk': polity_id}) + '#crisis_case_var'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Z"
        context["mytitle"] = "Update the crisis case below:"
        context["mysubtitle"] = "Please complete the form below to update the Crisis Case:"

        return context

class Crisis_consequenceDelete(PermissionRequiredMixin, DeleteView):
    model = Crisis_consequence
    success_url = reverse_lazy('crisis_consequences_all')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'

class Crisis_consequenceListView(PermissionRequiredMixin, generic.ListView):
    model = Crisis_consequence
    template_name = "crisisdb/crisis_consequence/crisis_consequence_list.html"
    permission_required = 'core.add_capital'

    #paginate_by = 50

    def get_absolute_url(self):
        return reverse('crisis_consequences')
    
    def get_queryset(self):
        order = self.request.GET.get('orderby', 'home_nga')
        order2 = self.request.GET.get('orderby2', 'year_from')

        new_context = Crisis_consequence.objects.all().annotate(
            home_nga=ExpressionWrapper(
                F('polity__home_nga__name'),
                output_field=CharField()
            )
        ).order_by(order, order2)

        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fields"] = ['decline', 'collapse', 'epidemic', 'downward_mobility', 'extermination', 'uprising', 'revolution', 'successful_revolution', 'civil_war', 'century_plus', 'fragmentation', 'capital', 'conquest', 'assassination', 'depose', 'constitution', 'labor', 'unfree_labor', 'suffrage', 'public_goods', 'religion']

        context["myvar"] = "XX"
        context["var_main_desc"] = "YY"
        context["var_main_desc_source"] = ""
        context["var_section"] = "frffrr"
        context["var_subsection"] = "frtgtz"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'crisis_consequence': {'min': None, 'max': None, 'scale': 1000, 'var_exp_source': None, 'var_exp': 'No Explanations.', 'units': 'mu?', 'choices': None}}
        context["potential_cols"] = ['Scale', 'Units']

        return context
    
class Crisis_consequenceListViewAll(PermissionRequiredMixin, generic.ListView):
    model = Crisis_consequence
    template_name = "crisisdb/crisis_consequence/crisis_consequence_list_all.html"
    permission_required = 'core.add_capital'

    #paginate_by = 50

    def get_absolute_url(self):
        return reverse('crisis_consequences_all')

    def get_queryset(self):
        #order = self.request.GET.get('orderby', 'year_from')
        order = self.request.GET.get('orderby', 'home_nga')
        order2 = self.request.GET.get('orderby2', 'year_from')
        #polity.home_nga.id
        #orders = [order, order2]
        new_context = Crisis_consequence.objects.all().annotate(
            home_nga=ExpressionWrapper(
                F('polity__home_nga__name'),
                output_field=CharField()
            )
        ).order_by(order, order2)
        #.polity.home_nga.id
        #new_context = Crisis_consequence.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "uu"
        context["var_main_desc"] = "xx"
        context["var_main_desc_source"] = ""
        context["var_section"] = "Religion and Normative Ideology"
        context["var_subsection"] = "uu"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'Crisis_consequence': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of Human Sacrifce.', 'units': None, 'choices': ['- Unknown', '- Present', '- Transitional (Present -> Absent)', '- Absent', '- Transitional (Absent -> Present)']}}
        context["potential_cols"] = ["choices"]
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Crisis_consequenceDetailView(PermissionRequiredMixin, generic.DetailView):
    model = Crisis_consequence
    template_name = "crisisdb/crisis_consequence/crisis_consequence_detail.html"
    permission_required = 'core.add_capital'


@permission_required('core.view_capital')
def crisis_consequence_download(request):
    items = Crisis_consequence.objects.all()

    response = HttpResponse(content_type='text/csv')

    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"crisis_consequences_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                   'polity_new_ID', 'polity_old_ID', 'polity_long_name',
                    'other_polity_new_ID', 'other_polity_old_ID', 'other_polity_long_name', 'crisis_consequence_id', 'decline', 'collapse', 'epidemic', 'downward_mobility', 'extermination', 'uprising', 'revolution', 'successful_revolution', 'civil_war', 'century_plus', 'fragmentation', 'capital', 'conquest', 'assassination', 'depose', 'constitution', 'labor', 'unfree_labor', 'suffrage', 'public_goods', 'religion', 'description'])

    for obj in items:
        if obj.other_polity:
            writer.writerow([obj.year_from, obj.year_to,
                            obj.polity.new_name, obj.polity.name, obj.polity.long_name, 
                            obj.other_polity.new_name, obj.other_polity.name, obj.other_polity.long_name, obj.crisis_case_id, obj.decline, obj.collapse, obj.epidemic, obj.downward_mobility, obj.extermination, obj.uprising, obj.revolution, obj.successful_revolution, obj.civil_war, obj.century_plus, obj.fragmentation, obj.capital, obj.conquest, obj.assassination, obj.depose, obj.constitution, obj.labor, obj.unfree_labor, obj.suffrage, obj.public_goods, obj.religion, ])
        else:
            writer.writerow([obj.year_from, obj.year_to,
                            obj.polity.new_name, obj.polity.name, obj.polity.long_name, 
                            "", "", "", obj.crisis_case_id, obj.decline, obj.collapse, obj.epidemic, obj.downward_mobility, obj.extermination, obj.uprising, obj.revolution, obj.successful_revolution, obj.civil_war, obj.century_plus, obj.fragmentation, obj.capital, obj.conquest, obj.assassination, obj.depose, obj.constitution, obj.labor, obj.unfree_labor, obj.suffrage, obj.public_goods, obj.religion, ])


    return response

@permission_required('core.view_capital')
def crisis_consequence_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="crisis_consequences_metadata.csv"'
    
    my_meta_data_dic = {'notes': 'Notes for the Variable crisis_consequence are missing!', 'main_desc': 'No Explanations.', 'main_desc_source': 'No Explanations.', 'section': 'Economy Variables', 'subsection': 'Productivity', 'null_meaning': 'The value is not available.'}
    my_meta_data_dic_inner_vars = {'crisis_consequence': {'min': None, 'max': None, 'scale': 1000, 'var_exp_source': None, 'var_exp': 'No Explanations.', 'units': 'mu?', 'choices': None}}
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
################################################

class Power_transitionCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    model = Power_transition
    form_class = Power_transitionForm
    success_url = reverse_lazy("power_transitions_all")
    template_name = "crisisdb/power_transition/power_transition_form.html"
    permission_required = 'core.add_capital'

    def get_success_url(self):
        polity_id = self.object.polity.id
        return reverse('polity-detail-main', kwargs={'pk': polity_id}) + '#power_transition_var'

    def get_absolute_url(self):
        return reverse('power_transition-create')
    def get_context_data(self, **kwargs):
        # get the explanattion:
        context = super().get_context_data(**kwargs)
        context["mysection"] = "X"
        context["mysubsection"] = "Y"
        context["myvar"] = "Z"
        context["my_exp"] = "Conequences of Crisis Explanataion"
        context["mytitle"] = "Add a NEW power transition below:"
        context["mysubtitle"] = "Please complete the form below to create a new power transition:"
        return context

class Power_transitionUpdate(PermissionRequiredMixin, UpdateView):
    model = Power_transition
    success_url = reverse_lazy('power_transitions_all')
    form_class = Power_transitionForm
    template_name = "crisisdb/power_transition/power_transition_update.html"
    permission_required = 'core.add_capital'

    def get_success_url(self):
        polity_id = self.object.polity.id
        return reverse('polity-detail-main', kwargs={'pk': polity_id}) + '#power_transition_var'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Z"
        context["mytitle"] = "Update the power transition below:"
        context["mysubtitle"] = "Please complete the form below to update the power transition:"

        return context
    
class Power_transitionCreateHeavy(PermissionRequiredMixin, CreateView):
    model = Power_transition
    form_class = Power_transitionForm
    success_url = reverse_lazy("power_transitions_all")
    template_name = "crisisdb/power_transition/power_transition_form_heavy.html"
    permission_required = 'core.add_capital'

    def get_success_url(self):
        polity_id = self.object.polity.id
        return reverse('polity-detail-main', kwargs={'pk': polity_id}) + '#power_transition_var'

    def get_absolute_url(self):
        return reverse('power_transition-create')
    def get_context_data(self, **kwargs):
        # get the explanattion:
        context = super().get_context_data(**kwargs)
        context["mysection"] = "X"
        context["mysubsection"] = "Y"
        context["myvar"] = "Z"
        context["my_exp"] = "Conequences of Crisis Explanataion"
        context["mytitle"] = "Add a NEW power transition below:"
        context["mysubtitle"] = "Please complete the form below to create a new power transition:"
        return context

class Power_transitionUpdateHeavy(PermissionRequiredMixin, UpdateView):
    model = Power_transition
    success_url = reverse_lazy('power_transitions_all')
    form_class = Power_transitionForm
    template_name = "crisisdb/power_transition/power_transition_form_heavy.html"
    permission_required = 'core.add_capital'

    def get_success_url(self):
        polity_id = self.object.polity.id
        return reverse('polity-detail-main', kwargs={'pk': polity_id}) + '#power_transition_var'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Z"
        context["mytitle"] = "Update the power transition below:"
        context["mysubtitle"] = "Please complete the form below to update the power transition:"

        return context

class Power_transitionDelete(PermissionRequiredMixin, DeleteView):
    model = Power_transition
    success_url = reverse_lazy('power_transitions')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Power_transitionListView(PermissionRequiredMixin, generic.ListView):
    model = Power_transition
    template_name = "crisisdb/power_transition/power_transition_list.html"
    permission_required = 'core.add_capital'

    paginate_by = 500

    def get_absolute_url(self):
        return reverse('power_transitions')
    
    def get_queryset(self):
        order = self.request.GET.get('orderby', 'home_nga')
        order2 = self.request.GET.get('orderby2', 'year_from')

        new_context = Power_transition.objects.all().annotate(
            home_nga=ExpressionWrapper(
                F('polity__home_nga__name'),
                output_field=CharField()
            )
        ).order_by(order2, order)
        return new_context
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fields"] = ['contested', 'overturn', 'predecessor_assassination', 'intra_elite', 'military_revolt', 'popular_uprising', 'separatist_rebellion', 'external_invasion', 'external_interference', ]


        context["myvar"] = "XX"
        context["var_main_desc"] = "YY"
        context["var_main_desc_source"] = ""
        context["var_section"] = "frffrr"
        context["var_subsection"] = "frtgtz"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'power_transition': {'min': None, 'max': None, 'scale': 1000, 'var_exp_source': None, 'var_exp': 'No Explanations.', 'units': 'mu?', 'choices': None}}
        context["potential_cols"] = ['Scale', 'Units']

        return context
    
class Power_transitionListViewAll(PermissionRequiredMixin, generic.ListView):
    model = Power_transition
    template_name = "crisisdb/power_transition/power_transition_list_all_new.html"
    permission_required = 'core.add_capital'
    #paginate_by = 50

    def get_absolute_url(self):
        return reverse('power_transitions_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_to')
        order2 = self.request.GET.get('orderby2', 'year_from')

        new_context = Power_transition.objects.all().order_by(order2, order)

        #grouped_dict = {}
        pols_dict  = {}
        for transition in new_context:
            polity_id = transition.polity_id
            if not polity_id:
                polity_id = 0
            if polity_id not in pols_dict:
                try:
                    pols_dict[polity_id] = {
                        'polity_new_name': transition.polity.new_name,
                        'polity_long_name': transition.polity.long_name,
                        'polity_start_year': transition.polity.start_year,
                        'polity_end_year': transition.polity.end_year,
                        'trans_list': []
                    }
                except:
                    pols_dict[0] = {
                        'polity_new_name': "NO_NAME",
                        'polity_long_name': "NO_LONG_NAME",
                        'polity_start_year': -10000,
                        'polity_end_year': 2000,
                        'trans_list': []
                        }

            pols_dict[polity_id]['trans_list'].append({
                'year_from': transition.year_from,
                'year_to': transition.year_to,
                'predecessor': transition.predecessor,
                'successor': transition.successor,
                'name': transition.name,
                'trans_id': transition.id,


                'overturn': transition.overturn,
                'predecessor_assassination':  transition.predecessor_assassination,
                'intra_elite': transition.intra_elite,
                'military_revolt': transition.military_revolt,
                'popular_uprising': transition.popular_uprising,
                'separatist_rebellion': transition.separatist_rebellion,
                'external_invasion': transition.external_invasion,
                'external_interference': transition.external_interference,
            })
        #print(grouped_dict)

        return pols_dict
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "uu"
        context["var_main_desc"] = "xx"
        context["var_main_desc_source"] = ""
        context["var_section"] = "Religion and Normative Ideology"
        context["var_subsection"] = "uu"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'Power_transition': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of Human Sacrifce.', 'units': None, 'choices': ['- Unknown', '- Present', '- Transitional (Present -> Absent)', '- Absent', '- Transitional (Absent -> Present)']}}
        context["potential_cols"] = ["choices"]
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Power_transitionDetailView(PermissionRequiredMixin, generic.DetailView):
    model = Power_transition
    template_name = "crisisdb/power_transition/power_transition_detail.html"
    permission_required = 'core.add_capital'


@permission_required('core.view_capital')
def power_transition_download(request):
    items = Power_transition.objects.all()

    response = HttpResponse(content_type='text/csv')

    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"power_transitions_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to', 'predecessor', 'successor',
                     'polity_new_ID', 'polity_old_ID', 'polity_long_form_name', 'conflict_name', 'contested', 'overturn', 'predecessor_assassination', 'intra_elite', 'military_revolt', 'popular_uprising', 'separatist_rebellion', 'external_invasion', 'external_interference',])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to, obj.predecessor, obj.successor,
                         obj.polity.new_name, obj.polity.name, obj.polity.long_name, obj.name, obj.contested, obj.overturn, obj.predecessor_assassination, obj.intra_elite, obj.military_revolt, obj.popular_uprising, obj.separatist_rebellion, obj.external_invasion, obj.external_interference])

    return response

@permission_required('core.view_capital')
def power_transition_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="power_transitions_metadata.csv"'
    
    my_meta_data_dic = {'notes': 'Notes for the Variable power_transition are missing!', 'main_desc': 'No Explanations.', 'main_desc_source': 'No Explanations.', 'section': 'Economy Variables', 'subsection': 'Productivity', 'null_meaning': 'The value is not available.'}
    my_meta_data_dic_inner_vars = {'power_transition': {'min': None, 'max': None, 'scale': 1000, 'var_exp_source': None, 'var_exp': 'No Explanations.', 'units': 'mu?', 'choices': None}}
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

##################################

class Human_sacrificeCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    model = Human_sacrifice
    form_class = Human_sacrificeForm
    template_name = "crisisdb/human_sacrifice/human_sacrifice_form.html"
    permission_required = 'core.add_capital'

    def get_success_url(self):
        polity_id = self.object.polity.id
        return reverse('polity-detail-main', kwargs={'pk': polity_id}) + '#hs_var'

    def get_absolute_url(self):
        return reverse('human_sacrifice-create')
    def get_context_data(self, **kwargs):
        # get the explanattion:
        all_var_hiers = Variablehierarchy.objects.all()
        if all_var_hiers:
            for item in all_var_hiers:
                if item.name == "Human_sacrifice":
                    my_exp = item.explanation
                    my_sec = item.section.name
                    my_subsec = item.subsection.name
                    my_name = "Human Sacrifice"
                    break
                else:
                    my_exp = "Human Sacrifice is the deliberate and ritualized killing of a person to please or placate supernatural entities (including gods, spirits, and ancestors) or gain other supernatural benefits."
                    my_sec = "No_SECTION"
                    my_subsec = "NO_SUBSECTION"
                    my_name = "Human Sacrifice"
            context = super().get_context_data(**kwargs)
            context["mysection"] = my_sec
            context["mysubsection"] = my_subsec
            context["myvar"] = my_name
            context["my_exp"] = my_exp

            return context
        else:
            context = super().get_context_data(**kwargs)
            my_exp = "No_Explanations"
            my_sec = "No_SECTION"
            my_subsec = "NO_SUBSECTION"
            my_name = "NO_NAME"
            context["mysection"] = my_sec
            context["mysubsection"] = my_subsec
            context["myvar"] = "Human Sacrifice"
            context["my_exp"] = my_exp
            return context

    def form_valid(self, form):
        the_mother_comment = SeshatComment.objects.get(pk=1)
        form.instance.comment = the_mother_comment
        return super().form_valid(form)


class Human_sacrificeUpdate(PermissionRequiredMixin, UpdateView):
    model = Human_sacrifice
    form_class = Human_sacrificeForm
    template_name = "crisisdb/human_sacrifice/human_sacrifice_update.html"
    permission_required = 'core.add_capital'

    def get_success_url(self):
        polity_id = self.object.polity.id
        return reverse('polity-detail-main', kwargs={'pk': polity_id}) + '#hs_var'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Human Sacrifice"

        return context

class Human_sacrificeDelete(PermissionRequiredMixin, DeleteView):
    model = Human_sacrifice
    success_url = reverse_lazy('human_sacrifices')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Human_sacrificeListView(PermissionRequiredMixin, generic.ListView):
    model = Human_sacrifice
    template_name = "crisisdb/human_sacrifice/human_sacrifice_list.html"
    paginate_by = 50
    permission_required = 'core.view_capital'

    def get_absolute_url(self):
        return reverse('human_sacrifices')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Human Sacrifice"
        context["var_main_desc"] = "The deliberate and ritualized killing of a person to please or placate supernatural entities (including gods, spirits, and ancestors) or gain other supernatural benefits."
        context["var_main_desc_source"] = ""
        context["var_section"] = "Religion and Normative Ideology"
        context["var_subsection"] = "Human Sacrifice"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'human_sacrifice': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of Human Sacrifce.', 'units': None, 'choices': ['- Unknown', '- Present', '- Transitional (Present -> Absent)', '- Absent', '- Transitional (Absent -> Present)']}}
        context["potential_cols"] = []

        return context


class Human_sacrificeListViewAll(PermissionRequiredMixin, generic.ListView):
    model = Human_sacrifice
    template_name = "crisisdb/human_sacrifice/human_sacrifice_list_all.html"
    permission_required = 'core.view_capital'


    #paginate_by = 50

    def get_absolute_url(self):
        return reverse('human_sacrifices_all')

    def get_queryset(self):
        #order = self.request.GET.get('orderby', 'year_from')
        order = self.request.GET.get('orderby', 'home_nga')
        order2 = self.request.GET.get('orderby2', 'year_from')
        #polity.home_nga.id
        #orders = [order, order2]
        new_context = Human_sacrifice.objects.all().annotate(
            home_nga=ExpressionWrapper(
                F('polity__home_nga__name'),
                output_field=CharField()
            )
        ).order_by(order, order2)
        #.polity.home_nga.id
        #new_context = Human_sacrifice.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Human Sacrifice"
        context["var_main_desc"] = "The deliberate and ritualized killing of a person to please or placate supernatural entities (including gods, spirits, and ancestors) or gain other supernatural benefits."
        context["var_main_desc_source"] = ""
        context["var_section"] = "Religion and Normative Ideology"
        context["var_subsection"] = "Human Sacrifice"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'human_sacrifice': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of Human Sacrifce.', 'units': None, 'choices': ['- Unknown', '- Present', '- Transitional (Present -> Absent)', '- Absent', '- Transitional (Absent -> Present)']}}
        context["potential_cols"] = ["choices"]
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Human_sacrificeDetailView(PermissionRequiredMixin, generic.DetailView):
    model = Human_sacrifice
    template_name = "crisisdb/human_sacrifice/human_sacrifice_detail.html"
    permission_required = 'core.view_capital'



@permission_required('core.view_capital')
def human_sacrifice_download(request):
    items = Human_sacrifice.objects.all()

    response = HttpResponse(content_type='text/csv')

    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"human_sacrifices_{current_datetime}.csv"
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to',
                     'polity_name', 'polity_new_ID', 'polity_old_ID', 'human_sacrifice_abbr', 'human_sacrifice_long', 'confidence', 'is_disputed', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.human_sacrifice, obj.get_human_sacrifice_display(), obj.get_tag_display(), obj.is_disputed,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@login_required
def create_a_comment_with_a_subcomment(request, hs_instance_id):
    """
    Upon calling this function, I want to create a subcomment and assign it to a comment and then assign the comment to the model_name with id=hs_instance_id.
    """
    # Create a new comment instance and save it to the database
    comment_instance = SeshatComment.objects.create(text='a new_comment_text')
    user_logged_in = request.user
    
    # Get the Seshat_Expert instance associated with the user
    try:
        seshat_expert_instance = Seshat_Expert.objects.get(user=user_logged_in)
    except Seshat_Expert.DoesNotExist:
        seshat_expert_instance = None
    #user_at_work = User.
    # Create the subcomment instance and save it to the database
    subcomment_instance = SeshatCommentPart.objects.create(comment_part_text='A subdescription text placeholder (to be edited)', comment=comment_instance, comment_curator= seshat_expert_instance,comment_order=1)
    #subcomment = comment_instance.seshatcommentpart.create(comment_part_text=request.POST.get('a subcomment text'))

    # Get the ModelName instance
    hs_instance = Human_sacrifice.objects.get(id=hs_instance_id)

    # Assign the comment to the ModelName instance
    hs_instance.comment = comment_instance

    hs_instance.save()

    # return redirect('human_sacrifice-detail', pk=hs_instance_id)
    return redirect('seshatcomment-update', pk=comment_instance.id)


@permission_required('core.view_capital')
def human_sacrifice_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="human_sacrifices.csv"'
    
    my_meta_data_dic = {'notes': 'This is a new model definition for Human Sacrifice', 'main_desc': 'The deliberate and ritualized killing of a person to please or placate supernatural entities (including gods, spirits, and ancestors) or gain other supernatural benefits.', 'main_desc_source': 'The deliberate and ritualized killing of a person to please or placate supernatural entities (including gods, spirits, and ancestors) or gain other supernatural benefits.', 'section': 'Conflict Variables', 'subsection': 'External Conflicts Subsection', 'null_meaning': 'The value is not available.'}
    my_meta_data_dic_inner_vars = {'human_sacrifice': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The Human Sacrifce', 'units': None, 'choices': ['U', 'A;P', 'P*', 'P', 'A~P', 'A', 'A*', 'P~A']}}
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

        

class External_conflictCreate(PermissionRequiredMixin, CreateView):
    model = External_conflict
    form_class = External_conflictForm
    template_name = "crisisdb/external_conflict/external_conflict_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('external_conflict-create')
    def get_context_data(self, **kwargs):
        # get the explanattion:
        all_var_hiers = Variablehierarchy.objects.all()
        if all_var_hiers:
            for item in all_var_hiers:
                if item.name == "External Conflict":
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
        else:
            context = super().get_context_data(**kwargs)
            my_exp = "No_Explanations"
            my_sec = "No_SECTION"
            my_subsec = "NO_SUBSECTION"
            my_name = "NO_NAME"
            context["mysection"] = my_sec
            context["mysubsection"] = my_subsec
            context["myvar"] = "External Conflict"
            context["my_exp"] = my_exp
            return context


class External_conflictUpdate(PermissionRequiredMixin, UpdateView):
    model = External_conflict
    form_class = External_conflictForm
    template_name = "crisisdb/external_conflict/external_conflict_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "External Conflict"

        return context

class External_conflictDelete(PermissionRequiredMixin, DeleteView):
    model = External_conflict
    success_url = reverse_lazy('external_conflicts')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class External_conflictListView(generic.ListView):
    model = External_conflict
    template_name = "crisisdb/external_conflict/external_conflict_list.html"
    paginate_by = 50

    def get_absolute_url(self):
        return reverse('external_conflicts')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "External Conflict"
        context["var_main_desc"] = "Main descriptions for the variable external Conflict are missing!"
        context["var_main_desc_source"] = ""
        context["var_section"] = "Conflict Variables"
        context["var_subsection"] = "External Conflicts Subsection"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'conflict_name': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The unique name of this external conflict', 'units': None, 'choices': None}}
        context["potential_cols"] = []

        return context
        
class External_conflictDetailView(generic.DetailView):
    model = External_conflict
    template_name = "crisisdb/external_conflict/external_conflict_detail.html"


@permission_required('core.view_capital')
def external_conflict_download(request):
    items = External_conflict.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="external_conflicts.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'conflict_name', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.conflict_name, ])

    return response

@permission_required('core.view_capital')
def external_conflict_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="external_conflicts.csv"'
    
    my_meta_data_dic = {'notes': 'This is a new model definition for External conflicts', 'main_desc': 'Main Descriptions for the Variable external_conflict are missing!', 'main_desc_source': 'Main Descriptions for the Variable external_conflict are missing!', 'section': 'Conflict Variables', 'subsection': 'External Conflicts Subsection', 'null_meaning': 'The value is not available.'}
    my_meta_data_dic_inner_vars = {'conflict_name': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The unique name of this external conflict', 'units': None, 'choices': None}}
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

        

class Internal_conflictCreate(PermissionRequiredMixin, CreateView):
    model = Internal_conflict
    form_class = Internal_conflictForm
    template_name = "crisisdb/internal_conflict/internal_conflict_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('internal_conflict-create')
    def get_context_data(self, **kwargs):
        # get the explanattion:
        all_var_hiers = Variablehierarchy.objects.all()
        if all_var_hiers:
            for item in all_var_hiers:
                if item.name == "Internal Conflict":
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
        else:
            context = super().get_context_data(**kwargs)
            my_exp = "No_Explanations"
            my_sec = "No_SECTION"
            my_subsec = "NO_SUBSECTION"
            my_name = "NO_NAME"
            context["mysection"] = my_sec
            context["mysubsection"] = my_subsec
            context["myvar"] = "Internal Conflict"
            context["my_exp"] = my_exp
            return context


class Internal_conflictUpdate(PermissionRequiredMixin, UpdateView):
    model = Internal_conflict
    form_class = Internal_conflictForm
    template_name = "crisisdb/internal_conflict/internal_conflict_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Internal Conflict"

        return context

class Internal_conflictDelete(PermissionRequiredMixin, DeleteView):
    model = Internal_conflict
    success_url = reverse_lazy('internal_conflicts')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Internal_conflictListView(generic.ListView):
    model = Internal_conflict
    template_name = "crisisdb/internal_conflict/internal_conflict_list.html"
    paginate_by = 50

    def get_absolute_url(self):
        return reverse('internal_conflicts')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Internal Conflict"
        context["var_main_desc"] = "Main descriptions for the variable internal Conflict are missing!"
        context["var_main_desc_source"] = ""
        context["var_section"] = "Conflict Variables"
        context["var_subsection"] = "Internal Conflicts Subsection"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'conflict': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The name of the conflict', 'units': None, 'choices': None}, 'expenditure': {'min': None, 'max': None, 'scale': 1000000, 'var_exp_source': None, 'var_exp': 'The military expenses in millions silver taels.', 'units': 'silver taels', 'choices': None}, 'leader': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The leader of the conflict', 'units': None, 'choices': None}, 'casualty': {'min': None, 'max': None, 'scale': 1, 'var_exp_source': None, 'var_exp': 'The number of people who died in this conflict.', 'units': 'People', 'choices': None}}
        context["potential_cols"] = ['Scale', 'Units']

        return context
        
class Internal_conflictDetailView(generic.DetailView):
    model = Internal_conflict
    template_name = "crisisdb/internal_conflict/internal_conflict_detail.html"


@permission_required('core.view_capital')
def internal_conflict_download(request):
    items = Internal_conflict.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="internal_conflicts.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'conflict', 'expenditure', 'leader', 'casualty', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.conflict, obj.expenditure, obj.leader, obj.casualty, ])

    return response

@permission_required('core.view_capital')
def internal_conflict_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="internal_conflicts.csv"'
    
    my_meta_data_dic = {'notes': 'This is a new model definition for internal conflicts', 'main_desc': 'Main Descriptions for the Variable internal_conflict are missing!', 'main_desc_source': 'Main Descriptions for the Variable internal_conflict are missing!', 'section': 'Conflict Variables', 'subsection': 'Internal Conflicts Subsection', 'null_meaning': 'The value is not available.'}
    my_meta_data_dic_inner_vars = {'conflict': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The name of the conflict', 'units': None, 'choices': None}, 'expenditure': {'min': None, 'max': None, 'scale': 1000000, 'var_exp_source': None, 'var_exp': 'The military expenses in millions silver taels.', 'units': 'silver taels', 'choices': None}, 'leader': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The leader of the conflict', 'units': None, 'choices': None}, 'casualty': {'min': None, 'max': None, 'scale': 1, 'var_exp_source': None, 'var_exp': 'The number of people who died in this conflict.', 'units': 'People', 'choices': None}}
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

        

class External_conflict_sideCreate(PermissionRequiredMixin, CreateView):
    model = External_conflict_side
    form_class = External_conflict_sideForm
    template_name = "crisisdb/external_conflict_side/external_conflict_side_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('external_conflict_side-create')
    def get_context_data(self, **kwargs):
        # get the explanattion:
        all_var_hiers = Variablehierarchy.objects.all()
        if all_var_hiers:
            for item in all_var_hiers:
                if item.name == "External Conflict Side":
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
        else:
            context = super().get_context_data(**kwargs)
            my_exp = "No_Explanations"
            my_sec = "No_SECTION"
            my_subsec = "NO_SUBSECTION"
            my_name = "NO_NAME"
            context["mysection"] = my_sec
            context["mysubsection"] = my_subsec
            context["myvar"] = "External Conflict Side"
            context["my_exp"] = my_exp
            return context


class External_conflict_sideUpdate(PermissionRequiredMixin, UpdateView):
    model = External_conflict_side
    form_class = External_conflict_sideForm
    template_name = "crisisdb/external_conflict_side/external_conflict_side_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "External Conflict Side"

        return context

class External_conflict_sideDelete(PermissionRequiredMixin, DeleteView):
    model = External_conflict_side
    success_url = reverse_lazy('external_conflict_sides')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class External_conflict_sideListView(generic.ListView):
    model = External_conflict_side
    template_name = "crisisdb/external_conflict_side/external_conflict_side_list.html"
    paginate_by = 50

    def get_absolute_url(self):
        return reverse('external_conflict_sides')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "External Conflict Side"
        context["var_main_desc"] = "Main descriptions for the variable external Conflict Side are missing!"
        context["var_main_desc_source"] = ""
        context["var_section"] = "Conflict Variables"
        context["var_subsection"] = "External Conflicts Subsection"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'conflict_id': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The external_conflict which is the actual conflict we are talking about', 'units': None, 'choices': None}, 'expenditure': {'min': None, 'max': None, 'scale': 1, 'var_exp_source': None, 'var_exp': 'The military expenses (from this side) in silver taels.', 'units': 'silver taels', 'choices': None}, 'leader': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The leader of this side of conflict', 'units': None, 'choices': None}, 'casualty': {'min': None, 'max': None, 'scale': 1, 'var_exp_source': None, 'var_exp': 'The number of people who died (from this side) in this conflict.', 'units': 'People', 'choices': None}}
        context["potential_cols"] = ['Scale', 'Units']

        return context
        
class External_conflict_sideDetailView(generic.DetailView):
    model = External_conflict_side
    template_name = "crisisdb/external_conflict_side/external_conflict_side_detail.html"


@permission_required('core.view_capital')
def external_conflict_side_download(request):
    items = External_conflict_side.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="external_conflict_sides.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'conflict_id', 'expenditure', 'leader', 'casualty', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.conflict_id, obj.expenditure, obj.leader, obj.casualty, ])

    return response

@permission_required('core.view_capital')
def external_conflict_side_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="external_conflict_sides.csv"'
    
    my_meta_data_dic = {'notes': 'This is a new model definition for External conflict sides', 'main_desc': 'Main Descriptions for the Variable external_conflict_side are missing!', 'main_desc_source': 'Main Descriptions for the Variable external_conflict_side are missing!', 'section': 'Conflict Variables', 'subsection': 'External Conflicts Subsection', 'null_meaning': 'The value is not available.'}
    my_meta_data_dic_inner_vars = {'conflict_id': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The external_conflict which is the actual conflict we are talking about', 'units': None, 'choices': None}, 'expenditure': {'min': None, 'max': None, 'scale': 1, 'var_exp_source': None, 'var_exp': 'The military expenses (from this side) in silver taels.', 'units': 'silver taels', 'choices': None}, 'leader': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The leader of this side of conflict', 'units': None, 'choices': None}, 'casualty': {'min': None, 'max': None, 'scale': 1, 'var_exp_source': None, 'var_exp': 'The number of people who died (from this side) in this conflict.', 'units': 'People', 'choices': None}}
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

        

class Agricultural_populationCreate(PermissionRequiredMixin, CreateView):
    model = Agricultural_population
    form_class = Agricultural_populationForm
    template_name = "crisisdb/agricultural_population/agricultural_population_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('agricultural_population-create')
    def get_context_data(self, **kwargs):
        # get the explanattion:
        all_var_hiers = Variablehierarchy.objects.all()
        if all_var_hiers:
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
        else:
            context = super().get_context_data(**kwargs)
            my_exp = "No_Explanations"
            my_sec = "No_SECTION"
            my_subsec = "NO_SUBSECTION"
            my_name = "NO_NAME"
            context["mysection"] = my_sec
            context["mysubsection"] = my_subsec
            context["myvar"] = "Agricultural Population"
            context["my_exp"] = my_exp
            return context


class Agricultural_populationUpdate(PermissionRequiredMixin, UpdateView):
    model = Agricultural_population
    form_class = Agricultural_populationForm
    template_name = "crisisdb/agricultural_population/agricultural_population_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Agricultural Population"

        return context

class Agricultural_populationDelete(PermissionRequiredMixin, DeleteView):
    model = Agricultural_population
    success_url = reverse_lazy('agricultural_populations')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Agricultural_populationListView(generic.ListView):
    model = Agricultural_population
    template_name = "crisisdb/agricultural_population/agricultural_population_list.html"
    paginate_by = 50

    def get_absolute_url(self):
        return reverse('agricultural_populations')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Agricultural Population"
        context["var_main_desc"] = "No explanations."
        context["var_main_desc_source"] = ""
        context["var_section"] = "Economy Variables"
        context["var_subsection"] = "Productivity"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'agricultural_population': {'min': 0, 'max': None, 'scale': 1000, 'var_exp_source': None, 'var_exp': 'No Explanations.', 'units': 'People', 'choices': None}}
        context["potential_cols"] = ['Scale', 'Units']

        return context
        
class Agricultural_populationDetailView(generic.DetailView):
    model = Agricultural_population
    template_name = "crisisdb/agricultural_population/agricultural_population_detail.html"


@permission_required('core.view_capital')
def agricultural_population_download(request):
    items = Agricultural_population.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="agricultural_populations.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'agricultural_population', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.agricultural_population, ])

    return response

@permission_required('core.view_capital')
def agricultural_population_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="agricultural_populations.csv"'
    
    my_meta_data_dic = {'notes': 'Notes for the Variable agricultural_population are missing!', 'main_desc': 'No Explanations.', 'main_desc_source': 'No Explanations.', 'section': 'Economy Variables', 'subsection': 'Productivity', 'null_meaning': 'The value is not available.'}
    my_meta_data_dic_inner_vars = {'agricultural_population': {'min': 0, 'max': None, 'scale': 1000, 'var_exp_source': None, 'var_exp': 'No Explanations.', 'units': 'People', 'choices': None}}
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

        

class Arable_landCreate(PermissionRequiredMixin, CreateView):
    model = Arable_land
    form_class = Arable_landForm
    template_name = "crisisdb/arable_land/arable_land_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('arable_land-create')
    def get_context_data(self, **kwargs):
        # get the explanattion:
        all_var_hiers = Variablehierarchy.objects.all()
        if all_var_hiers:
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
        else:
            context = super().get_context_data(**kwargs)
            my_exp = "No_Explanations"
            my_sec = "No_SECTION"
            my_subsec = "NO_SUBSECTION"
            my_name = "NO_NAME"
            context["mysection"] = my_sec
            context["mysubsection"] = my_subsec
            context["myvar"] = "Arable Land"
            context["my_exp"] = my_exp
            return context


class Arable_landUpdate(PermissionRequiredMixin, UpdateView):
    model = Arable_land
    form_class = Arable_landForm
    template_name = "crisisdb/arable_land/arable_land_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Arable Land"

        return context

class Arable_landDelete(PermissionRequiredMixin, DeleteView):
    model = Arable_land
    success_url = reverse_lazy('arable_lands')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Arable_landListView(generic.ListView):
    model = Arable_land
    template_name = "crisisdb/arable_land/arable_land_list.html"
    paginate_by = 50

    def get_absolute_url(self):
        return reverse('arable_lands')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Arable Land"
        context["var_main_desc"] = "No explanations."
        context["var_main_desc_source"] = ""
        context["var_section"] = "Economy Variables"
        context["var_subsection"] = "Productivity"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'arable_land': {'min': None, 'max': None, 'scale': 1000, 'var_exp_source': None, 'var_exp': 'No Explanations.', 'units': 'mu?', 'choices': None}}
        context["potential_cols"] = ['Scale', 'Units']

        return context
        
class Arable_landDetailView(generic.DetailView):
    model = Arable_land
    template_name = "crisisdb/arable_land/arable_land_detail.html"


@permission_required('core.view_capital')
def arable_land_download(request):
    items = Arable_land.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="arable_lands.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'arable_land', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.arable_land, ])

    return response

@permission_required('core.view_capital')
def arable_land_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="arable_lands.csv"'
    
    my_meta_data_dic = {'notes': 'Notes for the Variable arable_land are missing!', 'main_desc': 'No Explanations.', 'main_desc_source': 'No Explanations.', 'section': 'Economy Variables', 'subsection': 'Productivity', 'null_meaning': 'The value is not available.'}
    my_meta_data_dic_inner_vars = {'arable_land': {'min': None, 'max': None, 'scale': 1000, 'var_exp_source': None, 'var_exp': 'No Explanations.', 'units': 'mu?', 'choices': None}}
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

        

class Arable_land_per_farmerCreate(PermissionRequiredMixin, CreateView):
    model = Arable_land_per_farmer
    form_class = Arable_land_per_farmerForm
    template_name = "crisisdb/arable_land_per_farmer/arable_land_per_farmer_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('arable_land_per_farmer-create')
    def get_context_data(self, **kwargs):
        # get the explanattion:
        all_var_hiers = Variablehierarchy.objects.all()
        if all_var_hiers:
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
        else:
            context = super().get_context_data(**kwargs)
            my_exp = "No_Explanations"
            my_sec = "No_SECTION"
            my_subsec = "NO_SUBSECTION"
            my_name = "NO_NAME"
            context["mysection"] = my_sec
            context["mysubsection"] = my_subsec
            context["myvar"] = "Arable Land Per Farmer"
            context["my_exp"] = my_exp
            return context


class Arable_land_per_farmerUpdate(PermissionRequiredMixin, UpdateView):
    model = Arable_land_per_farmer
    form_class = Arable_land_per_farmerForm
    template_name = "crisisdb/arable_land_per_farmer/arable_land_per_farmer_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Arable Land Per Farmer"

        return context

class Arable_land_per_farmerDelete(PermissionRequiredMixin, DeleteView):
    model = Arable_land_per_farmer
    success_url = reverse_lazy('arable_land_per_farmers')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Arable_land_per_farmerListView(generic.ListView):
    model = Arable_land_per_farmer
    template_name = "crisisdb/arable_land_per_farmer/arable_land_per_farmer_list.html"
    paginate_by = 50

    def get_absolute_url(self):
        return reverse('arable_land_per_farmers')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Arable Land Per Farmer"
        context["var_main_desc"] = "No explanations."
        context["var_main_desc_source"] = ""
        context["var_section"] = "Economy Variables"
        context["var_subsection"] = "Productivity"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'arable_land_per_farmer': {'min': None, 'max': None, 'scale': 1, 'var_exp_source': None, 'var_exp': 'No Explanations.', 'units': 'mu?', 'choices': None}}
        context["potential_cols"] = ['Scale', 'Units']

        return context
        
class Arable_land_per_farmerDetailView(generic.DetailView):
    model = Arable_land_per_farmer
    template_name = "crisisdb/arable_land_per_farmer/arable_land_per_farmer_detail.html"


@permission_required('core.view_capital')
def arable_land_per_farmer_download(request):
    items = Arable_land_per_farmer.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="arable_land_per_farmers.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'arable_land_per_farmer', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.arable_land_per_farmer, ])

    return response

@permission_required('core.view_capital')
def arable_land_per_farmer_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="arable_land_per_farmers.csv"'
    
    my_meta_data_dic = {'notes': 'Notes for the Variable arable_land_per_farmer are missing!', 'main_desc': 'No Explanations.', 'main_desc_source': 'No Explanations.', 'section': 'Economy Variables', 'subsection': 'Productivity', 'null_meaning': 'The value is not available.'}
    my_meta_data_dic_inner_vars = {'arable_land_per_farmer': {'min': None, 'max': None, 'scale': 1, 'var_exp_source': None, 'var_exp': 'No Explanations.', 'units': 'mu?', 'choices': None}}
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

        

class Gross_grain_shared_per_agricultural_populationCreate(PermissionRequiredMixin, CreateView):
    model = Gross_grain_shared_per_agricultural_population
    form_class = Gross_grain_shared_per_agricultural_populationForm
    template_name = "crisisdb/gross_grain_shared_per_agricultural_population/gross_grain_shared_per_agricultural_population_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('gross_grain_shared_per_agricultural_population-create')
    def get_context_data(self, **kwargs):
        # get the explanattion:
        all_var_hiers = Variablehierarchy.objects.all()
        if all_var_hiers:
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
        else:
            context = super().get_context_data(**kwargs)
            my_exp = "No_Explanations"
            my_sec = "No_SECTION"
            my_subsec = "NO_SUBSECTION"
            my_name = "NO_NAME"
            context["mysection"] = my_sec
            context["mysubsection"] = my_subsec
            context["myvar"] = "Gross Grain Shared Per Agricultural Population"
            context["my_exp"] = my_exp
            return context


class Gross_grain_shared_per_agricultural_populationUpdate(PermissionRequiredMixin, UpdateView):
    model = Gross_grain_shared_per_agricultural_population
    form_class = Gross_grain_shared_per_agricultural_populationForm
    template_name = "crisisdb/gross_grain_shared_per_agricultural_population/gross_grain_shared_per_agricultural_population_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Gross Grain Shared Per Agricultural Population"

        return context

class Gross_grain_shared_per_agricultural_populationDelete(PermissionRequiredMixin, DeleteView):
    model = Gross_grain_shared_per_agricultural_population
    success_url = reverse_lazy('gross_grain_shared_per_agricultural_populations')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Gross_grain_shared_per_agricultural_populationListView(generic.ListView):
    model = Gross_grain_shared_per_agricultural_population
    template_name = "crisisdb/gross_grain_shared_per_agricultural_population/gross_grain_shared_per_agricultural_population_list.html"
    paginate_by = 50

    def get_absolute_url(self):
        return reverse('gross_grain_shared_per_agricultural_populations')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Gross Grain Shared Per Agricultural Population"
        context["var_main_desc"] = "No explanations."
        context["var_main_desc_source"] = ""
        context["var_section"] = "Economy Variables"
        context["var_subsection"] = "Productivity"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'gross_grain_shared_per_agricultural_population': {'min': None, 'max': None, 'scale': 1, 'var_exp_source': None, 'var_exp': 'No Explanations.', 'units': '(catties per capita)', 'choices': None}}
        context["potential_cols"] = ['Scale', 'Units']

        return context
        
class Gross_grain_shared_per_agricultural_populationDetailView(generic.DetailView):
    model = Gross_grain_shared_per_agricultural_population
    template_name = "crisisdb/gross_grain_shared_per_agricultural_population/gross_grain_shared_per_agricultural_population_detail.html"


@permission_required('core.view_capital')
def gross_grain_shared_per_agricultural_population_download(request):
    items = Gross_grain_shared_per_agricultural_population.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="gross_grain_shared_per_agricultural_populations.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'gross_grain_shared_per_agricultural_population', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.gross_grain_shared_per_agricultural_population, ])

    return response

@permission_required('core.view_capital')
def gross_grain_shared_per_agricultural_population_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="gross_grain_shared_per_agricultural_populations.csv"'
    
    my_meta_data_dic = {'notes': 'Notes for the Variable gross_grain_shared_per_agricultural_population are missing!', 'main_desc': 'No Explanations.', 'main_desc_source': 'No Explanations.', 'section': 'Economy Variables', 'subsection': 'Productivity', 'null_meaning': 'The value is not available.'}
    my_meta_data_dic_inner_vars = {'gross_grain_shared_per_agricultural_population': {'min': None, 'max': None, 'scale': 1, 'var_exp_source': None, 'var_exp': 'No Explanations.', 'units': '(catties per capita)', 'choices': None}}
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

        

class Net_grain_shared_per_agricultural_populationCreate(PermissionRequiredMixin, CreateView):
    model = Net_grain_shared_per_agricultural_population
    form_class = Net_grain_shared_per_agricultural_populationForm
    template_name = "crisisdb/net_grain_shared_per_agricultural_population/net_grain_shared_per_agricultural_population_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('net_grain_shared_per_agricultural_population-create')
    def get_context_data(self, **kwargs):
        # get the explanattion:
        all_var_hiers = Variablehierarchy.objects.all()
        if all_var_hiers:
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
        else:
            context = super().get_context_data(**kwargs)
            my_exp = "No_Explanations"
            my_sec = "No_SECTION"
            my_subsec = "NO_SUBSECTION"
            my_name = "NO_NAME"
            context["mysection"] = my_sec
            context["mysubsection"] = my_subsec
            context["myvar"] = "Net Grain Shared Per Agricultural Population"
            context["my_exp"] = my_exp
            return context


class Net_grain_shared_per_agricultural_populationUpdate(PermissionRequiredMixin, UpdateView):
    model = Net_grain_shared_per_agricultural_population
    form_class = Net_grain_shared_per_agricultural_populationForm
    template_name = "crisisdb/net_grain_shared_per_agricultural_population/net_grain_shared_per_agricultural_population_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Net Grain Shared Per Agricultural Population"

        return context

class Net_grain_shared_per_agricultural_populationDelete(PermissionRequiredMixin, DeleteView):
    model = Net_grain_shared_per_agricultural_population
    success_url = reverse_lazy('net_grain_shared_per_agricultural_populations')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Net_grain_shared_per_agricultural_populationListView(generic.ListView):
    model = Net_grain_shared_per_agricultural_population
    template_name = "crisisdb/net_grain_shared_per_agricultural_population/net_grain_shared_per_agricultural_population_list.html"
    paginate_by = 50

    def get_absolute_url(self):
        return reverse('net_grain_shared_per_agricultural_populations')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Net Grain Shared Per Agricultural Population"
        context["var_main_desc"] = "No explanations."
        context["var_main_desc_source"] = ""
        context["var_section"] = "Economy Variables"
        context["var_subsection"] = "Productivity"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'net_grain_shared_per_agricultural_population': {'min': None, 'max': None, 'scale': 1, 'var_exp_source': None, 'var_exp': 'No Explanations.', 'units': '(catties per capita)', 'choices': None}}
        context["potential_cols"] = ['Scale', 'Units']

        return context
        
class Net_grain_shared_per_agricultural_populationDetailView(generic.DetailView):
    model = Net_grain_shared_per_agricultural_population
    template_name = "crisisdb/net_grain_shared_per_agricultural_population/net_grain_shared_per_agricultural_population_detail.html"


@permission_required('core.view_capital')
def net_grain_shared_per_agricultural_population_download(request):
    items = Net_grain_shared_per_agricultural_population.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="net_grain_shared_per_agricultural_populations.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'net_grain_shared_per_agricultural_population', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.net_grain_shared_per_agricultural_population, ])

    return response

@permission_required('core.view_capital')
def net_grain_shared_per_agricultural_population_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="net_grain_shared_per_agricultural_populations.csv"'
    
    my_meta_data_dic = {'notes': 'Notes for the Variable net_grain_shared_per_agricultural_population are missing!', 'main_desc': 'No Explanations.', 'main_desc_source': 'No Explanations.', 'section': 'Economy Variables', 'subsection': 'Productivity', 'null_meaning': 'The value is not available.'}
    my_meta_data_dic_inner_vars = {'net_grain_shared_per_agricultural_population': {'min': None, 'max': None, 'scale': 1, 'var_exp_source': None, 'var_exp': 'No Explanations.', 'units': '(catties per capita)', 'choices': None}}
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

        

class SurplusCreate(PermissionRequiredMixin, CreateView):
    model = Surplus
    form_class = SurplusForm
    template_name = "crisisdb/surplus/surplus_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('surplus-create')
    def get_context_data(self, **kwargs):
        # get the explanattion:
        all_var_hiers = Variablehierarchy.objects.all()
        if all_var_hiers:
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
        else:
            context = super().get_context_data(**kwargs)
            my_exp = "No_Explanations"
            my_sec = "No_SECTION"
            my_subsec = "NO_SUBSECTION"
            my_name = "NO_NAME"
            context["mysection"] = my_sec
            context["mysubsection"] = my_subsec
            context["myvar"] = "Surplus"
            context["my_exp"] = my_exp
            return context


class SurplusUpdate(PermissionRequiredMixin, UpdateView):
    model = Surplus
    form_class = SurplusForm
    template_name = "crisisdb/surplus/surplus_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Surplus"

        return context

class SurplusDelete(PermissionRequiredMixin, DeleteView):
    model = Surplus
    success_url = reverse_lazy('surplus')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class SurplusListView(generic.ListView):
    model = Surplus
    template_name = "crisisdb/surplus/surplus_list.html"
    paginate_by = 50

    def get_absolute_url(self):
        return reverse('surplus')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Surplus"
        context["var_main_desc"] = "No explanations."
        context["var_main_desc_source"] = ""
        context["var_section"] = "Economy Variables"
        context["var_subsection"] = "Productivity"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'surplus': {'min': None, 'max': None, 'scale': 1, 'var_exp_source': None, 'var_exp': 'No Explanations.', 'units': '(catties per capita)', 'choices': None}}
        context["potential_cols"] = ['Scale', 'Units']

        return context
        
class SurplusDetailView(generic.DetailView):
    model = Surplus
    template_name = "crisisdb/surplus/surplus_detail.html"


@permission_required('core.view_capital')
def surplus_download(request):
    items = Surplus.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="surplus.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'surplus', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.surplus, ])

    return response

@permission_required('core.view_capital')
def surplus_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="surplus.csv"'
    
    my_meta_data_dic = {'notes': 'Notes for the Variable surplus are missing!', 'main_desc': 'No Explanations.', 'main_desc_source': 'No Explanations.', 'section': 'Economy Variables', 'subsection': 'Productivity', 'null_meaning': 'The value is not available.'}
    my_meta_data_dic_inner_vars = {'surplus': {'min': None, 'max': None, 'scale': 1, 'var_exp_source': None, 'var_exp': 'No Explanations.', 'units': '(catties per capita)', 'choices': None}}
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

        

class Military_expenseCreate(PermissionRequiredMixin, CreateView):
    model = Military_expense
    form_class = Military_expenseForm
    template_name = "crisisdb/military_expense/military_expense_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('military_expense-create')
    def get_context_data(self, **kwargs):
        # get the explanattion:
        all_var_hiers = Variablehierarchy.objects.all()
        if all_var_hiers:
            for item in all_var_hiers:
                if item.name == "Military Expense":
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
        else:
            context = super().get_context_data(**kwargs)
            my_exp = "No_Explanations"
            my_sec = "No_SECTION"
            my_subsec = "NO_SUBSECTION"
            my_name = "NO_NAME"
            context["mysection"] = my_sec
            context["mysubsection"] = my_subsec
            context["myvar"] = "Military Expense"
            context["my_exp"] = my_exp
            return context


class Military_expenseUpdate(PermissionRequiredMixin, UpdateView):
    model = Military_expense
    form_class = Military_expenseForm
    template_name = "crisisdb/military_expense/military_expense_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Military Expense"

        return context

class Military_expenseDelete(PermissionRequiredMixin, DeleteView):
    model = Military_expense
    success_url = reverse_lazy('military_expenses')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Military_expenseListView(generic.ListView):
    model = Military_expense
    template_name = "crisisdb/military_expense/military_expense_list.html"
    paginate_by = 50

    def get_absolute_url(self):
        return reverse('military_expenses')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Military Expense"
        context["var_main_desc"] = "Main descriptions for the variable military Expense are missing!"
        context["var_main_desc_source"] = "https://en.wikipedia.org/wiki/Disease_outbreak"
        context["var_section"] = "Economy Variables"
        context["var_subsection"] = "State Finances"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'conflict': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The name of the conflict', 'units': None, 'choices': None}, 'expenditure': {'min': None, 'max': None, 'scale': 1000000, 'var_exp_source': None, 'var_exp': 'The military expenses in millions silver taels.', 'units': 'silver taels', 'choices': None}}
        context["potential_cols"] = ['Scale', 'Units']

        return context
        
class Military_expenseDetailView(generic.DetailView):
    model = Military_expense
    template_name = "crisisdb/military_expense/military_expense_detail.html"


@permission_required('core.view_capital')
def military_expense_download(request):
    items = Military_expense.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="military_expenses.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'conflict', 'expenditure', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.conflict, obj.expenditure, ])

    return response

@permission_required('core.view_capital')
def military_expense_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="military_expenses.csv"'
    
    my_meta_data_dic = {'notes': 'Not sure about Section and Subsection.', 'main_desc': 'Main Descriptions for the Variable military_expense are missing!', 'main_desc_source': 'Main Descriptions for the Variable military_expense are missing!', 'section': 'Economy Variables', 'subsection': 'State Finances', 'null_meaning': 'The value is not available.'}
    my_meta_data_dic_inner_vars = {'conflict': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The name of the conflict', 'units': None, 'choices': None}, 'expenditure': {'min': None, 'max': None, 'scale': 1000000, 'var_exp_source': None, 'var_exp': 'The military expenses in millions silver taels.', 'units': 'silver taels', 'choices': None}}
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

        

class Silver_inflowCreate(PermissionRequiredMixin, CreateView):
    model = Silver_inflow
    form_class = Silver_inflowForm
    template_name = "crisisdb/silver_inflow/silver_inflow_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('silver_inflow-create')
    def get_context_data(self, **kwargs):
        # get the explanattion:
        all_var_hiers = Variablehierarchy.objects.all()
        if all_var_hiers:
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
        else:
            context = super().get_context_data(**kwargs)
            my_exp = "No_Explanations"
            my_sec = "No_SECTION"
            my_subsec = "NO_SUBSECTION"
            my_name = "NO_NAME"
            context["mysection"] = my_sec
            context["mysubsection"] = my_subsec
            context["myvar"] = "Silver Inflow"
            context["my_exp"] = my_exp
            return context


class Silver_inflowUpdate(PermissionRequiredMixin, UpdateView):
    model = Silver_inflow
    form_class = Silver_inflowForm
    template_name = "crisisdb/silver_inflow/silver_inflow_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Silver Inflow"

        return context

class Silver_inflowDelete(PermissionRequiredMixin, DeleteView):
    model = Silver_inflow
    success_url = reverse_lazy('silver_inflows')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Silver_inflowListView(generic.ListView):
    model = Silver_inflow
    template_name = "crisisdb/silver_inflow/silver_inflow_list.html"
    paginate_by = 50

    def get_absolute_url(self):
        return reverse('silver_inflows')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Silver Inflow"
        context["var_main_desc"] = "Silver inflow in millions of silver taels??"
        context["var_main_desc_source"] = ""
        context["var_section"] = "Economy Variables"
        context["var_subsection"] = "State Finances"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'silver_inflow': {'min': None, 'max': None, 'scale': 1000000, 'var_exp_source': None, 'var_exp': 'Silver inflow in Millions of silver taels??', 'units': 'silver taels??', 'choices': None}}
        context["potential_cols"] = ['Scale', 'Units']

        return context
        
class Silver_inflowDetailView(generic.DetailView):
    model = Silver_inflow
    template_name = "crisisdb/silver_inflow/silver_inflow_detail.html"


@permission_required('core.view_capital')
def silver_inflow_download(request):
    items = Silver_inflow.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="silver_inflows.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'silver_inflow', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.silver_inflow, ])

    return response

@permission_required('core.view_capital')
def silver_inflow_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="silver_inflows.csv"'
    
    my_meta_data_dic = {'notes': 'Needs suoervision on the units and scale.', 'main_desc': 'Silver inflow in Millions of silver taels??', 'main_desc_source': 'Silver inflow in Millions of silver taels??', 'section': 'Economy Variables', 'subsection': 'State Finances', 'null_meaning': 'The value is not available.'}
    my_meta_data_dic_inner_vars = {'silver_inflow': {'min': None, 'max': None, 'scale': 1000000, 'var_exp_source': None, 'var_exp': 'Silver inflow in Millions of silver taels??', 'units': 'silver taels??', 'choices': None}}
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

        

class Silver_stockCreate(PermissionRequiredMixin, CreateView):
    model = Silver_stock
    form_class = Silver_stockForm
    template_name = "crisisdb/silver_stock/silver_stock_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('silver_stock-create')
    def get_context_data(self, **kwargs):
        # get the explanattion:
        all_var_hiers = Variablehierarchy.objects.all()
        if all_var_hiers:
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
        else:
            context = super().get_context_data(**kwargs)
            my_exp = "No_Explanations"
            my_sec = "No_SECTION"
            my_subsec = "NO_SUBSECTION"
            my_name = "NO_NAME"
            context["mysection"] = my_sec
            context["mysubsection"] = my_subsec
            context["myvar"] = "Silver Stock"
            context["my_exp"] = my_exp
            return context


class Silver_stockUpdate(PermissionRequiredMixin, UpdateView):
    model = Silver_stock
    form_class = Silver_stockForm
    template_name = "crisisdb/silver_stock/silver_stock_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Silver Stock"

        return context

class Silver_stockDelete(PermissionRequiredMixin, DeleteView):
    model = Silver_stock
    success_url = reverse_lazy('silver_stocks')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Silver_stockListView(generic.ListView):
    model = Silver_stock
    template_name = "crisisdb/silver_stock/silver_stock_list.html"
    paginate_by = 50

    def get_absolute_url(self):
        return reverse('silver_stocks')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Silver Stock"
        context["var_main_desc"] = "Silver stock in millions of silver taels??"
        context["var_main_desc_source"] = ""
        context["var_section"] = "Economy Variables"
        context["var_subsection"] = "State Finances"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'silver_stock': {'min': None, 'max': None, 'scale': 1000000, 'var_exp_source': None, 'var_exp': 'Silver stock in Millions of silver taels??', 'units': 'silver taels??', 'choices': None}}
        context["potential_cols"] = ['Scale', 'Units']

        return context
        
class Silver_stockDetailView(generic.DetailView):
    model = Silver_stock
    template_name = "crisisdb/silver_stock/silver_stock_detail.html"


@permission_required('core.view_capital')
def silver_stock_download(request):
    items = Silver_stock.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="silver_stocks.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'silver_stock', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.silver_stock, ])

    return response

@permission_required('core.view_capital')
def silver_stock_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="silver_stocks.csv"'
    
    my_meta_data_dic = {'notes': 'Needs suoervision on the units and scale.', 'main_desc': 'Silver stock in Millions of silver taels??', 'main_desc_source': 'Silver stock in Millions of silver taels??', 'section': 'Economy Variables', 'subsection': 'State Finances', 'null_meaning': 'The value is not available.'}
    my_meta_data_dic_inner_vars = {'silver_stock': {'min': None, 'max': None, 'scale': 1000000, 'var_exp_source': None, 'var_exp': 'Silver stock in Millions of silver taels??', 'units': 'silver taels??', 'choices': None}}
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

        

class Total_populationCreate(PermissionRequiredMixin, CreateView):
    model = Total_population
    form_class = Total_populationForm
    template_name = "crisisdb/total_population/total_population_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('total_population-create')
    def get_context_data(self, **kwargs):
        # get the explanattion:
        all_var_hiers = Variablehierarchy.objects.all()
        if all_var_hiers:
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
        else:
            context = super().get_context_data(**kwargs)
            my_exp = "No_Explanations"
            my_sec = "No_SECTION"
            my_subsec = "NO_SUBSECTION"
            my_name = "NO_NAME"
            context["mysection"] = my_sec
            context["mysubsection"] = my_subsec
            context["myvar"] = "Total Population"
            context["my_exp"] = my_exp
            return context


class Total_populationUpdate(PermissionRequiredMixin, UpdateView):
    model = Total_population
    form_class = Total_populationForm
    template_name = "crisisdb/total_population/total_population_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Total Population"

        return context

class Total_populationDelete(PermissionRequiredMixin, DeleteView):
    model = Total_population
    success_url = reverse_lazy('total_populations')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Total_populationListView(generic.ListView):
    model = Total_population
    template_name = "crisisdb/total_population/total_population_list.html"
    paginate_by = 50

    def get_absolute_url(self):
        return reverse('total_populations')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Total Population"
        context["var_main_desc"] = "Total population or simply population, of a given area is the total number of people in that area at a given time."
        context["var_main_desc_source"] = ""
        context["var_section"] = "Social Complexity Variables"
        context["var_subsection"] = "Social Scale"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'total_population': {'min': 0, 'max': None, 'scale': 1000, 'var_exp_source': None, 'var_exp': 'The total population of a country (or a polity).', 'units': 'People', 'choices': None}}
        context["potential_cols"] = ['Scale', 'Units']

        return context
        
class Total_populationDetailView(generic.DetailView):
    model = Total_population
    template_name = "crisisdb/total_population/total_population_detail.html"


@permission_required('core.view_capital')
def total_population_download(request):
    items = Total_population.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="total_populations.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'total_population', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.total_population, ])

    return response

@permission_required('core.view_capital')
def total_population_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="total_populations.csv"'
    
    my_meta_data_dic = {'notes': 'Note that the population values are scaled.', 'main_desc': 'Total population or simply population, of a given area is the total number of people in that area at a given time.', 'main_desc_source': 'Total population or simply population, of a given area is the total number of people in that area at a given time.', 'section': 'Social Complexity Variables', 'subsection': 'Social Scale', 'null_meaning': 'The value is not available.'}
    my_meta_data_dic_inner_vars = {'total_population': {'min': 0, 'max': None, 'scale': 1000, 'var_exp_source': None, 'var_exp': 'The total population of a country (or a polity).', 'units': 'People', 'choices': None}}
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

        

class Gdp_per_capitaCreate(PermissionRequiredMixin, CreateView):
    model = Gdp_per_capita
    form_class = Gdp_per_capitaForm
    template_name = "crisisdb/gdp_per_capita/gdp_per_capita_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('gdp_per_capita-create')
    def get_context_data(self, **kwargs):
        # get the explanattion:
        all_var_hiers = Variablehierarchy.objects.all()
        if all_var_hiers:
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
        else:
            context = super().get_context_data(**kwargs)
            my_exp = "No_Explanations"
            my_sec = "No_SECTION"
            my_subsec = "NO_SUBSECTION"
            my_name = "NO_NAME"
            context["mysection"] = my_sec
            context["mysubsection"] = my_subsec
            context["myvar"] = "Gdp Per Capita"
            context["my_exp"] = my_exp
            return context


class Gdp_per_capitaUpdate(PermissionRequiredMixin, UpdateView):
    model = Gdp_per_capita
    form_class = Gdp_per_capitaForm
    template_name = "crisisdb/gdp_per_capita/gdp_per_capita_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Gdp Per Capita"

        return context

class Gdp_per_capitaDelete(PermissionRequiredMixin, DeleteView):
    model = Gdp_per_capita
    success_url = reverse_lazy('gdp_per_capitas')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Gdp_per_capitaListView(generic.ListView):
    model = Gdp_per_capita
    template_name = "crisisdb/gdp_per_capita/gdp_per_capita_list.html"
    paginate_by = 50

    def get_absolute_url(self):
        return reverse('gdp_per_capitas')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Gdp Per Capita"
        context["var_main_desc"] = "The gross domestic product per capita, or gdp per capita, is a measure of a country's economic output that accounts for its number of people. it divides the country's gross domestic product by its total population."
        context["var_main_desc_source"] = "https://www.thebalance.com/gdp-per-capita-formula-u-s-compared-to-highest-and-lowest-3305848"
        context["var_section"] = "Economy Variables"
        context["var_subsection"] = "Productivity"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'gdp_per_capita': {'min': None, 'max': None, 'scale': 1, 'var_exp_source': 'https://www.thebalance.com/gdp-per-capita-formula-u-s-compared-to-highest-and-lowest-3305848', 'var_exp': "The Gross Domestic Product per capita, or GDP per capita, is a measure of a country's economic output that accounts for its number of people. It divides the country's gross domestic product by its total population.", 'units': 'Dollars (in 2009?)', 'choices': None}}
        context["potential_cols"] = ['Scale', 'Units']

        return context
        
class Gdp_per_capitaDetailView(generic.DetailView):
    model = Gdp_per_capita
    template_name = "crisisdb/gdp_per_capita/gdp_per_capita_detail.html"


@permission_required('core.view_capital')
def gdp_per_capita_download(request):
    items = Gdp_per_capita.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="gdp_per_capitas.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'gdp_per_capita', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.gdp_per_capita, ])

    return response

@permission_required('core.view_capital')
def gdp_per_capita_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="gdp_per_capitas.csv"'
    
    my_meta_data_dic = {'notes': 'The exact year based on which the value of Dollar is taken into account is not clear.', 'main_desc': "The Gross Domestic Product per capita, or GDP per capita, is a measure of a country's economic output that accounts for its number of people. It divides the country's gross domestic product by its total population.", 'main_desc_source': "The Gross Domestic Product per capita, or GDP per capita, is a measure of a country's economic output that accounts for its number of people. It divides the country's gross domestic product by its total population.", 'section': 'Economy Variables', 'subsection': 'Productivity', 'null_meaning': 'The value is not available.'}
    my_meta_data_dic_inner_vars = {'gdp_per_capita': {'min': None, 'max': None, 'scale': 1, 'var_exp_source': 'https://www.thebalance.com/gdp-per-capita-formula-u-s-compared-to-highest-and-lowest-3305848', 'var_exp': "The Gross Domestic Product per capita, or GDP per capita, is a measure of a country's economic output that accounts for its number of people. It divides the country's gross domestic product by its total population.", 'units': 'Dollars (in 2009?)', 'choices': None}}
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

        

class Drought_eventCreate(PermissionRequiredMixin, CreateView):
    model = Drought_event
    form_class = Drought_eventForm
    template_name = "crisisdb/drought_event/drought_event_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('drought_event-create')
    def get_context_data(self, **kwargs):
        # get the explanattion:
        all_var_hiers = Variablehierarchy.objects.all()
        if all_var_hiers:
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
        else:
            context = super().get_context_data(**kwargs)
            my_exp = "No_Explanations"
            my_sec = "No_SECTION"
            my_subsec = "NO_SUBSECTION"
            my_name = "NO_NAME"
            context["mysection"] = my_sec
            context["mysubsection"] = my_subsec
            context["myvar"] = "Drought Event"
            context["my_exp"] = my_exp
            return context


class Drought_eventUpdate(PermissionRequiredMixin, UpdateView):
    model = Drought_event
    form_class = Drought_eventForm
    template_name = "crisisdb/drought_event/drought_event_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Drought Event"

        return context

class Drought_eventDelete(PermissionRequiredMixin, DeleteView):
    model = Drought_event
    success_url = reverse_lazy('drought_events')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Drought_eventListView(generic.ListView):
    model = Drought_event
    template_name = "crisisdb/drought_event/drought_event_list.html"
    paginate_by = 50

    def get_absolute_url(self):
        return reverse('drought_events')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Drought Event"
        context["var_main_desc"] = "Number of geographic sites indicating drought"
        context["var_main_desc_source"] = "https://www1.ncdc.noaa.gov/pub/data/paleo/historical/asia/china/reaches2020drought-category-sites.txt"
        context["var_section"] = "Well Being"
        context["var_subsection"] = "Biological Well-Being"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'drought_event': {'min': 0, 'max': None, 'scale': 1, 'var_exp_source': None, 'var_exp': 'number of geographic sites indicating drought', 'units': 'Numbers', 'choices': None}}
        context["potential_cols"] = ['Scale', 'Units']

        return context
        
class Drought_eventDetailView(generic.DetailView):
    model = Drought_event
    template_name = "crisisdb/drought_event/drought_event_detail.html"


@permission_required('core.view_capital')
def drought_event_download(request):
    items = Drought_event.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="drought_events.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'drought_event', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.drought_event, ])

    return response

@permission_required('core.view_capital')
def drought_event_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="drought_events.csv"'
    
    my_meta_data_dic = {'notes': 'Notes for the Variable drought_event are missing!', 'main_desc': 'number of geographic sites indicating drought', 'main_desc_source': 'number of geographic sites indicating drought', 'section': 'Well Being', 'subsection': 'Biological Well-Being', 'null_meaning': 'The value is not available.'}
    my_meta_data_dic_inner_vars = {'drought_event': {'min': 0, 'max': None, 'scale': 1, 'var_exp_source': None, 'var_exp': 'number of geographic sites indicating drought', 'units': 'Numbers', 'choices': None}}
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

        

class Locust_eventCreate(PermissionRequiredMixin, CreateView):
    model = Locust_event
    form_class = Locust_eventForm
    template_name = "crisisdb/locust_event/locust_event_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('locust_event-create')
    def get_context_data(self, **kwargs):
        # get the explanattion:
        all_var_hiers = Variablehierarchy.objects.all()
        if all_var_hiers:
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
        else:
            context = super().get_context_data(**kwargs)
            my_exp = "No_Explanations"
            my_sec = "No_SECTION"
            my_subsec = "NO_SUBSECTION"
            my_name = "NO_NAME"
            context["mysection"] = my_sec
            context["mysubsection"] = my_subsec
            context["myvar"] = "Locust Event"
            context["my_exp"] = my_exp
            return context


class Locust_eventUpdate(PermissionRequiredMixin, UpdateView):
    model = Locust_event
    form_class = Locust_eventForm
    template_name = "crisisdb/locust_event/locust_event_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Locust Event"

        return context

class Locust_eventDelete(PermissionRequiredMixin, DeleteView):
    model = Locust_event
    success_url = reverse_lazy('locust_events')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Locust_eventListView(generic.ListView):
    model = Locust_event
    template_name = "crisisdb/locust_event/locust_event_list.html"
    paginate_by = 50

    def get_absolute_url(self):
        return reverse('locust_events')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Locust Event"
        context["var_main_desc"] = "Number of geographic sites indicating locusts"
        context["var_main_desc_source"] = "https://www1.ncdc.noaa.gov/pub/data/paleo/historical/asia/china/reaches2020drought-category-sites.txt"
        context["var_section"] = "Well Being"
        context["var_subsection"] = "Biological Well-Being"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'locust_event': {'min': 0, 'max': None, 'scale': 1, 'var_exp_source': None, 'var_exp': 'number of geographic sites indicating locusts', 'units': 'Numbers', 'choices': None}}
        context["potential_cols"] = ['Scale', 'Units']

        return context
        
class Locust_eventDetailView(generic.DetailView):
    model = Locust_event
    template_name = "crisisdb/locust_event/locust_event_detail.html"


@permission_required('core.view_capital')
def locust_event_download(request):
    items = Locust_event.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="locust_events.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'locust_event', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.locust_event, ])

    return response

@permission_required('core.view_capital')
def locust_event_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="locust_events.csv"'
    
    my_meta_data_dic = {'notes': 'Notes for the Variable locust_event are missing!', 'main_desc': 'number of geographic sites indicating locusts', 'main_desc_source': 'number of geographic sites indicating locusts', 'section': 'Well Being', 'subsection': 'Biological Well-Being', 'null_meaning': 'The value is not available.'}
    my_meta_data_dic_inner_vars = {'locust_event': {'min': 0, 'max': None, 'scale': 1, 'var_exp_source': None, 'var_exp': 'number of geographic sites indicating locusts', 'units': 'Numbers', 'choices': None}}
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

        

class Socioeconomic_turmoil_eventCreate(PermissionRequiredMixin, CreateView):
    model = Socioeconomic_turmoil_event
    form_class = Socioeconomic_turmoil_eventForm
    template_name = "crisisdb/socioeconomic_turmoil_event/socioeconomic_turmoil_event_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('socioeconomic_turmoil_event-create')
    def get_context_data(self, **kwargs):
        # get the explanattion:
        all_var_hiers = Variablehierarchy.objects.all()
        if all_var_hiers:
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
        else:
            context = super().get_context_data(**kwargs)
            my_exp = "No_Explanations"
            my_sec = "No_SECTION"
            my_subsec = "NO_SUBSECTION"
            my_name = "NO_NAME"
            context["mysection"] = my_sec
            context["mysubsection"] = my_subsec
            context["myvar"] = "Socioeconomic Turmoil Event"
            context["my_exp"] = my_exp
            return context


class Socioeconomic_turmoil_eventUpdate(PermissionRequiredMixin, UpdateView):
    model = Socioeconomic_turmoil_event
    form_class = Socioeconomic_turmoil_eventForm
    template_name = "crisisdb/socioeconomic_turmoil_event/socioeconomic_turmoil_event_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Socioeconomic Turmoil Event"

        return context

class Socioeconomic_turmoil_eventDelete(PermissionRequiredMixin, DeleteView):
    model = Socioeconomic_turmoil_event
    success_url = reverse_lazy('socioeconomic_turmoil_events')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Socioeconomic_turmoil_eventListView(generic.ListView):
    model = Socioeconomic_turmoil_event
    template_name = "crisisdb/socioeconomic_turmoil_event/socioeconomic_turmoil_event_list.html"
    paginate_by = 50

    def get_absolute_url(self):
        return reverse('socioeconomic_turmoil_events')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Socioeconomic Turmoil Event"
        context["var_main_desc"] = "Number of geographic sites indicating socioeconomic turmoil"
        context["var_main_desc_source"] = "https://www1.ncdc.noaa.gov/pub/data/paleo/historical/asia/china/reaches2020drought-category-sites.txt"
        context["var_section"] = "Well Being"
        context["var_subsection"] = "Biological Well-Being"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'socioeconomic_turmoil_event': {'min': 0, 'max': None, 'scale': 1, 'var_exp_source': None, 'var_exp': 'number of geographic sites indicating socioeconomic turmoil', 'units': 'Numbers', 'choices': None}}
        context["potential_cols"] = ['Scale', 'Units']

        return context
        
class Socioeconomic_turmoil_eventDetailView(generic.DetailView):
    model = Socioeconomic_turmoil_event
    template_name = "crisisdb/socioeconomic_turmoil_event/socioeconomic_turmoil_event_detail.html"


@permission_required('core.view_capital')
def socioeconomic_turmoil_event_download(request):
    items = Socioeconomic_turmoil_event.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="socioeconomic_turmoil_events.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'socioeconomic_turmoil_event', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.socioeconomic_turmoil_event, ])

    return response

@permission_required('core.view_capital')
def socioeconomic_turmoil_event_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="socioeconomic_turmoil_events.csv"'
    
    my_meta_data_dic = {'notes': 'Notes for the Variable socioeconomic_turmoil_event are missing!', 'main_desc': 'number of geographic sites indicating socioeconomic turmoil', 'main_desc_source': 'number of geographic sites indicating socioeconomic turmoil', 'section': 'Well Being', 'subsection': 'Biological Well-Being', 'null_meaning': 'The value is not available.'}
    my_meta_data_dic_inner_vars = {'socioeconomic_turmoil_event': {'min': 0, 'max': None, 'scale': 1, 'var_exp_source': None, 'var_exp': 'number of geographic sites indicating socioeconomic turmoil', 'units': 'Numbers', 'choices': None}}
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

        

class Crop_failure_eventCreate(PermissionRequiredMixin, CreateView):
    model = Crop_failure_event
    form_class = Crop_failure_eventForm
    template_name = "crisisdb/crop_failure_event/crop_failure_event_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('crop_failure_event-create')
    def get_context_data(self, **kwargs):
        # get the explanattion:
        all_var_hiers = Variablehierarchy.objects.all()
        if all_var_hiers:
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
        else:
            context = super().get_context_data(**kwargs)
            my_exp = "No_Explanations"
            my_sec = "No_SECTION"
            my_subsec = "NO_SUBSECTION"
            my_name = "NO_NAME"
            context["mysection"] = my_sec
            context["mysubsection"] = my_subsec
            context["myvar"] = "Crop Failure Event"
            context["my_exp"] = my_exp
            return context


class Crop_failure_eventUpdate(PermissionRequiredMixin, UpdateView):
    model = Crop_failure_event
    form_class = Crop_failure_eventForm
    template_name = "crisisdb/crop_failure_event/crop_failure_event_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Crop Failure Event"

        return context

class Crop_failure_eventDelete(PermissionRequiredMixin, DeleteView):
    model = Crop_failure_event
    success_url = reverse_lazy('crop_failure_events')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Crop_failure_eventListView(generic.ListView):
    model = Crop_failure_event
    template_name = "crisisdb/crop_failure_event/crop_failure_event_list.html"
    paginate_by = 50

    def get_absolute_url(self):
        return reverse('crop_failure_events')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Crop Failure Event"
        context["var_main_desc"] = "Number of geographic sites indicating crop failure"
        context["var_main_desc_source"] = "https://www1.ncdc.noaa.gov/pub/data/paleo/historical/asia/china/reaches2020drought-category-sites.txt"
        context["var_section"] = "Well Being"
        context["var_subsection"] = "Biological Well-Being"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'crop_failure_event': {'min': 0, 'max': None, 'scale': 1, 'var_exp_source': None, 'var_exp': 'number of geographic sites indicating crop failure', 'units': 'Numbers', 'choices': None}}
        context["potential_cols"] = ['Scale', 'Units']

        return context
        
class Crop_failure_eventDetailView(generic.DetailView):
    model = Crop_failure_event
    template_name = "crisisdb/crop_failure_event/crop_failure_event_detail.html"


@permission_required('core.view_capital')
def crop_failure_event_download(request):
    items = Crop_failure_event.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="crop_failure_events.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'crop_failure_event', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.crop_failure_event, ])

    return response

@permission_required('core.view_capital')
def crop_failure_event_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="crop_failure_events.csv"'
    
    my_meta_data_dic = {'notes': 'Notes for the Variable crop_failure_event are missing!', 'main_desc': 'number of geographic sites indicating crop failure', 'main_desc_source': 'number of geographic sites indicating crop failure', 'section': 'Well Being', 'subsection': 'Biological Well-Being', 'null_meaning': 'The value is not available.'}
    my_meta_data_dic_inner_vars = {'crop_failure_event': {'min': 0, 'max': None, 'scale': 1, 'var_exp_source': None, 'var_exp': 'number of geographic sites indicating crop failure', 'units': 'Numbers', 'choices': None}}
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

        

class Famine_eventCreate(PermissionRequiredMixin, CreateView):
    model = Famine_event
    form_class = Famine_eventForm
    template_name = "crisisdb/famine_event/famine_event_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('famine_event-create')
    def get_context_data(self, **kwargs):
        # get the explanattion:
        all_var_hiers = Variablehierarchy.objects.all()
        if all_var_hiers:
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
        else:
            context = super().get_context_data(**kwargs)
            my_exp = "No_Explanations"
            my_sec = "No_SECTION"
            my_subsec = "NO_SUBSECTION"
            my_name = "NO_NAME"
            context["mysection"] = my_sec
            context["mysubsection"] = my_subsec
            context["myvar"] = "Famine Event"
            context["my_exp"] = my_exp
            return context


class Famine_eventUpdate(PermissionRequiredMixin, UpdateView):
    model = Famine_event
    form_class = Famine_eventForm
    template_name = "crisisdb/famine_event/famine_event_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Famine Event"

        return context

class Famine_eventDelete(PermissionRequiredMixin, DeleteView):
    model = Famine_event
    success_url = reverse_lazy('famine_events')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Famine_eventListView(generic.ListView):
    model = Famine_event
    template_name = "crisisdb/famine_event/famine_event_list.html"
    paginate_by = 50

    def get_absolute_url(self):
        return reverse('famine_events')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Famine Event"
        context["var_main_desc"] = "Number of geographic sites indicating famine"
        context["var_main_desc_source"] = "https://www1.ncdc.noaa.gov/pub/data/paleo/historical/asia/china/reaches2020drought-category-sites.txt"
        context["var_section"] = "Well Being"
        context["var_subsection"] = "Biological Well-Being"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'famine_event': {'min': 0, 'max': None, 'scale': 1, 'var_exp_source': None, 'var_exp': 'number of geographic sites indicating famine', 'units': 'Numbers', 'choices': None}}
        context["potential_cols"] = ['Scale', 'Units']

        return context
        
class Famine_eventDetailView(generic.DetailView):
    model = Famine_event
    template_name = "crisisdb/famine_event/famine_event_detail.html"


@permission_required('core.view_capital')
def famine_event_download(request):
    items = Famine_event.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="famine_events.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'famine_event', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.famine_event, ])

    return response

@permission_required('core.view_capital')
def famine_event_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="famine_events.csv"'
    
    my_meta_data_dic = {'notes': 'Notes for the Variable famine_event are missing!', 'main_desc': 'number of geographic sites indicating famine', 'main_desc_source': 'number of geographic sites indicating famine', 'section': 'Well Being', 'subsection': 'Biological Well-Being', 'null_meaning': 'The value is not available.'}
    my_meta_data_dic_inner_vars = {'famine_event': {'min': 0, 'max': None, 'scale': 1, 'var_exp_source': None, 'var_exp': 'number of geographic sites indicating famine', 'units': 'Numbers', 'choices': None}}
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

        

class Disease_outbreakCreate(PermissionRequiredMixin, CreateView):
    model = Disease_outbreak
    form_class = Disease_outbreakForm
    template_name = "crisisdb/disease_outbreak/disease_outbreak_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('disease_outbreak-create')
    def get_context_data(self, **kwargs):
        # get the explanattion:
        all_var_hiers = Variablehierarchy.objects.all()
        if all_var_hiers:
            for item in all_var_hiers:
                if item.name == "Disease Outbreak":
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
        else:
            context = super().get_context_data(**kwargs)
            my_exp = "No_Explanations"
            my_sec = "No_SECTION"
            my_subsec = "NO_SUBSECTION"
            my_name = "NO_NAME"
            context["mysection"] = my_sec
            context["mysubsection"] = my_subsec
            context["myvar"] = "Disease Outbreak"
            context["my_exp"] = my_exp
            return context


class Disease_outbreakUpdate(PermissionRequiredMixin, UpdateView):
    model = Disease_outbreak
    form_class = Disease_outbreakForm
    template_name = "crisisdb/disease_outbreak/disease_outbreak_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Disease Outbreak"

        return context

class Disease_outbreakDelete(PermissionRequiredMixin, DeleteView):
    model = Disease_outbreak
    success_url = reverse_lazy('disease_outbreaks')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Disease_outbreakListView(generic.ListView):
    model = Disease_outbreak
    template_name = "crisisdb/disease_outbreak/disease_outbreak_list.html"
    paginate_by = 50

    def get_absolute_url(self):
        return reverse('disease_outbreaks')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Disease Outbreak"
        context["var_main_desc"] = "A sudden increase in occurrences of a disease when cases are in excess of normal expectancy for the location or season."
        context["var_main_desc_source"] = "https://en.wikipedia.org/wiki/Disease_outbreak"
        context["var_section"] = "Well Being"
        context["var_subsection"] = "Biological Well-Being"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'longitude': {'min': -180, 'max': 180, 'scale': 1, 'var_exp_source': None, 'var_exp': 'The longitude (in degrees) of the place where the disease was spread.', 'units': 'Degrees', 'choices': None}, 'latitude': {'min': -180, 'max': 180, 'scale': 1, 'var_exp_source': None, 'var_exp': 'The latitude (in degrees) of the place where the disease was spread.', 'units': 'Degrees', 'choices': None}, 'elevation': {'min': 0, 'max': 5000, 'scale': 1, 'var_exp_source': None, 'var_exp': 'Elevation from mean sea level (in meters) of the place where the disease was spread.', 'units': 'Meters', 'choices': None}, 'sub_category': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The category of the disease.', 'units': None, 'choices': ['Peculiar Epidemics', 'Pestilence', 'Miasm', 'Pox', 'Uncertain Pestilence', 'Dysentery', 'Malaria', 'Influenza', 'Cholera', 'Diptheria', 'Plague']}, 'magnitude': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'How heavy the disease was.', 'units': None, 'choices': ['Uncertain', 'Light', 'Heavy', 'No description', 'Heavy- Multiple Times', 'No Happening', 'Moderate']}, 'duration': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'How long the disease lasted.', 'units': None, 'choices': ['No description', 'Over 90 Days', 'Uncertain', '30-60 Days', '1-10 Days', '60-90 Days']}}
        context["potential_cols"] = ['Min', 'Units', 'Scale', 'Max']

        return context
        
class Disease_outbreakDetailView(generic.DetailView):
    model = Disease_outbreak
    template_name = "crisisdb/disease_outbreak/disease_outbreak_detail.html"


@permission_required('core.view_capital')
def disease_outbreak_download(request):
    items = Disease_outbreak.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="disease_outbreaks.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'longitude', 'latitude', 'elevation', 'sub_category', 'magnitude', 'duration', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.longitude, obj.latitude, obj.elevation, obj.sub_category, obj.magnitude, obj.duration, ])

    return response

@permission_required('core.view_capital')
def disease_outbreak_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="disease_outbreaks.csv"'
    
    my_meta_data_dic = {'notes': 'Notes for the Variable disease_outbreak are missing!', 'main_desc': 'A sudden increase in occurrences of a disease when cases are in excess of normal expectancy for the location or season.', 'main_desc_source': 'A sudden increase in occurrences of a disease when cases are in excess of normal expectancy for the location or season.', 'section': 'Well Being', 'subsection': 'Biological Well-Being', 'null_meaning': 'The value is not available.'}
    my_meta_data_dic_inner_vars = {'longitude': {'min': -180, 'max': 180, 'scale': 1, 'var_exp_source': None, 'var_exp': 'The longitude (in degrees) of the place where the disease was spread.', 'units': 'Degrees', 'choices': None}, 'latitude': {'min': -180, 'max': 180, 'scale': 1, 'var_exp_source': None, 'var_exp': 'The latitude (in degrees) of the place where the disease was spread.', 'units': 'Degrees', 'choices': None}, 'elevation': {'min': 0, 'max': 5000, 'scale': 1, 'var_exp_source': None, 'var_exp': 'Elevation from mean sea level (in meters) of the place where the disease was spread.', 'units': 'Meters', 'choices': None}, 'sub_category': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The category of the disease.', 'units': None, 'choices': ['Peculiar Epidemics', 'Pestilence', 'Miasm', 'Pox', 'Uncertain Pestilence', 'Dysentery', 'Malaria', 'Influenza', 'Cholera', 'Diptheria', 'Plague']}, 'magnitude': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'How heavy the disease was.', 'units': None, 'choices': ['Uncertain', 'Light', 'Heavy', 'No description', 'Heavy- Multiple Times', 'No Happening', 'Moderate']}, 'duration': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'How long the disease lasted.', 'units': None, 'choices': ['No description', 'Over 90 Days', 'Uncertain', '30-60 Days', '1-10 Days', '60-90 Days']}}
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

        
# THE temporary function for creating the my_sections_dic dic: test_for_varhier_dic inside utils
# and the qing_vars_links_creator() inside utils.py
def QingVars(request):
    my_sections_dic = {
        #'Other_Sections': {'Other_Subsections': []}, 'Conflict Variables': {'External Conflicts Subsection': [['External conflict', 'external_conflicts', 'external_conflict-create', 'external_conflict-download', 'external_conflict-metadownload'], ['External conflict side', 'external_conflict_sides', 'external_conflict_side-create', 'external_conflict_side-download', 'external_conflict_side-metadownload'], ['Human_sacrifice', 'human_sacrifices', 'human_sacrifice-create', 'human_sacrifice-download', 'human_sacrifice-metadownload']], 'Internal Conflicts Subsection': [['Internal conflict', 'internal_conflicts', 'internal_conflict-create', 'internal_conflict-download', 'internal_conflict-metadownload']]},
                        'Economy Variables': {'Productivity': [['Agricultural population', 'agricultural_populations', 'agricultural_population-create', 'agricultural_population-download', 'agricultural_population-metadownload'], ['Arable land', 'arable_lands', 'arable_land-create', 'arable_land-download', 'arable_land-metadownload'], ['Arable land per farmer', 'arable_land_per_farmers', 'arable_land_per_farmer-create', 'arable_land_per_farmer-download', 'arable_land_per_farmer-metadownload'], ['Gross grain shared per agricultural population', 'gross_grain_shared_per_agricultural_populations', 'gross_grain_shared_per_agricultural_population-create', 'gross_grain_shared_per_agricultural_population-download', 'gross_grain_shared_per_agricultural_population-metadownload'], ['Net grain shared per agricultural population', 'net_grain_shared_per_agricultural_populations', 'net_grain_shared_per_agricultural_population-create', 'net_grain_shared_per_agricultural_population-download', 'net_grain_shared_per_agricultural_population-metadownload'], ['Surplus', 'surplus', 'surplus-create', 'surplus-download', 'surplus-metadownload'], ['Gdp per capita', 'gdp_per_capitas', 'gdp_per_capita-create', 'gdp_per_capita-download', 'gdp_per_capita-metadownload']], 'State Finances': [['Military expense', 'military_expenses', 'military_expense-create', 'military_expense-download', 'military_expense-metadownload'], ['Silver inflow', 'silver_inflows', 'silver_inflow-create', 'silver_inflow-download', 'silver_inflow-metadownload'], ['Silver stock', 'silver_stocks', 'silver_stock-create', 'silver_stock-download', 'silver_stock-metadownload']]}, 'Social Complexity Variables': {'Social Scale': [['Total population', 'total_populations', 'total_population-create', 'total_population-download', 'total_population-metadownload']]}, 'Well Being': {'Biological Well-Being': [['Drought event', 'drought_events', 'drought_event-create', 'drought_event-download', 'drought_event-metadownload'], ['Locust event', 'locust_events', 'locust_event-create', 'locust_event-download', 'locust_event-metadownload'], ['Socioeconomic turmoil event', 'socioeconomic_turmoil_events', 'socioeconomic_turmoil_event-create', 'socioeconomic_turmoil_event-download', 'socioeconomic_turmoil_event-metadownload'], ['Crop failure event', 'crop_failure_events', 'crop_failure_event-create', 'crop_failure_event-download', 'crop_failure_event-metadownload'], ['Famine event', 'famine_events', 'famine_event-create', 'famine_event-download', 'famine_event-metadownload'], ['Disease outbreak', 'disease_outbreaks', 'disease_outbreak-create', 'disease_outbreak-download', 'disease_outbreak-metadownload']]}}



#     my_sections_dic = {'Other_Sections': {'Other_Subsections': []},
#  'Economy Variables': {'Productivity': [['Agricultural population',
#     'agricultural_populations',
#     'agricultural_population-create'],
#    ['Arable land', 'arable_lands', 'arable_land-create'],
#    ['Arable land per farmer',
#     'arable_land_per_farmers',
#     'arable_land_per_farmer-create'],
#    ['Gross grain shared per agricultural population',
#     'gross_grain_shared_per_agricultural_populations',
#     'gross_grain_shared_per_agricultural_population-create'],
#    ['Net grain shared per agricultural population',
#     'net_grain_shared_per_agricultural_populations',
#     'net_grain_shared_per_agricultural_population-create'],
#    ['Surplus', 'surplus', 'surplus-create'],
#    ['Gdp per capita', 'gdp_per_capitas', 'gdp_per_capita-create']],
#   'State Finances': [['Military expense',
#     'military_expenses',
#     'military_expense-create'],
#    ['Silver inflow', 'silver_inflows', 'silver_inflow-create'],
#    ['Silver stock', 'silver_stocks', 'silver_stock-create']]},
#  'Social Complexity Variables': {'Social Scale': [['Total population',
#     'total_populations',
#     'total_population-create']]},
#  'Well Being': {'Biological Well-Being': [['Drought event',
#     'drought_events',
#     'drought_event-create'],
#    ['Locust event', 'locust_events', 'locust_event-create'],
#    ['Socioeconomic turmoil event',
#     'socioeconomic_turmoil_events',
#     'socioeconomic_turmoil_event-create'],
#    ['Crop failure event', 'crop_failure_events', 'crop_failure_event-create'],
#    ['Famine event', 'famine_events', 'famine_event-create'],
#    ['Disease outbreak', 'disease_outbreaks', 'disease_outbreak-create']]}}
    # all_sections = Section.objects.all()
    # all_subsections = Subsection.objects.all()
    # all_varhiers = Variablehierarchy.objects.all()
    # meta_data_dict = {}
    # for ct in my_sections_dic.items():
    #     m = ct.model_class()
    #     #full_name = m.__module__ + m.__name__
    #     full_name = m.__name__
    #     meta_data_dict[full_name.lower()] = [full_name.split('.')[-1].replace("_", ' '), m._default_manager.count(), full_name.lower()+"-create",full_name.lower()+"s"]
    #     print (f".{m.__name__}	{m._default_manager.count()}")
    # my_dict = {}
    context = {}

    # for sect in all_sections:
    #     my_dict[sect] = {}
    #     for subsect in all_subsections:
    #         list_of_all_varhiers_in_here = []
    #         for item in all_varhiers:
    #             #print(item, item.section, item.subsection, sect.name, subsect.name)
    #             if item.section.name == sect.name and item.subsection.name == subsect.name:
    #                 print("We hit it")
    #                 list_of_all_varhiers_in_here.append(meta_data_dict[item.name.lower()])
    #         if list_of_all_varhiers_in_here:
    #             my_dict[sect][subsect] = list_of_all_varhiers_in_here
    context["my_dict"] = my_sections_dic
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

    url = "http://127.0.0.1:8000/api/politys-api/"
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

    #print(all_my_data)
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

def fpl_all(request):
    return render(request, 'crisisdb/fpl_all.html')


# ... Your existing imports ...

class UsLocationListView(ListView):
    model = Us_location
    template_name = 'crisisdb/us_location/list.html'
    context_object_name = 'us_locations'

class UsLocationCreateView(CreateView):
    model = Us_location
    form_class = Us_locationForm
    template_name = 'crisisdb/us_location/create.html'
    success_url = reverse_lazy('us_location_list')

class UsLocationUpdateView(UpdateView):
    model = Us_location
    form_class = Us_locationForm
    template_name = 'crisisdb/us_location/update.html'
    success_url = reverse_lazy('us_location_list')

class UsViolenceSubtypeListView(ListView):
    model = Us_violence_subtype
    template_name = 'crisisdb/subtype/list.html'
    context_object_name = 'subtypes'

class UsViolenceSubtypeCreateView(CreateView):
    model = Us_violence_subtype
    form_class = Us_violence_subtypeForm
    template_name = 'crisisdb/subtype/create.html'
    success_url = reverse_lazy('subtype_list')

class UsViolenceSubtypeUpdateView(UpdateView):
    model = Us_violence_subtype
    form_class = Us_violence_subtypeForm
    template_name = 'crisisdb/subtype/update.html'
    success_url = reverse_lazy('subtype_list')

class UsViolenceDataSourceListView(ListView):
    model = Us_violence_data_source
    template_name = 'crisisdb/datasource/list.html'
    context_object_name = 'datasources'

class UsViolenceDataSourceCreateView(CreateView):
    model = Us_violence_data_source
    form_class = Us_violence_data_sourceForm
    template_name = 'crisisdb/datasource/create.html'
    success_url = reverse_lazy('datasource_list')

class UsViolenceDataSourceUpdateView(UpdateView):
    model = Us_violence_data_source
    form_class = Us_violence_data_sourceForm
    template_name = 'crisisdb/datasource/update.html'
    success_url = reverse_lazy('datasource_list')

class UsViolenceListView(ListView):
    model = Us_violence
    template_name = 'crisisdb/us_violence/list.html'
    context_object_name = 'us_violences'

    def get_queryset(self):
        # Get the query parameters from the request, if provided
        order_by = self.request.GET.get('order_by', self.ordering)
        
        # Check if the order_by parameter is valid
        valid_ordering = ['violence_date', '-violence_date', 'violence_type', '-violence_type', 'fatalities', '-fatalities']
        if order_by not in valid_ordering:
            order_by = '-violence_date'  # Use the default ordering if the parameter is invalid

        
        # Get the queryset with the specified ordering
        queryset = super().get_queryset().order_by(order_by)
        return queryset

class UsViolenceListViewPaginated(ListView):
    model = Us_violence
    template_name = 'crisisdb/us_violence/list_paginated.html'
    context_object_name = 'us_violences'
    paginate_by = 100

class UsViolenceCreateView(CreateView):
    model = Us_violence
    form_class = Us_violenceForm
    template_name = 'crisisdb/us_violence/create.html'
    success_url = reverse_lazy('us_violence_paginated')

class UsViolenceUpdateView(UpdateView):
    model = Us_violence
    form_class = Us_violenceForm
    template_name = 'crisisdb/us_violence/update.html'
    success_url = reverse_lazy('us_violence_paginated')


@permission_required('core.view_capital')
def download_csv_all_american_violence(request):
    #from bs4 import BeautifulSoup

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"american_violence_data_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    # Create a CSV writer
    writer = csv.writer(response, delimiter='|')

    # type the headers
    writer.writerow(['id','date', 'type', 'subtypes', 'locations', 'fatality', 'sources', 'url_address', 'source_details', 'narrative'])
    items = Us_violence.objects.all().order_by("id")
    if items:
        for obj in items:
            #locations_text = BeautifulSoup(obj.show_locations(), 'html.parser').get_text()
            locations_text = remove_html_tags(obj.show_locations())
            short_data_sources_text = remove_html_tags(obj.show_short_data_sources())

            writer.writerow([obj.id, obj.violence_date, obj.violence_type, obj.show_violence_subtypes(), locations_text, obj.fatalities,
                        short_data_sources_text, obj.url_address, obj.source_details, obj.narrative,])


    return response


@permission_required('core.view_capital')
def download_csv_all_american_violence2(request):
    #from bs4 import BeautifulSoup

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"american_violence_data_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    # Create a CSV writer
    writer = csv.writer(response, delimiter='|')

    # type the headers
    writer.writerow(['date', 'type', 'subtypes', 'locations', 'fatality', 'sources', 'url_address',])
    items = Us_violence.objects.all()
    if items:
        for obj in items:
            #locations_text = BeautifulSoup(obj.show_locations(), 'html.parser').get_text()
            locations_text = remove_html_tags(obj.show_locations())
            short_data_sources_text = remove_html_tags(obj.show_short_data_sources())

            writer.writerow([obj.violence_date, obj.violence_type, obj.show_violence_subtypes(), locations_text, obj.fatalities,
                        short_data_sources_text, obj.url_address,])


    return response


def confirm_delete_view(request, model_class, pk, var_name):
    permission_required = 'core.add_capital'
    
    # Retrieve the object for the given model class
    obj = get_object_or_404(model_class, pk=pk)

    # Check if the user has the required permission
    if not request.user.has_perm(permission_required):
        return HttpResponseForbidden("You don't have permission to delete this object.")

    template_name = "core/confirm_delete.html"
    
    context = {
        'var_name': var_name,
        'obj': obj,
        'delete_object': f'{var_name}-delete',
    }

    return render(request, template_name, context)

def delete_object_view(request, model_class, pk, var_name):
    permission_required = 'core.add_capital'
    # Retrieve the object for the given model class
    obj = get_object_or_404(model_class, pk=pk)

    if not request.user.has_perm(permission_required):
        return HttpResponseForbidden("You don't have permission to delete this object.")
    
    # Delete the object
    obj.delete()
    
    # Redirect to the success URL
    success_url_name = f'{var_name}_list'  # Adjust the success URL as needed
    success_url = reverse(success_url_name)
    
    # Display a success message
    messages.success(request, f"{var_name} has been deleted successfully.")
    
    return redirect(success_url)