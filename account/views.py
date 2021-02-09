from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect, Http404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from .forms import addUserForm
from .models import Algo_User, Member


# 메인 홈 
def Index (request):
    return render(request,'account/Index.html',None) 


# 일반 유저 회원가입
def signup(request):
    if request.method == "POST":
        form = addUserForm(request.POST)
        if form.is_valid():
            form.save() 
            web_id = form.cleaned_data.get('web_id')  
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(web_id=web_id, password=raw_password) 
            login(request, user) 
            return HttpResponseRedirect('/account')
    else:
        form = addUserForm()
    return render(request, 'account/signup.html', {'form': form})


# admin(운영진) 회원가입
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



# 로그인
def login_view(request): 
    if request.user.is_authenticated:
        return HttpResponseRedirect('/account')
    
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
                #print(user)
                login(request, user) 
                request.session['user'] = user.web_id  #web_id를 값으로 세션 생성 
                return HttpResponseRedirect('/account')
            else:
                print('User not found')
        else:
            return render(request, 'account/login.html', {'form': form})
    


# 로그아웃 
def logout_view(request):
    if request.session.get('user'):
        del(request.session['user'])
    logout(request)
    return HttpResponseRedirect('/account')


# 사용자 정보 조회
def showuserinfo(request):
    if not request.session.get('user'): 
        return redirect('/account/login')
        
    if request.method =='GET':
        try:
            user_web_id=request.session.get('user')
                   
            if Algo_User.objects.filter(web_id=user_web_id).exists() :
                algo_user=Algo_User.objects.get(web_id=user_web_id)
                discord_id = algo_user.discord_id

                if Member.objects.filter(discord_id=discord_id).exists(): 
                    member=Member.objects.get(discord_id=discord_id)
                    context={'algo_user' : algo_user, 'member': member}

        except algo_user.DoesNotExist: 
                raise Http404("member does not exist")

        return render(request, 'account/showuserinfo.html',context)  


          