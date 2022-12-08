#my own solution
# def duplicate_no(list):
#     for i in range(0,len(list)):
#         for j in range(0,len(list)):
#             if i==j:
#                 continue
#             if list[i]==list[j]:
#                 return list[i]

            
# list=[13,3,3,4,5,1,2]            
# print(duplicate_no(list))


# optimized solution 
def findDuplicate(arr):
    ans=0
    for i in range(0,len(arr)):
        ans=ans^arr[i]               # ans will hold 10^2^3^14^5^6^7^8^9^10
    for i in range(1,len(arr)):
        ans=ans^i              #  here  ans= 10^2^3^14^5^6^7^8^9^10^1^2^3^4^5^6^7^8^9^10
                                # same no xor will get cancelled only duplicate value will remain as it is 3 times occuring
    return ans



arr=[10,2,3,1,4,5,6,7,8,9,10]
print(findDuplicate(arr))
        
       