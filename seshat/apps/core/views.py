from seshat.utils.utils import adder, dic_of_all_vars, list_of_all_Polities, dic_of_all_vars_in_sections

from django.contrib.sites.shortcuts import get_current_site
from seshat.apps.core.forms import SignUpForm, VariablehierarchyFormNew, CitationForm, ReferenceForm, SeshatCommentForm, SeshatCommentPartForm, PolityForm, PolityUpdateForm, CapitalForm, NgaForm, SeshatCommentPartForm2, ReferenceFormSet
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db import IntegrityError
from django.db.models import Prefetch, F, Value, Q
from django.db.models.functions import Replace

from django.views.decorators.http import require_GET

from django.contrib.auth.decorators import login_required, permission_required
from seshat.apps.accounts.models import Seshat_Expert

from django.core.paginator import Paginator

from django.http import FileResponse
from django.shortcuts import get_object_or_404
import os

from django.apps import apps



from markupsafe import Markup, escape
from django.http import JsonResponse

from django.core.mail import EmailMessage
import html
import datetime
import csv

import json
from django.views import generic
from django.urls import reverse, reverse_lazy

from django.contrib.messages.views import SuccessMessageMixin

from ..general.models import Polity_research_assistant

from .models import Citation, Polity, Section, Subsection, Variablehierarchy, Reference, SeshatComment, SeshatCommentPart, Nga, Ngapolityrel, Capital, Seshat_region, Macro_region
import pprint
import requests
from requests.structures import CaseInsensitiveDict
from seshat.utils.utils import adder, dic_of_all_vars, list_of_all_Polities, dic_of_all_vars_in_sections, dic_of_all_vars_with_varhier, get_all_data_for_a_polity, polity_detail_data_collector, get_all_general_data_for_a_polity, get_all_sc_data_for_a_polity, get_all_wf_data_for_a_polity, get_all_crisis_cases_data_for_a_polity, get_all_power_transitions_data_for_a_polity, give_polity_app_data


from django.shortcuts import HttpResponse


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def ajax_test(request):
    if is_ajax(request=request):
        message = "This is ajax"
    else:
        message = "Not ajax"
    return HttpResponse(message)

# importing formset_factory
from django.forms import formset_factory, modelformset_factory


def index(request):
    return HttpResponse('<h1>Hello World.</h1>')

def four_o_four(request):
    return render(request, 'core/not_found_404.html')

def seshatindex2(request):
    context = {
        'insta': "Instabilities All Over the Place..",
        'trans': "Transitions All Over the Place",
    }
    #print('static_root:', settings.STATIC_ROOT)
    #print('STATICFILES_DIRS:', settings.STATICFILES_DIRS)
    return render(request, 'core/seshat-index.html', context=context)

def seshatmethods(request):
    context = {
        'insta': "Instabilities All Over the Place..",
        'trans': "Transitions All Over the Place",
    }
    #print('static_root:', settings.STATIC_ROOT)
    #print('STATICFILES_DIRS:', settings.STATICFILES_DIRS)
    return render(request, 'core/seshat-methods.html', context=context)

def seshatwhoweare(request):
    #json_url_inners = "https://eric.clst.org/assets/wiki/uploads/Stuff/gz_2010_us_040_00_500k.json"
    #json_url_outline = "https://eric.clst.org/assets/wiki/uploads/Stuff/gz_2010_us_outline_500k.json"
    json_file_path = "/home/majid/dev/seshat/seshat/seshat/apps/core/static/geojson/us_states_geojson.json"

    try:
        #response_inners = requests.get(json_url_inners)
        #response_outline = requests.get(json_url_outline)
        with open(json_file_path, "r") as json_file:
            json_data = json.load(json_file)
        #with open(json_file_path, "r") as json_file:
        #    json_data = json.load(json_file)
        # Check if the request was successful (status code 200)
        #if response_inners.status_code == 200 and response_outline.status_code == 200:
        #    # Parse the JSON data from the response_inners
        #    json_inners = response_inners.json()
        #    json_outline = response_outline.json()

        context = {
                'insta': "Instabilities All Over the Place..",
                'json_data': json_data,  # Add this line to your context
        }
        print(len(json_data))
        return render(request, 'core/seshat-whoweare.html', context=context)
    except FileNotFoundError:
        # Handle the case when the file is not found
        context = {
            'insta': "Instabilities All Over the Place..",
            'json_error': "JSON file not found",
        }
        return render(request, 'core/seshat-whoweare.html', context=context)
    except json.JSONDecodeError as e:
        # Handle JSON decoding errors if the file is not valid JSON
        context = {
            'insta': "Instabilities All Over the Place..",
            'json_error': f"JSON decoding error: {str(e)}",
        }
        return render(request, 'core/seshat-whoweare.html', context=context)

def seshatolddownloads(request):
    context = {
        'insta': "Instabilities All Over the Place..",
    }
    return render(request, 'core/old_downloads.html', context=context)

def seshatacknowledgements(request):
    context = {
        'insta': "Instabilities All Over the Place..",
    }
    return render(request, 'core/seshat-acknowledgements.html', context=context)

class ReferenceListView(generic.ListView):
    model = Reference
    template_name = "core/references/reference_list.html"
    paginate_by = 20

    def get_absolute_url(self):
        return reverse('references')

    def get_queryset(self):
        queryset = Reference.objects.exclude(creator='MAJIDBENAM').all()
        return queryset
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     selected_only_zotero_refs = Reference.objects.exclude(creator='MAJIDBENAM')
    #     context['object_list'] = selected_only_zotero_refs

    #     return context


class NlpReferenceListView(generic.ListView):
    model = Reference
    template_name = "core/references/nlp_reference_list.html"
    paginate_by = 50

    def get_absolute_url(self):
        return reverse('nlp-references')

    def get_queryset(self):
        # Import the list of Zotero links inside the method
        from .nlp_zotero_links import NLP_ZOTERO_LINKS_TO_FILTER

        # Use the imported list of Zotero links to filter references
        queryset = Reference.objects.filter(zotero_link__in=NLP_ZOTERO_LINKS_TO_FILTER)

        queryset = queryset.filter(year__gt=0)

        # Replace underscores in 'creator' with spaces
        queryset = queryset.annotate(
            creator_with_spaces=Replace('creator', Value('_'), Value(' '))
        )

        # Replace "_et_al" at the end of 'creator' with ", ..."
        queryset = queryset.annotate(
            creator_cleaned=Replace(F('creator_with_spaces'), Value(' et al'), Value(', ...'))
        )

        queryset = queryset.order_by('-year', 'title')

        # Create a list of Zotero links from the queryset
        #matched_zotero_links = list(queryset.values_list('zotero_link', flat=True))

        # Find the missing Zotero links
        #missing_zotero_links = [link for link in NLP_ZOTERO_LINKS_TO_FILTER if link not in matched_zotero_links]

        #print(missing_zotero_links)

        return queryset

# references without a Zotero link:
def no_zotero_refs_list(request):
    selected_no_zotero_refs = Reference.objects.filter(zotero_link__startswith='NOZOTERO_')
    #all_refs = Reference.objects.all()
    #selected_no_zotero_refs = []
    #for ref in all_refs:
    #    if "NOZOTERO_" in ref.zotero_link:
    #        selected_no_zotero_refs.append(ref)

    paginator = Paginator(selected_no_zotero_refs, 10) # Show 25 refs per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    context = {}
    context['object_list'] = selected_no_zotero_refs
    context['page_obj'] = page_obj
    context['is_paginated'] = False


    # Citation.objects.bulk_create(all_citations)
    return render (request, 'core/references/reference_list_nozotero.html', context)

def reference_update_modal(request, pk):
    # Either render only the modal content, or a full standalone page
    if is_ajax(request=request):
        template_name = 'core/references/reference_update_modal.html'
    else:
        template_name = 'core/references/reference_update.html'

    object = Reference.objects.get(pk=pk)
    if request.method == 'POST':
        form = ReferenceForm(instance=object, data=request.POST)
        if form.is_valid():
            form.save()
            if not is_ajax(request=request):
                # reload the page
                next = request.META['PATH_INFO']
                return HttpResponseRedirect(next)
            # if is_ajax(), we just return the validated form, so the modal will close
    else:
        form = ReferenceForm(instance=object)

    return render(request, template_name, {
        'object': object,
        'form': form,
    })

###########


class ReferenceCreate(PermissionRequiredMixin, CreateView):
    model = Reference
    form_class = ReferenceForm
    template_name = "core/references/reference_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('reference-create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mysection"] = "xyz"
        context["mysubsection"] = "abc"
        context["myvar"] = "def reference"
        context["errors"] = "Halooooooooo"
        #print(context)

        return context

    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return HttpResponseRedirect(reverse('seshat-index'))


