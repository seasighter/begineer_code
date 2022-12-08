#print all no occurring twice
#time complexity is high it should be optimized
def duplicate(list):
    arr=[]
    for i in range (0,len(list)):
        for j in range(1,len(list)):
            if i==j :
                break
            if list[i] == list[j]:
                arr.append(list[i])
    return arr
list=[1,4,4,3,2,2,5,6,7]
print(duplicate(list))
        


