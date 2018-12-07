"""
9.
매개변수로 넘어온 자연수가 소수인지 여부를 판별하여, 소수이면 True, 아니면 False를 반환하는 함수 is_prime을 정의하라. 2,3,5,7,11,13 등
1과 자기자신이외의 약수가 없는 자연수를 소수라 한다.
"""
def is_prime(a) : # 매개변수 값을 a에 저장
    count = 0 # 약수를 담을 변수 count 초기화
    for i in range(1, a+1) : # 1~a까지 반복
        if a % i == 0 : # a 나누기 i 의 나머지가 0이라면
            count += 1 # i가 a의 약수이기 때문에 count ++
    if count == 2 : # 소수는 count가 2
        return True # True 반환
    else : # 아니면
        return False # False 반환

a = int(input("숫자 입력: ")) # 숫자 입력
print(is_prime(a)) # 인수 전달