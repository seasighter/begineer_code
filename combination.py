def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
def combination(n,r):
    numerator = factorial(n)
    denominator= factorial(n-r)*factorial(r)
    ans=numerator//denominator
    return ans
n=int(input())
r=int(input())
answer=combination(n,r)
print(answer)


