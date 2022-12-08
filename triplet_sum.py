def triplet(list,sum):
    ans=[]
    for i in range(0,len(list)):
        for j in range(i+1,len(list)):
            for k in range(j+1,len(list)):
                if list[i]+list[j]+list[k]==sum:
                    temp=[]
                    temp.append(list[i])
                    temp.append(list[j])
                    temp.append(list[k])
                    ans.append(temp)
    return ans
        

list=[1,2,3,4,5,6,7]
sum=12
print(triplet(list,sum))

