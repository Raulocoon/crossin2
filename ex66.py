# -*- coding: cp936 -*-
list_1 = [1, 2, 3, 5, 8, 13, 22]
list_2 = []

for i in list_1:
    if i % 2 == 0:
        list_2.append(i)

print(list_2)

list_3 = [i for i in list_1 if i % 2 == 0]
print(list_3)

#用一行 Python 代码实现：把1到100的整数里，能被2、3、5整除的数取出，以分号（;）分隔的形式输出。
myList = []
for i in range(1, 101):
    if i % 2 ==0 or i % 3 == 0 or i % 5 == 0:
        myList.append(i)
print(myList)

myList2 = [str(i) for i in range(1, 101) if i % 2 ==0 or i % 3 == 0 or i % 5 == 0]
print(';'.join(myList2))