from django import template

from vlance.models import BaiThi

register = template.Library()


@register.simple_tag(name='is_already_ct')
def is_already_ct(ct, user):
    baithi = BaiThi.objects.filter(ct=ct, user=user)
    if baithi:
        return True
    else:
        return False