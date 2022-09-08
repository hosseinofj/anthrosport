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
    class Meta:
        model = target
        fields = ['height']

    def save(self, commit: bool = ...):
        self.instance = target.objects.get(pk=self.data['tr'])
        self.instance.height = self.cleaned_data['height']
    
        super().save(commit)
        return self.instance

class get_weight_form(forms.ModelForm):
    class Meta:
        model = target
        fields = ['weight']

    def save(self, commit: bool = ...):
        self.instance = target.objects.get(pk=self.data['tr'])
        self.instance.weight = self.cleaned_data['weight']

        super().save(commit)
        return self.instance

class get_armspan_form(forms.ModelForm):
    class Meta:
        model = target
        fields = ['armspan']

    def save(self, commit: bool = ...):
        self.instance = target.objects.get(pk=self.data['tr'])
        self.instance.armspan = self.cleaned_data['armspan']

        super().save(commit)
        return self.instance

class get_foot_length_form(forms.ModelForm):
    class Meta:
        model = target
        fields = ['foot_length']

    def save(self, commit: bool = ...):
        self.instance = target.objects.get(pk=self.data['tr'])
        self.instance.foot_length = self.cleaned_data['foot_length']

        super().save(commit)
        return self.instance

class get_one_hand_length_form(forms.ModelForm):
    class Meta:
        model = target
        fields = ['one_hand_length']

    def save(self, commit: bool = ...):
        self.instance = target.objects.get(pk=self.data['tr'])
        self.instance.one_hand_length = self.cleaned_data['one_hand_length']

        super().save(commit)
        return self.instance

class get_shoulder_size_form(forms.ModelForm):
    class Meta:
        model = target
        fields = ['shoulder_size']

    def save(self, commit: bool = ...):
        self.instance = target.objects.get(pk=self.data['tr'])
        self.instance.shoulder_size = self.cleaned_data['shoulder_size']

        super().save(commit)
        return self.instance