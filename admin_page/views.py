from django.shortcuts import render
from .models import Map, Member


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

    # 랭킹
    member_rank = Member.objects.all().order_by('-map_location')[:5]

    context = {
        'map_list': map_list,
        'member_rank': member_rank,
    }
    return render(request, 'admin/admin_page.html', context)
