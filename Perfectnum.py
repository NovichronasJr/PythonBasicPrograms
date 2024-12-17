"""
Given a number. Check whether the number is a perfect number.
"""

def findPerfect(num):
    a = []
    for i in range (1,num//2+1,1):
        if num%i == 0:
            a.append(i)

    return sum(a)

a = int(input("enter a num : "))
if a == findPerfect(a):
    print("num is a perfect num")

else:
    print("it is not a perfect num")