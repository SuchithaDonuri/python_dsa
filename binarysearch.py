#binary search

# def binary_search(arr,target):


#     size=len(arr)

#     start=0
#     end=size-1
#     while start <=end:
#         mid=(start+end)//2

#         if arr[mid] == target:
#             return target
#         elif arr[mid] < target:
#             end=mid-1
#         elif arr[mid] > target:
#             start=mid+1

#     return -1


# sorted_array=[23,34,47,49,54,62,70,90,108]
# target=90
# res=binary_search(sorted_array,target)
# print(res)



# Count Number of Occurrences
# Using binary search, count how many times a number appears.
# Example:Input: [1, 2, 2, 2, 3, 4], target = 2  
# Output: 3


# Count negative numbers in 
#  [
#   [4, 3, 2, 1], 
#   [3, 2, 1, -1], 
#   [1, 1, -1, -2], 
#   [-1, -1, -2, -3]
#   ]
# grid= [
#   [4, 3, 2, 1], 
#   [3, 2, 1, -1], 
#   [1, 1, -1, -2], 
#   [-1, -1, -2, -3]
#   ]
# n=len(grid)
# print("length:", n)
# print(grid[0][0])


# to count negative numbers in a list using linear search

# lst=[9,8,2,7,-2,-8,-3,9,-3]
# negative=[x for x in lst if x < 0]
# print(negative)

# Count Number of Occurrences
# Using binary search, count how many times a number appears.
# Example:Input: [1, 2, 2, 2, 3, 4], target = 2  
# Output: 3

# def count_occurrences(arr,target):
#     # n=len(arr)

#     start=0
#     end=len(arr)-1
#     for i in range(end):
#         count=0
#         for j in range(0,end):
#             mid=(start+end)//2
            
#             if arr[mid] == target:
                

# 5. Flight Ticket Availability An airline maintains a sorted list of available seat numbers on a flight. 
# A passenger wants to know if their preferred seat is still available and at what position it appears 
# in the availability list. 
# Implement Binary Search to check this efficiently.
# Input:
# available_seats = [2, 5, 9, 14, 21, 28, 35, 42, 48, 55]
# preferred_seat  = 28

# Output:
# Seat 28 is available!
# Position in list : 6
# Comparisons made : 2


# def check_seat(available_seats,preferred_seat):

#     left=0
#     right=len(available_seats)-1
#     comparisions=0

#     while left <= right:
#         mid = (left+right)//2
#         comparisions+=1

#         if available_seats[mid] == preferred_seat:

#             return f"""
# Seat {preferred_seat} is available!
# Position in list : {mid+1}
# Comparisons made : {comparisions}
# """
        
#         elif preferred_seat > available_seats[mid]:
#             left=mid+1

#         else:
#              right=mid-1

#     return "Seat is not in the list"

# available_seats = [2, 5, 9, 14, 21, 28, 35, 42, 48, 55]
# preferred_seat = 28

# print(check_seat(available_seats,preferred_seat))





# 6. Pharmacy Medicine Search A pharmacy stores medicines sorted alphabetically. 
# A customer comes in asking for a specific medicine. The pharmacist needs to quickly confirm 
# if it's in stock and which shelf it's on (its index in the sorted list). 
# Use Binary Search to help the pharmacist respond fast.

# Input:
# medicines = [
#     "Aspirin", "Cetirizine", "Dolo650", "Ibuprofen",
#     "Metformin", "Omeprazole", "Paracetamol", "Ranitidine"
# ]
# search = "Omeprazole"

# Output:
# Medicine found: Omeprazole
# Shelf position : 6
# Comparisons    : 2

# search = "Amoxicillin"

# Output:
# Amoxicillin is not in stock.
# Comparisons: 3

 

# def search_medicine(medicines,search):

#     left=0
#     right=len(medicines)-1
#     comparisions=0

#     while left <= right:
#         mid = (left+right)//2
#         comparisions+=1

#         if medicines[mid] == search:

#             return f"""
# Medicine found  : {search}
# Shelf position  : {mid+1}
# Comparisons     : {comparisions}
# """
        
