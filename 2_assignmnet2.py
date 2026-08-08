# wap to check whether the data is mutable or not
data = eval(input("Enter the data: "))

if type(data) in [list, dict, set]:
    print("Data type is mutable")

else:
    print("Data type is not mutable")

# wap to check whether the given character is a digit or not

char = input("Enter the data: ")
if '0'<= char <= '9':
    print("character is a digit")

# wap to check whether the given character is a special or not

char = input("Enter the character")
if "A"<=char<='Z' and 'a' <= char <='z' and '0'<= char <= '9':
    print("NOt a special character")

else:
    print("special character")

# wap to check whether a list consists of a middle value or not 
l= eval(input("Enter the list"))
if len(l)%2 == 0:
    print("NO middle value")

else:
    print("Middle value exists")

# wap to check whether the number is even or odd 

num = int(input("Enter the number"))
if num % 2==0:
    print("Number is even")

else:
    print("number is odd")


# wapt check whether 2 values are pointing to the same memory or not 
val1 = input("Enter the value 1")
val2 = input("Enter value 2")
if val1 is val2:
    print("pointing to the same memory")

else:
    print("Different memory locations")

# consider a tuple of length 2 and check whether the tuple is homogeneous or not 
data = eval (input("Enter the data: "))

if type(data[0])==type(data[1]):
    print("Homogeneous tuple")
else:
    print("not homogeneous")

# wap to check whether the string is  palindrome or not
number = int(input("Enter the number to check palindrome: "))
while p<=len(str(num)):
    num = number
    p=0
    reverse = 1
    remainder = num%10
    num = num/10
    reverse = remainder + reverse * ( 10**p)
    p+=1
if reverse ==  number:
    print('A palindrome ')
else:
    print("not a palindrome")

# wap to check whether the number is positive or negative

num = int(input("enter the number: "))
if num<0:
    print("Number is negative")
else:
    print("number is positive")
    



