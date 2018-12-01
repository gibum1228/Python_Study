"""
챕터: Day 6
주제: 정규식
문제: 정규식 연습
작성자: 김기범
작성일: 2018.11.22.
"""
"""
1. apple에 a가 들어있는지 확인
2. apple에 b가 들어있는지 확인
3. 정규식을 이용하여, 사용자가 입력한 영어 문장에서 a, e, i, o, u가 포함되어 있는지 찾아서 출력하시오. 만족하는 첫번째만 출력한다
<입력> This is a test.
"""
import re

print(re.search('a', 'apple'))
print(re.search('b', 'apple'))
test3 = input("문장 입력: ")
print(re.search('[aeiou]', test3))

"""
4. 입력한 단어가 a로 시작하는지 확인
5. 입력한 단어가 e로 끝나는지 검사
"""
test4 = input("단어 입력: ")
print(re.search('^a', test4))
test5 = input("단어 입력: ")
print(re.search('e$', test5))

"""
7. 입력된 문장에서 숫자부분을 모두 출력하라.
A. 입력 예: 2017년 3월 8일 5000원
B. 출력 예:
2017
3
8
5000
"""
test7 = input("문장 입력: ")
r = re.findall('\d*\d', test7)
for i in range(0, len(r)):
    print(r[i])

"""
10. 입력된 문장에서 <이후에 나오는 단어들을 출력하라.
A. 입력 예: <2015> <김영수> <성공회대학교>
"""
test10 = input("문장 입력: ")
r = re.findall("\w*\w", test10)
for j in range(0, len(r)):
    print(r[j])