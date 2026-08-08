# # NESTED IF ELSE 
# # wap to check the character is a vowel or consonant
# char = input("Enter the character")

# if 'A' <=char <= 'Z' or 'a' <=char <= 'z':
#     if char in "aeiouAEIOU":
#         print("vowel")

#     else:
#         print("consonant")
# else:
#     print("Not a Alphabet")

# # WAP to login the instagram with valid usename and password.(enter password only if user name is valid)
# login = input("Enter username: ")
# password = False
# if "@gmail.com" in login:
#     password = True
#     if password:
#         passw = input("Enter the password")

#     else:
#         print("Enter valid username")
# else:
#     print("Invalid username")



# # wap to print the middle value of a list only if it is string. 
# l = [1,2,3,4,5]
# if len(l)%2!=0:
#     middle = len(l)//2
#     if type(l[middle]) == str:
#         print("Middle value: ", l[middle])
#     else:
#         print("Middle value is not a string")
# else:
#     print("List has even number of values, no middle value")


# # wap to check whether the character is a vowel or a consonant
# string = input("Enter a character: ")
# if len(string) == 1 and ( 'A' <= string <= 'Z' or 'a' <= string <= 'z'):
#     if string in "aeiouAEIOU":
#         print("vowel")
#     else:
#         print("consonant")
# else:
#     print("Not a valid character")

# # # wap to find the greates of 4 numbers.
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))
# d = int(input("Enter d: ")) 
# if a>=b and a>=c and a>=d:
#     print("Greatest: ", a)
# elif b>=a and b>=c and b>=d:
#     print("Greatest: ", b)
# elif c>=a and c>=b and c>=d:
#     print("Greatest: ", c)
# else:    print("Greatest: ", d)


# # # wap to print the value as it is only if the length of the value is even.
# value = input("Enter the value: ")
# if len(value)%2==0:
#     print(value)
# else:    print("Length of the value is odd")

# # wap to print the last value of a list only if it is palindrome string starting with vowel else 

# # wap to print the reversed string obly if it is starting with vowel, ending with consonant and having a middle value
# string = input("Enter the string: ")
# if len(string)%2!=0 and string[0] in "aeiouAEIOU" and string[-1] not in "aeiouAEIOU":
#     reverse = ''
#     i = len(string)-1
#     while i>=0:
#         reverse+=string[i]
#         i-=1
#     print("Reversed String: ", reverse)
# else:    print("String does not meet the criteria")

# wap to find the second greatest of 4 values
# a= int(input("Enter a: "))
# b= int(input("Enter b: "))
# c= int(input("Enter c: "))
# d= int(input("Enter d: "))
# if a>=b and a>=c and a>=d:  
#     if b>=c and b>=d:
#         print("Second greatest: ", b)
#     elif c>=b and c>=d:
#         print("Second greatest: ", c)
#     else:
#         print("Second greatest: ", d)
# elif b>=a and b>=c and b>=d:
#     if a>=c and a>=d:
#         print("Second greatest: ", a)
#     elif c>=a and c>=d:
#         print("Second greatest: ", c)
#     else:
#         print("Second greatest: ", d)
# elif c>=a and c>=b and c>=d:
#     if a>=b and a>=d:
#         print("Second greatest: ", a)
#     elif b>=a and b>=d:
#         print("Second greatest: ", b)
#     else:
#         print("Second greatest: ", d)
# else:    
#     if a>=b and a>=c:
#         print("Second greatest: ", a)
#     elif b>=a and b>=c:
#         print("Second greatest: ", b)
#     else:
#         print("Second greatest: ", c)

# # wap to find the smalles of 4 values
# a= int(input("Enter a: "))
# b= int(input("Enter b: "))
# c= int(input("Enter c: "))  
# d= int(input("Enter d: "))
# if a<=b and a<=c and a<=d:
#     print("Smallest: ", a)
# elif b<=a and b<=c and b<=d:
#     print("Smallest: ", b)
# elif c<=a and c<=b and c<=d:
#     print("Smallest: ", c)      
# else:    print("Smallest: ", d)


# # wap to print the middle character of a givern string obly if it is uppercase character. 
string = input("Enter the string: ")
if len(string)%2!=0:
    middle = len(string)//2
    if "A" <= string[middle] <= "Z":
        print("Middle character: ", string[middle])
    else:
        print("Middle character is not an uppercase character")
else:    print("String has even number of characters, no middle character")

# # wap to print first n natural numbers
# n= int(input("Enter n value: "))
# i=1
# while i<n+1:
#     print(i)
#     i+=1

# wap to print all the even numbers between 1 to 100
# i = 1
# while i<100+1:
#     i+=2
#     print(i, end=" ")
#     # if i%2==0:
#     #     print(i, end=" ")
# print()

# wap to print the cube of the number from 1 to 50, which are divisible by 3 and 5
# i = 1
# while i<50+1:
#     if i%3 ==0 and i%5==0:
#         print(i,":",i**3,end=" ")
#     i+=1
# print()

# wap to print the numbers divisible by 3 between c and d, c,d are user inputs
# c = int(input("Enter starting: "))
# d = int(input("Enter ending: "))
# i=c
# while i<d+1:
#     if i%3 ==0 and i%5==0:
#         print(i,":",i**3,end=" ")
#     i+=1
# print()

# wap to print the reverse of a number
# number = int(input("Enter the number to check palindrome: "))
# num = number
# reverse = 0
# while num!=0:
#     remainder = num%10
#     num = num//10
#     reverse = reverse * 10 + remainder 

# print("Reverse: ",reverse)
# if reverse ==  number:
#     print('A palindrome ')
# else:
#     print("not a palindrome")

# wap to print the sum of first n natural numberes
# i=1
# n = int(input("Enter n: "))
# sum = 0
# while i<=n:
#     sum+=i
#     i+=1

# print("sum: ", sum)

# i=1
# n = int(input("Enter n: "))
# product = 1
# while i<=n:
#     product*=i
#     i+=1

# print("product: ", product)

# wap to extract all the uppercase alphabet from a given string 
# string= input("Enter String: ")
# extract = ''
# for i in string:
#     if "A" <= i <= 'Z':
#         extract += i
# print("Uppercase letters: ", extract)

    
# wap to extract all the uppercase alphabet from a given string but at even index
# string= input("Enter String: ")
# extract = ''
# i=0
# while i<=len(string):
#     if i%2==0:
#         if "A" <= string[i] <= 'Z':
#             extract += string[i]
#     i+=1
# print("Uppercase letters: ", extract)

# string= input("Enter String: ")
# string = "DaTAScienCE"
# extract = ''
# i=0
# while i<len(string):
#     if "A" <= string[i] <= 'Z':
#         extract += string[i]
#     i+=1
#     # print(i,extract)
# print(extract+str(len(extract)))


# wap to print all the integers present inside the list 

# l = [1,3,"34,353",345,'ad', 34.543]
# ints=[]
# i=0
# while i<len(l):
#     if type(l[i]) == int:
#         ints+=[l[i]] # ints.append(l[i])
#     i+=1
# print(ints)
# 
 