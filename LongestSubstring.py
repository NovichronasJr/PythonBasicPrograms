"""
Find the longest substring without repeating characters and also find the frequency of each repeating character.
"""

a = input("enter the string : ")
a = list(a)
repeat = []
non_repeat = []
i = 0
j = i+1
non_repeat.append(a[i])

while(i<len(a) and j<len(a)):
    if(a[i] == a[j]):
        repeat.append(a[j])
        del a[j]

    elif(j == len(a)-1):
        i = i+1
        non_repeat.append(a[i])
        j = i+1
    else:
        j=j+1

st = ""
for element in non_repeat:
    st = st+element

print("longest substring : ",st)
print("frequency of repeat : ")
element = repeat[0]
count = 0
for e in repeat:
    if e!=element:
        print(element,":",count)
        element = e
        count = 1
    else:
        count = count+1

print(element,":",count)