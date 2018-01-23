#-*- coding ：cp936 -*-
#变量前加上星号前缀（*），调用时的参数会存储在一个 tuple（元组）对象中，赋值给形参
def calcSum(*args):
    sum = 0
    for i in args:
        sum += i

    print(sum)

calcSum(1,2,3)
calcSum(123,456)
calcSum()


def printAll(*args):
    for i in args:
        print(i)

    print()

printAll(1,2,3)
printAll(3,2,1)

# func(*args) 方式是把参数作为 tuple 传入函数内部。而 func(**kargs) 则是把参数以键值对字典的形式传入。
def printAll2(**kargs):
    for k in kargs:
        print(k , " : " , kargs[k] )


printAll2(a=1, b=2, c=3)
printAll2(x=4, y=5)