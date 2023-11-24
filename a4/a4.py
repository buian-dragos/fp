import random

list = []
n = 30
for i in range(0, n):
    list.append(random.randint(0, 999))
print(list)

def verif(frecv1,frecv2):       #checks if 2 numbers have at least 1 common digit
    for i in range(10):
        if frecv1[i]==frecv2[i] and frecv1[i]==1:
            return True
    return False

def frec(frecv,cop):            #saves the digits of a number in a list
    for j in range(0, 10):
        frecv[j] = 0
    # print(frecv1)
    while cop > 0:
        frecv[cop % 10] = 1
        cop //= 10
    return frecv

def iterativ(list):         #iterative version of the program
    secv=0
    frecv1=[]
    frecv2=[]
    for i in range(0,10):
        frecv1.append(0)
        frecv2.append(0)
    for i in range(0,n):
        #print(secv)
        if secv==0:
            frec(frecv1,list[i])
            secv=1
            #print(frecv1,"1")
        else:
            frec(frecv2,list[i])
            #print(frecv2,"2")
            if i > 0 and list[i - 1] < list[i] and verif(frecv1, frecv2):
                #print(frecv1)
                #print(frecv2)
                secv += 1
                frecv1=frecv2.copy()
            else:
                if secv>1:
                    for j in range(i-secv,i):
                        print(list[j],end=" ")
                    print()
                secv=1
                frecv1=frecv2.copy()


def recursiv(list,i,n,secv,frecv1,frecv2):     #recursive version of the program
    if i==n:
        return
    else:
        if secv==0:
            frec(frecv1,list[i])
            recursiv(list,i+1,n,1,frecv1,frecv2)
        else:
            frec(frecv2,list[i])
            if i > 0 and list[i - 1] < list[i] and verif(frecv1, frecv2):
                frecv1=frecv2.copy()
                recursiv(list, i + 1, n, secv+1, frecv1, frecv2)
            else:
                if secv>1:
                    for j in range(i-secv,i):
                        print(list[j],end=" ")
                    print()
                frecv1=frecv2.copy()
                recursiv(list,i+1,n,1,frecv1,frecv2)

print("Iterative results:")
iterativ(list)
frecv1=[]
frecv2=[]
for i in range(0,10):
    frecv1.append(0)
    frecv2.append(0)
print("Recursive results:")
recursiv(list,0,n,0,frecv1,frecv2)



