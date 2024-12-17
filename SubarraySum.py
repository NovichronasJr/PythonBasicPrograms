"""
Find the longest subarray sum in a list 
"""
a=[]
n = int(input("enter the size"))
for i in range (0,n,1):
     b = int(input())
     a.append(b)
    
Sum = 0
max_sum = 0
i=0
for i in range(0,len(a),1):
     Sum = Sum + a[i]
     max_sum = max(max_sum,Sum)

     if Sum < 0:
          Sum = 0
        
print(f"max_sum = {max_sum}")   


