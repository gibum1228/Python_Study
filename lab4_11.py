"""
챕터: Day 4
주제: 반복문(for 문)
문제:
사용자로부터 5개의 숫자를 입력받아, 이를 리스트에 저장한 후 합과 평균을 구하여 출력한다.
작성자: 김기범
작성일: 2018.09.27.
"""
l = [] # l 초기화
sum = 0 # sum 초기화

for i in range(0, 5) : # i는 0부터 4
    l.append(int(input())) # l에 입력받은 수를 저장

for add in l : # add에 l 값 대입
    sum += add # sum에 add 더하기

average = sum / len(l) # 평균 구하기

print("%d %f" %(sum, average)) # 합과 평균 출력