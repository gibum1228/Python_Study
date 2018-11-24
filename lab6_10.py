"""
챕터: Day 6
주제: 정규식
문제: 정규식 기호 연습
작성자: 김기범
작성일: 2018.11.20.
"""
import re

s7 = 'href =       "C:\Python34\Kim.jpg"' # href는 링크 이동을 위한 코드
s8 = 'href="C:\Python34|Kim.jpg"'

# s7에서 공백(탭 포함)이 나타나는 곳 찾기
print(re.search('\s', s7))
# s7에서 공백(탭 포함)이 아닌 것이 처음 나타나는 곳 찾기
print(re.search('\S', s7))

# s7, s8에서 'href='가 있는 곳 찾기
# 하나의 패턴을 여러 문자열에서 찾고 있으므로 compile 후 search 이용
r = re.compile('href=')
print(r.search(s7))
print(r.search(s8))
# s7에서 'href='가 있는 곳 찾기, =의 좌우에 빈 칸이 있든 없든 상관없이 찾기
r = re.compile("href\s*=\s*")
print(r.search(s7))
print(r.search(s8))