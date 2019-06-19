from django import template
from vlance.models import *
from search.forms import *
from django.http import HttpResponseRedirect

from search.forms import JobFilterForm
register = template.Library()

@register.inclusion_tag("tags/job_filter.html")
def job_filter(request):
    filter_form = JobFilterForm(request.GET)
    return {'filter_form': filter_form}
