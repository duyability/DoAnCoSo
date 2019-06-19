import django_filters
from django import forms
from vlance.models import Job, NganhNghe


class JobFilter(django_filters.FilterSet):

    Nganh_Nghe = django_filters.ModelChoiceFilter(queryset=NganhNghe.objects.all(),
                                                      widget=forms.Select)
    class Meta:
        model = Job
        fields = ['title', 'description', 'Nganh_Nghe','Thanh_Pho',]