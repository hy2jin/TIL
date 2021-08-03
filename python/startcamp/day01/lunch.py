# 무작위로 뽑기위해서 random 이라는걸 쓸건데,
# 이 random은 그냥 쓸 수 는 없고 import를 통해 불러온다.
import random

# lunch라고 하는 변수에 점심메뉴 3가지를 담아보자.

# 리스트를 만들 때 중요한건 대괄호
# 그 안에 담길 요소들 -> 문자열이라면, 각 요소들 전부 ""
# 쉼표로 구분해준다.
lunch = ['짜장', '돈가스', '냉면']

# lunch 전체 출력
print(lunch)
# lunch 중에 3번째 요소 출력
print(lunch[2])

# lunch가 가지고 있는 값중 하나를 무작위로 골라서 menu라고 하는 변수에 담는다.
menu = random.choice(lunch)
print(menu)