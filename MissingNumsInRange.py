"""
Given an integer n denoting the range from 0 to integer n-1. Read any three numbers within this range and 
find the missing numbers <---( all other numbers except for the one's which are read)
"""

n = 10
a = []
for i in range(0,3,1):
    b = int(input("enter the num :"))
    a.append(b)

b = [i for i in range(0, n, 1)]

b = set(b)
print(b)
a = set(a)
print(a)

print(b.difference(a))


