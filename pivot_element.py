# smallest element of array
def pivot(arr,n): 
    s=0
    e=n-1
    while s<e:
        mid=s+((e-s)//2)
        if arr[mid]>arr[0]: # binary search also be applied to monotonous function increasing or decreasing array
            s=mid+1          # to check pivot occurs in which array section
        else:
            e=mid
    return arr[s]


arr=[8,10,17,25,1,3,6]
n=len(arr)
print(pivot(arr,n))
