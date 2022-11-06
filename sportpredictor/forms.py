# from dataclasses import fields
# from unicodedata import name
from django import forms
from .models import target
from django.db.models import Q
from .Calculator import fat_calcer



class get_Personal_information_form(forms.ModelForm):
    class Meta:
        model = target
        fields = ['name','gender','age','nationality','Location','e_mail','tel']


    def save(self, commit: bool = ...):
        data = self.cleaned_data
        t_email = data['e_mail']
        t_tel = data['tel']
        
        if t_tel:
            q = target.objects.all().filter(Q(tel=t_tel) | Q(e_mail=t_email))
            if len(q)>0:
                if t_email == "":
                    print("empty Email")
                return q[0]
        else:
            q = target.objects.all().filter(Q(e_mail=t_email))
            if len(q)>0:
                # return q[0]
                pass
        self.instance.save()
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

class get_fat_form_male(forms.ModelForm):
    class Meta:
        model = target
        fields = ['waist','neck']

    def save(self, commit: bool = ...):
        self.instance = target.objects.get(pk=self.data['tr'])
        self.instance.waist = self.cleaned_data['waist']
        self.instance.neck = self.cleaned_data['neck']
        # self.instance.hip = self.cleaned_data['hip']
        self.instance.fat = fat_calcer(self.cleaned_data['waist'],self.cleaned_data['neck'],self.instance.height,0,self.instance.gender)

        super().save(commit)
        return self.instance

class get_fat_form_female(forms.ModelForm):
    class Meta:
        model = target
        fields = ['waist','neck','hip']

    def save(self, commit: bool = ...):
        self.instance = target.objects.get(pk=self.data['tr'])
        self.instance.waist = self.cleaned_data['waist']
        self.instance.neck = self.cleaned_data['neck']
        self.instance.hip = self.cleaned_data['hip']
        self.instance.fat = fat_calcer(self.cleaned_data['waist'],self.cleaned_data['neck'],self.instance.height,self.cleaned_data['hip'],self.instance.gender)

        super().save(commit)
        return self.instance
     
class get_back_flexibility_form(forms.ModelForm):
    class Meta:
        model = target
        fields = ['back_flexibility']

    def save(self, commit: bool = ...):
        self.instance = target.objects.get(pk=self.data['tr'])
        self.instance.back_flexibility = self.cleaned_data['back_flexibility']

        super().save(commit)
        return self.instance

class get_shoulder_flexibility_form(forms.ModelForm):
    class Meta:
        model = target
        fields = ['shoulder_flexibility']

    def save(self, commit: bool = ...):
        self.instance = target.objects.get(pk=self.data['tr'])
        self.instance.shoulder_flexibility = self.cleaned_data['shoulder_flexibility']

        super().save(commit)
        return self.instance

class get_finger_ratio_2_4_form(forms.ModelForm):
    class Meta:
        model = target
        fields = ['finger_2','finger_4']

    def save(self, commit: bool = ...):
        self.instance = target.objects.get(pk=self.data['tr'])
        self.instance.finger_2 = self.cleaned_data['finger_2']
        self.instance.finger_4 = self.cleaned_data['finger_4']

        super().save(commit)
        return self.instance

class get_super_test_form(forms.ModelForm):
    class Meta:
        model = target
        fields = ['super_test_1','super_test_2','super_test_3']

    def save(self, commit: bool = ...):
        self.instance = target.objects.get(pk=self.data['tr'])
        self.instance.super_test_1 = self.cleaned_data['super_test_1']
        self.instance.super_test_2 = self.cleaned_data['super_test_2']
        self.instance.super_test_3 = self.cleaned_data['super_test_3']

        super().save(commit)
        return self.instance




















