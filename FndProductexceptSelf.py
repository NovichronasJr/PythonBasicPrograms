"""
Given a list of integers. For each integer find the product of all other integers except for that number.
"""

a = [1,2,3,4]
a.sort()
product = 1
for element in a:
    product = product * element

ans = []
for element in a:
    ans.append(product//element)

print(ans)


