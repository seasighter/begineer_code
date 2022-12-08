def swap(list):
    temp=0
    i=1 
    while i<len(list):
        temp=list[i-1]
        list[i-1]=list[i]
        list[i]=temp
        i+=2
    print(list) 

list=[1,3,5,6,7,8,9]
print(list[0])
swap(list)