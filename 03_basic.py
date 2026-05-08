# 표준 입력 함수 - input()
#   --> 입력을 받으면 문자열로 인식

# name = input('이름을 입력하세요 : ')
# print(name)

# a = input('숫자1 입력 : ') # 10
# b = input('숫자2 입력 : ') # 20
# print(a + b) # 1020
# print(type(a), type(b)) # <class 'str'> <class 'str'>

# # 정수형으로 형변환을 한다
# a = int(input('정수1 입력 : ')) # 50
# b = int(input('정수2 입력 : ')) # 100
# print(a + b) # 150

# # 실수형으로 입력
# a = float(input('실수1 입력 : '))
# b = float(input('실수2 입력 : '))
# print(a + b)

# f 문자열 포매팅
a = int(input('정수1 입력 : '))
b = int(input('정수2 입력 : '))
print(f'{a} + {b} = {a + b}')
print('{} + {} = {}'.format(a, b, a + b))