#-*- coding: cp936 -*-
import time
#从epoch到当前的秒数 1516680830.7258022
print("%d" %int(time.time()))

start_time = time.time()
print("start time : %f" %start_time)
for i in range(10):
    print(i)
end_time = time.time()
print("end time : %f" %end_time)
print("total time : %f" %(end_time - start_time))