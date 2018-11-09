"""
작성자: 201814066 김기범
문제
Class Fraction의 4칙연산을 완성하라.
메쏘드: __init__, set 메소드, get 메소드, print(), 사칙연산
약분까지 해야 한다.

다음 실행 코드를 수행한다.
1/2, 5/4를 저장하는 변수를 정의한다.
두 변수의 사칙연산 결과를 보기 좋게 출력한다.

(출력 예)
1/2 + 5/4 = 7/4
"""
class Fraction:
    def __init__(self, n, d):
        """
        초기 값 정의해주는 메쏘드(자동 메쏘드)
        :param n: 분자
        :param d: 분모
        """
        self.numer = n
        self.denom = d

    # 새롭게 초기화하는 set 메쏘드
    def setNumer(self, n):
        self.numer = n
    def setDenom(self, d):
        self.denom = d

    # 현재 값을 반환하는 get 메쏘드
    def getNumer(self):
        return self.numer
    def getDenom(self):
        return self.denom

    # 현재 분수 값을 출력하는 print 메쏘드
    def print(self):
        print("%d/%d" %(self.numer, self.denom))

    # 덧셈 메쏘드
    def add(self, o):
        n = (self.numer * o.denom) + (self.denom  * o.numer) # 분자 계산
        d = self.denom * o.denom # 분모 계산
        ex = Fraction(n, d) # 덧셈 값을 ex에 저장
        return ex # 결과값 반환
    # 뺄셈 메쏘드
    def minus(self, o):
        n = (self.numer * o.denom) - (self.denom * o.numer)  # 분자 계산
        d = self.denom * o.denom  # 분모 계산
        ex = Fraction(n, d)  # 뺄셈 값을 ex에 저장
        return ex # 결과값 반환
    # 나눗셈 메쏘드
    def div(self, o):
        n = self.numer * o.denom # self 분자와 o 분모 곱하기
        d = self.denom * o.numer # self 분모와 o 분자 곱하기
        ex = Fraction(n, d) # 나눗셈 값을 ex에 저장
        return ex # 결과값 반환
    # 곱셈 메쏘드
    def multi(self, o):
        n = self.numer * o.numer # 분자끼리 곱하기
        d = self.denom * o.denom # 분모끼리 곱하기
        ex = Fraction(n, d) # 곱셈 값을 ex에 저장
        return ex # 결과값 반환
    # 최대공약수를 이용해 약분을 한다
    def reduction(self):
        # 유클리드 호제법을 사용하기 위해서는 a > b 가 성립되어야 한다
        a = max(self.numer, self.denom) # 큰 수를 a에 저장
        b = min(self.numer, self.denom) # 작은 수를 b에 저장

        # 2개의 자연수  a, b에 대해서 a를 b로 나눈 나머지를 r이라 하면(a>b), a와 b의 최대공약수는 b와 r의 최대공약수와 같다
        while (a % b) != 0 : # 유클리드 호제법 실행 ( 나머지가 0이면 조건문 탈출 )
            r = a % b # 나머지 r
            a = b
            b = r

        n = self.numer // b # 최대공약수로 분자 나누기
        d = self.denom // b # 최대공약수로 분모 나누기
        ex = Fraction(n, d) # 약분된 값을 ex에 저장
        return ex # 결과값 반환
    # 출력 간단하게 해주는 메쏘드
    def __str__(self):
        return str(self.numer) + "/" + str(self.denom)
    # 덧셈 간단하게 해주는 메쏘드
    def __add__(self, o):
        n = (self.numer * o.denom) + (self.denom * o.numer)  # 분자 계산
        d = self.denom * o.denom  # 분모 계산
        ex = Fraction(n, d)  # 덧셈 값을 ex에 저장
        return ex  # 결과값 반환
    # 오퍼레이터 오버로딩(등호) 메쏘드
    def __eq__(self, o):
        """
        self 와 o가 약분하여 같은 분수면 True 반환
        :param o: 다른 분수
        :return: 약분하여 같은 분수이면 True 반환 아니면 False 반환
        """
        g1 = gcm(self.numer, self.denom)
        g2 = gcm(o.numer, o.denom)
        if (self.numer//g1 == o.numer//g2) and (self.denom//g1 == o.denom//g2):
            return True
        else:
            return False

    def __ne__(self, o):
        """
        두 부눗가 같으면 True, 아니면 False를 반환
        """
        if (self == o): # eq 메쏘드에서 오버리딩을 했기 때문에 간단하게 표현 가능
            return False
        else:
            return True

# 최대공약수를 반환하는 함수
def gcm(x, y):
    # 두 정수 중 큰 수를 x에 저장, 작은 수를 y에 저장
    if y > x :
        temp = y
        y = x
        x = temp
    # 유클리드 호제법에 의해 최대공약수 구함
    while (y>0):
        r = x % y
        x = y
        y = r
    return x

# 실행 코드 시작
f1 = Fraction(1, 2) # f1 초기화
f2 = Fraction(5, 4) # f2 초기화

print("첫 번째 분수: ", end = ""); f1.print() # 첫 번쨰 분수 f1 출력
print("두 번째 분수: ", end = ""); f2.print() # 두 번째 분수 f2 출력
print("") # 출력 창 깔끔하게 만들기 위한 공백
print("%d/%d + %d/%d =" %(f1.getNumer(),f1.getDenom(),f2.getNumer(),f2.getDenom()), end = " "); f1.add(f2).reduction().print() # 덧셈 값 출력
print("%d/%d - %d/%d =" %(f1.getNumer(),f1.getDenom(),f2.getNumer(),f2.getDenom()), end = " "); f1.minus(f2).reduction().print() # 뺄셈 값 출력
print("%d/%d / %d/%d =" %(f1.getNumer(),f1.getDenom(),f2.getNumer(),f2.getDenom()), end = " "); f1.div(f2).reduction().print() # 나눗셈 값 출력
print("%d/%d * %d/%d =" %(f1.getNumer(),f1.getDenom(),f2.getNumer(),f2.getDenom()), end = " "); f1.multi(f2).reduction().print() # 곱셈 값 출력

# __str__ 메쏘드 활용
print("__str__ 메쏘드 활용")
print(f1,"+", f2, "=", f1.add(f2).reduction())
print(f1,"-", f2, "=", f1.minus(f2).reduction())
print(f1,"/", f2, "=", f1.div(f2).reduction())
print(f1,"*", f2, "=", f1.multi(f2).reduction())

# __add__ 메쏘드 활용
print("__add__ 메쏘드 활용")
print(f1+f2)

# __eq__ 메쏘드 활용
print("__eq__ 메쏘드 활용")
f3 = Fraction(8, 10)
if(f1 == f3):
    print("f1과 f3은 같습니다.")
else:
    print("f1과 f3은 다릅니다.")

# __ne__ 메쏘드 활용
print("__ne__ 메쏘드 활용")
if (f1 != f3):
    print("f1과 f3은 다릅니다")
else:
    print("f1과 f3은 같습니다.")