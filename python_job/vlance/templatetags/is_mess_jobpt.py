from django import template

from vlance.models import GuiTBChapNhanJobpt

register = template.Library()


@register.simple_tag(name='is_mess_jobpt')
def is_mess_jobpt(cvonsite, user):
    mess = GuiTBChapNhanJobpt.objects.filter(cvonsite=cvonsite, user=user)
    if mess:
        return True
    else:
        return False
