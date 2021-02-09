from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.utils import timezone
from django.contrib import messages

from account.models import Algo_User
from .models import Board
from .forms import BoardForm

# 글 목록 불러오기 
def board_list(request): 
    boards = Board.objects.all().order_by('-id')
    return render(request, 'board/board_list.html', {'boards':boards})

# 글쓰기
def board_write(request):  
    if not request.session.get('user'): 
        return redirect('/account/login')
    
    if request.method == 'POST':
        form=BoardForm(request.POST)
        if form.is_valid():
            user_web_id=request.session.get('user')
            writer = Algo_User.objects.get(web_id=user_web_id) 

            board=Board(
                title =form.cleaned_data['title'],
                contents = form.cleaned_data['contents'],
                writer= writer
            )
            board.save()

            return redirect('/board/list/')
    else:
        form=BoardForm()
    return render(request, 'board/board_write.html',{'form':form})


# 글 수정
def board_edit(request,pk): 
    board = get_object_or_404(Board, pk=pk)

    if request.method == "POST":
        # 작성자 여부 확인
        if str(request.session.get('user')) == str(board.writer):
            form = BoardForm(request.POST,instance=board)  
            if form.is_valid():
                edit_board = form.save(commit=False) 
                edit_board.registered_dttm = timezone.now()
                form.save()
                return redirect('/board/detail/' + str(pk))
        else:
            return HttpResponseRedirect('/board/list') 
    
    else : 
         form = BoardForm(instance=board)
  

    return render(request, 'board/board_edit.html',{'form':form})
   
  

# 글 상세보기 
def board_detail(request,pk):  
    try:
        board=Board.objects.get(pk=pk)
        isWriter=False
        #작성자 여부 확인
        if str(request.session.get('user')) == str(board.writer):
            isWriter=True
   
    except board.DoesNotExist:
        raise Http404('해당 게시물을 찾을 수 없습니다.')
    return render (request,'board/board_detail.html',{'board':board, "isWriter":isWriter})



# 글 삭제
def board_delete(request,pk):   
    try:
        board=Board.objects.get(pk=pk)
        # 작성자 여부 확인
        if str(request.session.get('user')) == str(board.writer):
            board.delete()

    except board.DoesNotExist:
        raise Http404('해당 게시물을 찾을 수 없습니다.')
    return redirect ('/board/list')