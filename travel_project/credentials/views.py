from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def register(request):
    #fetching values from database
    if request.method=='POST':
        user1=request.POST['username']
        email=request.POST['email']
        name1=request.POST['firstname']
        name2=request.POST['lastname']
        passcode1=request.POST['pass1']
        passcode2=request.POST['pass2']
        if passcode1==passcode2:
            #checking username,email etc are exists in the database
            if User.objects.filter(username=user1).exists():
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register')
            elif User.objects.filter(first_name=name1).exists():
                messages.info(request,'first name taken')
                return redirect('register')
            elif User.objects.filter(last_name=name2).exists():
                messages.info(request,'last name taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=user1, email=email, first_name=name1, last_name=name2, password=passcode1)
                user.save()
                messages.info(request,'user created successfully')
                # print('user created')
                return redirect('login')
        else:
            messages.info(request,'password mismatch')
            return redirect('register')
        return redirect('/')
    return render(request,"reg.html")

def login(request):
    if request.method=='POST':
        user1=request.POST['username']
        passcode1=request.POST['pass1']
        user=auth.authenticate(username=user1, password=passcode1)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')