from datetime import datetime
import re
from django import template
register = template.Library()


@register.filter
def stars(count: int):
    return '⭐' * count


@register.filter
def date_converter(date: str):
    try:
        date_object = datetime.strptime(date, '%Y%m%dT%H%M%S.%fZ')
        return date_object.strftime('%d-%m-%Y %H:%M')
    except ValueError:
        return date


@register.filter
def split_camel_case(value):
    return ' '.join(re.sub('([A-Z][a-z]+)', r' \1', re.sub('([A-Z]+)', r' \1', value)).split()).capitalize()
