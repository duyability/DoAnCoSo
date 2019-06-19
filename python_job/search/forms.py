from django import forms

from vlance.models import ThanhPho, NganhNghe


class JobFilterForm(forms.Form):
	Thanh_Pho__id = forms.ModelChoiceField(queryset=ThanhPho.objects.all(),widget=forms.Select(attrs={"class":"form-control","style":"width:220px"}))
	Nganh_Nghe__id = forms.ModelChoiceField(queryset=NganhNghe.objects.all(),widget=forms.Select(attrs={"class":"form-control","style":"width:220px"}))
