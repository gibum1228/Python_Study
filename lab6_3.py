"""
챕터: Day 6
주제: class
문제:
fraction 클래스는 애트리뷰트로 numer(분자)와 denom(분모)을 가진다. 초기화하는 메쏘드를 정의하라.
작성자: 김기범
작성일: 2018.10.23.
"""

# 분수 클래스 정의
class Fraction :
    def __init__(self, n, d) :
        """
        분수를 초기화하는 메쏘드
        :param n: 분자에 해당하는 값
        :param d:  분모에 해당하는 값
        """
        self.numer = n
        self.denom = d

    def print(self):
        print("%d/%d" %(self.numer,self.denom))

    # 분자를 반환하는 메쏘드 getNumer 정의
    def getNumer(self):
        return self.numer
    # 분모를 반환하는 메쏘드 getDenom 정의
    def getDenom(self):
        return self.denom

    # 값을 수정하는 메쏘드 setNumer, setDenom 정의
    def setNumer(self, n):
        self.numer = n
    def setDenom(self, d):
        self.denom = d

    # 분수의 더하기
    def add(self, other):
        """
        self에 other를 더하여 결과 값을 반환
        self 값을 변경하지 않는다
        :param other: self에 더할 분수
        :return: 더한 결과값을 저장한 Fraction을 반환
        """
        # 분자 계산
        n = (self.numer * other.denom) + (other.numer * self.denom)
        # 분모 계산
        d = self.denom * other.denom
        fr = Fraction(n, d) # 결과값을 담을 fr 생성
        return fr
# 클래스 정의 끝


# 실행 코드 시작
half = Fraction(1, 2) # 1/2 분수 객체 생성하여 half에 저장
                      # class Fraction의 __init__메쏘드가 호출됨
half.print() # self 매개변수에는 half가 직접 전달

# 분수 2/7을 저장하는 변수 f1 정의
f1 = Fraction(2, 7)
# 분수 2/7을 저장하는 변수 f1을 출력
f1.print()

# 분수 1/8을 저장하는 변수 f2를 정의
f2 = Fraction(1, 8)
# f2의 분자를 가져와서 다음 형식으로출력
# 분자: 1
print("분자:", f2.getNumer())
# f2의 분모를 가져와서 다음 형식으로 출력
# 분모: 8z
print("분모:",f2.getDenom())

# f2의 타입을 출력
print(type(f2)) # f2의 타입은 class
# 어떤 타입의 인스턴스인지 불리언 값을 반환하는 isinstance() 함수를 호출하여 결과 출력
print(isinstance(f2, Fraction)) # 실생활에서 타입을 구분할 때 많이 쓰인다

# f2를 2/8로 수정
f2.setNumer(2) # 함수로 수정하는 것보다 메쏘드로 수정하는 것이 더 안전하고 좋다
f2.print()
# 클래스는 알약에 꽁꽁 싸매어 있다고 해서 encapsulation라고 한다.

# f1과 f2를 더한 결과를 출력
f1.add(f2).print() # f1.add(f2) == fr이니깐 fr.print()와 같다
# f1.add()의 반환 타입이 Fraction이므로 Fraction의 메쏘드인 print() 수행 가능