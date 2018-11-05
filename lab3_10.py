"""
챕터: day 3
주제: set(mutable) > 값 추가&삭제 가능
작성자: 김기범
작성일: 2018.09.13.
"""
s = {7, 8, 9, 7} # set은 순서 의미 없음, 중복을 허용하지 않는다
fruits = { 'a': '사과', 'b': '배', 'c': '복숭아', 'd': '딸기'}
print(s)
# 딕셔너리를 set으로 변환
print(set(fruits)) # key 값만 출력

# [3, 4, 5]를 set으로 형병환하여 s에 저장하고 출력
s = set([3, 4, 5])
print(s)

# 인덱스를 사용할 수 없음, 위치가 의미 없으므로
s.add(10) # add로 추가
print(s)
# remove로 삭제
s.remove(10)
print(s)

# 정렬한 결과를 출력
print(sorted(s))