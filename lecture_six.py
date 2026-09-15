# def sum(a,b):
#     s=a+b
#     return s
# print(sum(4,5))


# def print_hello():
#     print("hello")
# print_hello()


#average of three number
# def average(a,b,c):
#     avg=((a+b+c)/3)
#     return avg
# print(average(10,20,30))


# def cal_prod(a=3,b=4):
#     return a*b
# print(cal_prod(3,9))


# cities=["delhi","Noida","mumbai","chennai","pune"]
# def print_len(list):
#     print(len(list))
# print_len(cities)



# cities=["delhi","Noida","mumbai","chennai","pune"]
# def print_list(list):
#     for item in list:
#         print(item, end=" ")
# print_list(cities)

# def find_fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     print(fact)
# find_fact(5)


# def convertor(usd_val):
#     inr_val=usd_val *83
#     print(usd_val,"USD=",inr_val,"INR")
# convertor(2)


# def find(n):
#     if(n%2==0):
#         print("EVEN")
#     else:
#         print("ODD")
# find(int(input("enter a number:")))

#recursion
# def show (n):
#     if(n==0):
#         return 
#     print(n)
#     show(n-1)
# show(5)


#find factorial using recursion
# def fact(n):
#     if(n==1 or n==0):
#         return 1
#     return fact(n-1)*n
# print(fact(6))


# def calc_sum(n):
#     if(n==0):
#         return 0
#     return calc_sum(n-1)+n
# print(calc_sum(10))

def print_list(list,idx=0):
    if(idx==len(list)):
        return 
    print(list[idx])
    print_list(list,idx+1)
fruits=["mango","litchi","apple","banana","grapes"]
print_list(fruits)