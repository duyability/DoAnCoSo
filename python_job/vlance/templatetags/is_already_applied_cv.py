from django import template

from vlance.models import CVonsite

register = template.Library()


@register.simple_tag(name='is_already_applied_cv')
def is_already_applied_cv(jobpt, user):
    cvonsite = CVonsite.objects.filter(jobpt=jobpt, user=user)
    if cvonsite:
        return True
    else:
        return False