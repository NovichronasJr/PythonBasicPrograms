"""
calculate the frequency of odd and even elements in a list.
"""

a = [1,23,4,5,7,78,8]
odd = []
even = []
for element in a:
    if element%2 == 0:
        even.append(element)
    else:
        odd.append(element)
    
print(f"no of odd elem :- {len(odd)} , no of even elements :- {len(even)}")