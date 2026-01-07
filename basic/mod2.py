# 모듈 불러오기
import mod1

print(f"3 + 4 = {mod1.add(3, 4)}")
print(f"6 -2 = {mod1.sub(6, 2)}")


# 혹은 이렇게도 가능
from mod1 import add, sub

print(f"3 + 4 = {add(3, 4)}")
print(f"6 - 2 = {sub(6, 2)}")
