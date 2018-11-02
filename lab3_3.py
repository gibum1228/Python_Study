"""
챕터: Day 3
주제: 문자열 함수
작성자: 김기범
작성일: 2018년 9월 6일
"""
s = "   Test your Python debugging skills    "
print(s.upper()) # 대문자로 변환
print(s.lower()) # 소문자로 변환

# 문자열 안의 t의 갯수 출력
print(s.count("t"))
print(s.count("T", 1)) # 두번째 매개변수는 count 계산을 시작하는 위치

# 사용자로부터 문자를 입력 받아, 대소문자 구분없이 해당 문자의 개수를 출력
c = input("문자 입력: ") # 사용자로부터 문자 입력 받기
s1 = s.upper() # 비교되는 문자열을 대문자로 변환하여 s1에 저장
# upper 함수를 사용했을 때, s가 바뀌는 것이 아니라 반환값을 저장하는 s1의 값이 변화함
print(s)
print(s1)
print(s1.count(c.upper())) # 비교되는 문자를 대문자로 변환하여 개수를 계산

# t가 있는 위치를 출력
print(s.index("t"))
print(s.index("t", 4)) # 두번째 매개변수는 검색 시작 위치
# print(s.index("x")), index() 함수는 찾으려는 문자가 없으면 오류 발생

# 대상 문자를 찾을 수 있는 함수
print(s.find("t"))
print(s.find("x")) # find() 함수는 찾으려는 값이 없을 경우, -1 반환

# 공백 제거 strip() 함수
print(s)
print(s.lstrip()) # 왼쪽 공백 제거
print(s.rstrip()) # 오른쪽 공백 제거
print(s.strip()) # 양쪽 공백 제거

# 내용 바꾸기 replace()
print(s.replace("Python", "Java")) # Python -> Java 교체
print(s) # s 값의 영향을 주진 않는다

# 문장에서 e를 i로 모두 바꾸어 출력
print(s.replace("e", "i", 1)) # 3번째 매개변수는 변경할 최대 개수를 지정

# 문자열 나누기 split()
# 양쪽 공백을 제거한 후 빈칸을 기준으로 단어를 모두 나누기
print(s.strip().split(" ")) # s.strip()의 반환값이 문자열이기 때문에 문자열함수 split()를 사용할 수 있다
print(s.strip().split(" ", 2)) # 두번째 매개변수는 개수를 지정 + split()의 반환값은 리스트이기 때문에 문자열을 반환하는 함수를 사용할 수 없다

# s의 길이 출력
print(len(s))

s = "test"
s = '  kkk'
s = '''
Kim
Yee
Hi
'''

i = input("문자열: ") # i는 str형, input()의 반환형은 str
i = int(input("문자열: ")) # i는 int형, int()로 형변환함
j = 100 # j는 int형
s1 = str(j) # s1는 str형