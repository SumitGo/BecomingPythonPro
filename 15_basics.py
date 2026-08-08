# use args and kwargs 
# def rand(*args, **kwargs):
#     print(args)
#     print(kwargs)

# rand(1,23,34,5,6,name='sumit', world='god', mode='saitama')

# tuple unpacking 
# tup  = (1,2,3,4,"hello")
# a,b,*c = tup
# print(a)
# print(b)
# print(c)

# list unpacking 
# l=[1,2,3,4,5,6,6]
# a,*d=l
# print(a,d)

# swap variables using tuple unpacking 
# a=20
# b='hellp'
# b,a = (20,'hellp')

# # a,b = b,a
# print(a,b)


# sum numbers using *args
# def total(*args):
#     s=0
#     for i in args:
#         s+=i
#     print(s)
# total(1,2,3,4,5,6)

# print key value pairs using **kwargs 
# def display(**kwargs):
#     print(kwargs)
#     for key, value in kwargs.items():
#         print(f'{key} : {value}')
# display(name='sumit', mode='saitama', technique='iron cutting fist')


# nested unpacking
# a=['wow', 12, 33, 5+5j,('anythin', 'else')]
# b,d,*c,(g) =a
# print(b,d,c,g,sep='\n')


# function with *args and **kwargs with real life example
def details(customer,mode, *items, **details):
    print(customer)
    print(mode)
    for i in items:
        print(f'--{i}')

    for key, value in details.items():
        print(f"{key} : {value}")

details(
    'saitama',
    'god mode',
    'Laptop',
    'Bag',
    'Dhoti',
    name='Gojo',
    Lastname="sharma",
    address = "SwargNark",
    power= 'MoneyNhi'
)

def details(*anv):
    print(anv)

details({1,2,3,4,5,5,6,6})