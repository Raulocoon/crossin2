#(021)88776543
#010-55667890
#02584453362
#0571 66345673
#(02188776543
import re

f = open("num.txt")
content = f.read()
f.close()

result = re.findall("\(?0\d{2,3}[) -]?\d{7,8}", content)
#(02188776543 -- guolv
result2 = re.findall("0\d{2,3}[ -]?\d{7,8}|\(0\d{2,3}\)\d{7,8}", content)
result3 = re.findall("\(0\d{2,3}\)\d{7,8}|0\d{2,3}[ -]?\d{7,8}", content)

if result:
    print(result)
else:
    print("not found!")

if result2:
    print(result2)
else:
    print("not found2!")

if result3:
    print(result3)
else:
    print("not found3!")
