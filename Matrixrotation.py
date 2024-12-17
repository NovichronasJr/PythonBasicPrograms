"""
Given the matrix implement matrix rotation
"""

a = [[1,2,3],[4,5,6],[7,8,9]]

for i in range (0,len(a),1):
    for j in range (i+1,len(a[0]),1):
        t = a[i][j]
        a[i][j] = a[j][i]
        a[j][i] = t

print(a)
    


