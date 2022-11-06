from cmath import nan
from django.shortcuts import render,redirect
from .forms import get_Personal_information_form,get_height_form,get_weight_form,get_armspan_form,get_foot_length_form,get_one_hand_length_form,get_shoulder_size_form
from .forms import get_fat_form_female,get_fat_form_male,get_back_flexibility_form,get_shoulder_flexibility_form,get_finger_ratio_2_4_form,get_super_test_form
from .models import target
from .Calculator import *#Param_calc,sport_predictor,medians_adding,recalc_height_to_age_medians,recalc_armspan_medians,recalc_foot_length_to_age_medians,recalc_one_hand_length_to_age_medians,recalc_shoulder_size_medians,recalc_fat_medians,recalc_back_flexibility_medians,recalc_shoulder_flexibility_medians,recalc_finger_ratio_medians,recalc_aeros_medians


def index(request):

    return render(request,'sportpredictor/index.html')


def get_information(request):
    if request.method == 'POST':
        form = get_Personal_information_form(request.POST)
        if form.is_valid():
            targeted = form.save()
            request.session['target'] = targeted.pk
            return redirect("height")
        else:
            print(form.errors)
    else:
        form = get_Personal_information_form()

    return render(request, 'sportpredictor/personalinformation.html', {'form': form})


def get_height(request):
    target_id = request.session.get('target')
    tr = target.objects.get(pk = target_id)
    if request.method == 'POST':
        data = request.POST.copy()
        data['tr'] = target_id
        form = get_height_form(data)
        if form.is_valid():
            targeted = form.save()
            # request.session['target'] = targeted.pk
            return redirect("weight")

    else:
        form = get_height_form()

    return render(request,'sportpredictor/get_param.html',{"target":tr.name,'form':form,"param":'height',"num":1})


def get_weight(request):
    target_id = request.session.get('target')
    tr = target.objects.get(pk = target_id)
    if request.method == 'POST':
        data = request.POST.copy()
        data['tr'] = target_id
        form = get_weight_form(data)
        if form.is_valid():
            targeted = form.save()
            # request.session['target'] = targeted.pk
            return redirect("armspan")

    else:
        form = get_weight_form()

    return render(request,'sportpredictor/get_param.html',{"target":tr.name,'form':form,"param":'weight',"num":2})

    
def get_armspan(request):
    target_id = request.session.get('target')
    tr = target.objects.get(pk = target_id)
    if request.method == 'POST':
        data = request.POST.copy()
        data['tr'] = target_id
        form = get_armspan_form(data)
        if form.is_valid():
            targeted = form.save()
            # request.session['target'] = targeted.pk
            return redirect("foot_length")

    else:
        form = get_armspan_form()

    return render(request,'sportpredictor/get_param.html',{"target":tr.name,'form':form,"param":'armspan',"num":3})

    
def get_foot_length(request):
    target_id = request.session.get('target')
    tr = target.objects.get(pk = target_id)
    if request.method == 'POST':
        data = request.POST.copy()
        data['tr'] = target_id
        form = get_foot_length_form(data)
        if form.is_valid():
            targeted = form.save()
            # request.session['target'] = targeted.pk
            return redirect("one_hand_length")

    else:
        form = get_foot_length_form()

    return render(request,'sportpredictor/get_param.html',{"target":tr.name,'form':form,"param":'foot',"num":4})

    
def get_one_hand_length(request):
    target_id = request.session.get('target')
    tr = target.objects.get(pk = target_id)
    if request.method == 'POST':
        data = request.POST.copy()
        data['tr'] = target_id
        form = get_one_hand_length_form(data)
        if form.is_valid():
            targeted = form.save()
            # request.session['target'] = targeted.pk
            return redirect("shoulder_size")

    else:
        form = get_one_hand_length_form()

    return render(request,'sportpredictor/get_param.html',{"target":tr.name,'form':form,"param":'hand',"num":5})

    
def get_shoulder_size(request):
    target_id = request.session.get('target')
    tr = target.objects.get(pk = target_id)
    if request.method == 'POST':
        data = request.POST.copy()
        data['tr'] = target_id
        form = get_shoulder_size_form(data)
        if form.is_valid():
            targeted = form.save()
            # request.session['target'] = targeted.pk
            return redirect("fat")

    else:
        form = get_shoulder_size_form()

    return render(request,'sportpredictor/get_param.html',{"target":tr.name,'form':form,"param":'shoulder',"num":6})

     
def get_fat(request):
    target_id = request.session.get('target')
    tr = target.objects.get(pk = target_id)
    if request.method == 'POST':
        data = request.POST.copy()
        data['tr'] = target_id
        if tr.gender == "M":
            form = get_fat_form_male(data)
        else:
            form = get_fat_form_female(data)

        if form.is_valid():
            targeted = form.save()
            # request.session['target'] = targeted.pk
            return redirect("back_flexibility")

    else:        
        if tr.gender == "M":
            form = get_fat_form_male()
        else:
            form = get_fat_form_female()


    return render(request,'sportpredictor/get_param.html',{"target":tr.name,'form':form,"param":'fat',"num":7})

    