#         elif search > medicines[mid]:
#             left=mid+1

#         else:
#              right=mid-1

#     return f"""
# {search} not in stock
# Comparisions: {comparisions}
# """

# medicines = [
# "Aspirin", "Cetirizine", "Dolo650", "Ibuprofen",
# "Metformin", "Omeprazole", "Paracetamol", "Ranitidine"
# ]
# search = "Omeprazole"
# # search = "Amoxicillin"

# print(search_medicine(medicines,search))


#cds 2,3
# def first_occurance(arr,target):

#     left=0
#     right=len(arr)-1
#     result=-1
#     while left <= right:
#         mid=(left+right)//2
#         if arr[mid] == target:
#             result=mid
#             right=mid-1
            
#         elif arr[mid] > target:
#             right=mid-1
#         else:
#             left=mid+1

#     return f"The target first occurance is at position {result}"

# arr=[1,2,3,4,5,5,5,5,5,5,5,5,6,7,8]
# target=5
# print(first_occurance(arr,target))

# cds 4 
# sentence="I hate python"
# words=sentence.split()
# search='python'
# for word in words:
#     if search == word:
#         print("yes")
#     else:("no")


# def find_target(arr,target):

#     left=0
#     right=len(arr)-1 #3

#     while left <= right:  # 1:0<3,2:0<=0
#         mid=(left+right)//2         #1:0+3=1,2:0
#         if arr[mid] == target: #3!=2 ,1==2
#             return mid
        
#         elif arr[mid] > target: # 5 >2 ,1>2
#             right=mid-1          # 3=1-1=0
#         else:               # 1<2
#             left=mid+1   #0=0+1=1

#     return left

# nums = [1, 3, 5, 6]
# target = 2
# print(find_target(nums,target))


# cds 7
# Square Root Problem

# There is no array, so we create an imaginary number line
# # Why are we taking n?
# Because square root of n will ALWAYS lie between:

# 0 to n

# def sqrt_binary(number):
#     left=0
#     right=number

#     while left <= right: #1:0<16,2:0<7,3:4<7,4:4<=4
#         mid=(left+right)//2  # 8,3,5

#         if mid*mid==number: #64!=16,9!=16,25!=16,16==16
#             return mid
#         elif mid*mid < number: #64 < 16 F , 9 < 16 T,25 < 16 F
#             left=mid+1          # 0=0+3=4
#         else:           #64 > 16,25>16
#             right=mid-1     # 16=8-1=7, 7=5-1=4

#     return right

# print(sqrt_binary(16))

        
# def roated_sort(arr,target):
#     left=0
#     right=len(arr) -1

#     while left <= right:
#         mid=(left+right) // 2
#         if arr[mid] == target:
#             return mid
#         if arr[left] <= arr[mid]:

#             if arr[left] <= target < arr[mid]:
#                 right=mid-1
#             else:
#                 left=mid+1

#         else:
#             if arr[mid] < target < arr[right]:
#                 left=mid+1
#             else:
#                 right=mid-1

#     return-1
# arr=[4,5,6,1,2,3]
# target=2
# print(roated_sort(arr,target))


#cds 9 

def first_occurance(arr,target):
    left=0
    right=len(arr)-1
    first=-1

    while left <= right:
        mid=(left+right)//2
        if arr[mid] == target:
            first=mid
            right=mid-1
        elif arr[mid] > target:
            right=mid-1
        else:
            left=mid+1

    return first

def last_occurance(arr,target):
    left=0
    right=len(arr)-1
    last=-1

    while left <= right:
        mid=(left+right)//2
        if arr[mid] == target:
            last=mid
            left=mid+1
        elif arr[mid] > target:
            right=mid-1
        else:
            left=mid+1

    return last

def count_occurances(nums,target):
    first=first_occurance(nums,target)
    if first==-1:
        return 0
    last=last_occurance(nums,target)

    return last - first + 1

nums = [1, 2, 2, 2, 3, 4]
target=2
print(count_occurances(nums,target))
    

