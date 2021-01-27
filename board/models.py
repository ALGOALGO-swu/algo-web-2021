from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=120, verbose_name='제목')
    writer = models.ForeignKey('account.Algo_User', on_delete=models.CASCADE, verbose_name='작성자')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='작성시간')
    contents = models.TextField(verbose_name='내용')
   
    def __str__(self):
        return self.title
        
'''
    class Meta:
        db_table = 'algoalgo_board'
        verbose_name = '알고알고 게시글'  # 관리자 화면에 모델 객체 이름 지정 
        verbose_name_plural = '알고알고 게시글들'
'''