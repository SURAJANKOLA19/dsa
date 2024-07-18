def reverse(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
    
def rotate(a,d):
    size=len(a)
    d=d%size
    
    reverse(a,0,size-1)
    reverse(a,0,d-1)
    reverse(a,d,size-1)
    
    return a

arr = [1, 2, 3, 4, 5,6,7]
n = 7
print(rotate(arr,n))