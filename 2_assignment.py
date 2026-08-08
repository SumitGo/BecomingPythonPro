# wap to print the square of a number only if it is even.
num = int(input("Enter any number: "))

if num%2==0:
    out = num**2
    print("square of even number: ", out)

#wap to print ascii value of a character only if it is uppercase
char = input("Enter any number: ")
vowel = 'aeiouAEIOU'
if char in vowel:
    print("Character is a Vowel")

else:
    print("now a vowel")

if 'A' <= char <= 'Z':
    print(char,' : ', ord(char))

else:
    print("not uppercase character")


# wap to print the cube of a number only if it is divisible by 9 or 6

num= int(input("Enter any number: "))

if num%6==0 and num%9==0:
    print("number is divisible by 9 and 6")
    print("cube of ",num,": ", num**3)

# wap to check whether the given digit is a 3 digit number

if len(str(num))==3:
    print("Given digit is a 3 digit number")

# wap to check whether the last digit of a given number is 5

if num%10==5:
    print("Last digit is 5")

# wap to check whether the given data is float

if type(num) == float:
    print("The number is Float")

# wap to check whether the data is a single value data

data = eval(input("Enter the data: "))

if type(data) in [str, tuple,list, set, dict]:
    print("Multi value data")
else:
    print("single value data")

# wap to check whether the given character is a digit or not
char = input("Enter any number: ")
digit = '0123456789'
if char in digit:
    pirnt("character is a digit")

    

# wap to check whether the given integer is a multiple of 3

num = int(input("Enter any number: "))

if num%3==0:
    print(num,'is a multiple of 3')