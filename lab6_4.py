"""
챕터: Day 6
주제: class, class variable(클래스 당 1개), default 매개변수, operator overloading 복습
문제: 정수집합 클래스
작성자: 김기범
작성일: 2018.11.06.
"""
"""
Student 클래스를 정의한다. 다음 학생에게 줄 학번을 클래스 변수(class variable) tag로 정의한다.
(메소드와 같은 레벨에서 변수를 정의하면 클래스 변수가 된다. self가 필요 없다.)
"""
class Student:
    tag = 1 # 다음 학생에게 줄 학번, 모든 instrance가 공유하여 사용, class variable(member)
    def __init__(self, name, grade = 1):
        """
        이름, 학년을 매개변수로 받는다.
        grade는 학년을 매개변수로 받지 않는 경우, 1학년이 default이다.
        :return: 없음
        """
        # 매개변수 값을 self 멤버(instrance variable)에 배정한다
        self.name = name
        self.grade = grade
        # 클래스 변수인 tag의 값을 학번으로 배정
        self.snum = Student.tag
        Student.tag += 1

    def __str__(self):
        return "학번:" + str(self.snum) + " 이름:" + self.name + " 학년:" + str(self.grade)

    """
    Student 클래스에 학년을 올리는 upgrade()라는 메쏘드를 정의한다.
    self를 매개변수로 받는다. 몇 학년을 올릴지를 매개변수로 받는다. 1년 올리는 것이 디폴트이다.
    """
    def upgrade(self, up = 1):
        """
        진급시킨다, 4학년인 경우, 진급시키지 않고 '%s는 졸업 예정 학생입니다'를 출력(%s에는 학생 이름)
        :param up: up이 매개변수로 넘어오면, up 만큼 진급, 아니면 1학년 진급
        """
        if self.grade == 4:
            print("%s는(은) 졸업 예정 학생입니다." %self.name)
        else:
            self.grade += up

    """
   Student 클래스에 __eq__ 메소드를 정의한다. 이름을 비교하여 같은 학생이면 True, 아니면 False를 반환한다.
    """
    def __eq__(self, o):
        if self.name == o.name:
            return True
        else:
            return False

# 실행부 시작
# 학생 인스턴스 2개 생성
s1 = Student("김일수", 4)
s2 = Student("김이수", 2)
s3 = Student("김삼수")

# 3명의 학생 인스턴스 값을 출력
print("====초기 값 출력====")
print(s1)
print(s2)
print(s3)

# s2의 학년을 한 학년 높인다.(매개변수 안 보내기)
s2.upgrade()
# s3의 학년을 2 학년 높인다.(매개변수 보내기)
s3.upgrade(2)
# 진급 후의 학생 정보 출력
print("====진급 후 출력====")
print(s1)
print(s2)
print(s3)

# list에 3학생 정보 저장하기
l = []
l.append(s1)
l.append(s2)
l.append(s3)
l.append(Student("김사수")) # 리스트의 요소(elenent)를 직접 생성하여 배정, 클래스 변수 불필요

print("====리스트에 있는 요소 출력====")
for s in l:
    s.upgrade() # 리스트에 있는 요소의 데이터타입이 Student이므로, Student의 메소드를 호출할 수 있다
    print(s)

# s5 학생의 이름은 "김일수"로 생성
s5 = Student("김일수")
# s1과 s5가 같은 학생인지를 검사여 결과를 출력
if s1 == s5:
    print("같은 학생입니다.")
else:
    print("다른 학생입니다.")
# s6에 s1을 배정
# s6과 s1이 같은 학생인지 검사하여 결과를 출력
s6 = s1
if s1 == s6:
    print("같은 학생입니다.")
else:
    print("다른 학생입니다.")

# 인스턴스의 멤버를 외부에서 직접 수정할 수 있다.
# 권장하지 않는다.
# 인스턴스의 멤버는 자신의 메소드에서 수정하는 것이 옳다.
# encapsulation
s1.name = "이일수" # 기본으로 Public이고 s1.__name라고 하면 private가 된다
print(s1)