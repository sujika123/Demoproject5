from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from demoapp.forms import LoginForm, userloginform, eventaddform
from demoapp.models import userlogin, addevent


# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    form = LoginForm()
    form1 = userloginform()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        form1 = userloginform(request.POST,request.FILES)
        if form.is_valid() and form1.is_valid():
            user = form.save(commit=False)
            user.is_user = True
            user.save()
            tcr = form1.save(commit=False)
            tcr.user = user
            tcr.save()
            return redirect("loginview")
    return render(request,'registration.html',{'form':form,'form1':form1})

def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password=password)
        if user is not None and user.is_staff:
            login(request,user)
            return redirect('adminhome')
        if user is not None and user.is_user:
            login(request,user)
            return redirect('userhome')
        else:
            messages.info(request,'Invalid credentials')
    return render(request,'login.html')

def adminhome(request):
    return render(request,'adminhome.html')

def userhome(request):
    return render(request,'userhome.html')

def profileview(request):
    u= request.user
    data = userlogin.objects.filter(user=u)
    print(data)
    return render(request,'profileview.html',{'data':data})

def profileupdate(request,id):
    user = userlogin.objects.get(id=id)
    form = userloginform(instance=user)
    if request.method == 'POST':
        form = userloginform(request.POST or None,request.FILES,instance=user or None)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect('profileview')
    return render(request,'profileupdate.html',{'form':form})

def addeventuser(request):
    u = request.user
    form = eventaddform()
    if request.method == 'POST':
        form = eventaddform(request.POST,request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            obj.save()
        return redirect('viewevent')
    return render(request,'addevent.html',{'form':form})

def viewevent(request):
    u = request.user
    data = addevent.objects.filter(user=u)
    return render(request,'viewevent.html',{'data':data})

# def deleteevent(request,id):
#     event = addevent.objects.get(id=id)
#     event.delete()
#     return redirect('viewevent')

def eventdelete(request,id):
    data=addevent.objects.get(id=id)
    data.delete()
    return redirect('viewevent')

def eventupdate(request,id):
    user = addevent.objects.get(id=id)
    form = eventaddform(instance=user)
    if request.method == 'POST':
        form = eventaddform(request.POST or None,request.FILES,instance=user or None)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect('viewevent')
    return render(request,'eventupdate.html',{'form':form})

def userview(request):
    data = userlogin.objects.all()
    print(data)
    return render(request,'userview.html',{'data':data})