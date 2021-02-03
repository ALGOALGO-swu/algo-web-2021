from django.shortcuts import render
from django.db import connection
from .models import MemberBoss
from .models import Boss

def getBossRank(request):
    # sql = "select discord_id, total_dmg from algoalgo.member_boss order by total_dmg DESC limit 5;"

    try:
        boss_rank = MemberBoss.objects.all().order_by('-total_dmg')[:5]
        curr_life = Boss.objects.all()[0]

        # cursor = connection.cursor()

        # sql_result = cursor.execute(sql)
        # result = cursor.fetchall()
        # boss_rank = result

        # connection.commit()
        # connection.close()

    except Exception as ex:
        raise ex

    return render(request, 'boss_rank.html', {'boss_rank': boss_rank, 'curr_life': curr_life})