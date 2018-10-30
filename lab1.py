number = "Hi" #number의 타입이 문자열
print(number) #문자열 출력
number = 10 #number에 정수를 저장했으므로, number의 타입이 정수형이 되었음
print(number) #정수형 number를 출력

# 변수 a, b에 값을 저장한 후, 합을 c변수에 저장 후, c를 출력
a = 4
b = 5
c = a+b
#4 + 5 = 9와 같이 출력하라.
msg = "%d + %d = %d" #출력하려는 문자열을 변수로 정의할 수 있다.
print(msg %(a, b, c)) #변수를 여러 개 출력하고 싶을 때, %( , , )를 이용해 순서대로 출력한다.

#문자열 출력
money = 10000
print("나는 현재 %d원을 가지고 있습니다." %money) #서식문자를 이용할 수 있다. ,를 대신해 변수이름 앞에 %를 쓴다.

#입력
money = input("얼마를 가지고 계세요?") #input의 결과값은 문자열
print("입력하신 값은 %s입니다." %money) #input의 결과값이 문자열이기 때문에 money의 타입이 문자열이다. 따라서 %s를 사용한다.