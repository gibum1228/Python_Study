"""
８.	정규식을 사용하려고 한다. 정규식을 사용하기 위해  #의 밑줄 친 곳에 포함해야 하는 표현을 써라.
９.	#9에 의해 출력되는 값을 써라.
１０.	#10에 의해 출력되는 값을 써라.
１１.	#11에서 문자열 s를 :을 기준으로 분리하여 아래와 같이 출력하려고 한다. 이를 위한 코드를 써라.
(출력)
['SungKongHoe University', ' 2018']
"""

import re #8

s="SungKongHoe University: 2018"
r=re.compile("\d+")
result=r.search(s)
print()

print(result.span()) #9
print(result.group()) #10

#11
m = re.split(": ",s)
print(m)

