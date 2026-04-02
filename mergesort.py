
# def merge_sort(arr):

#     if len(arr) <=1:
#         return arr
    

#     mid=len(arr)//2
#     left=merge_sort(arr[:mid])
#     right=merge_sort(arr[mid:])


#     return merge(left,right)




# def merge(left,right):

#     result=[]
#     i=j=0

#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i+=1

#         else:
#             result.append(right[j])
#             j+=1

#     result.extend(left[i:])
#     result.extend(right[j:])

#     return result

# arr=[6,3,8,2,5]
# print("Sorted array: ", merge_sort(arr))



# def merge_arrays(list1,list2):

#     i=j=0
#     result=[]

#     while i < len(list1) and j < len(list2):

#         if list1[i] < list2[j]:
#             result.append(list1[i])
#             i+=1
            
#         else:
#             result.append(list2[j])
#             j+=1

#     while i < len(list1):
#         result.append(list1[i])
#         i+=1

#     while j < len(list2):
#         result.append(list2[j])
#         j+=1

#     return result

# list1 = [1, 3, 5]
# list2 = [2, 4, 6]

# print(merge_arrays(list1,list2))





    