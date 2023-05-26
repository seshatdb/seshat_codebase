from django import template
import re
register = template.Library()


@register.filter
def zip_lists(a, b):
    return zip(a, b)

@register.filter
def get_columns_with_value(instance, value):
    return instance.get_columns_with_value(value)

@register.filter
def get_columns_with_value_dic(instance, value):
    return instance.get_columns_with_value_dic(value)

@register.filter
def replace_underscore_and_capitalize(value):
    value = value.replace('_', ' ')
    return value.title()

@register.filter
def make_references_look_nicer(value):
    value = value.replace("'", "&rsquo;")
    pattern = r'§REF_MJD_BEN§(.*?)§REF_MJD_BEN§'
    replacement = r"""<sup>
        <span type="button"  tabindex="0" data-bs-toggle="popover" data-bs-html="true" data-bs-trigger="focus" data-bs-content='<b>Citation: </b>\1'>&#x1F4D4;
        </span>
    </sup>
    """
    #replacement = r'XYZ_\1_XYZ'
    new_string = re.sub(pattern, replacement, value)
    return new_string