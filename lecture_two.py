# light="blue"
# if(light=="red"):
#     print("stop")
# elif(light=="green"):
#     print("go")
# elif(light=="yellow"):
#     print("look")
# else:
#     print("light is broken")


# marks= int(input("enter marks:"))
# if(marks>=90):
#     print("A")
# elif(marks<90 and marks>=80 ):
#     print("B")
# elif(marks<80 and marks>=70):
#     print("C")
# else:
#     print("D")


# a=int(input("enter first number:"))
# b=int(input("enter second number:"))
# c=int(input("enter third number:"))
# d=int(input("enter fourth number:"))
# if(a>=b and a>c and a>=d):
#     print("first is largest:",a)
# elif(b>=a and b>=c and b>=d):
#     print("second is largest: ",b)
# elif(c>=a and c>=b and c>=d):
#     print ("Third is largest:",c)
# else:
#     print("fourth is largest:",d)



# num=int(input("enter a number:"))
# if(num%7==0):
#     print("multiple of 7")
# else:
#     print("not a multiple")


# a=int (input ("enter a number"))
# b=int (input ("enter a number"))
# if a>b:
#     print(f"{a} is greater than {b}")
# elif b>a:
#     print(f"{b}is greater than {a}")
# else:
#     print(f"{a} both are equal {b}")
    

# num=int(input("enter a number:"))
# if num%2==0:
#     print(f"{num} is a even number")
# else:
#     print(f"{num} is a odd number")


t=int (input("please tell the temperature:"))
if(t<0):
    print("Freezing cold")
elif t>=0 and t<10:
    print("Very cold")
elif t>=10 and t<20:
    print(" cold")
elif t>=20 and t<30:
    print("plesant")
elif t>=30 and t<40:
    print("hot")
else:
    print("temp is very hot")
