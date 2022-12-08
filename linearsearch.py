def linear_search(list,n):
    for i in range(0,len(list)):
         if list[i] == n:
             return i
    else :
        return False
        

n=23
list=[12,23,1,3,5,6,1,7,8,3]
print(linear_search(list,n))
