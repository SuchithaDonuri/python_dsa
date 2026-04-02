# Linear search using iteration called for loop

# def linear_search(arr,target):
#     n=len(arr)
#     for index in range(0,n):
#         if arr[index] == target:
#             return index
        
#     return -1

# lst=[8,7,5,2,11,16]
# target=11
# res=linear_search(lst,target)
# print(res)


# def linearsearch(arr,x,index):
#     #if element is not there in the list
#     if len(arr) == index:
#         return False
    
#     if arr[index]== x:
#         return True
#     return linearsearch(arr,x,index+1)
    
# arr=[2,9,7,6,4,4,3,10]
# print(linearsearch(arr,8,0))






# 3. Hospital Patient Lookup A small clinic maintains a list of patient records in the order they registered. 
# A nurse needs to quickly look up whether a particular patient is registered and retrieve their details. 
# Since records are unsorted, 
# implement Linear Search to find the patient by name.
# Input:
# patients = [
#     {"name": "Arjun",  "age": 34, "disease": "Fever"},
#     {"name": "Meena",  "age": 22, "disease": "Flu"},
#     {"name": "Ravi",   "age": 45, "disease": "Diabetes"},
#     {"name": "Sneha",  "age": 29, "disease": "Migraine"}
# ]
# search = "Ravi"

# Output:
# Patient found!
# Name    : Ravi
# Age     : 45
# Disease : Diabetes
# Position: Record #3

# def is_registered(patients,search):
#     for i in range(len(patients)):
#         if patients[i]["name"] == search:
#             return f""" Patient found!
# Name           : {patients[i]["name"]}
# Age            : {patients[i]["age"]}
# Disease        : {patients[i]["disease"]}
# Position       : Record #{i+1}
# """
        
#     return "Patient not found"


# patients = [
# {"name": "Arjun","age": 34, "disease": "Fever"},
# {"name": "Meena","age": 22, "disease": "Flu"},
# {"name": "Ravi","age": 45, "disease": "Diabetes"},
# {"name": "Sneha","age": 29, "disease": "Migraine"}
# ]
# search = "Ravi"

# print(is_registered(patients,search))




# 4. Supermarket Discount Finder A supermarket wants to display all products currently priced above ₹500 
# so they can apply a 10% discount on them. 
# The product list is unsorted. Use Linear Search to scan through and 
# identify all eligible products along with their discounted price.

# Input:
# products = [
#     ("Rice 5kg", 450), ("Olive Oil", 850), ("Cornflakes", 380),
#     ("Almonds 500g", 650), ("Detergent", 520), ("Bread", 60)
# ]
# threshold = 500

# Output:
# Products eligible for 10% discount:
# - Olive Oil     : ₹850 → ₹765.0
# - Almonds 500g  : ₹650 → ₹585.0
# - Detergent     : ₹520 → ₹468.0

# def display_products(products,threshold):
#     result="Products eligible for 10% discount\n"

#     for product in products:   # product = ("Rice 5kg", 450)
#         name=product[0]         #product[0]="Rice 5kg"
#         price=product[1]        #product[1]=450
        

#         if price > threshold:

#             discount_price=price - (price*0.10)

#             result+=f" - {name}  :  rs{price} -> rs{discount_price}\n"
#     return result
    
    
# products = [
# ("Rice 5kg", 450), ("Olive Oil", 850), ("Cornflakes", 380),
# ("Almonds 500g", 650), ("Detergent", 520), ("Bread", 60)]

# threshold = 500
# print(display_products(products,threshold))

# cds 1
# def linear_search(arr,target):

#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i , target
        
#     return -1

# arr=[0,4,1,6,7,2]
# target=7
# print(linear_search(arr,target))

# def find_id(dict,key,target):

#     for item in dict:
#         if item[key]==target:
#             return item
        
#     return -1


# data = [
#     {"id": 1, "name": "Ravi"},
#     {"id": 2, "name": "Anu"},
#     {"id": 2, "name": "Kiran"}
# ]

# print(find_id(data,"id",2))


# def find_id(dict,key,target):

#     for item in dict:
#         if item.get(key)==target:
#             return item[key]
        
#     return -1


# data = [
#     {"id": 1, "name": "Ravi"},
#     {"id": 2, "name": "Anu"},
#     {"id": 2, "name": "Kiran"}
# ]

# print(find_id(data,"id",2))

# .get() is used to get the value for a given key and if key not prsent it doesnt give error

# dict={
#     "name":"suchitha",
#     "age":23
# }

# print(dict.get("nam"))

#cds 10 

# def search_product(products,target):
#     target=target.lower()
#     for i in range(len(products)):
#         if products[i].lower() == target:
#             return i 
        
#     return -1



# products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
# print(search_product(products,target="MOUSE"))
# print(search_product(products,target="Mouse"))
