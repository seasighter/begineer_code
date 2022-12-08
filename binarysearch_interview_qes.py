# to find the first and last occurrence of no in a given sorted array
def first_occurrence(arr,key,n):
    #for first occurrence
    start=0
    end=n-1
    ans=-1
    
    while start<=end:
        mid=start+(end-start)//2
        if key==arr[mid]:
            ans=mid
            end=mid-1

        elif key<arr[mid]:
            end=mid-1
        elif key>arr[mid]:
            start=mid+1
    return ans
   #for last occurrence
def last_occurrence(arr,key,n):
    start=0
    end=n-1
    ans=-1
    while start<=end:
        mid=start+(end-start)//2
        if key==arr[mid]:
            ans=mid
            start=mid+1
        elif key<arr[mid]:
            end=mid-1
        elif key>arr[mid]:
            start=mid+1
    return ans
arr=[0,1,1,1,2,2,2,3]
key=2
n=len(arr)
print(first_occurrence(arr,key,n))
print(last_occurrence(arr,key,n))

#to find the no of occurrence of that no.
print((last_occurrence(arr,key,n)-first_occurrence(arr,key,n))+1)