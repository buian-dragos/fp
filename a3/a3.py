import random
import timeit

def isSorted(list):
    n=len(list)
    for i in range(0,n-1):
        if list[i]>list[i+1]:
            return False
    return True

def genratePermutation(list):
    n=len(list)
    for i in range(0,n):
        r=random.randint(0,n-1)
        list[i], list[r]= list[r], list[i]
def permutationSort(list):
    s=1
    while isSorted(list)==False:
        genratePermutation(list)


def gnomeSort(list):
    s=1
    k = 0
    n=len(list)
    while k < n:
        if k == 0:
            k = k + 1
        if list[k] >= list[k - 1]:
            k = k + 1
        else:
            list[k], list[k - 1] = list[k - 1], list[k]
            k = k - 1

def bestCaseList(list,n):
    for i in range(0,n):
        list.append(i)

def worstCaseList(list,n):
    for i in range(0,n):
        list.append(n-i)


n=int(input("List size:"))
list=[]
print("1.Permutation sort - best case")        #best case is an already sorted array since the complexity is linear
print("2.Permutation sort - worst case")       #worst case is any array that isn't already sorted
print("3.Gnome sort - best case")              #best case is an already sorted array since the complexity is linear
print("4.Gnome sort - worst case")             #worst case is an array sorted in reverse order
menu = int(input("Choose an option:"))
print(menu)
if  menu==1:
    bestCaseList(list, n)
    start=timeit.timeit()
    permutationSort(list)
    end=timeit.timeit()
    print(end-start)
    print("Linear complexity")
if  menu==2:
    worstCaseList(list, n)
    start = timeit.timeit()
    permutationSort(list)
    end = timeit.timeit()
    print(end - start)
    print("Random complexity")
elif menu==3:
    bestCaseList(list, n)
    start = timeit.timeit()
    gnomeSort(list)
    end = timeit.timeit()
    print(end - start)
    print("Linear complexity")
elif menu==4:
    worstCaseList(list, n)
    start = timeit.timeit()
    gnomeSort(list)
    end = timeit.timeit()
    print(end - start)
    print("n squared complexity")
