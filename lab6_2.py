"""
챕터: Day 6
주제: class
문제: 좌표를 표현하는 클래스 Coordinate를 정의한다.
1. __init__는 x, y 좌표를 받아서 self의 x, y에 배정
2. 거리를 구하는 distance 메소드를 정의한다. self와 다른 좌표 other를 매개 변수로 받는다.
거리는 ( x좌표 사이의 차의 제곱(**2로 계산)과 y좌표 사이 차의 제곱의 합)의 제곱근이다. 제곱근(**0.5로 계산)
작성자: 김기범
작성일: 2018.10.18.
"""


# 클래스 정의
class Coordinate :

    def __init__(self, x = 0, y = 0): # instance를 정의하면서 자동으로 좌표 받기
        """
        Python에서는 __init__함수를 한 클래스 당 하나만 정의할 수 있음
        """
        self.x = x # 매개변수 x는 좌표 x 값
        self.y = y # 매개변수 y는 좌표 y 값

    def distance(self, other):
        """
        두 좌표의 거리를 계산하여 반환
        :param other: 다른 좌표
        :return: self와 other와의 거리를 반환
        """
        r = ((self.x - other.x)**2 + (self.y - other.y)**2) ** 0.5 # 거리 구하기 공식, 제곱근(**0.5)
        return r # 거리를 반환


# 실행 코드 시작
"""
실행코드 부분
(3, 4) 좌표의 점 c를 정의
원점 origin 정의
(3. 4)와 원점과의 거리를 출력
"""
c = Coordinate(3, 4) # (3, 4) 좌표의 점 c를 정의
origin = Coordinate() # 원점 origin 정의
c1 = Coordinate(10, 9) # 새로운 좌표 c1 정의

print("거리: %.2f" %c.distance(origin)) # 원점과의 거리 출력하기, 소수점 둘째 자리까지 출력, c가 self이고 origin이 other
print("거리: %.2f" %c1.distance(c)) # c1과 c의 거리 구하기, c1이 self, c가 other
# 클래스 이름과 함께 메소드 호출 가능, 이 때는 self에 해당되는 매개변수를 보내야 한다
print("거리: %.2f" %Coordinate.distance(c1, origin))