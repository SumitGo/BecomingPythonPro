# for i in range(1, 11):
#     print(i)
#     if i==5 or i==7:
#         print(i)
#         break

# user_name ='AngelPriya'

# while True:
#     user_id = input("Enter userid: ")
#     if user_id == user_name:
#         print("welcome")
#         break

#     else:
#         print("write proper id")

# wap a program to play casino

# while True:
#     user = int(input("enter any number"))
#     casino = 10

#     if user==casino:
#         print('Wow, you just won the game')
#         break

#     else:
#         print("better luck next time")

# wap to check whether a number is a prime number or composite number

# n = int(input("Enter your number: "))
# prime = True
# for i in range(2,n):
#     if n%i==0:
#         prime = False
#         break

# print(f"{n} is Prime: {prime}")

# wap to check the collection is homo and hetrogeneous data 
# data = ["2,","124","23vas","234"]
# for i in range(len(data)):
#     if len(data)-i in [0,1]:
#         print("Homogeneous data")
#         break
#     if type(data[i])!=type(data[i+1]):
#         print("Hetrogeneous Data")
#         break
# else:
#     print("Homogeneous Data")

# wap to find the uppercase letter from a given string 

# a="heHeiLKDSOPIhfoiffh"
# out=''
# for i in a:
#     if i.isupper():
#         out+=i 

# print(out)

# wap to print all the single value datatype present inside the list
# data = [1, 2, 3, "hello", 4.5, True, 6+ 3j]
# for i in data:
#     if type(i) in [int, float , bool, complex]:
#         print(i)

