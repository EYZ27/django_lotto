from django import forms
from .models import GuessNumbers


class PostForm(forms.ModelForm):

    class Meta:
        # 상위의 클래스라는 뜻. 기본적으로 사용해야한다.
        # 기반으로 할 model을 불러온다
        model = GuessNumbers
        fields = ('name', 'text',)	 # 유저에게 받을 부분 / 그 이외에는 기능에서 만들어지므로 받지 않아야 한다.
