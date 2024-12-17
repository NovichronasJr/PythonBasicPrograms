"""
Given the string find the ASCII of each character in a string.
"""
a = input("enter a string : ")
b = list(a)
upper = 0
lower = 0
for element in b:
    print(element," ",ord(element))

