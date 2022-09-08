from django.shortcuts import render,redirect
from .forms import get_Personal_information_form,get_height_form,get_weight_form,get_armspan_form,get_foot_length_form,get_one_hand_length_form,get_shoulder_size_form
from .models import target
# Create your views here.
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
            return redirect("result")

    else:
        form = get_shoulder_size_form()

    return render(request,'sportpredictor/get_param.html',{"target":tr.name,'form':form})


def take_result(request):
    target_id = request.session.get('target')
    tr = target.objects.get(pk = target_id)


    return render(request,'sportpredictor/result.html',{"target":tr})


    