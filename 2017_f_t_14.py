"""
１４.	문자열 S가 주어졌을 때, S의 서로 다른 부분 문자열을 구하여 substring.txt 파일에 한 줄에 하나씩 저장하는 프로그램을 작성하라.
①	부분 문자열은 S에서 연속된 일부분을 말하며, 길이가 1보다 크거나 같아야 한다.
(입력 예) ababc
(파일 저장) a, b, a, b, c, ab, ba, ab, bc, aba, bab, abc, abab, babc, ababc와 같은 12개의 부분 문자열이 substring.txt에 한 줄에 하나씩 저장되어야 한다.
"""

f = open("substring.txt", "w") # 파일 오픈
count = 0 # 출력 문자 크기
S = input("문장 입력: ") # 원하는 문자열 입력

for i in range(0, len(S)): # 문자열 크기 만큼
    a = 0
    b = 1
    for j in range(0, len(S)-count):
        f.write(S[a:b+count] + "\n") # 슬라이싱 a:b+count 범위를 출력
        a += 1 # 하나씩 증가
        b += 1
    count += 1 # 카운트 증가

f.close() # 파일 닫기