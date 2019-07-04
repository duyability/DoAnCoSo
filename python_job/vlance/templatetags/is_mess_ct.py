from django import template
from django.http import request

from vlance.models import GuiTBChapNhanct

register = template.Library()


@register.simple_tag(name='is_mess_ct')
def is_mess_ct(bt, user):
    mess = GuiTBChapNhanct.objects.filter(bt=bt, user=user)
    if mess:

        return True
    else:
        return False
