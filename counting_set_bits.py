# counting total set bits ("1") of given two numbers

def count(a):
    counts=0
    while a:
        if a&1:   #it return 1 if last digit is 1 and 0 if 0 in last digit
            counts+=1
        a=a>>1   # it will right shift digits 
    return counts
answer=count(0)+count(3)  #benefits of functions doing same thing twice 
                        # adding the count to get total 1's on both the no

print(answer)
