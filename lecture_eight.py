# class Student:
#     name="karan"
# s1=Student()
# print(s1.name)

# s2=Student()
# print(s2.name)


# class Car:
#     color="blue"
#     brand="mercedes"
# car1=Car()
# print(car1.color)
# print(car1.brand)


# class Student:
#     college_name="ABC college"
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
        
#     def welcome(self):
#         print("Welcome Student")

#     def get_marks(self):
#         return self.marks
# s1=Student("karan",94)
# print(s1.name, s1.marks)

# s2=Student("Arjun",98)
# print(s2.name, s2.marks, s2.college_name)
# s1.welcome()
# print (s1.get_marks())


# class Student:
#     def __init__(self, name,marks):
#         self.name=name
#         self.marks=marks
    
#     def get_avg(self):
#         sum=0
#         for val in self.marks:
#             sum+=val
#         print("hi",self.name,"your avg score is:",sum/3)

# s1=Student("tony stark",[99,98,97])
# s1.get_avg()


# class Car:
#     def __init__(self):
#         self.acc=False
#         self.brk=False
#         self.cluch=False
#     def start(self):
#         self.cluch=True
#         self.acc=True
#         print("car started..")
# car1=Car()
# car1.start()        

class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc
    #debit method
    def debit(self,amount):
        self.balance-=amount
        print("Rs.",amount,"was debited")
        print("total balance=",self.get_balance())

    def credit(self,amount):
        self.balance+=amount
        print("Rs.",amount,"was credited")
        print("total balance=",self.get_balance())

    def get_balance(self):
        return self.balance  
acc1=Account(10000,12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
acc1.debit(2000)
