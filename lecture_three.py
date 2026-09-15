# marks=[94.4,87.5,95.3,66.9,98.2]
# print(marks)
# print(type(marks))
# print(marks[0],marks[1])
# print(len(marks))


# student=["Karan",85,"Delhi"]
# print(student)
# student[0]="Dipanshu"
# print(student)


# marks=[85,94,76,63,48]
# print(marks[1:4])
# print(marks[:4])
# print(marks[1:])
# print(marks[-3:-1])

# list=[2,1,3]
# list.append(4)
# print(list)
# list.sort()
# print(list)
# list.sort(reverse=True)
# print(list)
# list.reverse()
# print(list)
# list.insert(1,5)
# print(list)
# list.pop(2)
# print(list)


# tup=(2,1,3,1)
# print(type(tup))
# print(tup.count(1))



# m1=str(input("Enter your 1st favourite movie:"))
# m2=str(input("Enter your 1st favourite movie:"))
# m3=str(input("Enter your 1st favourite movie:"))
# movies=[]
# movies.append(m1)
# movies.append(m2)
# movies.append(m3)
# print(movies)


# list1=["m","a","a","m"]
# list2=[1,2,3,4,5]
# cpy_list1=list1.copy()
# cpy_list1.reverse()
# if(list1==cpy_list1):
#     print("Palindrome")
# else:
#     print("Not a Palindrome")
# cpy_list2=list2.copy()
# cpy_list2.reverse()
# if(list2==cpy_list2):
#     print("Palindrome")
# else:
#     print("Not a Palindrome")


# a=[12,13,14,15,16,34.5]
# for i in range(len(a)):
#     print(a[i])

# l=[1,3,4,5]
# l.append(6)
# l.append(7)
# l.insert(1,2)
# l.extend([7,8])
# print(l)
# l.remove(2)
# print(l)
# l[0]=13
# print(l)


# # print positive and negative element in list
# l=[-45,67,9,-2,-4,5]
# print("positive elements are:")
# for i in l:
#     if i>=0:
#         print(i)

# print("negative elements are:")
# for i in l:
#     if(i<0):
#         print(i)


# # find maximum in list
# l=[12,36,14,19,128,6,13]

# largest=l[0]
# index=0
# for i in range(len(l)):
#     if l[i]>largest:
#         largest=l[i]
#         index=i
# print(f"your largest number is {largest} at index {index}")


# grade=["C","D","A","A","B","B","A"]
# grade.sort()
# print(grade)


# Tuple:- it is immutable
# tup=("C","D","A","A","B","B","A")
# print(tup.count("A"))


# a=(1,2,3,4,5,6,6,7,8)
# for i in range(len(a)):
#     print(a[i])

# index= a.index(5)
# print(index)

# count=a.count(6)
# print(count)


# # Tuple unpacking
# a,b,c,d=(1,2,3,4)
# print(b)


# Set in python:-set are mutable and not store any duplicate



# b=hash("hello")
# print(b)

# c=hash((1,2,344))
# print(c)

# s={1,8,9,"hello",2,3,4,5}

# for i in s:
#     print (i)

# s={1,2,3,4}
# s.remove(2)
# print(s)
# s.pop()
# print(s)
# s.clear()
# print(s)

a={1,2,3,4,5}
b={4,5,6,7,8}
s=a.union(b)

print(s)
i=a.intersection(b)
print(i)

d=a.difference(b)
print(d)

sd=a.symmetric_difference(b)
print(sd)