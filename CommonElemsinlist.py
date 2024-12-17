"""
find the common elements between two lists.
"""
x = [1,2,3,4,5,9,6]
y = [9,8,7,6,5,3,4]
common = [element for element in x if element in y] 
print("common element : ",common)