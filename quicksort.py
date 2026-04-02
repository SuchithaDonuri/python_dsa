# pivot is last element

# def quick_sort(arr):

#     if len(arr)<=1:
#         return arr
#     pivot=arr[-1]

#     left=[x for x in arr[:-1] if x <= pivot]
#     right=[x for x in arr[:-1] if x > pivot]

#     return quick_sort(left) +[pivot] + quick_sort(right)
    

# arr=[8,3,7,2,12,19]
# print(quick_sort(arr))


# pivot is first element

# def quick_sort(arr):

#     if len(arr)<=1:
#         return arr
    
#     pivot=arr[0]
#     remaining=arr[1:]

#     left=[x for x in remaining if x <= pivot]
#     right=[x for x in remaining if x > pivot]
#     print(left,right,pivot)

#     return quick_sort(left) + [pivot] + quick_sort(right)
# arr=[8,3,7,2,12,19]
# print(quick_sort(arr))


# if pivot element is the middle element

# def quick_sort(arr):

#     if len(arr) <= 1:
#         return arr
    
#     pivot_index=len(arr)//2

#     pivot=arr[pivot_index]

#     remaining=arr[:pivot_index]+arr[pivot_index+1:]

#     left=[x for x in remaining if x <= pivot]
#     right=[x for x in remaining if x > pivot]

#     return quick_sort(left) + [pivot] + quick_sort(right)

# arr=[8,3,7,2,12,19]
# print(quick_sort(arr))

# if pivot element is the element other than element

# def quick_sort(arr):

#     if len(arr) <= 1:
#         return arr
    
#     pivot_index=-2
#     pivot_index=pivot_index % len(arr)

#     pivot=arr[pivot_index]

#     remaining=arr[:pivot_index]+arr[pivot_index+1:]

#     left=[x for x in remaining if x <= pivot]
#     right=[x for x in remaining if x > pivot]

#     return quick_sort(left)+[pivot]+quick_sort(right)
# arr=[12,25,11,34,22]

# print(quick_sort(arr))


# 1 Library Book Sorter A school library has received a new batch of books with their page counts all jumbled up. 
# The librarian wants them arranged from fewest to most pages so students can easily pick books by length. I
# mplement QuickSort to help the librarian sort the books. input is an array with random number of pages eg. 
# Number_of_pages=[400,50,300,200]

# def sort_books(pages):
#     if len(pages) <= 1:
#         return pages

#     pivot=pages[-1]
    

#     left=[x for x in pages[:-1] if x <= pivot]

#     right=[x for x in pages[:-1] if x > pivot]

#     return sort_books(left)+[pivot]+sort_books(right)

# pages=[400,50,300,200]
# print("Sorted Books",sort_books(pages))

# 2. Cricket Scoreboard After a T20 tournament, the scoreboard is out of order. 
# The team coach wants players ranked by their total runs scored 
# so he can decide the batting order for the next match. 
# Use QuickSort to rank players from highest to lowest runs.
# Input: players = [  ("Rohit", 85), ("Virat", 120), ("Dhoni", 60),  ("Hardik", 95), ("Rahul", 110) ]

# Output: 
# Batting order for next match: 1. Virat → 120 runs 2. Rahul → 110 runs 3. Hardik → 95 runs 4. Rohit → 85 runs 5. Dhoni → 60 runs

def sort_scores(players_scores):

    if len(players_scores) <= 1:
        return players_scores
    

    pivot=players_scores[0]
    left=[]
    right=[]

    for i in range(1,len(players_scores)):
        if players_scores[i][1] >= pivot[1]:
            left.append(players_scores[i])

        else:
            right.append(players_scores[i])

    return sort_scores(left)+[pivot]+sort_scores(right)

players = [("Rohit", 85), ("Virat", 120), ("Dhoni", 60), ("Hardik", 95), ("Rahul", 110) ]

sort_players=sort_scores(players)

for i,(name,runs) in enumerate(sort_players,start=1):
    print(f"{i}. {name} -> {runs} runs")

















