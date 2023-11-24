#Find the smallest number m from the Fibonacci sequence, defined by f[0]=f[1]=1, f[n]=f[n-1] + f[n-2], for n > 2, larger than the given natural number n. (e.g. for n = 6, m = 8).

def fib(a,b,n):
    if b>n:
        print(b)
        return
    fib(b,a+b,n)

n=int(input())
fib(1,1,n)