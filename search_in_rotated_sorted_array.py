# search in rotated sorted array


# to find pivot 
def pivot(arr,n): 
    s=0
    e=n-1
    while s<e:
        mid=s+((e-s)//2)
        if arr[mid]>arr[0]: # binary search also be applied to monotonous function increasing or decreasing array
            s=mid+1          # to check pivot occurs in which array section
        else:
            e=mid
    return s
# for binary search 
def binary(arr,p,n,key):
    low=p
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

def find_no(arr,n,k):
    pivot_no=pivot(arr,n) # function calling to find pivot element 
    if k>=arr[pivot_no] and k<=arr[n-1]: #  checking in the 1 st part of array
        return binary(arr,pivot_no,n-1,k)
    else :                                # if k occurs in second part of array
        return binary(arr,0,pivot_no-1,k)  # calling binary function to find the element 

    
arr=[8,10,17,25,1,3,6]
k=10 #  no to find  in array
n=len(arr)
print(find_no(arr,n,k))
