from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import GuessNumbers
from .forms import PostForm

# Create your views here.


def index(request):

    lottos = GuessNumbers.objects.all()

    return render(request, 'lotto/default.html', {'lottos': lottos})


def hello(request):
    return HttpResponse("<h1 style='color:red;'>Hello, world!</h1>")


def post(request):

    form = PostForm(request.POST)

    # # 따로 후처리를 할 필요가 없다면
    # form.save() # DB에 바로 저장

    if form.is_valid():
      # validation check
      lotto = form.save(commit=False) # commit : DB에 확정적으로 저장할지(True: default) 안할지(False)
      lotto.generate()
      # generate 기능 안에 save까지 포함되어 있다.

      return redirect('index') # urls.py에 있는 리스트 중 name에 당하는 것을 작성

    return render(request, 'lotto/form.html', {'form': form})


def detail(request, lottokey):
    # lottokey라는 파라미터를 받아온다
    lotto = GuessNumbers.objects.get(id=lottokey)  # id 대신 pk도 가능

    return render(request, 'lotto/detail.html', {'lotto': lotto})

# ---
# index.html 안에 아래와 같은 태그가 있다면
    # <input name='name' type='text'></input>
    # 사용자에게 input 창이 보여진다
    # 값을 입력하고 전송버튼을 클릭하면 -> 입력한 값을 가지고 HTTP POST request가 날아옴

    # user_input_name = request.POST['name']  #HTML에서 name이 'name'인 input tag에 대해 USER가 입력한 값을 꺼낼 때
    # user_input_text = request.POST['text']

    # new_row = GuessNumbers(name=user_input_name, text=user_input_text)

    # print(new_row)  # -> "pk 1: name - text(설명)"
    # pk == id

    # new_row.name = new_row.name.upper()

    # new_row.generate()  # 아래 과정을 models의 GuessNumbers 클래스의 generate 함수로 대체

    # new_row.lottos = [ np.randint(1, 50) for i in range(6) ]

    # # 개별적으로 row의 값들을 수정하고, 저장하는 과정

    # new_row.save()  # Model 클래스 내부의 save() 함수 사용
    # # 테이블의 하나의 행에 저장되도록 함