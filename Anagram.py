"""
Given two strings chack whether they are anagrams or not.
"""

def find(first, second):
    flag = 1
    if(len(first) > len(second)):
         return find(second,first)
       
    for element in second:
        try:
            first.remove(element)
        except ValueError:
            flag = 0
            break
    return flag



a = input("enter the first string : ")
b = input("enter the second string : ")
first = list(a)
second = list(b)

if find(first, second):
    print("valid anagrams")

else :
    print("invalid anagrams")



         

    

