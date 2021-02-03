from django.shortcuts import render,redirect, get_object_or_404
from account.models import Algo_User
from board.models import Board
from board.forms import BoardForm
from django.utils import timezone
# from django.contrib import messages

def board_list(request):  #글 목록 불러오기 
    boards = Board.objects.all().order_by('-id')
    return render(request, 'board_list.html', {'boards':boards})


def board_write(request):  # 글쓰기
    if not request.session.get('user'): 
        return redirect('/account/login')
    
    if request.method == 'POST':
        form=BoardForm(request.POST)
        if form.is_valid():
            user_id=request.session.get('user')
            writer = Algo_User.objects.get(pk=user_id) 

            board=Board(
                title =form.cleaned_data['title'],
                contents = form.cleaned_data['contents'],
                writer= writer
            )
            board.save()

            return redirect('/board/list/')
    else:
        form=BoardForm()
    return render(request, 'board_write.html',{'form':form})


def board_edit(request,pk):  # 글 수정
    board = Board.objects.get(pk=pk)
    if request.method == "POST":
        form = BoardForm(request.POST,board)
        if form.is_valid():
            board= form.save(commit=False)  # <-- 여기서 자꾸 에러 뜬다. 수정필요
            #editBoard.registered_dttm = timezone.now()
            board.save()
           # messages.success(request,"수정되었습니다.")
            return redirect('board_detail', pk=post.pk)
    else : 
        form = BoardForm(board)
    return render(request, 'board_write.html',{'form':form})
   
  


def board_detail(request,pk):  # 글 상세보기 
    try:
        board=Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('해당 게시물을 찾을 수 없습니다.')
    return render (request,'board_detail.html',{'board':board})



def board_delete(request,pk):   #글 삭제
    try:
        board=Board.objects.get(pk=pk)
        board.delete()
    except Board.DoesNotExist:
        raise Http404('해당 게시물을 찾을 수 없습니다.')
    return redirect ('/board/list')