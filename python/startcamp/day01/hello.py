# greeting 이라는 변수에 '안녕하세요' 라는 문자를 할당한다.
greeting = '안녕하세요'

# greeting변수가 담고 있는 값을 출력한다.
print(greeting)
print(greeting)
print(greeting)
print(greeting)
print(greeting)
print()

# 반복문을 통해서 한번 인사를 여러번 하도록 한다
# while 조건, count가 4 미만인 동안만 반복 실행
# while은 종료 조건이 중요
count = 0
while count < 4:
    print(greeting)
    count += 1
print()

# for문을 통한 반복
for i in range(5):
    print(i)
    print(greeting)