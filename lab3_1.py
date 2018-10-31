"""
챕터: Day 3
주제: 데이터형 연습
작성자: 김기범
작성일: 2018년 9월 4일
"""

f = 3.4 # f의 데이터 타입은 float형, f에 저장된 3.4가 실수이기 때문이다.
print(f)
i = 3 # i는 int형, i에 저장된 3이 정수이기 때문이다.
print(i)
b = True # b는 불리언(boolean) 타입, b에 true가 저장되서, 불리언 타입은 true 또는 false를 저장한다.
print(b)
s = "안녕하세요" # s는 문자열 str, 문자열은 " " 또는 ' ' 로 묶는다.
print(s)
s = '1' # s는 문자열 str
print(s)

# f와 i를 더해서 출력 -> i를 float형으로 자동변환 후 계산함
print(f + i)
# s + i를 출력
# TypeError: Can't convert 'int' object to str implicitly 발생 -> 문자열이 int형으로 자동변환되지 않음
# print(s + i)
# s를 int형으로 변환하여 i와 더하기
print(int(s)+i)
# i를 str형으로 변환하여 s와 더하기, 문자열 이어주기 연산이 실행됨
print(s+str(i))

# 정수 계산
print("정수 계산")
i = 57
j = 28
# i를 j로 나눈 값 출력
print(i/j)
# i를j j로 나눈 몫 출력
print(i//j)
# i를 j로 나누었을 때, 나머지 출력
print(i%j)
# j의 제곱 출력
print(j**2)
# j의 세제곱 출력
print(j**3)

# 실수 계산
print("실수 계산")
i = 57.0
j = 28.0
# i를 j로 나눈 값 출력
print(i/j)
# i를j j로 나눈 몫 출력
print(i//j)
# i를 j로 나누었을 때, 나머지 출력
print(i%j)
# j의 제곱 출력
print(j**2)
# j의 세제곱 출력
print(j**3)

# or 연산자(boolean type)
print(b or False)
# and 연산자(boolean type)
print(b and False)

# 복소수(실수부와 허수부로 구성된 숫자) 타입 변수 k, 허수 i를 대신해서 j를 씀
k = 5 + 7j
print(k)
print(k.real) # 복소수에서 실수부만 뽑는 real
print(k.imag) # 복소수에서 허수부만 뽑는 imag
print(k.conjugate()) # 켤레 복소수를 가져오는 함수 conjugate()

# 8진수
o = 0o16 # 십진수로는 14를 의미, int형
print(o) # 기본 출력은 십진수
print("%o" %o) # 8진수로 출력
print("%x" %o) # 16진수로 출력

# 16진수
x = 0XA5
print(x) # 십진수 출력
print("%o" %x) # 8진수 출력
print("%X" %x) # 16진수 출력