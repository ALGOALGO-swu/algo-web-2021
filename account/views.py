from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import addUserForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


# 메인 홈 
def Index (request):
    return render(request,'account/Index.html',None) 


# 일반 유저 용 회원가입
def signup(request):
    if request.method == "POST":
        form = addUserForm(request.POST)
        if form.is_valid():
            form.save() 
            username = form.cleaned_data.get('username') 
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  
            login(request, user)
            return HttpResponseRedirect('/account')
    else:
        form = addUserForm()
    return render(request, 'account/signup.html', {'form': form})


# admin 용 회원가입
def signupAdmin(request):
    if request.method == "POST":
        form = addUserForm(request.POST)   
        if form.is_valid():
            check_staff= form.save(commit=False)
            check_staff.is_admin = True  # admin 옵션 추가  
            form.save()

            web_id = form.cleaned_data.get('web_id')  
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(web_id=web_id, password=raw_password) 
            login(request, user) 
            return HttpResponseRedirect('/account')
    else:
        form = addUserForm()
    return render(request, 'account/signupAdmin.html', {'form': form})



#로그인
def login_view(request): 
    if request.user.is_authenticated:
        return HttpResponseRedirect('/account/Index')
    
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'account/login.html', {'form': form})
    
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                print(user)
                login(request, user) 
                return HttpResponseRedirect('/account')
            else:
                print('User not found')
        else:
            return render(request, 'account/login.html', {'form': form})
    


# 로그아웃 
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/account')
