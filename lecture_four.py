# dict={
#     "name":"apnacollege",
#     "subjects":["python","c","java"],
#     "topics":("dict","set"),
#     "age" : 24,
#     "is_adult":True,
#     "marks":94.4

# }
# print(dict)
# print(dict["name"])
# print(dict["subjects"])
# dict["name"]="shradha"
# dict["surname"]="khapra"
# print(dict)


# student={
#     "name":"rahul",
#     "subjects":{
#         "phy":87,
#         "chem":56,
#         "math":97
#     }
# }
# print(student["subjects"]["chem"])

# print(student.keys())
# print(list(student.keys()))
# print(len(list(student.keys())))

# print(student.values())
# print(list(student.values()))

# print(student.items())

# print(student["name2"])
# print(student.get("name2"))

# collection={1,2,2,2,2,3,4,"hello","world","world"}
# print (type(collection))
# print(collection)
# print(len(collection))
# s=set()
# print(type(s))
# collection.add(7)
# collection.add("aman")
# print(collection)

# collection.remove("aman")
# print(collection)

# print(len(collection))
# collection.clear()
# print(len(collection))
# print(collection)



# set1={1,2,3}
# set2={2,3,4}
# print(set1.union(set2))
# set1={1,2,3}
# set2={2,3,4}
# print(set1.intersection(set2))


# dic={
#   "table":["a piece of furniture","list of facts & figures"],
#   "cat":"a small animal"
# }
# print(dic)


# subjects={
#     "python","java","C++","python","javascript","java",
#     "python","java","C++","C"
# }
# print(subjects)
# print(len(subjects))

# marks={}
# x=int(input("enter your physics marks:"))
# marks.update({"phy":x})
# y=int(input("enter your chemistry marks:"))
# marks.update({"chem":y})
# z=int(input("enter your math marks:"))
# marks.update({"math":z})
# print(marks)


# values={
#     ("float",9.0),
#     ("int",9)
# }
# print(values)

# d={
#     10:100,
#     20:200,
#     30:300,
#     40:400
# }
# d[10]=100 #updating
# d[50]=500 #creating
# del d[30] #deleting
# print(d)


# d={
#     10:100,
#     20:200,
#     30:300,
#     40:400
# }
# for i in d.values():
#     print(i)


# d={
#     10:100,
#     20:200,
#     30:300,
#     40:400
# }
# d2=d.copy()
# d3=d.get(20)
# print(d.items())

# d1={10:100,20:200,30:300}
# d2={40:400,50:500,60:600}

# for i in d2:
#     d1[i]=d2[i]
# print(d1)


d1={10:100,20:200,30:300}
sum=0
for i in d1:
    sum=sum+d1[i]
print(sum)