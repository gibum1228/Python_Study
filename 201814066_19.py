"""
과제번호: 19
201814066 김기범
"""
class Shape: # 슈퍼 클래스 Shape
    def area(self): # 면적 메소드
        return 0
    def perimeter(self): # 둘레 메소드
        return 0
    def __str__(self): # __str__ 특수 연산자
        return "도형"

class Circle(Shape): # Shape를 계승하는 어린이클래스 Circle
    PI = 3.1415 # 파이 값 정의
    def __init__(self, r): # 생성자
        self.r = r # 반지름

    def area(self): # 면적 메소드
        return (self.r ** 2) * Circle.PI # 원의 넓이 공식

    def perimeter(self): # 둘레 메소드
        return self.r * 2 * Circle.PI # 원의 둘레 공식

    def __str__(self): # 특수 연산자
        return "<원> " + "반지름:" + str(self.r)

    def getRadius(self): # 반지름을 반환하는 메소드
        return self.r

class Rectangle(Shape): # 섭 클래스 Rectangle
    def __init__(self, w, h): # 생성자
        self.w = w # 가로
        self.h = h # 세로

    def area(self): # 면적 메소드
        return self.w * self.h # 직사각형의 넓이 공식

    def perimeter(self): # 둘레 메소드
        return (2 * self.w) + (2 * self.h) # 직사각형의 둘레 공식

    def __str__(self): # 특수 연산자
        return "<직사각형> " + "밑변:" + str(self.w) + " 높이:" + str(self.h)

    def getHeight(self): # 세로 반환하기
        return self.h

    def getWidth(self): # 가로 반환하기
        return self.w

    def getSides(self): # 시계 방향으로 변의 길이를 갖는 리스트를 반환하는 메소드
        l = [self.w, self.h, self.w, self.h] # 윗면 > 오른쪽 면 > 밑면 > 왼쪽 면
        return l

class Triangle(Shape): # 섭 클래스 Triangle
    def __init__(self, uw, wr, wl, h): # 생성자
        self.uw = uw # 밑변
        self.wr = wr # 오른쪽 변
        self.wl = wl # 왼쪽 변
        self.h = h # 높이

    def area(self): # 면적 메소드
        return self.uw * self.h * 0.5 # 삼각형의 넓이 공식

    def perimeter(self): # 둘레 메소드
        return self.uw + self.wr + self.wl # 삼각형의 둘레 공식

    def __str__(self): # 특수 연산자
        return "<삼각형> " + "밑변:" + str(self.uw) + " 높이:" + str(self.h)

    def getHeight(self): # 높이 반환하기
        return self.h

    def getWidth(self): # 밑변 반환하기
        return self.uw

    def getSides(self): # 시계 방향으로 변의 길이를 갖는 리스트를 반환하는 메소드
        l = [self.wr, self.uw, self.wl] # 오른쪽 변 > 밑변 > 왼쪽 변
        return l

# 실행부 코드 시작
s = Shape() # 객체 정의, A ~ D
c = Circle(5)
r = Rectangle(5, 10)
t = Triangle(3, 4, 5, 4)

print("c의 면적:%d, 둘레:%d" %(c.area(), c.perimeter())) # area()와 perimeter() 사용하기, E ~ G
print("r의 면적:%d, 둘레:%d" %(r.area(), r.perimeter()))
print("t의 면적:%d, 둘레:%d" %(t.area(), t.perimeter()))

print("")
for i in t.getSides(): # t의 변들을 시계 방향으로 출력, H
    print("변의 길이:",i) # t의 변들을 t.getSides()의 반환값인 리스트로 받아 출력하기
print(t.getSides())

print("")
l = [s, c, r] # s, c, r을 담는 리스트 l2 생성, I
for j in l: # J
    print("현재 요소:", j) # j는 l2요소 중 어떤 요소의 값을 받고 있는지 출력
    print("면적:%d, 둘레:%d" %(j.area(), j.perimeter())) # 위에 출력한 요소의 면적과 둘레를 출력
    # 테스트:getRadius() 메소드를 수행해보기 (오류발생), getRadius() 메소드는 c(Circle)만 가지고 있기 때문이다, K
    j.getRadius()