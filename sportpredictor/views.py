from cmath import nan
from django.shortcuts import render,redirect
from .forms import get_Personal_information_form,get_height_form,get_weight_form,get_armspan_form,get_foot_length_form,get_one_hand_length_form,get_shoulder_size_form
from .forms import get_fat_form,get_back_flexibility_form,get_shoulder_flexibility_form,get_finger_ratio_2_4_form,get_super_test_form
from .models import target
from .Calculator import Param_calc,sport_predictor,medians_adding,recalc_height_to_age_medians,recalc_armspan_medians,recalc_foot_length_to_age_medians,recalc_one_hand_length_to_age_medians,recalc_shoulder_size_medians,recalc_fat_medians,recalc_back_flexibility_medians,recalc_shoulder_flexibility_medians,recalc_finger_ratio_medians


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

    return render(request,'sportpredictor/get_param.html',{"target":tr.name,'form':form})


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

    return render(request,'sportpredictor/get_param.html',{"target":tr.name,'form':form})

    
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

    return render(request,'sportpredictor/get_param.html',{"target":tr.name,'form':form})

    
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

    return render(request,'sportpredictor/get_param.html',{"target":tr.name,'form':form})

    
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

    return render(request,'sportpredictor/get_param.html',{"target":tr.name,'form':form})

    
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

    return render(request,'sportpredictor/get_param.html',{"target":tr.name,'form':form})

     
def get_fat(request):
    target_id = request.session.get('target')
    tr = target.objects.get(pk = target_id)
    if request.method == 'POST':
        data = request.POST.copy()
        data['tr'] = target_id
        form = get_fat_form(data)
        if form.is_valid():
            targeted = form.save()
            # request.session['target'] = targeted.pk
            return redirect("back_flexibility")

    else:
        form = get_fat_form()

    return render(request,'sportpredictor/get_param.html',{"target":tr.name,'form':form})

    
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

    return render(request,'sportpredictor/get_param.html',{"target":tr.name,'form':form})


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

    return render(request,'sportpredictor/get_param.html',{"target":tr.name,'form':form})


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

    return render(request,'sportpredictor/get_param.html',{"target":tr.name,'form':form})


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

    return render(request,'sportpredictor/get_param.html',{"target":tr.name,'form':form})




def take_result(request):
    target_id = request.session.get('target')
    tr = target.objects.get(pk = target_id)

    params = Param_calc(tr)

    five_sports = sport_predictor(params)

    medians_adding(params)

    return render(request,'sportpredictor/result.html',{"target":tr,"params":params,"sports":five_sports})


    

def do(request):

    recalc_height_to_age_medians()
    recalc_armspan_medians()
    recalc_foot_length_to_age_medians()
    recalc_one_hand_length_to_age_medians()
    recalc_shoulder_size_medians()
    recalc_fat_medians()
    recalc_back_flexibility_medians()
    recalc_shoulder_flexibility_medians()
    recalc_finger_ratio_medians()

    return render(request,'sportpredictor/done.html')