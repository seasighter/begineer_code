# finding square root of a number using binary search 
#time complexity = o(log n)
def sq_root(n):
    s=0
    e=n
    while s<=e:
        mid=s+((e-s)//2)
        square=mid*mid # here 
        if square == n:
            return mid
        if square < n:
            ans=mid
            s=mid+1
        else:
            e=mid-1
    return ans



n=37
answer = sq_root(n)
print(answer)


