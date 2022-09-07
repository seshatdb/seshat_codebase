from seshat.utils.utils import adder, dic_of_all_vars, list_of_all_Polities, dic_of_all_vars_in_sections

from django.contrib.sites.shortcuts import get_current_site
from seshat.apps.core.forms import SignUpForm, VariablehierarchyFormNew, CitationForm
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

from markupsafe import Markup, escape
from django.http import JsonResponse

from django.core.mail import EmailMessage
import html
import json
from django.views import generic
from django.urls import reverse, reverse_lazy

from .models import Citation, Polity, Section, Subsection, Variablehierarchy, Reference
import pprint
import requests
from requests.structures import CaseInsensitiveDict


# importing formset_factory
from django.forms import formset_factory, modelformset_factory


def index(request):
    return HttpResponse('<h1>Hello World.</h1>')

def four_o_four(request):
    return render(request, 'core/not_found_404.html')

def seshatindex(request):
    context = {
        'insta': "Instabilities All Over the Place..",
        'trans': "Transitions All Over the Place",
    }
    #print('static_root:', settings.STATIC_ROOT)
    #print('STATICFILES_DIRS:', settings.STATICFILES_DIRS)
    return render(request, 'core/seshat-index.html', context=context)


class ReferenceListView(generic.ListView):
    model = Reference
    template_name = "core/references/reference_list.html"
    paginate_by = 20

    def get_absolute_url(self):
        return reverse('references')

class CitationListView(generic.ListView):
    model = Citation
    template_name = "core/references/citation_list.html"
    paginate_by = 20

    def get_absolute_url(self):
        return reverse('citations')

class CitationCreate(PermissionRequiredMixin, CreateView):
    model = Citation
    form_class = CitationForm
    template_name = "core/references/citation_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('citation-create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mysection"] = "xyz"
        context["mysubsection"] = "abc"
        context["myvar"] = "def citation"
        context["errors"] = "Halooooooooo"
        print(context)

        return context

    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return HttpResponseRedirect(reverse('seshat-index'))


class CitationUpdate(PermissionRequiredMixin, UpdateView):
    model = Citation
    form_class = CitationForm
    template_name = "core/references/citation_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mysection"] = "Fiscal Helath"
        context["mysubsection"] = "No Subsection Provided"
        context["myvar"] = "Citation Data"

        return context

class CitationDelete(PermissionRequiredMixin, DeleteView):
    model = Citation
    success_url = reverse_lazy('citations')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class CitationDetailView(generic.DetailView):
    model = Citation
    template_name = "core/references/citation_detail.html"


# POLITY
class PolityListView(generic.ListView):
    model = Polity
    template_name = "core/polity/polity_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('polities')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mysection"] = "Fiscal Helath"
        context["mysubsection"] = "No Subsection Provided"
        context["myvar"] = "Revenue Official"

        return context


