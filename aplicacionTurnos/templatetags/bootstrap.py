
from django import template

register = template.Library()

@register.inclusion_tag('aplicacionTurnos/form_input.html')
def form_input(elem, attrs=''):
    return {'elem':elem, 'attrs':attrs}
