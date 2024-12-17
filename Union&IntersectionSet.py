"""
Find union and intersection of the two arrays :- 
""" 
a = [1,2,5,6,8,9]
b = [10,2,5,6,2]

# Union of the two arrrays :- 
setA = set(a)
setB = set(b)

setC = setA.union(setB)
print("Union :- ",setC)

# intersection of two array :- 
print("intersection :- ",setA.intersection(setB))