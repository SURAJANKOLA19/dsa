size=5
a='a'
for i in range(size):
    for j in range(i+1):
        print(a,end=' ')
        a=chr(ord(a)+1)
    print()