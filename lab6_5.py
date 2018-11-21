"""
챕터: Day 6
주제: class 상속/계승(inheritance)
문제:
작성자: 김기범
작성일: 2018.11.08.
"""
"""
사람 클래스를 정의한다. 이름과 나이를 (data) attribute로 가지고 있다.
이름과 나이를 매개변수로 받는 생성자가 있다.
나이를 1살 더하는 getOler 메소드가 있다.
문자열 반환, 프린트 메소드
"""
class Person:
    def __init__(self, name, age): # 생성자
        self.n = name # 이름
        self.a = age # 나이

    def getOlder(self): # 한 살 더해주는 메소드, Person.getOlder(객체이름)으로 호출 가능
        self.a += 1

    def print(self): # 이름과 나이를 출력하는 메소드
        print(self) # __str__를 정의해서 간단하게 출력 가능

    def __str__(self): # 이름과 나이가 담긴 문자열을 반환하는 특수연산자
        return "이름: " + str(self.n) + ", 나이: " + str(self.a)

"""
사람을 계승하는 학생 클래스를 정의한다. 학교와 학년, 학번을 data attribute로 가지고 있다.
이름, 나이, 학년, 학번을 받는 생성자가 있다. 생성자 내에서 사람의 생성자(Person.__init__)를 호출한다
학년을 진급하는 upgrade() 메소드가 있다
문자열 반환(override), 프린트 메소드
"""
class Student(Person): # Student 클래스는 Person 클래스를 계승한다
    def __init__(self, name, age, grade, snum):
        """
        이름, 나이, 학년, 학번을 받는 생성자
        """
        """
        생성자 내에서 사람의 생성자(Person.__init__)를 호출한다
        Student도 일종의 Person이다
        Person이라서 가지고 있는 attribute면 age와 name은
        Person의 생성자(__init__)를 통해 초기화한다
        """
        Person.__init__(self, name, age) # 사람의 생성자를 호출
        """
        학번과 학년은 Student의 생성자 내에서 초기화
        """
        self.g = grade
        self.sn = snum
        self.school = "성공회대학교"

    def upgrade(self): # 1학년 진급하는 메소드
        self.g += 1

    def __str__(self):
        """
        Person 클래스에서 정의된 __str__를 overriding(재정의)한다
        :return: 문자열
        """
        s = Person.__str__(self) # Person 클랫의 __str__를 먼저 호출한 후 문자열 연결 예정
        return s + "\n" + "학교: " + self.school + ", 학년: " + str(self.g) + ", 학번: " + self.sn

    def print(self):
        """
        Person 클래스에 정의된 print()를 overriding(재정의)한다
        """
        print(self)

# 코드 실행 부분
# 두 명의 Person instrance르 만들어서 나이를 한 살 올린 후 출력한다
p1 = Person("김일수", 123) # 두 개의 객체 생성
p2 = Person("김이수", 80)

p1.getOlder() # 메소드를 각각 호출함
p2.getOlder()
# p1.upgrade() # p1은 Student가 아니므로, upgrade() 메소드를 사용할 수 없다

print(p1) # __str__ 특수연산자로 간단하게 출력
print(p2)
p1.print() # print()로 출력
p2.print()

# 두 명의 Student instrance를 만든다
s1 = Student("김삼수", 20, 2, "203222123")
s2 = Student("김사수", 21, 3, "202232453")

s1.getOlder() # s1은 Student인데 Person을 계승했으므로 Person의 메소드 사용이 가능하다
s1.upgrade()
s1.print() # s1은 Student인데 Person을 계승했으므로 Person의 메소드 사용이 가능하다

# Person과 Student를 포함하는 리스트 생성
l = [p1, p2, s1, s2]
for a in l:
    a.getOlder()
    a.print()