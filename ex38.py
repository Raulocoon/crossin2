from math import pi as math_pi
import random

print(math_pi)
print(dir(random))

boolValue = True
guessTimes = 0
while boolValue:
    print("请输入你的幸运数字")
    num = int(input())
    guessTimes += 1

    if num == 2:
        print("--- 恭喜，你赢得了一辆奔奔！（你猜了%d次）" %guessTimes)
        break;
        boolValue = False
    else:
        continue