# 函数的默认参数
def Hello(name = "world"):
    print("Hello " + name)

Hello()
Hello("python")

#当函数有多个参数时，如果你想给部分参数提供默认参数，那么这些参数必须在参数的末尾。
def addResult(a, b=3, c=5):
    return a + b + c

print(addResult(1))   #9
print(addResult(1, 2)) #8