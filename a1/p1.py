#Generate the first prime number larger than a given natural number n.

def isPrime(x):
    d=3
    if x==2:
        return True
    if x<2 or x%2==0:
        return False
    while d < x:
        if x%d==0:
            return False
        d=d+2
    return True

n=int(input())
n=n+1
while True:
    if isPrime(n):
        print(n)
        break
    n=n+1