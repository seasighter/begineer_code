# find the max amount of time a person study in a day to finish a certain syllabus
def ispossible(mid,n, m, time)  
    study_time=0
        days=0
        for i in range(m):
            if study_time+m[i]<=mid:
                 study_time+=m[i]
            else :
                days+=1
                  if days>n or m[i]>mid:
                        return False
                  study_time=arr[i]   
        return True

def ayushGivesNinjatest(n, m, time):
        ans=-1
        s=0
        sum=0
        for int i in range(m):
            sum+=m[i]
        e=sum
        while s<e:
            mid=s+((e-s))//2
            if ispossible(mid,n, m, time):
                ans=mid
                e=mid-1
            else:
                s=mid+1
         return ans
n=3  
m=[20,30,15,]          
print(ayushGivesNinjatest(n,m,time))