<<<<<<< HEAD
=======

>>>>>>> 09fa0cbb645e2337055e3dfa6e8fe974e23424e6
from django import template

register = template.Library()

<<<<<<< HEAD
@register.inclusion_tag('../templates/aplicacionTurnos/form_input.html')
=======
@register.inclusion_tag('aplicacionTurnos/form_input.html')
>>>>>>> 09fa0cbb645e2337055e3dfa6e8fe974e23424e6
def form_input(elem, attrs=''):
    return {'elem':elem, 'attrs':attrs}