class PolityDetailView(generic.DetailView):
    model = Polity
    template_name = "core/polity/polity_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vars"] = {}
        mybalances = self.object.crisisdb_balance_related.all()

        # We can theoretically write a loop that goes through a list of everything we might be interested in
        # we can then put if loops to check if the graphs are available to templates.
        # Then we show them.
        for_chart_year_balance_list = list()
        for_chart_balance_list = list()
        for_chart_year_salt_tax_list = list()
        for_chart_salt_tax_list = list()

        context["vars"]["balance"] = {}
        for item in mybalances:
            context["vars"]["balance"][item] = []
            context["vars"]["balance"][item].append(item.year_from)
            context["vars"]["balance"][item].append(item.balance)
            # for charts:
            for_chart_year_balance_list.append(item.year_from)
            for_chart_balance_list.append(item.balance)

        mysalttaxes = self.object.crisisdb_salt_tax_related.all()
        context["vars"]["salt_tax"] = {}
        for item in mysalttaxes:
            context["vars"]["salt_tax"][item] = []
            context["vars"]["salt_tax"][item].append(item.year_from)
            context["vars"]["salt_tax"][item].append(item.salt_tax)
            # for charts
            for_chart_year_salt_tax_list.append(item.year_from)
            for_chart_salt_tax_list.append(item.salt_tax)

        context["year_bals"] = for_chart_year_balance_list
        context["bals"] = for_chart_balance_list
        context["year_sals"] = for_chart_year_salt_tax_list
        context["sals"] = for_chart_salt_tax_list

        years = context["year_bals"]
        salts = context["sals"]
        bals = context["bals"]

        #print('printing years lllllllllllnnnnlllllllll')
        # print(years)
        full_year_range = []
        full_salt_range = []
        full_bal_range = []
        year_max = max(years)
        year_min = min(years)
        for i in range(year_min, year_max+1):
            if i in years:
                my_index = years.index(i)
                full_year_range.append(years[my_index])
                full_salt_range.append(salts[my_index])
                full_bal_range.append(bals[my_index])

            else:
                full_year_range.append(i)
                full_salt_range.append(None)
                full_bal_range.append(None)

        print(full_year_range)
        print(full_bal_range)

        context["sals"] = json.dumps(full_salt_range)
        context["yearsals"] = json.dumps(full_year_range)
        context["bals"] = json.dumps(full_bal_range)
        context["yearmin"] = json.dumps(year_min)

        #context["vars"]["salt_tax"] = [mysalttaxes, 'salt_tax']
        # print(self)
        # print("----")
        # print(context["bals"])
        # print("++++")
        # print(context["year_sals"])

        return context


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your Seshat Account'
            message = render_to_string('core/account_activation_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user)
            })
            #user.email_user(subject, message)
            to_be_sent_email = EmailMessage(subject=subject, body=message,
                                            from_email=settings.EMAIL_FROM_USER, to=[user.email])

            print(settings.EMAIL_HOST_USER)
            to_be_sent_email.send()
            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})


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
    print(all_var_hiers_to_be_hidden_names)
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
                print(var_obj)
                list_to_be.append(var_obj.name)
            subsect_dic[subsec] = list_to_be
        sections_tree[list_item['name']] = subsect_dic
        sections_options_for_JS[list_item['name']] = subsects_only_list
    context = {
        'sectionOptions': sections_options_for_JS, 
        'section_tree_data': sections_tree,
    }
    print(context['sectionOptions'])
    print(context['section_tree_data'])


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
                print('Valid Foooooooooooorm: \n\n',)
                # print(data)
                my_message = f'''You have successfully submitted {variable_name} to: {section_name} >  {subsection_name}'''
                messages.success(request, my_message)
                return HttpResponseRedirect(reverse('variablehierarchysetting'))
            else:
                messages.warning(request, 'Form submission unssuccessful, section and subsection do not match.')
                #return render(request, 'core/Variablehierarchy.html', {'form': VariablehierarchyFormNew()})

        else:
            data = request.POST
            print('halllooooooooo:', data["variable_name"])
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
        a_key = item['data']['key']
        if a_key == "3BQQ8WN8":
            print("I skipped over  youuuuuuuuuuuuuuu: 3BQQ8WN8")
            continue
        if a_key == 'RR6R3383':
            print("I skipped over  youuuuuuuuuuuuuuu: RR6R3383")
            continue
            
            #print(pprint.pprint(item))
        try:
            potential_new_ref = Reference.objects.get(zotero_link=a_key)
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
                            print("I saw youuuuuuuuuuuuuuu more")
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
                
            newref = Reference(title=my_dic['title'], year=my_dic['year'], creator=my_dic['mainCreator'], zotero_link=my_dic['key'])
            if my_dic['year'] < 2040:
                newref.save()
                mother_ref_dic.append(my_dic)

    print(len(mother_ref_dic))
    #print(counter_bookTitle)
    print("Bye Zotero")
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

def synczotero(request):
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