class ReferenceUpdate(PermissionRequiredMixin, UpdateView):
    model = Reference
    form_class = ReferenceForm
    template_name = "core/references/reference_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mysection"] = "Fiscal Heeeelath"
        context["mysubsection"] = "No Subsection Proeeeevided"
        context["myvar"] = "Reference Daeeeeta"

        return context

class ReferenceDelete(PermissionRequiredMixin, DeleteView):
    model = Reference
    success_url = reverse_lazy('references')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class ReferenceDetailView(generic.DetailView):
    model = Reference
    template_name = "core/references/reference_detail.html"



@permission_required('core.view_capital')
def references_download(request):
    items = Reference.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="referencess.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['zotero_link', 'creator'])

    for obj in items:
        writer.writerow([obj.zotero_link, obj.creator])

    return response


# Citations
class CitationListView(generic.ListView):
    model = Citation
    template_name = "core/references/citation_list.html"
    paginate_by = 20

    def get_absolute_url(self):
        return reverse('citations')

class CitationCreate(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Citation
    form_class = CitationForm
    template_name = "core/references/citation_form.html"
    permission_required = 'core.add_capital'
    success_message = "Yoohoooo..."

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        context.update({"my_message": "Soemthign went wrong"})
        return self.render_to_response(context)

    def get_absolute_url(self):
        return reverse('citation-create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mysection"] = "xyz"
        context["mysubsection"] = "abc"
        context["myvar"] = "def citation"
        context["errors"] = "Halooooooooo"
        #print(context)

        return context

    def form_valid(self, form):
        return super().form_valid(form)
    
    # def form_invalid(self, form):
    #     return HttpResponseRedirect(reverse('seshat-index'))


class CitationUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Citation
    form_class = CitationForm
    template_name = "core/references/citation_update.html"
    permission_required = 'core.add_capital'
    success_message = "Yoohoooo..."

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        context.update({"my_message": "Soemthign went wrong"})
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mysection"] = "Fiscal Helath"
        context["mysubsection"] = "No Subsection Provided"
        context["myvar"] = "Citation Data xyz"

        return context

class CitationDelete(PermissionRequiredMixin, DeleteView):
    model = Citation
    success_url = reverse_lazy('citations')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class CitationDetailView(generic.DetailView):
    model = Citation
    template_name = "core/references/citation_detail.html"

# SeshatComment
class SeshatCommentListView(generic.ListView):
    model = SeshatComment
    template_name = "core/seshatcomments/seshatcomment_list.html"
    paginate_by = 20

    def get_absolute_url(self):
        return reverse('seshatcomments')

class SeshatCommentCreate(PermissionRequiredMixin, CreateView):
    model = SeshatComment
    form_class = SeshatCommentForm
    template_name = "core/seshatcomments/seshatcomment_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('seshatcomment-create')


    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return HttpResponseRedirect(reverse('seshat-index'))


class SeshatCommentUpdate(PermissionRequiredMixin, UpdateView):
    model = SeshatComment
    form_class = SeshatCommentForm
    template_name = "core/seshatcomments/seshatcomment_update.html"
    permission_required = 'core.add_capital'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)

    #     related_models = [model for model in dir(self.object) if '_related' in model]

    #     for model_name in related_models:
    #         print(model_name)
    #         related_objects = getattr(self.object, model_name)
    #         if related_objects:
    #             context['related_objects'] = related_objects
    #             break

    #     return context


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     #an_instance = SeshatComment.objects.first()
    #     #related_fact = 
    #     #print("Haloooooo_________ooooooooooo", self.kwargs['com_id'])
    #     #print("Halooooooooooooooooo", self.kwargs['subcom_order'])
    #     #related_fact = self.        context["com_id"] = self.kwargs['com_id']
    #     #context["subcom_order"] = self.kwargs['subcom_order']
    #     #context["subcom_order"] = self.comment_order

    #     print("HEre we gooooooooooo: ", dir(self.object))
    #     #for potential_attr in dir(isinstance):
            
    #     #if an_instance

    #     return context

class SeshatCommentDelete(PermissionRequiredMixin, DeleteView):
    model = SeshatComment
    success_url = reverse_lazy('seshatcomments')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class SeshatCommentDetailView(generic.DetailView):
    model = SeshatComment
    template_name = "core/seshatcomments/seshatcomment_detail.html"


# SeshatCommentPart
class SeshatCommentPartListView(generic.ListView):
    model = SeshatCommentPart
    template_name = "core/seshatcomments/seshatcommentpart_list.html"
    paginate_by = 20

    def get_absolute_url(self):
        return reverse('seshatcommentparts')

class SeshatCommentPartCreate(PermissionRequiredMixin, CreateView):
    model = SeshatCommentPart
    form_class = SeshatCommentPartForm
    template_name = "core/seshatcomments/seshatcommentpart_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('seshatcommentpart-create')


    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return HttpResponseRedirect(reverse('seshat-index'))

class SeshatCommentPartCreate2(PermissionRequiredMixin, CreateView):
    model = SeshatCommentPart
    form_class = SeshatCommentPartForm
    template_name = "core/seshatcomments/seshatcommentpart_form_prefilled.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        return reverse('seshatcommentpart-create2')


    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return HttpResponseRedirect(reverse('seshat-index'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        logged_in_user = self.request.user
        logged_in_expert = Seshat_Expert.objects.get(user=logged_in_user)
        #print("Haloooooo_________ooooooooooo", self.kwargs['com_id'])
        #print("Halooooooooooooooooo", self.kwargs['subcom_order'])
        context["com_id"] = self.kwargs['com_id']
        context["subcom_order"] = self.kwargs['subcom_order']
        context["comment_curator"] = logged_in_expert
        context["comment_curator_id"] = logged_in_expert.id
        context["comment_curator_name"] = "Selected USER"

        #context["subcom_order"] = self.comment_order

        #print(context)

        return context

class SeshatCommentPartUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = SeshatCommentPart
    form_class = SeshatCommentPartForm
    template_name = "core/seshatcomments/seshatcommentpart_update.html"
    permission_required = 'core.add_capital'
    success_message = "You successfully updated the subdescription."


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        logged_in_user = self.request.user
        logged_in_expert = Seshat_Expert.objects.get(user=logged_in_user)
        #context["com_id"] = self.kwargs['com_id']
        #context["subcom_order"] = self.kwargs['subcom_order']
        context["comment_curator"] = logged_in_expert
        context["comment_curator_id"] = logged_in_expert.id
        context["comment_curator_name"] = "Selected USER"

        #context["subcom_order"] = self.comment_order

        #print(context)

        return context


class SeshatCommentPartDelete(PermissionRequiredMixin, DeleteView):
    model = SeshatCommentPart
    success_url = reverse_lazy('seshatcommentparts')
    #success_url = reverse_lazy('seshatcommentparts')

    #('seshatcomment-update', self.pk)
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class SeshatCommentPartDetailView(generic.DetailView):
    model = SeshatCommentPart
    template_name = "core/seshatcomments/seshatcommentpart_detail.html"




##### Extra function for seshat comments


# POLITY

class PolityCreate(PermissionRequiredMixin, CreateView):
    model = Polity
    form_class = PolityForm
    template_name = "core/polity/polity_form.html"
    permission_required = 'core.add_capital'
    success_url = reverse_lazy('polities')

    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        #return HttpResponseRedirect(reverse('seshat-index'))
        messages.error(self.request, "Form submission failed. Please check the form.")
        # Redirect to the 'polities' page
        return self.render_to_response(self.get_context_data(form=form))


class PolityUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Polity
    form_class = PolityUpdateForm
    template_name = "core/polity/polity_form.html"
    permission_required = 'core.add_capital'
    success_message = "You successfully updated the Polity."
    
    def get_success_url(self):
        return reverse_lazy('polity-detail-main', kwargs={'pk': self.object.pk})
    #success_url = reverse_lazy('polity-detail-main')



# class PolityListView(PermissionRequiredMixin, SuccessMessageMixin, generic.ListView):
#     model = Polity
#     template_name = "core/polity/polity_list.html"
#     permission_required = 'core.add_capital'

#     def get_absolute_url(self):
#         return reverse('polities')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         all_ngas = Nga.objects.all()
#         all_pols = Polity.objects.select_related('ngapolityrel__polity_party', 'ngapolityrel__nga_party').order_by('start_year').all()
#         all_nga_pol_rels = Ngapolityrel.objects.all()

#         all_world_regions = {a_nga.world_region: [a_nga.subregion] for a_nga in all_ngas}

#         ultimate_wregion_dic = {}

#         for a_world_region, all_its_sub_regions in all_world_regions.items():
#             ultimate_wregion_dic[a_world_region] = {}

#             for a_subregion in all_its_sub_regions:
#                 all_politys_on_the_polity_list_page = Polity.objects.filter(
#                     ngapolityrel__polity_party__name=F('name'),
#                     ngapolityrel__nga_party__world_region=a_world_region,
#                     ngapolityrel__nga_party__subregion=a_subregion
#                 ).distinct()

#                 ultimate_wregion_dic[a_world_region][a_subregion] = list(all_politys_on_the_polity_list_page)

#         context["all_ngas"] = all_ngas
#         context["all_nga_pol_rels"] = all_nga_pol_rels
#         context["all_world_regions"] = all_world_regions
#         context["ultimate_wregion_dic"] = ultimate_wregion_dic

#         return context


class PolityListView_old(PermissionRequiredMixin, SuccessMessageMixin, generic.ListView):
    model = Polity
    template_name = "core/polity/polity_list.html"
    permission_required = 'core.add_capital'

    #paginate_by = 10

    def get_absolute_url(self):
        return reverse('polities')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_ngas = Nga.objects.all()
        all_pols = Polity.objects.all().order_by('start_year')
        all_nga_pol_rels  = Ngapolityrel.objects.all()
        all_world_regions = {}
        for a_nga in all_ngas:
            if a_nga.world_region not in all_world_regions.keys():
                all_world_regions[a_nga.world_region] = [a_nga.subregion]
            else:
                if a_nga.subregion not in all_world_regions[a_nga.world_region]:
                    all_world_regions[a_nga.world_region].append(a_nga.subregion)
        
        ultimate_wregion_dic = {'Europe': {},
        'Southwest Asia': {},
        'Africa':  {},
        'Central Eurasia': {},
        'South Asia':  {},
        'Southeast Asia': {},
        'East Asia':  {},
        'Oceania-Australia':  {},
        'North America':  {},
        'South America':  {},
        }
        all_politys_on_the_polity_list_page = []
        for a_world_region, all_its_sub_regions in all_world_regions.items():
            for a_subregion in all_its_sub_regions:
                list_for_a_subregion = []
                for a_polity in all_pols:
                    for a_rel in all_nga_pol_rels:
                        if a_rel.polity_party.name == a_polity.name and a_world_region == a_rel.nga_party.world_region and a_subregion == a_rel.nga_party.subregion and a_polity not in list_for_a_subregion:
                            list_for_a_subregion.append(a_polity)
                            if a_polity not in all_politys_on_the_polity_list_page:
                                all_politys_on_the_polity_list_page.append(a_polity)
                        
                ultimate_wregion_dic[a_world_region][a_subregion] = list_for_a_subregion
        context["all_ngas"] = all_ngas
        context["all_nga_pol_rels"] = all_nga_pol_rels
        context["all_world_regions"] = all_world_regions
        context["ultimate_wregion_dic"] = ultimate_wregion_dic
        #print(ultimate_wregion_dic)

        #print(f"out of {len(all_pols)}: {len(all_politys_on_the_polity_list_page)} were taken care of.")
        

        return context

class PolityListView1(SuccessMessageMixin, generic.ListView):
    model = Polity
    template_name = "core/polity/polity_list.html"

    #paginate_by = 10

    def get_absolute_url(self):
        return reverse('polities')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_ngas = Nga.objects.all()
        all_pols = Polity.objects.all().order_by('start_year')
        all_nga_pol_rels  = Ngapolityrel.objects.all()
        all_world_regions = {}
        for a_nga in all_ngas:
            if a_nga.world_region not in all_world_regions.keys():
                all_world_regions[a_nga.world_region] = [a_nga.subregion]
            else:
                if a_nga.subregion not in all_world_regions[a_nga.world_region]:
                    all_world_regions[a_nga.world_region].append(a_nga.subregion)
        
        ultimate_wregion_dic = {'Europe': {},
        'Southwest Asia': {},
        'Africa':  {},
        'Central Eurasia': {},
        'South Asia':  {},
        'Southeast Asia': {},
        'East Asia':  {},
        'Oceania-Australia':  {},
        'North America':  {},
        'South America':  {},
        'Nomad Polities': {
            "Nomad Land": []
        },
        }
        all_politys_on_the_polity_list_page = []
        nomad_polities = []
        for a_world_region, all_its_sub_regions in all_world_regions.items():
            for a_subregion in all_its_sub_regions:
                list_for_a_subregion = []
                for a_polity in all_pols:
                    for a_rel in all_nga_pol_rels:
                        if a_rel.polity_party.name == a_polity.name and a_world_region == a_rel.nga_party.world_region and a_subregion == a_rel.nga_party.subregion and a_polity not in list_for_a_subregion:
                            list_for_a_subregion.append(a_polity)
                            if a_polity not in all_politys_on_the_polity_list_page:
                                all_politys_on_the_polity_list_page.append(a_polity)
                        
                ultimate_wregion_dic[a_world_region][a_subregion] = list_for_a_subregion
        # nomads
        for a_polity in all_pols:
            if a_polity not in nomad_polities and a_polity not in all_politys_on_the_polity_list_page:
                nomad_polities.append(a_polity)
        ultimate_wregion_dic['Nomad Polities'][ "Nomad Land"] = nomad_polities
        context["all_ngas"] = all_ngas
        context["all_nga_pol_rels"] = all_nga_pol_rels
        context["all_world_regions"] = all_world_regions
        context["ultimate_wregion_dic"] = ultimate_wregion_dic
        #print(ultimate_wregion_dic)

        #print(f"out of {len(all_pols)}: {len(all_politys_on_the_polity_list_page)} were taken care of.")
        

        return context
    

class PolityListViewX(SuccessMessageMixin, generic.ListView):
    model = Polity
    template_name = "core/polity/polity_list.html"

    #paginate_by = 10

    def get_absolute_url(self):
        return reverse('polities')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_ngas = Nga.objects.all()
        all_pols = Polity.objects.all().order_by('start_year')
        pol_count = len(all_pols)
        #import time
        #start_time = time.time()

        all_polities_g_sc_wf = give_polity_app_data()


        #all_nga_pol_rels  = Ngapolityrel.objects.all()
        all_world_regions = {}
        for a_nga in all_ngas:
            if a_nga.world_region not in all_world_regions.keys():
                all_world_regions[a_nga.world_region] = [a_nga.subregion]
            else:
                if a_nga.subregion not in all_world_regions[a_nga.world_region]:
                    all_world_regions[a_nga.world_region].append(a_nga.subregion)
        
        ultimate_wregion_dic = {'Europe': {},
        'Southwest Asia': {},
        'Africa':  {},
        'Central Eurasia': {},
        'South Asia':  {},
        'Southeast Asia': {},
        'East Asia':  {},
        'Oceania-Australia':  {},
        'North America':  {},
        'South America':  {},
        'Nomad Polities': {
            "Nomad Land": []
        },
        }

        sub_regions_details = {'Western Europe': 'British Isles, France, Low Countries, Switzerland', 'Southern Europe': 'Iberia, Italy, Sicily, Sardinia, Corsica, Balearics', 'Northern Europe': 'Iceland, Scandinavia, Finland, Baltics, Karelia, Kola Peninsula', 'Central Europe': 'Germany, Poland, Austria, Hungary, Czechia, Slovakia', 'Southeastern Europe': 'Yugoslavia, Romania-Moldova, Bulgaria, Albania, Greece', 'Eastern Europe': 'Belarus, non-Steppe Russia and Ukraine', 'Maghreb': 'From Morocco to Libya', 'Northeastern Africa': 'Egypt and Sudan (the Nile Basin)', 'Sahel': 'Mauritania, Mali, Burkina Faso, Niger, Chad (Arid)', 'West Africa': 'From Senegal to Gabon (Tropical)', 'Central Africa': 'Angola and DRC', 'East Africa': 'Tanzania, Burundi, Uganda, So Sudan, Somalia, Ethiopia, Eritrea', 'Southern Africa': 'Namibia, Zambia, Malawi, Mozambique and south', 'Anatolia-Caucasus': 'Turkey, Armenia, Georgia, Azerbaijan', 'Levant-Mesopotamia': 'Israel, Jordan, Lebanon, Syria, Iraq, Kuwait, Khuzestan (Susiana)', 'Arabia': 'Arabian Peninsula', 'Iran': 'Persia, most of Afghanistan, (western Pakistan?)', 'Pontic-Caspian ': 'The steppe belt of Ukraine and Russia', 'Turkestan': 'Turkmenistan, Uzbekistan, Tajikistan, Kyrgyzstan, Kazakstan, Xinjiang', 'Afghanistan': 'Afghanistan', 'Mongolia': 'Mongolia, Inner Mongolia, the steppe part of Manchuria', 'Siberia': 'Urals, West Siberia, Central Siberia, Yakutia', 'Arctic Asia': 'The tundra and arctic regions of Eurasia sans Scandinavia', 'Tibet': 'Tibet', 'Northeast Asia': 'Korea, Japan, forest part of Manchuria, Russian Far East', 'China': 'China without Tibet, Inner Mongolia, and Xinjiang', 'Indo-Gangetic Plain': 'Pakistan, Punjab, upper and middle Ganges', 'Eastern India': 'Lower Ganges (Bangladesh) and eastern India (Assam)', 'Central India': 'Deccan, etc', 'Southern India': 'Southern India and Sri Lanka', 'Mainland': 'Myanmar, Thailand, Cambodia, Laos, south Vietnam', 'Archipelago': 'Malaysia, Indonesia, Philippines', 'Australia': 'Australia', 'New Guinea': 'New Guinea', 'Polynesia': 'Polynesia', 'Arctic America': 'Alaska, Arctic Canada, Greenland', 'Western NA': 'West Coast, the Rockies, and the American SouthWest', 'Great Plains': 'American Great Plains', 'Mississippi Basin': 'From the Great Lakes to Louisiana', 'East Coast': 'East Coast of US', 'Mexico': 'Mexico and Central America (without Panama)', 'Caribbean': 'Caribbean islands, Panama, coastal Columbia-Venezuela', 'Andes': 'From Ecuador to Chile', 'Amazonia': 'Brazil, Guyanas, plus Amazonian parts of bordering states', 'Southern Cone': 'Parguay, Uruguay, Argentina'}
        all_politys_on_the_polity_list_page = []
        nomad_polities = []

        # modify the world regions:
        all_world_regions["Africa"].append("East Africa")
        all_world_regions["Africa"].append("Southern Africa")
        all_world_regions["South Asia"].append("Southern India")

        for a_polity in all_pols:
            try:
                #a_polity.has_general = has_general_data_for_polity(a_polity.id)
                #a_polity.has_sc = has_sc_data_for_polity(a_polity.id)
                #a_polity.has_wf = has_wf_data_for_polity(a_polity.id)
                #a_polity.has_cc = has_crisis_cases_data_for_polity(a_polity.id)
                #a_polity.has_pt = has_power_transition_data_for_polity(a_polity.id)
                a_polity.has_g_sc_wf = all_polities_g_sc_wf[a_polity.id]
                
            except:
                #a_polity.has_general = None
                #a_polity.has_sc = None
                #a_polity.has_wf = None
                #a_polity.has_cc = None
                #a_polity.has_pt = None
                a_polity.has_g_sc_wf = None

        #end_time = time.time()
        #print('elapsed_time ', end_time-start_time)

        for a_world_region, all_its_sub_regions in all_world_regions.items():
            for a_subregion in all_its_sub_regions:
                list_for_a_subregion = []
                extras_for_AFR_WEST = []
                extras_for_AFR_EAST = []
                extras_for_AFR_SA = []
                extras_for_SA_SI = []

                for a_polity in all_pols:
                    if a_polity.home_nga and a_world_region == a_polity.home_nga.world_region and a_subregion == a_polity.home_nga.subregion and a_polity not in list_for_a_subregion:
                        list_for_a_subregion.append(a_polity)
                        if a_polity not in all_politys_on_the_polity_list_page:
                            all_politys_on_the_polity_list_page.append(a_polity)
                    elif a_polity.polity_tag == "POL_AFR_WEST":
                        extras_for_AFR_WEST.append(a_polity)
                        if a_polity not in all_politys_on_the_polity_list_page:
                            all_politys_on_the_polity_list_page.append(a_polity)
                    elif a_polity.polity_tag == "POL_AFR_EAST":
                        extras_for_AFR_EAST.append(a_polity)
                        if a_polity not in all_politys_on_the_polity_list_page:
                            all_politys_on_the_polity_list_page.append(a_polity)
                    elif a_polity.polity_tag == "POL_AFR_SA":
                        extras_for_AFR_SA.append(a_polity)
                        if a_polity not in all_politys_on_the_polity_list_page:
                            all_politys_on_the_polity_list_page.append(a_polity)
                    elif a_polity.polity_tag == "POL_SA_SI":
                        extras_for_SA_SI.append(a_polity)
                        if a_polity not in all_politys_on_the_polity_list_page:
                            all_politys_on_the_polity_list_page.append(a_polity)

                if a_world_region == "Africa" and a_subregion == "West Africa":
                    ultimate_wregion_dic[a_world_region][a_subregion] = list_for_a_subregion + extras_for_AFR_WEST
                elif a_world_region == "Africa" and a_subregion == "East Africa":
                    ultimate_wregion_dic[a_world_region][a_subregion] = list_for_a_subregion + extras_for_AFR_EAST
                elif a_world_region == "Africa" and a_subregion == "Southern Africa":
                   ultimate_wregion_dic[a_world_region][a_subregion] = list_for_a_subregion + extras_for_AFR_SA
                elif a_world_region == "South Asia" and a_subregion == "Southern India":
                   ultimate_wregion_dic[a_world_region][a_subregion] = list_for_a_subregion + extras_for_SA_SI
                else:
                    ultimate_wregion_dic[a_world_region][a_subregion] = list_for_a_subregion

                        
        # nomads
        for a_polity in all_pols:
            if a_polity not in nomad_polities and a_polity not in all_politys_on_the_polity_list_page:
                nomad_polities.append(a_polity)

        ultimate_wregion_dic['Nomad Polities'][ "Nomad Land"] = nomad_polities
        context["sub_regions_details"] = sub_regions_details
        #context["all_nga_pol_rels"] = all_nga_pol_rels
        context["all_world_regions"] = all_world_regions
        context["ultimate_wregion_dic"] = ultimate_wregion_dic
        #print(ultimate_wregion_dic)
        context['all_pols'] = all_pols
        context["pol_count"] = pol_count

        #print(f"out of {len(all_pols)}: {len(all_politys_on_the_polity_list_page)} were taken care of.")
        

        return context
    


class PolityListView(SuccessMessageMixin, generic.ListView):
    model = Polity
    template_name = "core/polity/polity_list.html"

    def get_absolute_url(self):
        return reverse('polities')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        import time
        start_time = time.time()
        all_srs_unsorted = Seshat_region.objects.all()
        all_mrs_unsorted = Macro_region.objects.all()

        # 1 | World
        # 2 | Africa
        # 3 | Central and Northern Eurasia
        # 4 | East Asia
        # 5 | Europe
        # 6 | South America
        # 7 | North America
        # 8 | Oceania-Australia
        # 9 | South Asia
        # 10 | Southeast Asia
        # 11 | Southwest Asia



        custom_order = [5, 2, 11, 3, 4, 9, 10, 8, 7, 6, 1, 23, 24, 27, 26,25, 29,28, 31,33,32,30, ]  

        custom_order_sr = [20, 18, 17, 15, 19, 16, 3, 4, 5, 7, 1, 2, 6, 43, 61, 62, 44, 45, 10, 13, 8, 9, 11, 12, 14, 58, 59, 38, 39, 37, 36, 40, 41, 42, 28, 29, 30, 26,25, 27,24, 22, 23, 21, 32, 31, 33, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57 ]

        all_mrs = sorted(all_mrs_unsorted, key=lambda item: custom_order.index(item.id))
        all_srs = sorted(all_srs_unsorted, key=lambda item: custom_order_sr.index(item.id))

        all_pols = Polity.objects.all().order_by('start_year')
        pol_count = len(all_pols)

        ultimate_wregion_dic = {}
        ultimate_wregion_dic_top = {}
        for a_mr in all_mrs:
            if a_mr not in ultimate_wregion_dic:
                ultimate_wregion_dic[a_mr.name] = {}
            if a_mr not in ultimate_wregion_dic_top:
                ultimate_wregion_dic_top[a_mr.name] = {}
            for a_sr in all_srs:
                if a_sr.mac_region_id == a_mr.id:
                    if a_sr.name not in ultimate_wregion_dic[a_mr.name]:
                        ultimate_wregion_dic[a_mr.name][a_sr.name] = []
                    if a_sr.name not in ultimate_wregion_dic_top[a_mr.name]:
                        ultimate_wregion_dic_top[a_mr.name][a_sr.name] = [a_sr.subregions_list, 0]

        all_polities_g_sc_wf, freq_dic = give_polity_app_data()
        #all_polities_g_sc_wf = give_polity_app_data()

        freq_dic["d"] = 0

        for a_polity in all_pols:
            if a_polity.home_seshat_region:
                ultimate_wregion_dic[a_polity.home_seshat_region.mac_region.name][a_polity.home_seshat_region.name].append(a_polity)
            if a_polity.home_seshat_region:
                ultimate_wregion_dic_top[a_polity.home_seshat_region.mac_region.name][a_polity.home_seshat_region.name][1] += 1
            if a_polity.general_description:
                freq_dic["d"] += 1

        for a_polity in all_pols:
            try:
                a_polity.has_g_sc_wf = all_polities_g_sc_wf[a_polity.id]
            except:
                a_polity.has_g_sc_wf = None

        context["ultimate_wregion_dic"] = ultimate_wregion_dic
        context["ultimate_wregion_dic_top"] = ultimate_wregion_dic_top
        context['all_pols'] = all_pols
        context['all_srs'] = all_srs
        context["pol_count"] = pol_count
        freq_dic['pol_count'] = pol_count
        context["freq_data"] = freq_dic

        end_time = time.time()
        print('elapsed_time ', end_time-start_time)

        return context
    

class PolityListViewCommented(PermissionRequiredMixin, SuccessMessageMixin, generic.ListView):
    model = Polity
    template_name = "core/polity/polity_list_commented.html"
    permission_required = 'core.add_capital'


    def get_absolute_url(self):
        return reverse('polities')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #all_pols = Polity.objects.filter(private_comment__isnull=False).order_by('start_year')
        all_pols = Polity.objects.exclude(Q(private_comment__isnull=True) | Q(private_comment=''))

        pol_count = len(all_pols)

        all_polities_g_sc_wf, freq_dic = give_polity_app_data()

        for a_polity in all_pols:
            try:
                a_polity.has_g_sc_wf = all_polities_g_sc_wf[a_polity.id]
            except:
                a_polity.has_g_sc_wf = None

        context['all_pols'] = all_pols
        context["pol_count"] = pol_count

        return context
    



class PolityDetailView(SuccessMessageMixin, generic.DetailView):
    model = Polity
    template_name = "core/polity/polity_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context["all_data"] = get_all_data_for_a_polity(self.object.pk, "crisisdb") 
            context["all_general_data"] = get_all_general_data_for_a_polity(self.object.pk)
            context["all_sc_data"] = get_all_sc_data_for_a_polity(self.object.pk)
            context["all_wf_data"] = get_all_wf_data_for_a_polity(self.object.pk)
            context["all_crisis_cases_data"] = get_all_crisis_cases_data_for_a_polity(self.object.pk)
            context["all_power_transitions_data"] = get_all_power_transitions_data_for_a_polity(self.object.pk)
            all_Ras = Polity_research_assistant.objects.filter(polity_id=self.object.pk)
            all_Ras_ids = all_Ras.values_list('polity_ra_id', flat=True)
            experts = Seshat_Expert.objects.filter(id__in=all_Ras_ids)
            
            all_general_ras = []
            for xx in experts:
                an_ra = xx.user.first_name + " " + xx.user.last_name
                if an_ra not in all_general_ras:
                    all_general_ras.append(an_ra)

            all_general_ras_string = ", ".join(all_general_ras)

            

            #my_users_general = [User.objects.get(pk=aa.polity_ra_id) for aa in all_Ras]
            context["majid"] = {"utm_zone": "benam"}
            context["all_Ras"] = all_general_ras_string

        except:
            context["all_data"] = None
            context["all_general_data"] = None
            context["all_sc_data"] = None
            context["all_wf_data"] = None


        #x = polity_detail_data_collector(self.object.pk)
        #context["all_data"] = dict(x)
        #print(self.object.pk)
        context["all_vars"] = {
            "arable_land": "arable_land",
            "agricultural_population": "agricultural_population",
        }
        try:
            my_pol = Polity.objects.get(pk=self.object.pk)
            nga_pol_rels = my_pol.polity_sides.all()
            time_deltas = []
            for nga_pol_rel in nga_pol_rels:
                if (nga_pol_rel.year_from, nga_pol_rel.year_to) not in time_deltas:
                    time_deltas.append((nga_pol_rel.year_from, nga_pol_rel.year_to))

            concise_rels = {}
            for time_delta in time_deltas:
                nga_list = []
                for nga_pol_rel in nga_pol_rels:
                    if time_delta[0] == nga_pol_rel.year_from and time_delta[1] == nga_pol_rel.year_to:
                        nga_list.append(nga_pol_rel.nga_party)
                
                concise_rels[time_delta] = nga_list # "  ~~~   ".join(nga_list)
            context["nga_pol_rel"] = concise_rels
            #print("__________________________")
        except:
            context["nga_pol_rel"] = None
            #print("*************")

        return context


    
# NGA

class NgaCreate(PermissionRequiredMixin, CreateView):
    model = Nga
    form_class = NgaForm
    template_name = "core/nga/nga_form.html"
    permission_required = 'core.add_capital'
    success_url = reverse_lazy('ngas')

    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return HttpResponseRedirect(reverse('seshat-index'))


class NgaUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Nga
    form_class = NgaForm
    template_name = "core/nga/nga_update.html"
    permission_required = 'core.add_capital'
    success_message = "You successfully updated the Nga."
    success_url = reverse_lazy('ngas')


class NgaListView(generic.ListView):
    model = Nga
    template_name = "core/nga/nga_list.html"
    #paginate_by = 10

class NgaDetailView(generic.DetailView):
    model = Nga
    template_name = "core/nga/nga_detail.html"


# Capital

class CapitalCreate(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Capital
    form_class = CapitalForm
    template_name = "core/capital/capital_form_create.html"
    permission_required = 'core.add_capital'
    success_message = "You successfully created a new Capital."
    success_url = reverse_lazy('capitals')

    # def form_valid(self, form):
    #     return super().form_valid(form)
    
    # def form_invalid(self, form):
    #     return HttpResponseRedirect(reverse('capital-create'))


class CapitalUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Capital
    form_class = CapitalForm
    template_name = "core/capital/capital_form.html"
    permission_required = 'core.add_capital'
    success_message = "You successfully updated the Capital."
    success_url = reverse_lazy('capitals')


class CapitalListView(generic.ListView):
    model = Capital
    template_name = "core/capital/capital_list.html"
    #paginate_by = 10

    def get_absolute_url(self):
        return reverse('capitals')
    

class CapitalDelete(PermissionRequiredMixin, DeleteView):
    model = Capital
    success_url = reverse_lazy('capitals')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'
    success_message = "You successfully deleted one Capital."

    

@permission_required('core.view_capital')
def capital_download(request):
    items = Capital.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="capitals.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['capital', 'polity_old_ID', 'polity_new_ID', 'polity_long_name',
                     'current_country', 'longitude', 'latitude','is_verified', 'note'])

    for obj in items:
        writer.writerow([obj.name, obj.polity_cap.name, obj.polity_cap.new_name, obj.polity_cap.long_name, obj.current_country, obj.longitude, obj.latitude, obj.is_verified, obj.note])

    return response


def signup_traditional(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            #current_site = get_current_site(request)
            #subject = 'Activate Your Seshat Account'
            #message = render_to_string('core/account_activation_email.html', {
            #     'user': user,
            #     'domain': current_site,
            #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token': account_activation_token.make_token(user)
            # })
            #user.email_user(subject, message)
            # to_be_sent_email = EmailMessage(subject=subject, body=message,
            #                                 from_email=settings.EMAIL_FROM_USER, to=[user.email])

            # #print(settings.EMAIL_HOST_USER)
            # to_be_sent_email.send()
            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'core/signup_traditional.html', {'form': form})


def signupfollowup(request):
    print(settings.EMAIL_HOST_USER)
    return render(request, 'core/signup-followup.html')


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        #uid = str(urlsafe_base64_decode(uidb64))

        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('signup-followup')
    else:
        return render(request, 'core/account_activation_invalid.html')


# Discussion Room
def discussion_room(request):
    return render(request, 'core/discussion_room.html')

# NLP Room 1
def nlp_datapoints(request):
    return render(request, 'core/nlp_datapoints.html')

# NLP Room 2
def nlp_datapoints_2(request):
    return render(request, 'core/nlp_datapoints_2.html')

def account_activation_sent(request):
    return render(request, 'core/account_activation_sent.html')


def variablehierarchysetting(request):
    my_vars = dic_of_all_vars()
    my_vars_keys = list(my_vars.keys())
    my_vars_good_keys = []
    for item in my_vars_keys:
        good_key = item[0:9] + item[9].lower() + item[10:]
        good_key = good_key.replace('gdp', 'GDP')
        good_key = good_key.replace('gDP', 'GDP')
        my_vars_good_keys.append(good_key)
    all_var_hiers_to_be_hidden = Variablehierarchy.objects.filter(is_verified=True)
    all_var_hiers_to_be_hidden_names = []
    for var in all_var_hiers_to_be_hidden:
        with_crisisdb_name = "crisisdb_" + var.name
        var_name = with_crisisdb_name[0:9] + with_crisisdb_name[9].lower() + with_crisisdb_name[10:]
        var_name = var_name.replace('gdp', 'GDP')
        var_name = var_name.replace('gDP', 'GDP')

        if with_crisisdb_name in my_vars_good_keys:
            var_name = with_crisisdb_name[0:9] + with_crisisdb_name[9].lower() + with_crisisdb_name[10:]
            var_name = var_name.replace('gdp', 'GDP')
            var_name = var_name.replace('gDP', 'GDP')

            all_var_hiers_to_be_hidden_names.append(var_name)
    print('I am here...\n\n')
    #print(all_var_hiers_to_be_hidden_names)
    my_vars_tuple = [('', ' -- Select a CrisisDB Variable -- ')]
    for var in my_vars_good_keys:
        if var not in all_var_hiers_to_be_hidden_names:
            without_crisisdb_var = var[9:]
            var_name = without_crisisdb_var[0].lower() + without_crisisdb_var[1:]
            var_name = var_name.replace('gdp', 'GDP')
            var_name = var_name.replace('gDP', 'GDP')

            my_var_tuple = (var_name, var_name)
            my_vars_tuple.append(my_var_tuple)

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
    # Let's create an API serializer for section and subsection heierarchy
    url = "http://127.0.0.1:8000/api/sections/"
    #url = "https://www.majidbenam.com/api/sections/"
    #url = settings.MY_CURRENT_SERVER + "/api/sections/"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"

    resp = requests.get(url, headers=headers)

    all_my_data = resp.json()['results']
    sections_tree = {}
    sections_options_for_JS = {}
    for list_item in all_my_data:
        subsect_dic = {}
        subsects_only_list = []
        for subsec in list_item['subsections']:
            list_to_be = []
            subsects_only_list.append(subsec)
            sel_sect = Section.objects.get(name=list_item['name'])
            sel_subsect = Subsection.objects.get(name=subsec)
            my_selected_vars_objects = Variablehierarchy.objects.filter( section=sel_sect, subsection=sel_subsect,)
            for var_obj in my_selected_vars_objects:
                #print(var_obj)
                list_to_be.append(var_obj.name)
            subsect_dic[subsec] = list_to_be
        sections_tree[list_item['name']] = subsect_dic
        sections_options_for_JS[list_item['name']] = subsects_only_list
    context = {
        'sectionOptions': sections_options_for_JS, 
        'section_tree_data': sections_tree,
    }
    #print(context['sectionOptions'])
    #print(context['section_tree_data'])


    if request.method == 'POST':
        form = VariablehierarchyFormNew(request.POST)
        if True:
            data = request.POST
            variable_name = data["variable_name"]
            #is_verified_str = data["is_verified"]
            is_verified_str = data.get("is_verified", False)
            if is_verified_str == 'on':
                is_verified = True
            elif is_verified_str == 'off':
                is_verified = False
            else:
                is_verified = False
            section_name = Section.objects.get(name=data["section_name"])
            subsection_name = Subsection.objects.get(
                name=data["subsection_name"])
            # check to see if subsection and section match
            if data["subsection_name"] in sections_tree[data["section_name"]]:
                new_var_hierarchy = Variablehierarchy(
                    name=variable_name, section=section_name, subsection=subsection_name,  is_verified=is_verified)
                new_var_hierarchy.save()
                #print('Valid Foooooooooooorm: \n\n',)
                # print(data)
                my_message = f'''You have successfully submitted {variable_name} to: {section_name} >  {subsection_name}'''
                messages.success(request, my_message)
                return HttpResponseRedirect(reverse('variablehierarchysetting'))
            else:
                messages.warning(request, 'Form submission unssuccessful, section and subsection do not match.')
                #return render(request, 'core/Variablehierarchy.html', {'form': VariablehierarchyFormNew()})

        else:
            data = request.POST
            #print('halllooooooooo:', data["variable_name"])
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)

    else:
        form = VariablehierarchyFormNew()
    context['form'] = form
    context['variable_list'] = list(my_vars_tuple)
    context['section_list'] = list(all_sections_tuple)
    context['subsection_list'] = list(all_subsections_tuple)

    #context['SuccessMessage'] = "Done Perfectly."
    return render(request, 'core/variablehierarchy.html', context)



###############
def do_zotero(results):
    import re
    mother_ref_dic = []
    for i, item in enumerate(results):
        #print(i, ": ", item['data']['key'], item['data']['date'])
        #if item['data']['key'] in ["MJT9UJE4", "NIKCMK5L", "QTI79LX9"]:
        #    print("______________")
        #    print(item)
        a_key = item['data']['key']
        if a_key == "3BQQ8WN8":
            print("I skipped over  youuuuu: 3BQQ8WN8 because you are not in the database!")
            continue
        if a_key == 'RR6R3383':
            print("I skipped over  youuuuu: RR6R3383 because your title is too big")
            continue
            
            #print(pprint.pprint(item))
        try:
            # we need to make sure that all the changes in Zotero will be reflected here.
            potential_new_ref = Reference.objects.get(zotero_link=a_key)
            # full_date = item['data'].get('date')
            # if full_date:
            #     year = re.search(r'[12]\d{3}', full_date)
            #     if year:
            #         year_int = int(year[0])
            #         if potential_new_ref.year != year_int:
            #             print(f"Item Changed On Zotero: {a_key}")
            continue
        except:          
            my_dic = {}
            try:
                if item['data']['key']:
                    tuple_key = item['data']['key']
                    my_dic['key'] = tuple_key
                else:
                    pass #print("key is empty for index: ", i, item['data']['itemType'])
            except:
                pass #print("No key for item with index: ", i)
            try:
                if item['data']['itemType']:
                    tuple_item = item['data']['itemType']
                    my_dic['itemType'] = tuple_item
                else:
                    pass #print("itemType is empty for index: ", i, item['data']['itemType'])
            except:
                pass #print("No itemType for item with index: ", i)
            try:
                num_of_creators = len(item['data']['creators'])
                if num_of_creators < 4 and num_of_creators > 0:
                    all_creators_list = []  
                    for j in range(num_of_creators):
                        if a_key == "MM6AEU7H":
                            print("I saw youuuuuuuuuuuuuuu more probably because you have contributors instead of authors")
                        try:
                            try:
                                good_name = item['data']['creators'][j]['lastName']
                            except:
                                good_name = item['data']['creators'][j]['name']
                        except:
                            good_name = ("NO_NAMES",)
                        all_creators_list.append(good_name)
                    good_name_with_space = "_".join(all_creators_list)
                    good_name_with_underscore = good_name_with_space.replace(' ', '_')
                    my_dic['mainCreator'] = good_name_with_underscore
                elif num_of_creators > 3:
                    try:
                        try:
                            good_name = item['data']['creators'][0]['lastName']
                        except:
                            good_name = item['data']['creators'][0]['name']
                    except:
                        good_name = ("NO_NAME",)
                    good_name_with_space = good_name + '_et_al'
                    good_name_with_underscore = good_name_with_space.replace(' ', '_')
                    my_dic['mainCreator'] = good_name_with_underscore
                else:
                    my_dic['mainCreator'] = "NO_CREATOR" 
                #pass #print(my_dic['mainCreator'])
            except:
                my_dic['mainCreator'] = "NO_CREATORS"
                pass #print("No mainCreator for item with index: ", i, item['data']['itemType'])
            try:
                if item['data']['date']:
                    full_date = item['data']['date']
                    year = re.search(r'[12]\d{3}', full_date)
                    year_int = int(year[0])
                    my_dic['year'] = year_int
                else:
                    my_dic['year'] = 0
                    #pass #print("year is empty for index: ", i, item['data']['itemType'])
                #pass #print(my_dic['year'])
            except:
                my_dic['year'] = -1
                #pass #print("No year for item with index: ", i, item['data']['itemType'])
            try:
                try:
                    if item['data']['bookTitle']:
                        if a_key == "MM6AEU7H":
                            print("I saw youuuuuuuuuuuuuuu more")
                        if item['data']['itemType'] == 'bookSection':
                            good_title = item['data']['title'] + " (IN) " + item['data']['bookTitle']
                            pass #print (i, ": ", a_key, "    ", good_title)
                        else:
                            good_title = item['data']['title']
                            pass #print (i, ": ", a_key, "    ", good_title)
                        counter_bookTitle = counter_bookTitle + 1
                        my_dic['title'] = good_title
                    else:
                        good_title = item['data']['title']
                        my_dic['title'] = good_title
                        if a_key == "MM6AEU7H":
                            print("I saw youuuuuuuuuuuuuuu more")
                        pass #print (i, ": ", a_key, "    ", good_title)
                except:
                    my_dic['title'] = item['data']['title']
                    pass #print (i, ": ", a_key, "    ", item['data']['title'])
            except:
                pass #print("No title for item with index: ", i)
            
            pot_title = my_dic.get('title')
            if not pot_title:
                pot_title = "NO_TITLE_PROVIDED_IN_ZOTERO"
            #print("Years: ", my_dic.get('year'))
            #print("****************")
            newref = Reference(title=pot_title, year=my_dic.get('year'), creator=my_dic.get('mainCreator'), zotero_link=my_dic.get('key'))
            #newref = Reference(title=my_dic['title'], year=my_dic['year'], creator=my_dic['mainCreator'], zotero_link=my_dic['key'])

            if my_dic.get('year') < 2040:
                newref.save()
                mother_ref_dic.append(my_dic)

    #print(len(mother_ref_dic))
    #print(counter_bookTitle)
    print("Bye Zotero")
    return mother_ref_dic

def do_zotero_manually(results):
    mother_ref_dic = []
    for i, item in enumerate(results):

        a_key = item['key']
        if a_key == "3BQQ8WN8":
            print("I skipped over  youuuuu: 3BQQ8WN8 because you are not in the database!")
            continue
        if a_key == 'RR6R3383':
            print("I skipped over  youuuuu: RR6R3383 because your title is too big")
            continue
            
        try:
            potential_new_ref = Reference.objects.get(zotero_link=a_key)
            continue
        except:          
            my_dic = {}
            my_dic['key'] = a_key
            my_dic['mainCreator'] = item['mainCreator']
            my_dic['year'] = item['year']
            my_dic['title'] = item['title']

            newref = Reference(title=my_dic.get('title'), year=my_dic.get('year'), creator=my_dic.get('mainCreator'), zotero_link=my_dic.get('key'))

            if my_dic.get('year') < 2040:
                newref.save()
                mother_ref_dic.append(my_dic)


    print("Bye Zotero Manually")
    return mother_ref_dic


##########

def update_citations_from_inside_zotero_update():
    """
    this function gets all the references and build a citation for them
    """
    from datetime import datetime
    all_refs = Reference.objects.all()
    for ref in all_refs:
        a_citation = Citation.objects.get_or_create(ref=ref, page_from=None, page_to=None)
        a_citation[0].save()
    print("Halllooooo")
    # Citation.objects.bulk_create(all_citations)
    #return render (request, 'core/references/reference_list.html')

###########


def synczoteromanually(request):
    print("Hallo Zotero Manually")
    from .manual_input_refs import manual_input_refs 

    new_refs = do_zotero_manually(manual_input_refs)
    context = {}
    context["newly_adds"] = new_refs
    update_citations_from_inside_zotero_update()
    return render (request, 'core/references/synczotero.html', context)

def synczotero(request):
    print("Hallo Zotero")

    from pyzotero import zotero
    zot = zotero.Zotero(1051264, 'group', 'VF5X3TCC3bUYov8Au5gCHf3a')
    results = zot.everything(zot.top())
    #results = zot.top(limit=100)

    print(len(results))
    counter_bookTitle = 0
    new_refs = do_zotero(results[0:300])
    context = {}
    context["newly_adds"] = new_refs
    update_citations_from_inside_zotero_update()
    #num_1_ref = Reference.objects.get(zotero_link ="FGFSZUNB")
    #num_1_ref.year = 2014
    #num_1_ref.save()
    return render (request, 'core/references/synczotero.html', context)

def synczotero100(request):
    print("Hallo Zotero")

    from pyzotero import zotero
    zot = zotero.Zotero(1051264, 'group', 'VF5X3TCC3bUYov8Au5gCHf3a')
    #results = zot.everything(zot.top())
    results = zot.top(limit=100)

    print(len(results))
    counter_bookTitle = 0
    new_refs = do_zotero(results)
    context = {}
    context["newly_adds"] = new_refs
    update_citations_from_inside_zotero_update()
    #num_1_ref = Reference.objects.get(zotero_link ="FGFSZUNB")
    #num_1_ref.year = 2014
    #num_1_ref.save()
    return render (request, 'core/references/synczotero.html', context)



def update_citations(request):
    """
    this function gets all the references and build a citation for them
    """
    all_refs = Reference.objects.all()
    for ref in all_refs:
        a_citation = Citation.objects.get_or_create(ref=ref, page_from=None, page_to=None)
        a_citation[0].save()
    # Citation.objects.bulk_create(all_citations)
    return render (request, 'core/references/reference_list.html')


@require_GET
def polity_filter_options_view(request):
    search_text = request.GET.get('search_text', '')

    # Filter the options based on the search text
    options = Polity.objects.filter(name__icontains=search_text).values('id', 'name')

    response = {
        'options': list(options)
    }
    return JsonResponse(response)


def download_oldcsv(request, file_name):
    file_path = os.path.join(settings.STATIC_ROOT, 'csvfiles', file_name)
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    return response



def seshatindex(request):
    app_names = ['general','sc', 'wf', 'crisisdb']  # Replace with your app name
    context = {
        'pols_data': [],
        'general_data': [],
        'sc_data': [], 
        'wf_data': [],
        'crisisdb': [],
        'pt_data': [],
        'cc_data': [],
        'hs_data': [],
        'sr_data': [],
        'general_examples': [('Alternative Name', 'polity_alternative_names_all', 'Identity and Location'),
                            ('Polity Peak Years', 'polity_peak_yearss_all', 'Temporal Bounds'), 
                            ('Polity Capital', 'polity_capitals_all', 'Identity and Location'), 
                            ('Polity Language', 'polity_languages_all', 'Language'),
                            ('Polity Religion', 'polity_religions_all', 'Religion'),
                            ('Degree of Centralization', 'polity_degree_of_centralizations_all', 'Temporal Bounds'),
                            ('Succeeding Entity', 'polity_succeeding_entitys_all', 'Supra-cultural relations'),
                            ('Relationship to Preceding Entity', 'polity_relationship_to_preceding_entitys_all', 'Supra-cultural relations'),
                            ],

        'sc_examples': [('Polity Territory', 'polity_territorys_all', 'Social Scale'), 
                        ('Polity Population', 'polity_populations_all', 'Social Scale'), 
                        ('Settlement Hierarchy', 'settlement_hierarchys_all', 'Hierarchical Complexity'), 
                        ('Irrigation System', 'irrigation_systems_all', 'Specialized Buildings: polity owned'), 
                        ('Merit Promotion', 'merit_promotions_all', 'Bureaucracy Characteristics'), 
                        ('Formal Legal Code', 'formal_legal_codes_all', 'Law'), 
                        ('Road', 'roads_all', 'Transport Infrastructure'), 
                        ('Postal Station', 'postal_stations_all', 'Information / Postal System')],
        'wf_examples': [('Bronze', 'bronzes_all', 'Military use of Metals'),
                        ('Javelin', 'javelins_all', 'Projectiles'),
                        ('Battle Axe', 'battle_axes_all', 'Handheld Weapons'),
                        ('Sword', 'swords_all', 'Handheld Weapons'),
                        ('Horse', 'horses_all', 'Animals used in warfare'),
                        ('Small Vessels (canoes, etc)', 'small_vessels_canoes_etcs_all', 'Naval technology'),
                        ('Shield', 'shields_all', 'Armor'),
                        ('Wooden Palisade', 'small_vessels_canoes_etcs_all', 'Fortifications'),
                        ]
        #'crisisdb_examples': [],
        #'pt_examples': [],
        #'cc_examples': [],
        #'sr_examples': [],

        }
    all_srs_unsorted = Seshat_region.objects.exclude(name="Somewhere")
    all_mrs_unsorted = Macro_region.objects.exclude(name="World")
    to_be_appended_y = [len(all_srs_unsorted), len(all_mrs_unsorted)] 
    context['sr_data'] = to_be_appended_y

    all_pols_count = Polity.objects.count()
    to_be_appended_y = [all_pols_count, len(all_srs_unsorted)] 
    context['pols_data'] = to_be_appended_y

    eight_pols = Polity.objects.order_by('?')[:8]
    context['eight_pols'] = eight_pols

    eight_srs = Seshat_region.objects.exclude(name="Somewhere").order_by('?')[:8]
    context['eight_srs'] = eight_srs



  
  

    for app_name in app_names:
        models = apps.get_app_config(app_name).get_models()
        unique_politys = set()
        number_of_variables = 0
        number_of_rows_in_app = 0
        app_key = app_name + "_data"
        for model in models:
            model_name = model.__name__
            if model_name == "Ra":
                continue
            if  model_name.startswith("Us_violence"):
                queryset_count = model.objects.count()

                queryset = model.objects.all()

                to_be_appended_xxxx = [queryset_count, 1,]
                context['us_data'] = to_be_appended_xxxx
                eight_uss = queryset.order_by('?')[:8]
                context['eight_uss'] = eight_uss
                continue
            if  model_name.startswith("Us_"):
                continue
            if  model_name.startswith("Power_transition"):
                queryset_count = model.objects.count()

                queryset = model.objects.all()
                politys = queryset.values_list('polity', flat=True).distinct()

                to_be_appended_x = [queryset_count, 1, len(set(politys)),]
                context['pt_data'] = to_be_appended_x
                eight_pts = queryset.order_by('?')[:8]
                context['eight_pts'] = eight_pts
                continue
            if  model_name.startswith("Crisis_consequence"):
                queryset_count = model.objects.count()

                queryset = model.objects.all()
                politys = queryset.values_list('polity', flat=True).distinct()

                to_be_appended_xx = [queryset_count, 1, len(set(politys)),]
                context['cc_data'] = to_be_appended_xx
                eight_ccs = queryset.order_by('?')[:8]
                context['eight_ccs'] = eight_ccs
                continue
            if  model_name.startswith("Human_sacrifice"):
                queryset_count = model.objects.count()

                queryset = model.objects.all()
                politys = queryset.values_list('polity', flat=True).distinct()

                to_be_appended_xxx = [queryset_count, 1, len(set(politys)),]
                context['hs_data'] = to_be_appended_xxx
                eight_hss = queryset.order_by('?')[:8]
                context['eight_hss'] = eight_hss
                continue

            queryset_count = model.objects.count()

            queryset = model.objects.all()
            politys = queryset.values_list('polity', flat=True).distinct()
            unique_politys.update(politys)
            number_of_variables += 1

            number_of_rows_in_app += queryset_count

        to_be_appended = [number_of_rows_in_app, number_of_variables, len(unique_politys),]

        context[app_key] = to_be_appended

    return render(request, 'core/seshat-index.html', context=context)


def get_polity_data_single(polity_id):
    from seshat.apps.crisisdb.models import Crisis_consequence, Power_transition, Human_sacrifice
    from django.apps import apps

    app_models_general = apps.get_app_config('general').get_models()
    app_models_sc = apps.get_app_config('sc').get_models()
    app_models_wf = apps.get_app_config('wf').get_models()

    data = {
        'g': 0,
        'sc': 0,
        'wf': 0,
        'hs': 0,
        'cc': 0,
        'pt': 0,
    }

    for model in app_models_general:
        if hasattr(model, 'polity_id') and model.objects.filter(polity_id=polity_id).exists():
            data['g'] += model.objects.filter(polity_id=polity_id).count()

    for model in app_models_sc:
        if hasattr(model, 'polity_id') and model.objects.filter(polity_id=polity_id).exists():
            data['sc'] += model.objects.filter(polity_id=polity_id).count()

    for model in app_models_wf:
        if hasattr(model, 'polity_id') and model.objects.filter(polity_id=polity_id).exists():
            data['wf'] += model.objects.filter(polity_id=polity_id).count()

    data['hs'] = Human_sacrifice.objects.filter(polity=polity_id).count()
    data['cc'] = Crisis_consequence.objects.filter(polity=polity_id).count()
    data['pt'] = Power_transition.objects.filter(polity=polity_id).count()

    return data

@permission_required('core.view_capital')
def download_csv_all_polities(request):
    # Create a response object with CSV content type
    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"polities_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    # Create a CSV writer
    writer = csv.writer(response, delimiter='|')

    # type the headers
    writer.writerow(['macro_region', 'home_seshat_region',  'polity_new_id', 'polity_old_id', 'polity_long_name', 'start_year', 'end_year', 'home_nga', 'G', "SC", "WF", "HS", "CC", "PT", 'polity_tag'])

    items = Polity.objects.all()
    coded_value_data, freq_data = give_polity_app_data()

    for obj in items:
        #coded_values_data = get_polity_data_single(obj.id)
        #print(obj.id)
        #print(type(obj))
        if obj.home_seshat_region:
            writer.writerow([obj.home_seshat_region.mac_region.name, obj.home_seshat_region.name, obj.new_name, obj.name, obj.long_name, obj.start_year, obj.end_year, obj.home_nga,  coded_value_data[obj.id]['g'], coded_value_data[obj.id]['sc'], coded_value_data[obj.id]['wf'], coded_value_data[obj.id]['hs'], coded_value_data[obj.id]['cc'], coded_value_data[obj.id]['pt'], obj.get_polity_tag_display()])
        else:
            writer.writerow(["None", "None", obj.new_name, obj.name, obj.long_name, obj.start_year, obj.end_year, obj.home_nga,  coded_value_data[obj.id]['g'], coded_value_data[obj.id]['sc'], coded_value_data[obj.id]['wf'], coded_value_data[obj.id]['hs'], coded_value_data[obj.id]['cc'], coded_value_data[obj.id]['pt'], obj.get_polity_tag_display()])

    return response

##### additions for the seshatcommentpart enhancement
# views.py


def get_or_create_citation(reference, page_from, page_to):
    # Check if a matching citation already exists
    existing_citation = Citation.objects.filter(
        ref=reference,
        page_from=page_from,
        page_to=page_to
    ).first()

    # If a matching citation exists, return it; otherwise, create a new one
    return existing_citation or Citation.objects.create(
        ref=reference,
        page_from=page_from,
        page_to=page_to
    )
from django.shortcuts import render, redirect
from .forms import SeshatCommentPartForm
from .models import SeshatCommentPart, Citation

def seshatcommentpart_create_view_old(request):
    if request.method == 'POST':
        form = SeshatCommentPartForm2(request.POST)
        if form.is_valid():
            comment_text = form.cleaned_data['comment_text']
            reference = form.cleaned_data['reference']
            page_from = form.cleaned_data['page_from']
            page_to = form.cleaned_data['page_to']
            comment_order = form.cleaned_data['comment_order']

            # Get or create the Citation instance
            citation = get_or_create_citation(reference, page_from, page_to)
            user_logged_in = request.user

            comment_instance = SeshatComment.objects.create(text='a new_comment_text')

            try:
                seshat_expert_instance = Seshat_Expert.objects.get(user=user_logged_in)
            except Seshat_Expert.DoesNotExist:
                seshat_expert_instance = None

            # Create the SeshatCommentPart instance and associate the Citation
            comment_part = SeshatCommentPart.objects.create(
                comment=comment_instance,
                comment_part_text=comment_text,
                comment_order=comment_order,
                comment_curator=seshat_expert_instance 
            )
            comment_part.comment_citations.add(citation)

            return redirect('seshat-index')  # Redirect to a success page

    else:
        form = SeshatCommentPartForm2()

    return render(request, 'core/seshatcomments/seshatcommentpart_create.html', {'form': form})


# views.py
from django.shortcuts import render, redirect
from .models import SeshatCommentPart, Citation

def seshatcommentpart_create_view(request):
    if request.method == 'POST':
        form = SeshatCommentPartForm2(request.POST)
        if form.is_valid():
            comment_text = form.cleaned_data['comment_text']
            comment_order = form.cleaned_data['comment_order']
            user_logged_in = request.user

            comment_instance = SeshatComment.objects.create(text='a new_comment_text')

            try:
                seshat_expert_instance = Seshat_Expert.objects.get(user=user_logged_in)
            except Seshat_Expert.DoesNotExist:
                seshat_expert_instance = None

            # Create the SeshatCommentPart instance
            comment_part = SeshatCommentPart.objects.create(
                comment=comment_instance,
                comment_part_text=comment_text,
                comment_order=comment_order,
                comment_curator=seshat_expert_instance 
            )

            # Process the formset
            reference_formset = ReferenceFormSet(request.POST, prefix='refs')
            print("++++++ffffffff++++++++")
            if reference_formset.is_valid():
                print("Ahsaaaaant")
            else:
                print(f'Formset errors: {reference_formset.errors}, {reference_formset.non_form_errors()}')

            if reference_formset.has_changed():
                print("Ahsaaaaaaaaaaaaaaaaaant")
            else:
                print(f'Formset errors: {reference_formset.errors}, {reference_formset.non_form_errors()}')
            print("++++++ffffffff++++++++")
            for i, reference_form in enumerate(reference_formset):
                if reference_form.is_valid():
                    print("+++++++xxaaaaaaaaaxx+++++++")
                    reference = reference_form.cleaned_data['ref']
                    page_from = reference_form.cleaned_data['page_from']
                    page_to = reference_form.cleaned_data['page_to']

                    # Get or create the Citation instance
                    #citation = get_or_create_citation(reference, page_from, page_to)
                    citation, created = Citation.objects.get_or_create(
                        ref=reference,
                        page_from=int(page_from),
                        page_to=int(page_to)
                    )


                    # Associate the Citation with the SeshatCommentPart
                    comment_part.comment_citations.add(citation)
                    print("+++++++xxxx+++++++")
                    print("I am here::::::", citation)
                else:
                    print(f'Form errors: {reference_form.errors}')

            return redirect('seshat-index')  # Redirect to a success page

    else:
        form = SeshatCommentPartForm2()

    return render(request, 'core/seshatcomments/seshatcommentpart_create.html', {'form': form})

