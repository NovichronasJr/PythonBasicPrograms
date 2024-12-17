"""
Find GCD of two numbers
"""

def cal(a,b):
    if a<b:
        return cal(b,a)
    
    if a%b == 0:
        return b
    
    return cal(a-b,b) 


a = int(input("enter a num :"))
b = int(input("enter the sec num :"))

print("GCD : ",cal(a,b))

