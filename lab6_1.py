"""
챕터: Day 6
주제: class
문제:
숫자를 하나씩 발생시키는 Counter 클래스 정의
작성자: 김기범
작성일: 2018.10.18.
"""

# Counter 클래스 정의, instance는 아직 생성되지 않음
class Counter :
    def __init__(self, start = 0):
        """
        특별한 메소드이다.
        instance를 생성할 때 초기화하는 메소드, instance를 생성할 때 자동 호출됨
        :param start:
        """
        self.count = start

    def reset(self):
        """
        카운터를 초기화하는 메소드
        self: method가 수행되는 instance 자신을 의미
        :return:
        """
        self.count = 0 # count는 instance variable(member)

    def increment(self):
        """
        카운터를 하나 증가시킴
        :return:
        """
        self.count += 1 # count를 1 증가

    def get(self):
        """
        count 값을 반환
        :return:
        """
        return self.count

# 실행 코드 시작
# class Counter의 instance를 생성해서 변수 a의 저장
a = Counter() # Counter는 클래스 이름, ()가 있어야 한다, __init(self)__가 호출됨, 디폴트값 0

# class Counter의 instance를 생성해서 변수 b의 저장, 매개변수를 포함하는 __init함수가 호출됨
b = Counter(10)

a.reset() # 변수에 "."을 이용하여 메소드 호출, a가 self 매개변수값이 되어 넘어감
a.increment()
a.increment()
a.increment()
print("a = %d" %a.get())

print("b = %d" %b.get())