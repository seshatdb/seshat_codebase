from django import template

register = template.Library()

@register.filter
def get_attributes(obj):
    return vars(obj)