from django.contrib.sites.shortcuts import get_current_site
from seshat.apps.core.forms import SignUpForm
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

from django.core.mail import EmailMessage

import json
from django.views import generic
from django.urls import reverse, reverse_lazy

from .models import Polity


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
