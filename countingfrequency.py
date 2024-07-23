def count_v(a):
    count={}
    for i in a:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    return count

a=[1,2,4,1,2,4]
result=count_v(a)

for elem,count in result.items():
    print(elem,count)
    