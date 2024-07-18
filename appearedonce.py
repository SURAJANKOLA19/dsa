def once(arr):
    unique=0
    for i in arr:
        unique^=i
    return unique
    
    
    
    
    
    
arr=[1,1,2,3,2,4,4]
print(once(arr))