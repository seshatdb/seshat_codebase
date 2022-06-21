from seshat.apps.core.models import Polity, Variablehierarchy
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
    # my_vars = {
    #     'total_tax': 'Total Tax',
    #     'salt_tax': 'Salt Tax',
    #     'total_revenue': 'Total Revenue',
    # }
    my_vars = {}
    my_vars_2 = {}
    for ct in ContentType.objects.all():
        m = ct.model_class()
        if m.__module__ == "seshat.apps.crisisdb.models":
            app_name = m.__module__.split('.')[-2] + '_'
            better_key = app_name + m.__name__
            better_value = m.__name__.replace('_', ' ')
            my_vars[better_key] = better_value
            my_vars[better_key] = [better_value, m._default_manager.count()]
            #print(better_key, ': ', better_value)
            # print(f"{m.__module__}.{m.__name__}\t{m._default_manager.count()}")
    return (my_vars)


def dic_of_all_vars_with_varhier():
    myvars = django.apps.apps.get_models()
    # my_vars = {
    #     'total_tax': 'Total Tax',
    #     'salt_tax': 'Salt Tax',
    #     'total_revenue': 'Total Revenue',
    # }
    my_vars = {}
    my_vars_2 = {}
    my_secs = {}
    all_var_hiers = Variablehierarchy.objects.all()
    for varhier in all_var_hiers:
        var_subsec = str(varhier.subsection.name).replace(' ', '_')
        var_sec = str(varhier.section.name).replace(' ', '_')
        if var_sec not in my_secs.keys():
            my_secs[var_sec] = {var_subsec:{}}
        else:
            if var_subsec not in my_secs[var_sec].keys():
                my_secs[var_sec][var_subsec] = {}
            else:
                pass 
    for ct in ContentType.objects.all():
        m = ct.model_class()
        if m.__module__ == "seshat.apps.crisisdb.models":
            app_name = m.__module__.split('.')[-2] + '_'
            better_key = app_name + m.__name__
            best_key = better_key.replace(' ', '_')[9:]
            better_value = m.__name__.replace('_', ' ')
            this_varhier = Variablehierarchy.objects.get(name=best_key)
            this_varhier_sec = str(this_varhier.section.name).replace(' ', '_')
            this_varhier_subsec = str(this_varhier.subsection.name).replace(' ', '_')
            my_secs[this_varhier_sec][this_varhier_subsec][best_key] = [better_value, m._default_manager.count()]
    return (my_secs)


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


def section_dic_extractor():
    from seshat.apps.core.models import Section
    my_list = Section.objects.all()
    dic_to_be_returned = {}
    for item in list(my_list):
        dic_to_be_returned[item.name] = item.id
    
    print(dic_to_be_returned)
    return dic_to_be_returned

def subsection_dic_extractor():
    from seshat.apps.core.models import Subsection
    my_list = Subsection.objects.all()
    dic_to_be_returned = {}
    for item in list(my_list):
        dic_to_be_returned[item.name] = item.id
    
    print(dic_to_be_returned)
    return dic_to_be_returned


# def test_multi_select():
#     my_secs = {}
#     all_var_hiers = Variablehierarchy.objects.all()
#     for varhier in all_var_hiers:
#         var_subsec = str(varhier.subsection.name).replace(' ', '_')
#         var_sec = str(varhier.section.name).replace(' ', '_')
#         if var_sec not in my_secs.keys():
#             my_secs[var_sec] = {var_subsec:{}}
#         else:
#             if var_subsec not in my_secs[var_sec].keys():
#                 my_secs[var_sec][var_subsec] = {}
#             else:
#                 pass
#     print(all_var_hiers)
#     print(my_secs)

#     for ct in ContentType.objects.all():
#         m = ct.model_class()
#         if m.__module__ == "seshat.apps.crisisdb.models":
#             app_name = m.__module__.split('.')[-2] + '_'
#             better_key = app_name + m.__name__
#             best_key = better_key.replace(' ', '_')[9:]
#             better_value = m.__name__.replace('_', ' ')
#             this_varhier = Variablehierarchy.objects.get(name=best_key)
#             this_varhier_sec = str(this_varhier.section.name).replace(' ', '_')
#             this_varhier_subsec = str(this_varhier.subsection.name).replace(' ', '_')
#             my_secs[this_varhier_sec][this_varhier_subsec][best_key] = [better_value, m._default_manager.count()]
#             print(app_name, better_key, best_key)
#     print('\n\n')
#     print(all_var_hiers)
#     print(my_secs)