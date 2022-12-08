# finding element using binary search
#condition for binary search 
#it should be in monotonic condition
# means increasing or decreasing order

def binary(arr,key,n):
    low=0
    high=n
    while low <= high:
        #mid=(low+high)//2 # here if low and high =2**31-1 max value of int then low +high becomes greater than what a int cna hold
                        #   we have to change it
        mid=low+((high-low)//2) # here it will pass all test cases if we will open it becomes sames as above formula
        if key==arr[mid]:
            return mid
        elif key>arr[mid]:
            low=mid+1
        elif key<arr[mid]:
            high=mid-1
    return "notfound" # if not in the array


arr=[12,22,33,44,55,66]
n=len(arr)
key=66
print(binary(arr,key,n))