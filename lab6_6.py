"""
챕터: Day 6
주제:class 상속/계승
문제: shape,circlerectangle class define
작성자: 김기범
작성일:2018.11.01
"""
"""
1.Define shape class, method로 area(), perimeter()를 가지고 있다.
A.area()는 면적, perimeter()는 둘레를 반환한다. 하지만,shape class는 0을 반환
B.__str__()를 정의한다. "도형"을 반환

2.Shape를 계승하는, Circle,Rectangle,Triangle을 정의한다,__init__(),area(),perimeter(),__str__()를 정의한다.
  Triangle의  __init__는 세변(첫번째 변은 밑변)과 높이를 매개변수로 받는다.
A. Circle class에는 getRadius() method를 정의(반지름), 클래스변수PI=3.1415정의
B. Triangle,Rectangle class에는 getHeight() method를 정의(높이)
C. Triangle,Rectangle class에는 getWidth() method를 정의(밑변)
D. Triangle,Rectangle class에는 변의 길이를 list형태로 반환하는 getSides()method를 정의한다(변들을 반환한다.)
"""
class Shape: #개념적으로 되는 정의(특별한 개념은 없지만 크게 하나로 묶어내는 개념) abstract class
    def area(self):
        return 0
    def perimeter(self):
        return 0
    def __str__(self):
        return "도형"

class Circle(Shape):
    PI = 3.1415
    def __init__(self,r):
        self.raidus = r

    def area(self):
        return ((self.raidus**2)*PI)

    def perimeter(self):
        return (self.raidus*2*PI)

    def getRadius(self):
        return self.raidus

    def __str__(self):
        return "Circle"

class Rectangle(Shape):
    def __init__(self,x,y):
        self.height = x
        self.width = y

    def getHeight(self):
        return self.height

    def getWidth(self):
        return self.width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return (self.height + self.width)*2


"""
실행부
1. s 변수는 도형이다.
2. 반지름이 5인 원을 정의하여 c변수에 저장한다.
3. 가로,세로가 5,10인 직사각형을 정의하여 r에 저장한다.
4. 세변이 3(밑변),4,5이고 높이가 4인 삼각형을 정의하여 t에 저장한다.
5. c의 면적과 둘레를 출력한다.
6. r의 면적과 둘레를 출력한다.
7. t의 면적과 둘레를 출력한다.
8. t의 변들을 리스트로 받아 출력한다.
9. 리스트 l을 정의하여, s,c,r,t을 요소로 추가한다.
10. l의 각 요소에 대해, 해당요소를 출력하고, 면적과 둘레를 계산하여 출력한다.(for문 이용)
* for문 안에서 테스트: getRadius() method를 수행한다.(오류발생)
"""
s = Circle(5)
print(s.area())