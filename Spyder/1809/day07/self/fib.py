def fib(n):
    a,b,c = 0,1,1
    while c < n:
        a,b = b,a+b
        c += 1
        yield b

m = fib(3)
print(m.__next__())
print(m.__next__())
print(m.__next__())
