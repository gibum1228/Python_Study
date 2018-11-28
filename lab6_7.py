"""
챕터: Day 6
주제: 정규식
문제: 정규식 (. ? * +)기호 연습
작성자: 김기범
작성일: 2018.11.15.
"""
import re # regular expression 모듈을 수입

# 테스트할 각종 문자열 정의
s = "teeeest"
s2 = "tetst"
s3 = "tst"

r = re.compile('e.s') # e와 s사이에 문자가 있는 경우 찾기
print(r.search(s))
print(r.search(s2))
print(r.search(s3))

r = re.compile('e?s') # e가 0-1번 나타난 후, s가 나타나는 경우 찾기
print(r.search(s))
print(r.search(s2))
print(r.search(s3))

r = re.compile('e*s') # e가 0번 이상 존재한 후 s가 나타나는 경우 찾기
print(r.search(s))
print(r.search(s2))
print(r.search(s3))

r = re.compile('e+s') # e가 1번 이상 존재한 후 s가 나타나는 경우 찾기
print(r.search(s))
print(r.search(s2))
print(r.search(s3))