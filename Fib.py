"""
Given an integer n denoting no of terms. Find the first n fibonacci terms.
"""

def fib(index,n,x,y):
    if n == index :
        return 
    
    if index == 0:
        print(0)
        fib(index+1,n,x,y)
    
    elif index == 1:
        print(1)
        fib(index+1,n,x,y)
    
    else:
        t = y
        y = x+y
        print(y)
        x = t
        fib(index+1,n,x,y)
    


a = int(input("enter the terms :"))
fib(0,a,0,1)