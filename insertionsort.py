

# def insertion_sort(arr):

#     for i in range(1,len(arr)): # starts from index 1 and goes upto last element

#         pick=arr[i]
#         j=i-1  #to go to before  index

#         while j>=0 and arr[j] > pick:
#             arr[j+1]=arr[j]
#             j-=1
#         arr[j+1]=pick
    
#     return arr
# arr=[3,19,17,25,9,1]
# print(insertion_sort(arr))



# Insertion sort:

## Problem 1 — Insert Incoming Exam Scores
# Students submit their exam scores one at a time throughout the day. After each submission, 
# insert the score into the correct position in the already-sorted list 
# and display the updated leaderboard.

# Example 1:
# Input : scores = [72, 45, 88, 60, 95]
# Output: sorted = [45, 60, 72, 88, 95], shifts = 6

# Example 2:
# Input : scores = [10, 20, 30, 40, 50]
# Output: sorted = [10, 20, 30, 40, 50], shifts = 0

# def exam_scores(scores):
#     shifts=0


#     for i in range(1,len(scores)):       # starting from second element in the array
#         key=scores[i]   # storing second element (score) in the variable key
                   
#         j=i-1              # making j to go to previous step
            


#         while j>=0 and scores[j] > key:      # checking whether the j(index)is greater than or equal to 0 and first element is greater than second element
#             scores[j+1]=scores[j]       # here making second element is equal to first element
#             shifts+=1                   #no of times the element moved one position right
#             j-=1                         # reducing j means in first iteration (0-1=-1) again it will check in while loop

#         scores[j+1]=key                # here we are inserting the value in index 0 position means (-1+1=0) scores[0]=key 
#                                          #means scores[0]=45

#     return scores,shifts
# # scores=[72, 45, 88, 60, 95]
# scores = [10, 20, 30, 40, 50]
# result,shifts=exam_scores(scores)
# print("sorted = ", result, "shifts = ", shifts)
# print("shifts",shifts)


# A librarian receives books one at a time and wants to always maintain a shelf sorted by page count. 
# Each new book must be placed in the correct position without disturbing the existing order.

# Example 1:
# Input : pages = [300, 150, 400, 250, 100]
# Output: sorted = [100, 150, 250, 300, 400], shifts = 6

# Example 2:
# Input : pages = [500, 100, 400, 200, 300]
# Output: sorted = [100, 200, 300, 400, 500], shifts = 10

def arrange_books(pages):
    shifts=0

    for i in range(1,len(pages)):
        key=pages[i]
        j=i-1
        while j>=0 and pages[j] > key:
            pages[j+1]=pages[j]
            shifts+=1
            j-=1
            

        pages[j+1]=key
        
    return pages,shifts



pages = [300, 150, 400, 250, 100]
result,shifts=arrange_books(pages)

print("Pages: ",result)
print("Shifts: ",shifts)




        
        

    
