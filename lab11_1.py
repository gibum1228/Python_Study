"""
챕터: Day 6
주제: class
문제: 정수집합 클래스
1. IntSet 클래스는 정수들의 집합이다. 정수들을 관리하는 리스트 self.vals를 애트리뷰트로 가진다.
2. 새로운 정수 e를 추가하는 insert 메쏘드, 해당 요소가 이미 있다면 추가하지 않음
3. e가 정수집합에 포함되어 있는지 확인하는 메쏘드인 involve 정의(True, False 반환)
4. e를 제거하는 remove 메쏘드
5. 단, e가 해당 집합에 없다면 적당한 오류 메시지를 출력
6. 집합 형식의 문자열로 변환시켜주는 __str__메쏘드. 단, 정수들은 정렬되어 반환되어야 한다.

작성자: 김기범
작성일: 2018. 11. 01.
"""

class intSet:
    def __init__(self): # 빈 리스트 self.vals를 자동 생성
        self.vals = []

    def insert(self,e): # 리스트에 e를 추가하는 메쏘드
        if self.vals.count(e) < 1: # e가 존재하지 않으면
            self.vals.append(e) # e를 리스트에 추가

    def involve(self, e): # e가 이미 있는지 확인하는 메쏘드
        if self.vals.count(e) < 1: # e가 없으면
            return False # False 반환
        else: # 아니면
            return True # True 반환

    def remove(self, e): # e를 삭제하는 메쏘드
        if self.involve(e) == False : # e가 존재하지 않으면
            print("%d는(은) 존재하지 않습니다." %e) # 적당한 오류 메시지 출력
        else: # 아니면
            i = self.vals.index(e) # e의 인덱스를 찾아
            del self.vals[i] # e의 인덱스 i를 제거

    def __str__(self): # 문자열로 변환해서 반환
        self.vals.sort() # 리스트를 정렬
        o = "" # 빈 문자열 초기화
        for j in self.vals: # 리스트 길이만큼 반복
            o += str(j) + " " # 정수를 문자로 넣기
        return o # o을 반환

# 실행부분
"""
A. intSet을 저장하는 변수 s를 정의
B. s에 insert를 이용하여 하나씩 5, 3, 7을 삽입
C. s를 정렬하여 출력
D. s에 8이 있는지 결과 출력
E. s에 3이 있는지 결과 출력
F. s에서 3을 제거
G. s에서 4를 제거
H. s를 정렬하여 출력
"""

s = intSet() # s를 정의
s.insert(5) # 5 추가
s.insert(3) # 3 추가
s.insert(7) # 7 추가
print(s) # s를 정렬하여 출력
if s.involve(8) == False: # 8 소유 여부를 확인
    print("8은 존재하지 않습니다.")
else:
    print("8은 존재합니다.")
if s.involve(3) == False: # 3 소유 여부를 확인
    print("3은 존재하지 않습니다.")
else:
    print("3은 존재합니다.")
s.remove(3) # 3 삭제
s.remove(4) # 4 삭제
print(s) # s를 정렬하여 출력