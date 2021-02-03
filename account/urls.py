from django.urls import path

from . import views

app_name="account"
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signupAdmin/', views.signupAdmin, name='signupAdmin'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.Index, name='Index'),
    path('showuserinfo', views.showuserinfo, name='showuserinfo'),
]