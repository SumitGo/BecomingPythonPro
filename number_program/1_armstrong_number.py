# wap to check if a number is a armstrong number or not 
# 153 = 1^3 + 5^3 + 3^3



# n = 153
# n = str(n)
# sum = 0
# for i in n:
#     i= int(i)
#     sum += i**3
#     print(sum)

# if sum == int(n):
#     print("armstrong number")
# else:
#     print("not an armstrong number")


# n = 153
# n = str(n)
# sum = 0
# index = 0

# while index < len(n):
#     sum += int(n[index])**3
#     index+=1
#     print(sum)

# if sum == int(n):
#     print("armstrong number")
# else:
#     print("not an armstrong number")



# wap to check the perfect number
n = 6
sum=0
# for i in range(1,6):
#     if n%i==0:
#         sum+=i
# if sum==n:
#     print("perfect number")
# else:
#     print("not perfect")

# i=1
# while i<n:
#     if n%i==0:
#         sum+=i
#     i+=1

# print(sum)
# if sum==n:
#     print("perfect number")
# else:
#     print("not perfect")

# wap to check whether the number is a neon number or not 
# n= 9
# sq = n**2
# sq= str(sq)
# sum=0
# for i in range(len(sq)):
#     sum += int(sq[i])
# if sum == n:
#     print(f"{n} is a neon number")
# else:
#     print("not a neon number")

# n= 9
# sq = n**2
# sum=0
# while sq!=0:
#     sum+= sq % 10
#     sq = sq//10

# print(sum)
# n = 145
# sum=0
# a=n
# # print(n is a)
# while n!=0:
#     rem=n%10
#     # print("part:",part)
#     fact = 1
#     for i in range(1,rem+1): 
#         fact *= i
#     sum+=fact
#     # print(fact)
#     n=n//10

# if a == sum:
#     print("Strong Number")
# print(sum)


# a = int(input("enter number: "))

# a = str(a)
# b = a[1:-1]
# mid_sum = 0
# for i in b:
#     i = int(i)
#     mid_sum +=i

# print(mid_sum)
# if (int(a[0]) + int(a[-1])) == mid_sum:
#     print("xylem")
# else:
#     print("not equal | pholem")

# wap to print fibonacci series upto n numbers

# n= 10
# a= 0
# b= 1
# # sum =[a, b]
# for i in range(n+1): 
#     print(a)
#     a,b = b, a+b
#     # temp = b
#     # b = a+b                                                                                                                                        
#     # a = temp
#     sum+= [b]
    
# print(sum)


# # wap to check prime numbers 
# n = 37215
# prime = False
# div = []
# divide = True
# for i in range(2, n):
#     if len(div) != 0:
#         for j in div:
#             if i%j==0:
#                 divide = False
#                 continue
#     if divide==True:
#         if n%i == 0:
#             prime = False
#             break
#         else:
#             div+=[i]
#             prime = True
# if prime:
#     print("prime number")

# else:
#     print("not a prime")


# # wap to check prime numbers 
# n = 25
# prime = False
# for i in range(2, n):
#     if n%i == 0:
#         prime = False
#         break
#     else:
#         prime = True
# if prime==True:
#     print("prime number")

# else:
#     print("not a prime")


