from django.shortcuts import render
from django.db import connection
from .models import Boss

def getBossLife(request):
    # sql = "select life from algoalgo.boss limit 1"

    try:
        curr_life = Boss.objects.all()[0]
        # cursor = connection.cursor()

        # sql_result = cursor.execute(sql)
        # result = cursor.fetchall()
        # curr_life = result[0][0]

        # connection.commit()
        # connection.close()

    except Exception as ex:
        raise ex

    return render(request, 'boss_life.html', {'curr_life': curr_life})
