def sorting(arr,n):
    low=0
    mid=0
    high=n-1
    while (mid<high):
        if arr[mid]==1:
            mid+=1
        elif arr[mid]==0:
            temp=0
            temp=arr[low]
            arr[low]=arr[mid]
            arr[mid]=temp
            mid+=1
            low+=1
        elif arr[mid]==2:
            temp=0
            temp=arr[mid]
            arr[mid]=arr[high]
            arr[high]=temp
            high-=1
    return arr
arr=[0,1,2,0,2,1,1,0]
n=len(arr)
print(sorting(arr,n))
           