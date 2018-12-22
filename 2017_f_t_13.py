"""
１３.	사용자로부터 이동할 디렉토리를 입력받아 아래를 실행한다.
①	입력된 디렉토리로 이동한 후
②	해당 디렉토리의 이름을 os의 메쏘드를 이용하여 출력하고,
③	해당 디렉토리 아래에 있는 모든 파일 목록을 한 줄에 하나씩 출력하라.
④	만약, 입력한 디렉토리가 존재하지 않는다면, “입력한 디렉토리는 존재하지 않습니다.”를 출력한다. 반드시 FileNotFoundError를 이용하여 Exception으로 처리하라.
(입력 예)
이동할 디렉토리:D:\download
(출력 예)
현재 디렉토리: D:\download
===현재 디렉토리내의 파일 목록===
database
jdk-8u11-windows-i586-demos.zip
jdk-8u11-windows-i586.exe
KakaoTalk_Setup.exe
"""

import os # os를 수입

try:
    moveFile = input("이동할 디렉토리:") # 이동할 디렉
    os.chdir(moveFile)

    print("현재 디렉토리:", os.getcwd())

    print("===현재 디렉토리내의 파일 목록===")
    for i in os.listdir(moveFile):
        print(i)
except FileNotFoundError:
    print("입력한 디렉토리는 존재하지 않습니다.")