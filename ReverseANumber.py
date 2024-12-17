"""
Reverse the given number.
"""

def Rev(num):
    Sum = 0
    while(num!=0):
        rem = num%10
        Sum = Sum*10+rem
        num = num//10
    return Sum

a = int(input("enter the num :"))
ans = Rev(a)
print(ans)


