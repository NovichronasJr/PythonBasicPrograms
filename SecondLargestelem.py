"""
Find the second largest element in an array without sorting the array.
"""
a = [3,2,1,5,6,4]
e = a[0]
for element in a:
    e = max(e,element)

r = a[0]

for element in a:
    if element < e and element > r:
        r = element

print(r)  