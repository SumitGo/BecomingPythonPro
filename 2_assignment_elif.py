# wap to check a character is uppercase, lowecase, number, special character
char = input("Enter the character")
if "A"<=char<='Z':
    print("uppercase character")
elif 'a' <= char <='z':
    print("lowecase character")
elif '0'<= char <= '9':
    print("digit character")
else:
    print("special character")


# wap to check whether the given integer is single digit or two digit or three digot or more than three digits.
num = int(input("Enter your number: "))
if 0<= num <=9 :
    print("Single digit Number")

elif 10<= num <=99 :
    print("Double digit Number")

elif 100<= num <=999 :
    print("Three digit Number")

elif num >=1000 :
    print("more than three digit Number")

# wap to check the given points are lying in which quadrant
x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))    
if x > 0 and y > 0:
    print("Point is in the First Quadrant")
elif x < 0 and y > 0:
    print("Point is in the Second Quadrant")
elif x < 0 and y < 0:
    print("Point is in the Third Quadrant")
elif x > 0 and y < 0:
    print("Point is in the Fourth Quadrant")
else:
    print("Point is on the Origin or Axis")    

# wap to find the greatest of 3 numbers
val1 = int(input("First Number: "))
val2 = int(input("Second Number: "))
val3 = int(input("Third Number: "))
big = 0
if val1<val3:
    big = val3
else:
    big = val1

if big < val3:
    print("Greatest number is: ", val3)
else: 
    print("Greatest number is: ",big)


# wap to find the smallest of 3 numbers.
val1 = int(input("First Number: "))
val2 = int(input("Second Number: "))
val3 = int(input("Third Number: "))
small = 0
if val1<val3:
    small = val1
else:
    small = val3

if small < val3:
    print("Smallest number is: ", small)
else: 
    print("Smallest number is: ",val3)

# wap to ckeck the relation between two integer numbers
num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))
if num1 > num2:
    print(num1, "is greater than", num2)
elif num1 < num2:
    print(num1, "is smaller than", num2)
else:    
    print(num1, "is equal to", num2)

# consider a character input if it is uppercase convert it into lowercase, if it is lowercase convert it into uppercse, if it is digit print the remainder when it is divider by 3 else if it is special character print it's ASCII value. 
char = input("Enter the character: ")
if "A"<=char<='Z':
    print("Lowercase character: ", char.lower())
elif 'a' <= char <='z':
    print("Uppercase character: ", char.upper())
elif '0'<= char <= '9':
    print("Remainder when divided by 3: ", int(char)%3)
else:
    print("ASCII value: ", ord(char))

# wap to print the 'Fizz' if the given number is multiple of three print 'buzz' if the given number is multiple of 5 and print 'Fizzbuzz' if the number is multiple of both 3 and 5
num = int(input('Enter your number: '))
if num%3==0:
    print("Fizz")
elif num%5==0:
    print("buzz")
if num%3==0 and num%5 ==0:
    print("Fizzbuzz")