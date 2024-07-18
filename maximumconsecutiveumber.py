def maxi(a):
    n = len(arr)
    count=0
    result=0
    for i in range(0,n):
        if (a[i]==0):
            count=0
        else:
            count+=1
            result=max(result,count)
    return result
    
    
arr = [1, 1, 0, 0, 1, 0, 1, 
             0, 1, 1, 1, 1]

print(maxi(arr))