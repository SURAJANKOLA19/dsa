n = 5
z='a'
for i in range(n):
    for j in range(i+1):
        print(z, end=" ")
    print()
    z = chr(ord(z)+1)
        