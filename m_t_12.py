"""
１２.	아래 두 함수를 정의한다.
①	여러 개의 숫자를 매개변수로 받아서, 해당 숫자 중에 가장 큰 값을 반환하는 max. 어떤 개수의 숫자가 매개변수로 넘어와도 작동해야 한다.
②	여러 개의 숫자를 매개변수로 받아서, 해당 숫자 중에 가장 작은 값을 반환하는 min. 어떤 개수의 숫자가 매개변수로 넘어와도 작동해야 한다.
max(6, 8, 9, -10, 4), min(6, 8, 9, -10, 4)를 호출하여 출력
     <출력 예>
      최대값: 9
      최소값: -10
"""
def max(*a) :
    max_num = a[0]
    for i in a :
        if max_num < i :
            max_num = i
    return max_num

def min(*b) :
    min_num = b[0]
    for j in b :
        if min_num > j :
            min_num = j
    return min_num

print("최대값:", max(6, 8, 9, -10, 4))
print("최소값:", min(6, 8, 9, -10, 4))