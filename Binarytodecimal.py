"""
write a program for binary to decimal conversion :- 
"""
a = input("enter the string : ")
a = list(a)
i = 0
Sum = 0
while(i<len(a)):                                
    Sum = Sum + int(a[i]) * (2**(len(a)-i-1))             
    i = i+1
print(Sum)