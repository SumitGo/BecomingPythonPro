# Question: Print numbers 1 to 10

i = 1

while i <= 10:
    print(i)
    i += 1

# Question: Print numbers 10 to 1

i = 10

while i >= 1:
    print(i)
    i -= 1

# Question: Sum of first N numbers

n = int(input("Enter N: "))

i = 1
sum_num = 0

while i <= n:
    sum_num += i
    i += 1

print("Sum =", sum_num)


# Question: Print even numbers up to 100

i = 2

while i <= 100:
    print(i)
    i += 2

# Question: Print odd numbers up to 100

i = 1

while i <= 100:
    print(i)
    i += 2

# Question: Multiplication table using while loop

n = int(input("Enter a number: "))

i = 1

while i <= 10:
    print(f"{n} x {i} = {n * i}")
    i += 1

# Question: Count digits in a number

num = int(input("Enter a number: "))

count = 0

while num > 0:
    count += 1
    num //= 10

print("Number of digits =", count)


# Question: Reverse a number

num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Reversed number =", reverse)


# Question: Find sum of digits

num = int(input("Enter a number: "))

sum_digits = 0

while num > 0:
    digit = num % 10
    sum_digits += digit
    num //= 10

print("Sum of digits =", sum_digits)

# Question: Check palindrome number

num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if original == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

