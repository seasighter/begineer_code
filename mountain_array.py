#array is given in a form of mountains ]
# and we have to find its peak element
def peak_no(arr,n):
    s=0
    e=n-1
    while s<e:
        mid=s+((e-s)//2)
        if arr[mid]<arr[mid+1]:# checking the area where mid lies if true it 
            s=mid+1             # lies in increasing order
        else :
            e=mid  # else lies in decreasing order of mountain
    return s

arr=[0,1,2,3,2,0]
n=len(arr)
print(peak_no(arr,n))