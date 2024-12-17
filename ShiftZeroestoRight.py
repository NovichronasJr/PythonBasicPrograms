"""
Given a list containing elements and along with some zeroes in it. Without changing the order of other elements
shift all zeroes to right.
"""

nums = []
n = int(input("enter the size"))
for i in range (0,n,1):
    b = int(input())
    nums.append(b)
count = 0
i = 0
while(i < len(nums)):
    if nums[i] == 0:
        del nums[i]
        count = count+1
    
    else :
        i = i+1


for i in range(0,count,1):
    nums.append(0)

print(nums)
