from django import template

from vlance.models import GuiTBChapNhanJob

register = template.Library()


@register.simple_tag(name='is_mess_job')
def is_mess_job(applicant, user):
    mess = GuiTBChapNhanJob.objects.filter(applicant=applicant, user=user)
    if mess:
        return True
    else:
        return False
