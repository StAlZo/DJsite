from django import template
from car.models import *

register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.all()