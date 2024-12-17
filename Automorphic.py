"""
 write a code to find an automorphic number.
"""
def value(num) :
    x = num            
    count = 0
    while(x!=0):
        x = x//10
        count = count+1

    product = num*num
    if(product % (10**count) == num):
        return True
    else:
        return False

a = int(input("enter a num :- "))
if value(a) :
    print("number is automorphic num")
else:
    print("not an automorphic num")
