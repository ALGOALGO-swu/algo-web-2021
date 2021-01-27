from django.shortcuts import render,redirect
from account.models import Algo_User
from board.models import Board
from board.forms import BoardForm


def board_list(request):
    boards = Board.objects.all().order_by('-id')
    return render(request, 'board_list.html', {'boards':boards})


def board_write(request):  # 글쓰기 부분 현재 수정 중 
    if request.method == 'POST':
        form=BoardForm(request.POST)
        if form.is_valid():
            user_id=request.session.get('username')
            writer = Algo_User.objects.get(pk=user_id) # 오류 발생 부분 

            board=Board()
            board.title =form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer= writer
            board.save()

            return redirect('/board/list/')

    else:
        form=BoardForm()

    return render(request, 'board_write.html',{'form':form})


def board_detail(request,pk):
    board=Board.objects.get(pk=pk)
    return render (request,'board_detai.html',{'board':board})