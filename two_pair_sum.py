def sum_pair(list,n):
    temp=[]
    for i in range(0,len(list)):
       for j in range(i+1,len(list)):
            if list[i]+list[j]==n:
                ans=[]
                ans.append(min(list[i],list[j]))
                ans.append(max(list[i],list[j]))
                temp.append(ans)
    return sorted(temp)
list=[1,2,3,4,5,6]
n=5
print(sum_pair(list,n))