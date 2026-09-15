# #1. create a dictionary and apply following methods
# print dictionary item
# use get 
# change Value
# use length
# access time
student = {
    "name": "Dipanshu",
    "age": 20,
    "course": "B.Tech",
    "year": 2
}

# Print dictionary items
print("Dictionary items:", student)

# Use get() to access value safely
print("Student Name (using get):", student.get("name"))

# Change a value in dictionary
student["age"] = 21
print("After changing age:", student)

# Use len() to find length of dictionary
print("Length of dictionary:", len(student))

# Access time (import datetime module)
import datetime
current_time = datetime.datetime.now()
print("Access time:", current_time)


# #2.create a list and perform following methos
# # insert 
# # remove
# # apend 
# # clear
# # Create a list
# numbers = [10, 20, 30, 40]
# print("Original List:", numbers)
# numbers.insert(2, 25) 
# print("After insert:", numbers)
# numbers.remove(40) 
# print("After remove:", numbers)
# numbers.append(50)
# print("After append:", numbers)
# numbers.clear()
# print("After clear:", numbers)


# # 3.write a python program to print a number is positive or negative using if else 
# a=int (input("enter a number:"))
# if a>=0:
#     print("Number is positive")
# else:
#     print("Number is negative")


# #4. write a python program to find largest number among three numbers
# a=int (input("enter first number:"))
# b=int (input("enter second number:"))
# c=int (input("enter third number:"))
# if a>b and a>c:
#     print(a," is greater")
# elif b>a and b>c:
#     print(b," is greater")
# else:
#     print(c," is greater")
