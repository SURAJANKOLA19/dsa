def count_a(a):
    count={}
    for char in a:
        if char in count:
            count[char]+=1
        else:
            count[char]=1
    return count

a="hello world"
res=count_a(a)
for char,elem in res.items():
    print(char,elem)