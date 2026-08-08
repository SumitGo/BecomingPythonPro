# a= 45
# b= 55
# c=45+55
# print(c)
# print(a+b)
# print(45+55)

# a = input("Whats the day?")
# print(a)

# one = input("thara number")
# dusrka = input(" bhai ka number")
# print("Sum is This: ", one + dusrka)

# b= int(input("First Number"))
# c= int(input("Second Number"))
# print("Sum of Two numbers is: ", b+c)


# Write a program to find the area and perimeter of the square, rectangle, and circle

# for rectangle
# print("For Rectangle")
# length = int(input("Enter Length:"))
# width = int(input("Enter Width:"))
# area = length * width
# perimeter = 2 * (length + width)

# print("Area :", area)
# print("Perimeter:", perimeter)


# print("For Square")
# side = int(input("Enter Side:"))
# area = side **2
# perimeter = 4 * side

# print("Area :", area)
# print("Perimeter:", perimeter)

# eval('print("hello world")')

# l = eval(input("Enter list elements"))
# print(l, type(l))

# a= input("what to add: ")
# l.append(a)
# print(l)
# c = input("add element at second index: ")
# l.insert(1,c)
# print(l)
# b = int(input("what index value to remove: "))
# l.pop(b)
# print(l)


# Wap to print dict, update key, add key, update values, use three inbuilt functions, remove key
dic = {
    1:"ji",
    2: "ha",
    3: 'm',
    4: 'hu Khalnayak',
    5: [1,2,3],
    "age":22,
}

e = eval(str(dic))
print(e, type(e))
print(dic)
dic = eval(input("enter your dictionary: \m"))
dic[1]="sahi kha"
print(dic)
dic[10]= 1000
print(dic)
del dic[3]
print(dic)

print(dic.keys())
print(dic.values())
print(dic.items())