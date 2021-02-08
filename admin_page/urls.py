from django.urls import path
from . import views

urlpatterns = [
    # 맵 별 인원 분포
    path('', views.show_info, name='info'),
]