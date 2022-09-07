from django.shortcuts import render,redirect
from .forms import get_Personal_information_form
from .models import target
# Create your views here.
def index(request):

    return render(request,'sportpredictor/index.html')


def get_information(request):
    if request.method == 'POST':
        form = get_Personal_information_form(request.POST)
        if form.is_valid():
            targeted = form.save()
            # request.session['target'] = target
            request.session['target'] = targeted.pk
            return redirect("height")

    else:
        form = get_Personal_information_form()

    return render(request, 'sportpredictor/personalinformation.html', {'form': form})



def get_height(request):
    target_id = request.session.get('target')
    tr = target.objects.get(pk = target_id)
    return render(request,'sportpredictor/height.html',{"target":tr.name})