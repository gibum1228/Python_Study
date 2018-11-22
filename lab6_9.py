"""
챕터: Day 6
주제: 정규식
문제: 정규식 기호 연습
작성자: 김기범
작성일: 2018.11.15.
"""
import re # regular expression 모듈을 수입

# 테스트할 각종 문자열 정의
s = "teeeest"
s2 = "tetst"
s3 = "tst"
s4 = "apple"
s5 = "test1234Test"
s6 = "나는 \"왕\"이다" # "을 출력하고 싶으면 \"을 사용

r = re.compile('\d') # 숫자를 찾아서 반환
print(r.search(s))
print(r.search(s5))

r = re.compile('\D') # 숫자를 아닌 것 찾아서 반환
print(r.search(s))
print(r.search(s5))

r = re.compile('[a-zA-Z]') # 알파벳 찾아서 반환
print(r.search(s))
print(r.search(s5))

# 25-27라인의 코드를 search 함수를 이용하여 다시 쓰기
print(re.search('[a-zA-z]',s))
print(re.search('[a-zA-z]',s5))

# s5에서 알파벳 또는 숫자 찾기
print(re.search('[a-zA-Z0-9]',s5))
# s5에서 숫자 찾기
print(re.search('[0-9]',s5))
# s5에서 대문자 찾기
print(re.search('[A-Z]',s5))
# s5에서 소문자 찾기
print(re.search('[a-z]',s5))

# s6에서 \의 위치를 찾기
print(re.search('\"',s6))

print(re.search('\W',s6)) # 공백을 출력, 역슬래쉬W는 숫자 또는 문자가 아닌 것을 검색