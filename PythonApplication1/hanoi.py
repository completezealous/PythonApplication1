def func3(x):
    if x>0:
        print(x)
        func3(x-1)
print(func3(3))

def fun4(x):
    if x>0:
        fun4(x-1)
        print(x)
print(fun4(3))

'''def hanoi(n, a, b, c):
    if n>0:
        hanoi(n-1, a, c, b)
        print("moving from %s to %s" % (a, c))
        hanoi(n-1, b, a, c)

hanoi(30, 'A', 'B', 'C')'''
