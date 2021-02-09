from django import forms
from board.models import Board

class BoardForm(forms.ModelForm):
    title = forms.CharField(
        error_messages={
            'required' : '제목을 입력해주세요.'
        }
    ,max_length=128, label="제목")

    contents= forms.CharField(
         error_messages={
            'required' : '제목을 입력해주세요.'
        }, widget=forms.Textarea, label="내용")
    
    class Meta :
        model = Board
        fields =['title', 'contents']