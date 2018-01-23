from functools import reduce
sum=0
for i in range(1, 101):
    sum += i
print(sum)

lst=range(1, 101)
def add(x, y):
    return x + y
print(reduce(add, lst))

lst_1 = range(1, 101)
print(reduce(lambda x,y:x+y, lst_1))
