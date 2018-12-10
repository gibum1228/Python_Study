"""
M과 N이 주어질 때 M 이상 N이하의 자연수 중 오나전제곱수인 것을 모두 골라 그 합을 구하고 그 중 최솟값을 찾는 프로그램을 작성하라.
예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 완전제곱수는 64,91,100 이렇게 총 3개가 있으므로 그 합은 245가 되고 이 중 최솟값은 64가 된다.
<입력 예>
M: 60
N: 100
<출력 예>
합: 245
최솟값: 64
"""
l = [] # 완전제곱수 담을 리스트 초기화
sum = 0 # 완전제곱수 총합
M = int(input("M: ")) # ~이상
N = int(input("N: ")) # ~이하

for i in range(1, 11) : # 완전제곱수 값이 100까지
    n = i * i # 완전제곱수 n이
    if n >= M and n <= N : # M이상 N이하면
        l.append(n) # 리스트에 n 추가

for j in l : # l 요소 값을 지닌 j
    sum += j # sum에 j를 더한다.

print("합:", sum) # 완전제곱수 총합 출력
print("최솟값:", l[0]) # 작은 수부터 입력받기 때문에 l[0]이 최솟값이다.