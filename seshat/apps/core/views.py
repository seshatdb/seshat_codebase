from dataclasses import dataclass
from seshat.utils.utils import adder, dic_of_all_vars, list_of_all_Polities, dic_of_all_vars_in_sections

from django.contrib.sites.shortcuts import get_current_site
from seshat.apps.core.forms import SignUpForm, VariableHierarchyForm
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

from markupsafe import Markup, escape

from django.core.mail import EmailMessage
import html
import json
from django.views import generic
from django.urls import reverse, reverse_lazy

from .models import Polity, VariableHierarchy, Section, Subsection
from .forms import VariableHierarchy, VariableHierarchyFormNew

import requests
from requests.structures import CaseInsensitiveDict


# importing formset_factory
from django.forms import formset_factory, modelformset_factory


def index(request):
    return HttpResponse('<h1>Hello World.</h1>')


def seshatindex(request):
    context = {
        'insta': "Instabilities All Over the Place..",
        'trans': "Transitions All Over the Place",
    }
    #print('static_root:', settings.STATIC_ROOT)
    #print('STATICFILES_DIRS:', settings.STATICFILES_DIRS)
    return render(request, 'core/seshat-index.html', context=context)


class PolityListView(generic.ListView):
    model = Polity
    template_name = "core/polity/polity_list.html"
    paginate_by = 5

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
    all_var_hiers_to_be_hidden = VariableHierarchy.objects.filter(is_verified=True)
    all_var_hiers_to_be_hidden_names = []
    for var in all_var_hiers_to_be_hidden:
        if var.name in my_vars.keys():
            all_var_hiers_to_be_hidden_names.append(var.name)
    print('I am here...\n\n')
    print(all_var_hiers_to_be_hidden_names)
    my_vars_tuple = [('', ' -- Select Variable -- ')]
    for var in my_vars.keys():
        if var not in all_var_hiers_to_be_hidden_names:
            my_var_tuple = (var, var)
            my_vars_tuple.append(my_var_tuple)
    # Let's create an API serializer for section and subsection heierarchy
    url = "http://127.0.0.1:8000/api/sections/"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"

    resp = requests.get(url, headers=headers)

    all_my_data = resp.json()['results']
    sections_tree = {}
    for list_item in all_my_data:
        sections_tree[list_item['name']] = list_item['subsections']

    context = {
        'sectionOptions': sections_tree
    }
    if request.method == 'POST':
        form = VariableHierarchyFormNew(request.POST)
        if form.is_valid():
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
                new_var_hierarchy = VariableHierarchy(
                    name=variable_name, section=section_name, subsection=subsection_name, is_verified=is_verified)
                new_var_hierarchy.save()
                print('Valid Foooooooooooorm: \n\n',)
                # print(data)
                my_message = f'''You <h5> Dadad </h5> successfully submitted {variable_name} to: {section_name} >  {subsection_name}'''
                messages.success(request, my_message)
                return HttpResponseRedirect(reverse('variablehierarchysetting'))
            else:
                messages.warning(request, 'Form submission unssuccessful, section and subsection do not match.')
                #return render(request, 'core/variablehierarchy.html', {'form': VariableHierarchyFormNew()})

        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)

    else:
        form = VariableHierarchyFormNew()
    context['form'] = form
    context['variable_list'] = list(my_vars_tuple)
    #context['SuccessMessage'] = "Done Perfectly."
    return render(request, 'core/variablehierarchy.html', context)


def varshierformset(request):
    # lets see
    all_vars = dic_of_all_vars()
    VarHierFormSet = formset_factory(
        VariableHierarchyForm, extra=0)
    if request.method == 'POST':
        formset = VarHierFormSet(request.POST, request.FILES)
        if formset.is_valid():
            for n in range(len(formset)):
                data = request.POST
                print(data.keys())
                name = data[f'form-{n}-name']
                is_verified_str = data[f'form-{n}-is_verified']
                if is_verified_str == 'on':
                    is_verified = True
                else:
                    is_verified = False
                section = Section.objects.get(pk=data[f'form-{n}-section'])
                subsection = Subsection.objects.get(
                    pk=data[f'form-{n}-subsection'])
                new_var_hierarchy = VariableHierarchy(
                    name=name, section=section, subsection=subsection, is_verified=is_verified)
                new_var_hierarchy.save()
                print(data)

        else:
            print('BAAAAAAD')
    else:
        my_initials = [
            {'name': key
             # 'is_verified': VariableHierarchy.objects.filter(name=key)[0].is_verified
             } for key in list(all_vars.keys())]
        formset = VarHierFormSet(initial=my_initials)
        print(my_initials)
    return render(request, 'core/varshiers.html',  {'formset': formset, },)


def dynamicdropdown(request):
    # Let's create aa API serializer for section and subsection heierarchy
    url = "http://127.0.0.1:8000/api/sections/"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"

    resp = requests.get(url, headers=headers)

    all_my_data = resp.json()['results']
    sections_tree = {}
    for list_item in all_my_data:
        sections_tree[list_item['name']] = list_item['subsections']

    context = {
        'sectionOptions': sections_tree
    }
    return render(request, 'core/dynamicdropdown.html', context=context)
