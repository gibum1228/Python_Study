"""
１２.	복소수(complex number) 클래스를 정의한다.
①	복소수는 실수부(real), 허수부(image)로 나누어 저장한다.
②	복소수의 더하기(add), 빼기(sub) 연산을 정의하라. 실수부를 각각 더하(빼)고, 허수부를 각각 더하(빼)면 된다.
③	아래와 같은 수행 코드가 수행되어, 출력결과가 출력될 수 있도록 클래스를 정의하라.
④	출력될 때, 실수부와 허수부는 각각 괄호로 묶여야 한다.
(수행 코드)
a=ComplexNumber(4, 6) #첫번째 매개변수는 실수부, 두번째 매개변수는 허수부
b=ComplexNumber(-5, 7)
print(“덧셈 결과:”,  a+b)
print(“뺄셈 결과:”,  a-b)

(출력결과)
덧셈 결과: (-1)+(13)i
뺄셈 결과: (9)+(-1)i
"""

class ComplexNumber(): # 복소수 클래스
    def __init__(self, r, i): # 생성자
        self.real = r # 실수부
        self.image = i # 허수부

    def __add__(self, o): # 덧셈 특수 연산자
        n = ComplexNumber(0, 0) # 결과값 담을 변수 초기화
        n.real = self.real + o.real
        n.image = self.image + o.image
        return n # 양식에 맞게 출력

    def __sub__(self, o): # 뺄셈 특수 연산자
        n = ComplexNumber(0, 0) # 결과값 담을 변수 초기화
        n.real = self.real - o.real
        n.image = self.image - o.image
        return n # 양식에 맞게 출력

    def __str__(self):
        return "(" + str(n.real)+


# 실행부 시작
a = ComplexNumber(4, 6) # 클래스 변수 만들기
b = ComplexNumber(-5, 7)

print("덧셈결과: ", a+b) # 결과값 출력
print("뺄셈결과: ", a-b)