#from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import views
from .models import *
from .forms import *


# Create your views here.

def logout(request):
    try:
        del request.session['user_id_session_login']
    except:
        pass
    else:
        return HttpResponse("<strong>You are logged out.</strong>")

def lfihome(request):
    if not request.session.has_key('user_id_session_login'):
        return redirect('login')
    li = LostItem.objects.all()

    total_lost_items = li.count()

    fi = FoundItem.objects.all()

    total_found_items = fi.count()
    context = {
        'uli_count': total_lost_items, 'ufi_count': total_found_items,
    }
    return render(request, 'lfi/lfidashboard.html', context)


def lostreport(request):
    if not request.session.has_key('user_id_session_login'):
        return redirect('login')
    form = LostForm()
    if request.method == 'POST':
        # print('Printing_POST :',request.POST)
        form = LostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('LFI/lostentryadded')
    context = {'form': form}
    return render(request, 'lfi/lostreport.html', context)


def foundreport(request):
    if not request.session.has_key('user_id_session_login'):
        return redirect('login')
    if not request.session.has_key('user_id_session_login'):
        return redirect('login')
    form = FoundForm()
    if request.method == 'POST':
        # print('Printing_POST :',request.POST)
        form = FoundForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('founditemadded')
    context = {'form': form}
    return render(request, 'lfi/foundreport.html', context)


def lostentryadded(request):
    return render(request, 'lfi/lostentryadded.html')


def founditemadded(request):
    return render(request, 'lfi/founditemadded.html')


def matchingitems(request):
    return HttpResponse('match Page work in progress >/ >/ >/')


def userfoundentries(request):
    if request.GET.get('fid'):
        key = request.GET.get('fid')
        items = FoundItem.objects.filter(id=key)
        return render(request, 'lfi/userfoundentries.html', {'itemsfound': items})
    else:
        items = FoundItem.objects.filter(student="1")
        return render(request, 'lfi/userfoundentries.html', {'items': items})


def userslostentries(request):
    items = LostItem.objects.filter(student="2")
    return render(request, 'lfi/userslostentries.html', {'items': items})

# Create your views here.


def lostreportdelete(request,pk):
    report = LostItem.objects.get(id=pk)
    if request.method == "POST":
        report.delete()
        return redirect('lostentryadded')
    context = { 'report':report}
    return render(request,'lfi/userslostentries.html',context)


def foundreportdelete(request, pk):
    report = FoundItem.objects.get(id=pk)
    if request.method == "POST":
        report.delete()
        return redirect('founditemadded')
    context = {'report': report}
    return render(request, 'lfi/usersfoundentries.html', context)


def lostreportupdate(request,pk):
    report = LostItem.objects.get(id=pk)
    form = LostForm(instance = report)
    if request.method == 'POST':
        form = LostForm(request.POST, instance=report)
        if form.is_valid():
            form.save()
            return redirect('userslostentries')
    context = {'form': form}
    return render(request, 'lfi/lostreport.html', context)


def foundreportupdate(request,pk):
    report = FoundItem.objects.get(id=pk)
    form = FoundForm(instance = report)
    if request.method == 'POST':
        form = FoundForm(request.POST, instance=report)
        if form.is_valid():
            form.save()
            return redirect('usersfoundentries')
    context = {'form': form}
    return render(request, 'lfi/foundreport.html', context)