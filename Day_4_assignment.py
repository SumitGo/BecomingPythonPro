# 1. Check whether a number is positive or negative

num = int(input("Enter a number: "))

if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")

# 2. Check whether a number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# 3. Find the largest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)

# 4. Check voting eligibility
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


# 5. Check leap year
year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# 6. Grade calculator using if-elif
marks = float(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")


# 7. Check whether a character is a vowel
ch = input("Enter a character: ")

if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("Vowel")
else:
    print("Consonant")


# 8. Nested if example
num = int(input("Enter a number: "))

if num >= 0:
    if num == 0:
        print("Number is Zero")
    else:
        print("Number is Positive")
else:
    print("Number is Negative")


# 9. Check divisibility by 5 and 11
num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both 5 and 11")
else:
    print("Not divisible by both 5 and 11")


# 10. ATM withdrawal condition program
balance = float(input("Enter your account balance: "))
withdrawal_amount = float(input("Enter withdrawal amount: "))
if withdrawal_amount <= balance:
    print("Withdrawal successful")
    balance -= withdrawal_amount
    print("Remaining balance:", balance)
else:
    print("Insufficient balance")
