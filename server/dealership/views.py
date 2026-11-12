import requests
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.http import JsonResponse,HttpResponseBadRequest
from django.shortcuts import render,redirect
from django.views.decorators.http import require_http_methods
from .models import CarMake

def remote_json(path,default):
    try:
        r=requests.get(settings.DEALER_SERVICE_URL+path,timeout=4)
        r.raise_for_status()
        return r.json()
    except (requests.RequestException,ValueError):return default

def home(request):
    state=request.GET.get('state','')
    dealers=remote_json('/fetchDealers',[])
    if state: dealers=[d for d in dealers if d.get('state','').lower()==state.lower()]
    states=sorted(set(d.get('state','') for d in remote_json('/fetchDealers',[]) if d.get('state')))
    return render(request,'home.html',{'dealers':dealers,'states':states,'selected_state':state})

def about(request):return render(request,'about.html')
def contact(request):return render(request,'contact.html')

def signup(request):
    form=UserCreationForm(request.POST or None)
    if request.method=='POST' and form.is_valid():
        user=form.save(); login(request,user);return redirect('home')
    return render(request,'auth.html',{'form':form,'heading':'Create account','button':'Sign up'})

def signin(request):
    form=AuthenticationForm(request,request.POST or None)
    if request.method=='POST' and form.is_valid():
        login(request,form.get_user());return redirect('home')
    return render(request,'auth.html',{'form':form,'heading':'Welcome back','button':'Log in'})

@require_http_methods(['GET','POST'])
def signout(request):
    if request.method=='POST':logout(request);messages.success(request,'You have logged out.');return redirect('home')
    return render(request,'logout.html')

def dealer_page(request,dealer_id):
    dealer=remote_json(f'/fetchDealer/{dealer_id}',{})
    reviews=remote_json(f'/fetchReview/dealer/{dealer_id}',[])
    return render(request,'dealer.html',{'dealer':dealer,'reviews':reviews})

@login_required(login_url='login')
@require_http_methods(['GET','POST'])
def post_review(request,dealer_id):
    dealer=remote_json(f'/fetchDealer/{dealer_id}',{})
    if request.method=='POST':
        text=request.POST.get('review','').strip()
        if not text or len(text)>2000:
            messages.error(request,'Review must contain 1 to 2000 characters.')
        else:
            payload={'dealerId':dealer_id,'author':request.user.username,'review':text}
            try:
                r=requests.post(settings.DEALER_SERVICE_URL+'/insertReview',json=payload,timeout=5)
                r.raise_for_status();messages.success(request,'Your review has been posted.');return redirect('dealer',dealer_id=dealer_id)
            except requests.RequestException:messages.error(request,'Review service is unavailable.')
    return render(request,'post_review.html',{'dealer':dealer})

def dealers_api(request,state=None):
    dealers=remote_json('/fetchDealers',[])
    if state:dealers=[d for d in dealers if d.get('state','').lower()==state.lower()]
    return JsonResponse(dealers,safe=False)

def reviews_api(request,dealer_id):return JsonResponse(remote_json(f'/fetchReview/dealer/{dealer_id}',[]),safe=False)

def cars_api(request):
    return JsonResponse([{'make':m.name,'models':[{'name':c.name,'year':c.year,'category':c.category} for c in m.models.all()]} for m in CarMake.objects.prefetch_related('models')],safe=False)

def sentiment_api(request,text):
    try:
        r=requests.get(settings.SENTIMENT_SERVICE_URL+'/analyze/'+requests.utils.quote(text,safe=''),timeout=4)
        r.raise_for_status();return JsonResponse(r.json())
    except requests.RequestException:return JsonResponse({'error':'sentiment service unavailable'},status=503)
