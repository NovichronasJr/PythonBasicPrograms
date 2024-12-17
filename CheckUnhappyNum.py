"""
Given a number. Check whether it is unhappy or not
"""

def calc(num):
    Sum = 0
    while(num!=0):
        rem = num%10
        Sum = Sum + rem**2
        num = num//10
    return Sum

a = int(input("enter the num"))
count = 0
n = a
while(count < 36):
     a = calc(a)
     count = count+1
     if a == n:
          break
        
    
if n==a:
     print("the number is unhappy")
else:
     print("not unhappy")