from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from account.models import Algo_User


# 회원가입 폼
class addUserForm(UserCreationForm):  
    class Meta:
        model = Algo_User
        fields =['web_id','discord_id', 'student_id', 'baekjoon_id','name','email']