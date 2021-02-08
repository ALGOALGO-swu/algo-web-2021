from django.shortcuts import render
from .models import Map, Member, Leaderboard
from django.db.models import OuterRef, Subquery

# Create your views here.


def show_info(request):
    maps = Map.objects.all()[:50]
    map_list = []

    # 맵 별 인원 분포
    for m in maps:
        member_list = Member.objects.filter(map_location=m.id)
        map_dict = {'id': m.id}
        members = []
        for member in member_list:
            members.append(member)
        map_dict['members'] = members
        map_list.append(map_dict)

    
    ### 시간별 리더보드 정보
    # 현재 DB에 있는 날짜 가져오기
    date_list = Leaderboard.objects.order_by('rank_datetime').dates('rank_datetime', 'day')

    # POST로 받은 날짜에 해당하는 순위 가져오기
    if request.method == 'POST':
        # 일별 랭킹
        selected_date = request.POST.get('selected_date')
        member_rank = Leaderboard.objects.filter(rank_datetime__contains=selected_date).order_by('rank_num', 'arrival_time')
        member_rank = Member.objects.filter(student_id__in=Subquery(member_rank.values('student_id')))

    else:
        # 전체 랭킹
        member_rank = Member.objects.all().order_by('-map_location')[:5]

    context = {
        'map_list': map_list,
        'member_rank': member_rank,
        'date_list': date_list,
        'member_list': member_list,
    }
    return render(request, 'admin/admin_page.html', context)
