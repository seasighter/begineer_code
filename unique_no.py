#my own solution
# def unique_no(list):
#     for i in range(0,len(list)):
#         for j in range(0,len(list)):
#             if i==j:
#                 continue
#             if list[i]==list[j]:
#                 break
#         else:
#             return list[i]
            
# list=[3,7,2,4,4,7,10,3,2,5,5]
# print(unique_no(list))
            

#Second optimize sol

def find_unique(list):
    ans=0
    for i in range (0,len(list)):
        ans=ans^list[i]     # ^ is xor which gives zero on same element
    return ans              # and o^no  is no. so same element xor becomes zero and unique element left
list=[1,2,4,5,3,2,4,1,5]    # 1^2^4...same as will get store in ans until same elements becomes zero
print(find_unique(list))