from random import randint

from django.shortcuts import render
from django.contrib import messages

from user.models import registrationmodel, uploadmodel

def adminhome(request):
    return render(request,'admin/adminhome.html')

def adminlogin(request):
    return render(request,'admin/adminlogin.html')

def adminloginaction(request):
    if request.method == "POST":
        if request.method == "POST":
            login = request.POST.get('username')
            print(login)
            pswd = request.POST.get('password')
            if login == 'admin' and pswd == 'admin':
                return render(request,'admin/adminhome.html')
            else:
                messages.success(request, 'Invalid user id and password')
    #messages.success(request, 'Invalid user id and password')
    return render(request,'admin/adminlogin.html')

def logout(request):
    return render(request,'index.html')

def userdetails(request):
    userdata = registrationmodel.objects.all()
    return render(request,'admin/viewuserdetails.html', {'object': userdata})

def userfiles(request):
    userfile = uploadmodel.objects.all()
    return render(request, 'admin/viewfiles.html',{'object': userfile})

def activateuser(request):
    if request.method=='GET':
        usid = request.GET.get('usid')
        authkey = random_with_N_digits(8)
        status = 'activated'
        print("USID = ",usid,authkey,status)
        registrationmodel.objects.filter(id=usid).update(authkey=authkey , status=status)
        userdata = registrationmodel.objects.all()
        return render(request,'admin/viewuserdetails.html',{'object':userdata})

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)