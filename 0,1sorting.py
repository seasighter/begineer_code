def sort(list):
    i=0
    j=len(list)-1
    while i<j:
        while list[i]==0 and i<j:
            i+=1
        while list[j]==1 and i<j:
            j-=1
        while list[i]==1 and list[j]==0:
            temp=0
            temp=list[i]
            list[i]=list[j]
            list[j]=temp
    return list



list=[0,1,1,0,1,0,0,1]
print(sort(list))
