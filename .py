def rotate(a,n):
    def reverse(a,s,e):
        while s<e:
            a[s],a[e]=a[e],a[s]
            s+=1
            e-=1
    
    size=len(a)
    n=n%size
    reverse(a,0,size-1)
    reverse(a,0,n-1)
    reverse(a,n,size-1)
    return a

a=[1,2,3,4,5,6]
print(rotate(a,2))