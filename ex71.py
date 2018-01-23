# -*- coding:cp936 -*-
lst_1 = [1,2,3,4,5,6]
lst_2 = []

#1
for i in lst_1:
    lst_2.append(i * 2)
print(lst_2)

#2
lst_3 = [i * 2 for i in lst_1]
print(lst_3)

#3
def double_func(x):
    return x * 2

lst_4 = map(double_func, lst_1)
print(list(lst_4))

#4
lst_5 = map(lambda x:x*2, lst_1)
print(list(lst_5))

#
lst_6 = [1,3,5,7,9,11]
lst_7 = map(lambda x, y : x + y, lst_1, lst_6)
print(list(lst_7))


#
lst_8 = [1,2,3,4,5,6]
lst_9 = [1,3,5,7,9,11]
lst_10 = map(None,lst_8)
print(list(lst_10))
