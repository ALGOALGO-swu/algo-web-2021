from django.urls import path
#from member.views import base
from member.views import member


urlpatterns = [
    path('', member, name='member'),  
]
