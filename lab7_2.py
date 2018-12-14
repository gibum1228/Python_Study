"""
챕터: Day 7
주제: os 모듈 사용
문제:
사용자가 입력한 디렉토리(1)로 이동한 후, 사용자가 입력한 이름의 새 디렉토리를 생성하라
사용자가 입력한 디렉토리(2)아래에 test 디렉토리를 생성하라.
사용자가 입력한 디렉토리를 포함하여 해당 디렉토리(2)와 test 디렉토리를 삭제하라.
삭제가 끝난 후, 사용자가 입력한 디렉토리(1)의 부모 디렉토리의 파일 목록을 출력하라

작성자: 김기범
작성일: 2018.12.04.
"""

import os  # os 수입

try:
    print(os.getcwd())  # 현재 디렉토리 출력
    moveFile = input("이동할 디렉토리: ")  # 이동할 디렉토리 주소 입력 받기
    os.chdir(moveFile)  # (1) 디렉토리로 이동

    newFile = input("생성할 파일 이름: ")  # 생성할 파일 이름 입력 받기
    os.mkdir(newFile)  # (1) 디렉토리에 생성

    os.chdir(newFile)  # (2) 디렉토리로 이동
    os.mkdir("test")  # test 파일 생성

    fullFile = moveFile + "\\" + newFile + "\\test"  # test 디렉토리 경로
    print("test 경로: " + fullFile)  # test 경로 출력
    os.chdir(moveFile)  # (1) 디렉토리로 이동
    os.removedirs(fullFile)  # (1) 디렉토리를 기준으로 하위 폴더 전부 삭제
    moveFile = os.chdir("..")  # (1) 디렉토리의 부모 디렉토리로 이동

    l = os.listdir(moveFile)  # (1) 디렉토리의 부모 디렉토리가 가지고 있는 파일 목록 출력
    for i in l:  # 출력
        print(i)

except FileNotFoundError:  # 입력한 디렉토리가 없는 오류가 발생한 경우
    print("존재하지 않는 주소입니다.")
    exit()
except Exception:  # 오류의 부모 > 어떤 오류든 발생했을 때
    print("알 수 없는 오류가 발생했습니다.")
    exit()

"""
os.path 모듈
isdir() 폴더가 존재하는지 판단
isfile() 대소문자 구분하기 때문에 isfile로 사용, 파일이 존재하는지 판단
exists() 파일이나 폴더가 유무하는지 판단
getsize() 파일 크기 반환
split() 파일 이름을 떼어낸다
splitext() 확장자명만 떼어낸다
join() 파일 이름과 폴더 이름 합치기, split로 나눈 것을 다시 합치기
"""