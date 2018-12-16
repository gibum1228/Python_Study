"""
챕터: Day 7
주제: os.path 모듈 사용
문제:
A. 프로그래밍이 아닌 수작업으로 C:\temp 디렉토리에 자신의 학번에 해당하는 디렉토리를 생성한 후, 임의의 파일을 3개 복사한다.
학번 디렉토리 아래에 room1 디렉토리를 만들어서 임의의 파일을 3개 복사한다.
room1 밑에 room2 디렉토리를 만들어서 임의의 파일을 3개 복사한다. 자신의 학번 아래 room3 디렉토리를 만든다.
- 여러 번 테스트하기 위해, 매번 생성하는 번거로움을 피하게 다른 디렉토리에 복사본을 만들어 놓는다

B. 아래를 프로그래밍한다
1. C:\temp 아래의 자신의 학번 디렉토리 아래에 있는 모든 파일과 디렉토리를 삭제해라.
디렉토리인지 확인한 후, 디렉토리라면 해당 디렉토리 내에 있는 모든 파일을 삭제한 후, 해당 디렉토리를 삭제하라.
2. 프로그램 실행 후 학번 아래에 파일과 디렉토리가 없음을 확인하라. 어떤 디렉토리 구조에서도 작동할 수 있게 프로그래밍하라.

작성자: 김기범
작성일: 2018.12.06.
"""
import os.path # os.path 수입
import os # os 수입

def clearfile(delPath): # 파일 정리하는 함수
    os.chdir(delPath) # 주소 옮기기
    while(bool(os.listdir())): # 파일과 디렉토리를 가지고 있으면
        l = os.listdir() # 현재 주소 아래에 있는 파일 및 디렉토리를 l에 list로 저장
        for i in l: # 파일인지 디렉토리인지 확인하기
            if os.path.isdir(i): # 디렉토리라면
                clearfile(i) # 함수 재호출
            else: # 아니면
                os.remove(i) # 파일 삭제
    if os.getcwd() == snumpath: # 현재 주소가 학번 파일이면
        exit() # 프로그램 종료
    os.chdir("..") # 상위 디렉토리로 이동
    os.rmdir(delPath) # 디렉토리 삭제


try: # 예외처리 try, except
    os.chdir("C:\\Temp") # Temp 디렉토리로 이동

    snum = input("학번: ") # 자신이 찾는 디렉토리 입력받기
    snumpath = os.getcwd() + "\\" + snum # 입력받은 디렉토리 주소
    print("현재 주소: " + snumpath) # 현재 주소 출력

    clearfile(snumpath) # 파일 정리하는 함수 호출

except FileNotFoundError: # 파일을 찾지 못 하면
    print("존재하지 않는 디렉토리입니다.")
except Exception: # 에러가 뜬다면
    print("알 수 없는 오류입니다.")