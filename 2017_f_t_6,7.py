"""
６.	사용자로부터 입력을 받아서, 만약 숫자가 아니라면 ValueError 오류를 발생시키려고 한다. #6의 밑줄 친 곳에 알맞은 표현을 써라.
７.	6을 완성하기 위해 #7의 밑줄 친 곳에 알맞은 표현을 써라.
"""

try: #6
    m=int(input("M:"))
    n=int(input("N:"))
except ValueError: #7
    print("숫자가 아닙니다.")

