import os
from django import template

register = template.Library()


@register.filter
def format_name(value):
    return value.replace('-', ' ')