def get_back_flexibility(request):
    target_id = request.session.get('target')
    tr = target.objects.get(pk = target_id)
    if request.method == 'POST':
        data = request.POST.copy()
        data['tr'] = target_id
        form = get_back_flexibility_form(data)
        if form.is_valid():
            targeted = form.save()
            # request.session['target'] = targeted.pk
            return redirect("shoulder_flexibility")

    else:
        form = get_back_flexibility_form()

    return render(request,'sportpredictor/get_param.html',{"target":tr.name,'form':form,"param":'back_f',"num":8})


def get_shoulder_flexibility(request):
    target_id = request.session.get('target')
    tr = target.objects.get(pk = target_id)
    if request.method == 'POST':
        data = request.POST.copy()
        data['tr'] = target_id
        form = get_shoulder_flexibility_form(data)
        if form.is_valid():
            targeted = form.save()
            # request.session['target'] = targeted.pk
            return redirect("finger_ratio_2_4")

    else:
        form = get_shoulder_flexibility_form()

    return render(request,'sportpredictor/get_param.html',{"target":tr.name,'form':form,"param":'sjoulder_f',"num":9})


def get_finger_ratio_2_4(request):
    target_id = request.session.get('target')
    tr = target.objects.get(pk = target_id)
    if request.method == 'POST':
        data = request.POST.copy()
        data['tr'] = target_id
        form = get_finger_ratio_2_4_form(data)
        if form.is_valid():
            targeted = form.save()
            # request.session['target'] = targeted.pk
            return redirect("super_test")

    else:
        form = get_finger_ratio_2_4_form()

    return render(request,'sportpredictor/get_param.html',{"target":tr.name,'form':form,"param":'finger',"num":10})


def get_super_test(request):
    target_id = request.session.get('target')
    tr = target.objects.get(pk = target_id)
    if request.method == 'POST':
        data = request.POST.copy()
        data['tr'] = target_id
        form = get_super_test_form(data)
        if form.is_valid():
            targeted = form.save()
            # request.session['target'] = targeted.pk
            return redirect("result")

    else:
        form = get_super_test_form()

    return render(request,'sportpredictor/get_param.html',{"target":tr.name,'form':form,"param":'super',"num":11})


def take_result(request):
    target_id = request.session.get('target')
   
    try:
        tr = target.objects.get(pk = target_id)
    except:
        tr = target.objects.get(pk = 3)

    sports_antro_sorted,log =antro_sport_selector(tr)
    
    sports = [  (sports_antro_sorted[-1][0],round(sports_antro_sorted[-1][1],1),sports_antro_sorted[-1][0]),
                (sports_antro_sorted[-2][0],round(sports_antro_sorted[-2][1],1),sports_antro_sorted[-2][0]),
                (sports_antro_sorted[-3][0],round(sports_antro_sorted[-3][1],1),sports_antro_sorted[-3][0]),
                (sports_antro_sorted[-4][0],round(sports_antro_sorted[-4][1],1),sports_antro_sorted[-4][0]),
                (sports_antro_sorted[-5][0],round(sports_antro_sorted[-5][1],1),sports_antro_sorted[-5][0]),
    ]
    
    
    contex ={"tr":tr,
            "sps":sports}

    return render(request,'sportpredictor/result.html',contex)


def do(request,pk):

    tr = target.objects.get(pk = pk)
    
    sports_antro_sorted,log =antro_sport_selector(tr)
    
    sports = [  (sports_antro_sorted[-1][0],round(sports_antro_sorted[-1][1],1),sports_antro_sorted[-1][0]),
                (sports_antro_sorted[-2][0],round(sports_antro_sorted[-2][1],1),sports_antro_sorted[-2][0]),
                (sports_antro_sorted[-3][0],round(sports_antro_sorted[-3][1],1),sports_antro_sorted[-3][0]),
                (sports_antro_sorted[-4][0],round(sports_antro_sorted[-4][1],1),sports_antro_sorted[-4][0]),
                (sports_antro_sorted[-5][0],round(sports_antro_sorted[-5][1],1),sports_antro_sorted[-5][0]),
    ]
    
    
    contex ={"tr":tr,
            "sps":sports}

    return render(request,'sportpredictor/result.html',contex)

def recalc_medians(request):
    log = recalc_height_to_age_medians()
    log+= recalc_armspan_medians()
    log+= recalc_foot_length_to_age_medians()
    log+= recalc_one_hand_length_to_age_medians()
    log+= recalc_shoulder_size_medians()


    # recalc_fat_medians()
    # recalc_back_flexibility_medians()
    # recalc_shoulder_flexibility_medians()
    # recalc_finger_ratio_medians()
    # recalc_aeros_medians()

    return render(request,'sportpredictor/done.html',context={"log":log})