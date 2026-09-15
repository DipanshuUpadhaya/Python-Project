# # linear search
# numbers=[10,25,30,45,50,75,90]
# target=int(input("Enter the value to search:"))
# found=False
# for i in range(len(numbers)):
#     if numbers[i]==target:
#         print("Target,",target," found at index",i)
#         found=True
#         break
# if not found:
#     print("Target {target} not found in the list")


# # Binary search
# numbers=[10,25,30,45,50,75,90]
# target=int(input("Enter the value to search:"))
# found=False
# st=0
# end=len(numbers)-1
# while st<=end:
#     mid=st+(end-st)//2
#     if numbers[mid]==target:
#         print("Target,",target," found at index",mid)
#         found=True
#         break
#     elif numbers[mid]>target:
#         end=mid-1
#     else:
#         st=mid+1
# if not found:
#     print("Target {target} not found in the list")
    


#recursive binary search in python
def binary_search(arr,left,right,target):
  if right>=left:
    mid=(left+right)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]>target:
        return binary_search(arr,left,mid-1,target)
    else:
        return binary_search(arr,mid+1,right,target)
  else:
    return-1

arr=[10,20,30,40,50,60,70,80]
target=int(input("Enter the value to search:"))
result=binary_search(arr,0,len(arr)-1,target)
if result != -1:
    print(f"Target {target} found at index {result}")
else:
    print(f"Target {target} not found in the list")




