"""
201814066 김기범
과제 14번
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
        if n > 0 and d < 0: # 분자가 양수고 분모가 음수면 - 부호를 분자로 이동
            self.denom = -d
            self.numer = -n

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
        print("%d/%d" % (self.numer, self.denom))

    # 덧셈 메쏘드
    def add(self, o):
        n = (self.numer * o.denom) + (self.denom * o.numer)  # 분자 계산
        d = self.denom * o.denom  # 분모 계산
        ex = Fraction(n, d)  # 덧셈 값을 ex에 저장
        return ex  # 결과값 반환
    def __add__(self, o): # 덧셈 특수연산자
        n = (self.numer * o.denom) + (self.denom * o.numer)  # 분자 계산
        d = self.denom * o.denom  # 분모 계산
        ex = Fraction(n, d)  # 덧셈 값을 ex에 저장
        return ex  # 결과값 반환

    # 뺄셈 메쏘드
    def minus(self, o):
        n = (self.numer * o.denom) - (self.denom * o.numer)  # 분자 계산
        d = self.denom * o.denom  # 분모 계산
        ex = Fraction(n, d)  # 뺄셈 값을 ex에 저장
        return ex  # 결과값 반환
    def __sub__(self, o): # 뺄셈 특수연산자
        n = (self.numer * o.denom) - (self.denom * o.numer)  # 분자 계산
        d = self.denom * o.denom  # 분모 계산
        ex = Fraction(n, d)  # 뺄셈 값을 ex에 저장
        return ex  # 결과값 반환

    # 나눗셈 메쏘드
    def div(self, o):
        n = self.numer * o.denom  # self 분자와 o 분모 곱하기
        d = self.denom * o.numer  # self 분모와 o 분자 곱하기
        ex = Fraction(n, d)  # 나눗셈 값을 ex에 저장
        return ex  # 결과값 반환
    def __truediv__(self, o): # 나눗셈 특수연산자
        n = self.numer * o.denom  # self 분자와 o 분모 곱하기
        d = self.denom * o.numer  # self 분모와 o 분자 곱하기
        ex = Fraction(n, d)  # 나눗셈 값을 ex에 저장
        return ex  # 결과값 반환

    # 곱셈 메쏘드
    def multi(self, o):
        n = self.numer * o.numer  # 분자끼리 곱하기
        d = self.denom * o.denom  # 분모끼리 곱하기
        ex = Fraction(n, d)  # 곱셈 값을 ex에 저장
        return ex  # 결과값 반환
    def __mul__(self, o): # 곱셈 특수연산자
        n = self.numer * o.numer  # 분자끼리 곱하기
        d = self.denom * o.denom  # 분모끼리 곱하기
        ex = Fraction(n, d)  # 곱셈 값을 ex에 저장
        return ex  # 결과값 반환

    # 최대공약수를 이용해 약분을 한다
    def reduction(self):
        # 유클리드 호제법을 사용하기 위해서는 a > b 가 성립되어야 한다
        a = max(self.numer, self.denom)  # 큰 수를 a에 저장
        b = min(self.numer, self.denom)  # 작은 수를 b에 저장

        # 2개의 자연수  a, b에 대해서 a를 b로 나눈 나머지를 r이라 하면(a>b), a와 b의 최대공약수는 b와 r의 최대공약수와 같다
        while (a % b) != 0:  # 유클리드 호제법 실행 ( 나머지가 0이면 조건문 탈출 )
            r = a % b  # 나머지 r
            a = b
            b = r

        n = self.numer // b  # 최대공약수로 분자 나누기
        d = self.denom // b  # 최대공약수로 분모 나누기
        ex = Fraction(n, d)  # 약분된 값을 ex에 저장
        return ex  # 결과값 반환

    # 출력 간단하게 해주는 메쏘드
    def __str__(self):
        return "(" + str(self.numer) + "/" + str(self.denom) + ")"

    # 오퍼레이터 오버로딩(등호) 메쏘드
    def __eq__(self, o): # 같다 특수연산자
        """
        self 와 o가 약분하여 같은 분수면 True 반환
        :param o: 다른 분수
        :return: 약분하여 같은 분수이면 True 반환 아니면 False 반환
        """
        g1 = gcm(self.numer, self.denom) # self 분모와 분자의 최대공약수 구하기
        g2 = gcm(o.numer, o.denom) # other 분모와 분자의 최대공약수 구하기
        if (self.numer // g1 == o.numer // g2) and (self.denom // g1 == o.denom // g2): # 약분된 분자와 분모가 같으면
            return True # 참 반환
        else:
            return False # 거짓 반환
    # 같지 않다 특수연산자
    def __ne__(self, o):
        """
        두 분수가 같으면 True, 아니면 False를 반환
        """
        if (self == o):  # eq 메쏘드에서 오버리딩을 했기 때문에 간단하게 표현 가능
            return False
        else:
            return True
    # 작다 특수연산자
    def __lt__(self, o):
        g1 = self.numer * o.denom # self 분자
        g2 = self.denom * o.numer # other 분자
        if g1 < g2:  # 분모는 같으니깐 분자 크기만 비교
            return True  # 참 반환
        else:
            return False  # 거짓 반환
    # 작거나 같다 특수연산자
    def __le__(self, o):
        if self == o or self < o: # eq, lt 메소드에서 오버리딩을 했기 때문에 간단하게 표현 가능
            return True # 참 반환
        else:
            return False # 거짓 반환
    # 크다 특수연산자
    def __gt__(self, o):
        g1 = self.numer * o.denom # self 분자
        g2 = self.denom * o.numer # other 분자
        if g1 > g2:  # 분모는 같으니깐 분자 크기만 비교
            return True  # 참 반환
        else:
            return False  # 거짓 반환
    # 크거나 같다 특수연산자
    def __ge__(self, o):
        if self == o or self > o: # eq, gt 메소드에서 오버리딩을 했기 때문에 간단하게 표현 가능
            return True # 참 반환
        else:
            return False # 거짓 반환

# 최대공약수를 반환하는 함수
def gcm(x, y):
    # 두 정수 중 큰 수를 x에 저장, 작은 수를 y에 저장
    if y > x:
        temp = y
        y = x
        x = temp
    # 유클리드 호제법에 의해 최대공약수 구함
    while (y > 0):
        r = x % y
        x = y
        y = r
    return x


# 프로그램 시작 부분
f1 = Fraction(4, -5) # 객체들 정의
f2 = Fraction(3, 2)
f3 = Fraction(8, 31)
f4 = Fraction(2, 3)
f5 = Fraction(3, 5)
f6 = Fraction(3, 7)
f7 = Fraction(4, 8)
f8 = Fraction(1, 2)
f9 = Fraction(2, 81)
f10 = Fraction(3, 9)

print(f1, "*", f2, "=", (f1*f2).reduction()) # 곱셈 출력
print(f3, "-", f4, "=", (f3-f4).reduction()) # 뺄셈 출력
print(f5, "+", f6, "=", (f5+f6).reduction()) # 덧셈 출력
if f7 == f8: # f7과 f8이 같으면
    print(f7, "==", f8, "= True") # 결과는 True
else: # 아니면
    print(f7, "==", f8, "= False") # 결과는 False
if f9 >= f10: # f10보다 f9가 크거나 같으면
    print(f9, ">=", f10, "= True") # 결과는 True
else:
    print(f9, ">=", f10, "= False") # 결과는 False