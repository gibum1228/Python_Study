"""
챕터: day 3
주제: Dictionary(특징: mutable, key와 value의 쌍으로 구성됨)
작성자: 김기범
작성일: 2018.09.13.
"""
# fruits = { 'a': '사과', 'b': '배', 'c': '복숭아, 'd': '딸기'}
fruits = { 'a': '사과', 'b': '배', 'c': '복숭아', 'd': '딸기'}
print(fruits)
# 키가 'a'인 경우의 값을 출력하라
print(fruits['a'])
# get() 함수는 키가 존재하지 않은 경우, None를 반환
print(fruits.get('k'))
# 키가 'b'인 경우의 값을 '체리'로 수정하라
fruits['b'] = '체리'
print(fruits)
# 키가 'f'인 '아보카도'를 추가
fruits['f'] = '아보카도'
print(fruits)
# fruits에서 키가 'a'인 값의 길이를 출력하라
print(len(fruits['a']))
# 모든 key 출력
print(fruits.keys())
# 모든 value 출력
print(fruits.values())
# fruits 안에 'a'라는 키가 있으면 True, 아니면 False를 출력
print('a' in fruits)
print('체리' in fruits) # 체리가 value라서 False가 출력, in은 key만 확인함
print('a' in fruits.keys())
# fruits의 value 중에 '복숭아'가 있으면 True, 아니면 False를
print('복숭아' in fruits.values())

f = sorted(fruits) # key 순서에 따라 정렬된 key list 반환
print(fruits)
print(f)

# value를 정렬된 순서의 list 출력
fv = sorted(fruits.values())
print(fv)

# 키와 값을 튜플의 리스트로 만들어 출력하라 (items()]
print(fruits.items())

# 삭제(del 사용)
# 'c'라는 키를 가진 fruit를 삭제
del fruits['c']
print(fruits)