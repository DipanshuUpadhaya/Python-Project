a= int (input("tell your number:"))
try:
    print(10/a)
except Exception as err:
    print(f"sorry there is an err as {err}")

else:
    print("good there is no exception0000")

finally:
    print("i will run no matter what")
print ("ok i have done the division ")