def rotate(a):
    """Rotate a list of integers by one position to the left."""
    size=len(a)
    temp=a[0]
    if size<1:
        return a
    for i in range(1,size):
        a[i-1]=a[i]
    a[-1]=temp
    return a
    
a=[1,2,3,4,5,6]
print(rotate(a))