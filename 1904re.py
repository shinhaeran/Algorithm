n = int(input())

def fibo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        # return fibo(n-1) + fibo(n-2)
        a,b = 1,2
        c = 0
        for _ in range(3,n+1):
            c = (a+b) % 15746
            a,b = b,c
        return c

print(fibo(n))