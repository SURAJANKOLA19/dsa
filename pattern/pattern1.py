size=5
a='a'
for i in range(size):
    for j in range(i+1):
        print(a,end=' ')
        a=chr(ord(a)+1)
    print()

"""
a
b c
d e f
g h i j
k l m n o"""