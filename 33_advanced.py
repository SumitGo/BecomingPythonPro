"""
Today's Learning in Python: Decorator, Iterator, (Module, packages and library)
"""

# @decorator  # NameError: name 'decorator' is not defined
# def post():
#     print("post")

# def decorator(func):
#     def kuchbhi(*args):
#         print("Agya Decorator m")
#         func(*args)
#         print("Bahar Decorator se")
#     return kuchbhi


# @decorator
# def greet(name):
#     print("Hello ji, ", name, " ji")

# greet("Bhau")

# def dec(func):
#     def inner(*args):
#         print("args",args)
#         return abs(func(*args))
#     return inner

# @dec
# def sub(a,b):
#     return a-b

# @dec
# def mul(a,b):
#     return a*b

# @dec
# def div(a,b):
#     return a/b

# @dec
# def add(a,b):
#     return a+b

# x = 5
# y = 6
# res = add(x,y)
# print(f"add {x}, {y} = {res}")
# res = sub(x,y)
# print(f"sub {x}, {y} = {res}")
# res = mul(x,y)
# print(f"mul {x}, {y} = {res}")
# res = div(x,y)
# print(f"div {x}, {y} = {res}")


# var =[1,2,3,4,5]
# v = iter(var)
# for i in v:
#     print(i)

# print(var)
# print(type(v))
# for i in v.__iter__():
#     print(i)


### Modules, packages, library
# import math
# print(math.factorial(5))


from math import factorial, pow
print(factorial(5), pow(2,3))

