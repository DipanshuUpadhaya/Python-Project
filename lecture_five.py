# count=1
# while count<=10:
#     print("Hello")
#     count+=1

#print number form 1 to 100
# i=1
# while i<=100:
#     print (i)
#     i+=1


# # palindrome number 
# a=int (input("enter number:"))
# copy=a
# rev=0
# while a>0:
#     rev=rev*10+a%10
#     a= a//10
# if copy == rev:
#     print("palinrome")
# else:
#     print("not a palindrome")



#print multiplication table of a number
# n=int(input("Enter a number:"))
# i=1
# while i<=10:
#     print(n,"*",i,"=",n*i)
#     i+=1


#qs4
# nums=[1,4,9,16,25,36,49,64,81,100]
# idx=0
# while idx<len(nums):
#     print(nums[idx])
#     idx+=1
    


# nums=(1,4,9,16,25,36,49,64,81,100)
# idx=0
# x=36
# while idx<len(nums):
#     if (nums[idx]==x):
#         print("Found at index",idx)
#         break
#     else:
#         print("finding")
#     idx+=1

# i=1
# while (i<=10):
#     if(i%2!=0):
#         i+=1
#         continue
#     print(i)
#     i+=1
# print("end of loop")


# nums=[1,2,3,4,5]
# for val in nums:
#     print(val)
# vaggies=["patato","brinjal","ladyfinger","cucumber"]
# for val in vaggies:
#     print (val)

# tup=(1,2,3,4,5)
# for num in tup:
#     print(num)
# string="apnacollege"
# for char in string:
#     if(char=="o"):
#         print("o found")
#         break
#     print(char)
# else:
#     print("end")


# num=[1,4,9,16,25,36,49,64,81,100]
# for el in num:
#     print(el)

# num=[1,4,9,16,25,36,49,64,81,36,100]
# x=36
# idx=0
# for el in num:
#     if(el==x):
#         print("number found at:",idx)
#     idx+=1



# for i in range(2,101,2):
#     print(i)

# for i in range(1,101,1):
#     print (i)

# for i in range(100,0,-1):
#     print (i)

# n=int(input("enter a number:"))
# for i in range(1,11):
#     print (n*i)


# for i in range(5):
#     pass
# print("some useful work")


# n=int(input("enter a num:"))
# sum=0
# for i in range(n+1):
#     sum+=i
# print(sum)

# n=int(input("enter a num:"))
# sum=0
# i=1
# while(n>=i):
#     sum+=i
#     i+=1
# print(sum)

# n=int(input("enter a num:"))
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print("factorial of",n,"=",fact)


# n=int (input("enter number:"))
# for i in range(n):
#     print("hello world")

# n= int (input("enter number:"))
# esum=0
# osum=0
# for i in range(1,n+1):
#     if i%2==0:
#         esum+=i
#     else:
#         osum+=i
# print(f"your even and odd sum are {esum} and {osum}")      



# n=int (input("which number factor you want:"))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)

# n=int (input("check your number perfect or not:"))
# factorSum=0
# for i in range(1,n):
#     if n%i==0:
#         factorSum+=i

# if factorSum==n:
#     print("your number is perfect:")
# else:
#     print("not a perfect number")


# # Prime number
# n= int (input("check your number is prime or not:"))

# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count+=1

# if count==2:
#     print(f"{n} is a prime number")
# else:
#     print(f"{n} is not a prime number")


# # Check string palindrome
# a="NAMAN"
# b=""
# for i in range(len(a)-1,-1,-1):
#     b=b+a[i]
# if b==a:
#     print(f"yur string is palindrome")
# else:
#     print(f"not palindrome")



# # random number generate game
# import random
# num=random.randint(1,10)

# tries=0
# while True:
#     guess=int (input("please guess your number:"))
#     if num==guess:
#         tries+=1
#         print(f"you are right you guessed the number is {tries} tries.")
#         break
#     elif num<guess:
#         print("go a little lower")
#     elif num>guess:
#         print("go a little higher")
#     else:
#         print("sorry you are wrong")

