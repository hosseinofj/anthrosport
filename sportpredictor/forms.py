from dataclasses import fields
from unicodedata import name
from django import forms
from .models import target
from django.db.models import Q




class get_Personal_information_form(forms.ModelForm):
    class Meta:
        model = target
        fields = ['name','gender','dateofbirth','nationality','Location','e_mail','tel']

    def save(self, commit: bool = ...):
        data = self.cleaned_data
        t_email = data['e_mail']
        t_tel = data['tel']
        if t_tel:
            q = target.objects.all().filter(Q(tel=t_tel) | Q(e_mail=t_email))
            print(q)
            if len(q)>0:
                return q[0]
        else:
            q = target.objects.all().filter(Q(e_mail=t_email))
            print(q)
            if len(q)>0:
                return q[0]

        super().save(commit)
        return self.instance


class get_height_form(forms.ModelForm):
    class meta:
        model = target
        fields = ['height']

    def save(self, commit: bool = ...):
        data = self.cleaned_data

        super().save(commit)
        return self.instance

class get_weight_form(forms.ModelForm):
    class meta:
        model = target
        fields = ['weight']

    def save(self, commit: bool = ...):
        data = self.cleaned_data

        super().save(commit)
        return self.instance

class get_armspan_form(forms.ModelForm):
    class meta:
        model = target
        fields = ['armspan']

    def save(self, commit: bool = ...):
        data = self.cleaned_data

        super().save(commit)
        return self.instance

class get_foot_length_form(forms.ModelForm):
    class meta:
        model = target
        fields = ['foot_length']

    def save(self, commit: bool = ...):
        data = self.cleaned_data

        super().save(commit)
        return self.instance

class get_one_hand_length_form(forms.ModelForm):
    class meta:
        model = target
        fields = ['one_hand_length']

    def save(self, commit: bool = ...):
        data = self.cleaned_data

        super().save(commit)
        return self.instance