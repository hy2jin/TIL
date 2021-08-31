from django.shortcuts import render
import random

# Create your views here.
def index(request):
    # index.html 반환
    # 메인 페이지 보여줄 것
    # 첫번째 인자는 항상 request
    # 두번째 인자는 보여줄 template
    return render(request, 'index.html')

def greeting(request):
    # name 키값에 본인 이름을 벨류로 html에게 넘겨주려면
    foods = ['바나나', '청국장', '초밥']
    info = {
        'name': '이혜진'
    }
    context = {
        'foods': foods,
        'info': info
    }
    return render(request, 'greeting.html', context)

def dinner(request):
    menu = ['햄버거', '초밥', '피자', '탕수육', '카레', '닭갈비']
    pick = random.choice(menu)
    context = {
        'pick': pick
    }
    return render(request, 'dinner.html', context)