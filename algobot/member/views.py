from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
# Create your views here.
from .models import Map
from .models import Member

def member(request):
    
    sql = "select discord_id, daily_steps from algoalgo.member order by daily_steps DESC limit 5;"
    
    try:
        cursor = connection.cursor()

        sql_result = cursor.execute(sql)
        result = cursor.fetchall()
        mem = result

        connection.commit()
        connection.close()
        
    except Exception as ex:
        raise ex
    return render(request, 'm_result.html', {'mem':mem})   