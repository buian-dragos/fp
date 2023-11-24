#Generate the largest perfect number smaller than a given natural number n. If such a number does not exist, a message should be displayed. A number is perfect if it is equal to the sum of its divisors, except itself. (e.g. 6 is a perfect number, as 6=1+2+3).

def isPerfect(x):
    s=0
    d=1
    while d < x:
        if x%d==0:
            s=s+d
        d=d+1
    if s==x:
        return True
    return False

n=int(input())
n=n-1
while True:
    if isPerfect(n):
        print(n)
        break
    n=n-1
    if n==0:
        print("Such a number does not exist")
        break