"""
Given the list of string. Find the largest string in it.
"""

a = ["hellie","Bellieman","dgdjesggsis"]
e = a[0]
for element in a:
    if  len(element) > len(e):
        e = element

print("the longest element is : ",e,"length is : ",len(e))

