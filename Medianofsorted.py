"""
Given two sorted arrays which can be of any length. Find the median both arrays.
"""

def findmedian(a,b):
    if len(b)<len(a): return findmedian(b,a) 
    n1 = len(a)
    n2 = len(b)
    top = 0
    bottom = n1
    n = n1+n2
    left = (n1+n2+1)//2
    while(top<=bottom):
        mid1 = (top+bottom)//2
        mid2 = left - mid1
        l1 = -10**18
        l2 = -10**18
        r1 = 10**18
        r2 = 10**18

        if mid1 < n1 : 
            r1 = a[mid1]
        if mid2 < n2 :
            r2 = b[mid2]

        if mid1 - 1 >= 0 :
            l1 = a[mid1 - 1]
        if mid2 - 1 >= 0:
            l2 = b[mid2 - 1]
            
        if l1 <= r2 and l2 <= r1:
            if (n % 2 == 1) : return max(l1,l2)

            else:
                 return ((max(l1,l2)+min(r1,r2)))//(2.0);
           
        elif l1 > r2 :
            bottom = mid1-1
        else:
            top = mid1 + 1
    return 0

a = [3,4,6,9,11,15]
b = [2,6,7,8,9]

print(findmedian(a,b))




    