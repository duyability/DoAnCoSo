from django import forms
from django.http import request
from django.shortcuts import render

from vlance.models import Job, Applicant, JobPartTime, CVonsite, GuiTBChapNhanJob, GuiTBChapNhanJobpt, CuocThi


# From viec theo du an - Pham Minh Duc
class CreateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('user', 'created_at', 'slug', 'filled')

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
        exclude = ('user', 'created_at', 'slug','filled')

    def is_valid(self):
        valid = super(PartTimeFrom, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        j = super(PartTimeFrom, self).save(commit=False)
        if commit:
            j.save()
        return j


# From Dang cuoc thi  by Pham Minh Duc
class CuocThiFrom(forms.ModelForm):
    class Meta:
        model = CuocThi
        exclude = ('user', 'created_at', 'slug','filled')

    def is_valid(self):
        valid = super(CuocThiFrom, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        c = super(CuocThiFrom, self).save(commit=False)
        if commit:
            c.save()
        return c


# ######### From gui bao gia ##############

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


# ######### From nop cv ##############

class ApplyCVForm(forms.ModelForm):
    class Meta:
        model = CVonsite
        exclude = ('user', 'created_at')

    def is_valid(self):
        valid = super(ApplyCVForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        jpt = super(ApplyCVForm, self).save(commit=False)
        if commit:
            jpt.save()
        return jpt


# ######### From nop cv ##############

class ChapnhanJob(forms.ModelForm):
    class Meta:
        model = GuiTBChapNhanJob
        exclude = ('user', 'created_at')

    def is_valid(self):
        valid = super(ChapnhanJob, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        t = super(ChapnhanJob, self).save(commit=False)
        if commit:
            t.save()
        return t


# ######### From nop cv pt ##############

class ChapnhanJobpt(forms.ModelForm):
    class Meta:
        model = GuiTBChapNhanJobpt
        exclude = ('user', 'created_at')

    def is_valid(self):
        valid = super(ChapnhanJobpt, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        t = super(ChapnhanJobpt, self).save(commit=False)
        if commit:
            t.save()
        return t
