"""
챕터: Day 5
주제: sum 함수 이용
문제:
작성자: 김기범
작성일: 2018.10.04.
"""
"""
sum(...)
    sum(iterable[, start]) -> value

    Return the sum of an iterable of numbers (NOT strings) plus the value
    of parameter 'start' (which defaults to 0).  When the iterable is
    empty, return start.

"""
"""
1에서 30까지의 합 출력 sum(range(1, 31))
"""
print(sum(range(1, 31)))

"""
1, 3, 5, 7을 list[]로, tuple()로, set{}으로 전달하여 합 출력
"""
l = [1, 3, 5, 7]
t = (1, 3, 5, 7)
s = {1, 3, 5, 7}

print(sum(l))
print(sum(t))
print(sum(s))

"""
50에서 1, 3, 5, 7의 합을 더하여 출력
"""
print(sum(l, 50)) # L 에 50 더하기

#  print(sum(1, 2, 3, 4, 5)) >> 오류뜸