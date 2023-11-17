from django import template

register = template.Library()

@register.filter
def get_attributes(obj):
    return vars(obj)

@register.filter
def zip_lists(a, b):
    return zip(a, b)

