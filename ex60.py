# -*- coding: cp936 -*-
import random

print("randint > %d"  %random.randint(1,100))
#生成一个0到1之间的随机浮点数
print("random > %d"  %random.random())
#生成a、b之间的随机浮点数
print("uniform > %d"  %random.uniform(1.5, 9.5))
#从序列中随机选取一个元素。seq需要是一个序列，比如list、元组、字符串。
print("choice list > %r" %random.choice([1, 2, 3, 5, 8, 13]))
print("choice string > %r" %random.choice("hello world"))
print("choice list > %r" %random.choice(['hello', 'world']))
print("choice tuple > %r" %random.choice((1, 2, 3, 4, 5)))
#生成一个从start到stop（不包括stop），间隔为step的一个随机数。
print("randomrange > %r" %random.randrange(1, 9, 2))
#从population序列中，随机获取k个元素，生成一个新序列。sample不改变原来序列。
sampleList = [1, 2, 3, 4, 5, 6]
print("sample > %r" %random.sample(sampleList, 3))
print("sampleOriginal > %r" %sampleList)
#把序列x中的元素顺序打乱。shuffle直接改变原有的序列
myList = [1, 2, 3, 4, 5, 6]
print(myList)
random.shuffle(myList)
print("shuffle > %s" %myList)
#seed() 方法改变随机数生成器的种子，可以在调用其他随机模块函数之前调用此函数。
random.seed(10)
print(random.random())