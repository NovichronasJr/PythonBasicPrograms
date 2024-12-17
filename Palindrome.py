"""
given a string write a function to check if it is a palindrome, ignoring spaces, special characters and 
case sensitivity.
"""

import string
a = input("enter the string : ")
a = a.lower()
a = list(a)
for element in a:
    if element in string.punctuation:
        a.remove(element)
print(a)
i = 0
j = len(a)-1
flag = 1

while(i<=j):
    if a[i] == a[j]:
        j = j-1
        i = i+1
    else:
        flag = 0
        break
if(flag):
    print("it is a palindrome")
else:
    print("not a palindrome")