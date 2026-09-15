# f=open("demo.txt","r")
# data=f.read()
# print(data)
# print(type(data))
# f.close()

# f=open("demo.txt","r")
# line1=f.readline()
# print(line1)
# line2=f.readline()
# print(line2)
# f.close()


# f=open("demo.txt","w")
# f.write("I want to learn JavaScript tomorrow.")
# f.close


# f=open("demo.txt","a")
# f.write("\nThen I will move to ReactJS")
# f.close


# f=open("demo.txt","w+")
# f.write("abc")
# print(f.read())
# f.close

# with open("demo.txt","r") as f:
#     data=f.read()
#     print(data)

# with open("demo.txt","w")as f:
#     data=f.write("new data")

# to delete a file
# import os
# os.remove("sample.txt")


# with open("practice.txt","w")as f:
#     f.write("Hi everyone\n we are leaning File I/O ")
#     f.write("\nusing Java.\n I like programming in Java")


# with open("practice.txt","r")as f:
#     data=f.read()
# newdata=data.replace("Java","Python")
# print(newdata)

# with open("practice.txt","w")as f:
#     f.write(newdata)


# def check_for_word():
#     word="leaning"
#     with open("practice.txt","r")as f:
#         data=f.read()
#         if(data.find(word)!=-1):
#             print("found")
#         else:
#             print("not found")
# def check_for_line():
#     word="learning"
#     data=True
#     line_no=1
#     with open("practice.txt","r")as f:
#         while data:
#             data=f.readline()
#             if(word in data):
#                 print(line_no)
#                 return 
#             line_no+=1
#     return -1
# print(check_for_line())

count=0
with open("practice.txt","r")as f:
    data=f.read()
    print(data)
    num=data.split(",")
    for val in num:
        if(int(val)%2==0):
            count+=1

print(count)



