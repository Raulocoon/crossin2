# -*- coding: cp936 -*-
import random

print("randint > %d"  %random.randint(1,100))
#����һ��0��1֮������������
print("random > %d"  %random.random())
#����a��b֮������������
print("uniform > %d"  %random.uniform(1.5, 9.5))
#�����������ѡȡһ��Ԫ�ء�seq��Ҫ��һ�����У�����list��Ԫ�顢�ַ�����
print("choice list > %r" %random.choice([1, 2, 3, 5, 8, 13]))
print("choice string > %r" %random.choice("hello world"))
print("choice list > %r" %random.choice(['hello', 'world']))
print("choice tuple > %r" %random.choice((1, 2, 3, 4, 5)))
#����һ����start��stop��������stop�������Ϊstep��һ���������
print("randomrange > %r" %random.randrange(1, 9, 2))
#��population�����У������ȡk��Ԫ�أ�����һ�������С�sample���ı�ԭ�����С�
sampleList = [1, 2, 3, 4, 5, 6]
print("sample > %r" %random.sample(sampleList, 3))
print("sampleOriginal > %r" %sampleList)
#������x�е�Ԫ��˳����ҡ�shuffleֱ�Ӹı�ԭ�е�����
myList = [1, 2, 3, 4, 5, 6]
print(myList)
random.shuffle(myList)
print("shuffle > %s" %myList)
#seed() �����ı�����������������ӣ������ڵ����������ģ�麯��֮ǰ���ô˺�����
random.seed(10)
print(random.random())