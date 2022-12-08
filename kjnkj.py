n=int(input())
m=n
mask =0
while m!=0:
    mask= (mask<<1)|1
    n=n>>1
ans= (~n) & mask
print(ans)
    