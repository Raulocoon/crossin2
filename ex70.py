sum = lambda a, b, c : a + b + c
print(sum(1, 2, 3))
print(sum(4, 5, 6))

def fn(x):
    return lambda y:x+y

a = fn(2)
print(a(3))