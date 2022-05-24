from seshat.apps.core.models import Polity
from seshat.apps.crisisdb.models import *
import django.apps

from django.contrib.contenttypes.models import ContentType


def list_of_all_Polities():
    '''
    returns all the polity names in the database.
    '''
    all_pols = Polity.objects.all()
    pol_names = []
    for pol in all_pols:
        pol_names.append(pol.name)

    return(pol_names)


def dic_of_all_vars():
    myvars = django.apps.apps.get_models()
    my_vars = {
        'total_tax': 'Total Tax',
        'salt_tax': 'Salt Tax',
        'total_revenue': 'Total Revenue',
    }
    my_vars_2 = {}
    for ct in ContentType.objects.all():
        m = ct.model_class()
        if m.__module__ == "seshat.apps.crisisdb.models":
            app_name = m.__module__.split('.')[-2] + '_'
            better_key = app_name + m.__name__
            better_value = m.__name__.replace('_', ' ')
            my_vars[better_key] = better_value
            print(better_key, ': ', better_value)
            # print(f"{m.__module__}.{m.__name__}\t{m._default_manager.count()}")
    return (my_vars)


def dic_of_all_vars_in_sections():
    my_vars = {
        'finances': {
            'total_tax': 'Total Tax',
            'salt_tax': 'Salt Tax',
            'total_revenue': 'Total Revenue',
        },
        'goodies': {'bad_boy': 'chips',
                    'worse_boy': 'cookie eater'

                    },
    }
    return (my_vars)


def adder(a, b):
    print(a+b)
