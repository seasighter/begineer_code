list=["harry","elve","elve","harry","harry"]
i=0

while i < len(list):
    count=0
    for j in list:
        if list[i]==j:
            count+=1
    print(list[i],count)
    i+=1
