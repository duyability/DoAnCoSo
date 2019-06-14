from django import forms
from django.http import request
from django.shortcuts import render

from vlance.models import Job, Applicant, JobPartTime


# From viec theo du an - Pham Minh Duc
class CreateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('user', 'created_at', 'slug')

    def is_valid(self):
        valid = super(CreateJobForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        job = super(CreateJobForm, self).save(commit=False)
        if commit:
            job.save()
        return job

# From viec lam part time , ban thoi gian  by Pham Minh Duc
class PartTimeFrom(forms.ModelForm):
    class Meta:
        model = JobPartTime
        exclude = ('user', 'created_at', 'slug')

    def is_valid(self):
        valid = super(PartTimeFrom, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        job = super(PartTimeFrom, self).save(commit=False)
        if commit:
            job.save()
        return job

class ApplyJobForm(forms.ModelForm):
    class Meta:
        model = Applicant
        exclude = ('user', 'created_at')

    def is_valid(self):
        valid = super(ApplyJobForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        job = super(ApplyJobForm, self).save(commit=False)
        if commit:
            job.save()
        return job


