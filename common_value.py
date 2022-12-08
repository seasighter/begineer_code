def findArrayIntersection(arr: list, n: int, brr: list, m: int):
  
    list=[]
    i=0
    j=0
    while (i<n and j<m):
        if arr[i] <brr[j]:
            i+=1
        
        elif arr[i]==brr[j]:
            list.append(arr[i])
            i+=1
            j+=1
        else:
            j+=1
    return list
arr=[1,3,4,5,6]
n=5
brr=[1,5,6]
m=3
print(findArrayIntersection(arr,n,brr,m) )
        