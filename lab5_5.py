"""
챕터: Day 5
주제: min 함수 이용
문제:
작성자: 김기범
작성일: 2018.10.04.
"""
"""
    iterable == 하나씩 꺼내어 검사하는 것
View > Tool Windows > Python Console
help(min)


min(...)
    min(iterable, *[, default=obj, key=func]) -> value
    min(arg1, arg2, *args, *[, key=func]) -> value

    With a single iterable argument, return its smallest item. The
    default keyword-only argument specifies an object to return if
    the provided iterable is empty.
    With two or more arguments, return the smallest argument.
"""
"""
l 변수에 [4, 7, 9, 11, -5]를 제공한다.
l에서 최소값, 최대값을 출력한다.
"""
l = [4, 7, 9, 11, -5] # iterable로 쓰인 l 정의
print(min(l)) # min 함수를 이용해 최소값 출력
print(max(l)) # max 함수를 이용해 최대값 출력

"""
fruits 변수에 apple, orange, banana를 tuple로 배정한다.
fruits에서 최소값과 최대값을 출력한다.
"""
fruits = ( 'apple', 'orange', 'banana') # 튜플 fruits 정의
print(min(fruits)) # 최소값 출력
print(max(fruits)) # 최대값 출력

"""
orange를 Orange로 변경
최소값과 최대값 출력
"""
fruits = ( 'apple', 'Orange', 'banana') # 튜플 fruits 정의
print(min(fruits)) # 최소값 출력
print(max(fruits)) # 최대값 출력

"""
대소문자를 구분하지 않고 최대, 최소를 얻기 위해 min, max 함수의 마지막
key 매개변수로 str.lower(모두 소문자로 바꾸어 비교)를 전달한다.
"""
print(min(fruits,key=str.lower))
print(max(fruits,key=str.lower))

"""
1부터 50까지의 수 중 최대, 최소값을 출력한다. (range이용, min(range(1, 51))
"""
print(min(range(1, 51)))
print(max(range(1, 51)))

"""
min 함수에 직접 1, 3, 6 값을 전달하여 최소값 출력
"""
print(min(1,3,6))