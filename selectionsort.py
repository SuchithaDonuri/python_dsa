# def selection_sort(arr):
#     n=len(arr)

#     min_index=0

#     for j in range(1,n-1):
#         if arr[j] < arr[min_index]:
#             min_index=j

#     arr[0],arr[min_index]=arr[min_index],arr[0]

#     return arr
# unsorted_list = [12,25,11,34,90,22]
# sorted_list = selection_sort(unsorted_list)
# print("Sorted Elements :", sorted_list)

# optimization
# def selection_sort(arr):
#     n=len(arr)

    
#     for i in range(n-1):
#         min_index=i
#         for j in range(i+1,n-1):
#             if arr[j] < arr[min_index]:
#                 min_index=j

#         arr[i],arr[min_index]=arr[min_index],arr[i]

#     return arr
# unsorted_list = [12,25,11,34,90,22]
# sorted_list = selection_sort(unsorted_list)
# print("Sorted Elements :", sorted_list)


# def selection_sort(arr):

    
#     n=len(arr)
    

#     for i in range(1,n-1):
#         if arr[i] < arr[min_index]:
#             min_index=i

#     arr[0],arr[min_index]=arr[min_index],arr[0]

#     return arr

# unsorted_list = [12,25,11,34,90,22]
# sorted_list = selection_sort(unsorted_list)
# print("Sorted Elements :", sorted_list)



# def selection_sort(arr):
#     n=len(arr)

#     for i in range(n-1):
#         min_index=i

#         for j in range(i+1,n):
#             if arr[j] < arr[min_index]:
#                 min_index=j

#         arr[i],arr[min_index]=arr[min_index],arr[i]

#     return arr
    

# unsorted_list = [12,25,11,34,90,22]
# sorted_list = selection_sort(unsorted_list)
# print("Sorted Elements :", sorted_list)


# def selection_sort(arr):

#     n=len(arr)
#     for i in range(n):
#         max_index=i
#         for j in range(i+1,n-1):
#             if arr[j] > arr[j+1]:
#                 max_index=j

#         arr[i],arr[max_index]=arr[max_index],arr[i]

#     return arr
# arr=[12,25,11,34,90,22]
# print(selection_sort(arr))

            
# merge two sorted arrays

