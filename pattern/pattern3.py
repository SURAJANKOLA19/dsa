size=5
for i in range(size):
    for j in range(i+1):
        print("*",end=" ")
    print()
"""
* 
* * 
* * * 
* * * * 
* * * * *
"""
size=5
count=1
for i in range(size):
    for j in range(i+1):
        print(count,end=" ")
        count+=1
    print()