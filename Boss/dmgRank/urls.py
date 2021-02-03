from django.urls import path
from . import views

urlpatterns = [
    path('', views.getBossRank, name='getBossRank'),
]