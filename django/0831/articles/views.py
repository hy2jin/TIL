from django.shortcuts import render
import random

# Create your views here.
def index(request):
    # index.html 반환
    # 메인 페이지 보여줄 것
    # 첫번째 인자는 항상 request
    # 두번째 인자는 보여줄 template
    return render(request, 'articles/index.html')

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
    return render(request, 'articles/greeting.html', context)

def dinner(request):
    menu = ['햄버거', '초밥', '피자', '탕수육', '카레', '닭갈비']
    pick = random.choice(menu)
    context = {
        'pick': pick
    }
    return render(request, 'articles/dinner.html', context)

def dtl_practice(request):
    # 사전준비로 각종 데이터 초기화
    foods = ['짜장면', '짬뽕', '탕수육', '초밥']
    fruits = ['apple', 'banana', 'kiwi', 'orange']
    info = []
    context = {
        'foods': foods,
        'fruits': fruits,
        'info': info
    }
    return render(request, 'articles/dtl_practice.html', context)

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    print(request.GET.get('message'))
    message = request.GET.get('message')
    context = {
        'message': message
    }
    # print(dir(request))
    return render(request, 'articles/catch.html', context)

def hello(request, name):
    print(name)
    context = {
        'name': name
    }
    return render(request, 'articles/hello.html', context)