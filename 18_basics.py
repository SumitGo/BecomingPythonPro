# wap to extract all the integers from a given list
# using yield, we will extract integer one at a time, and dont extract all the integers at a time, just to be more memory efficient

# def extract(l):
#     # out=[]
#     for i in l:
#         if type(i) == int:
#             # out+=[i]
#             yield i


# a=[12,'wed23',23.34,343,23,5,6,32,21]
# for i in extract(a):
#     print(i)

# wap to extract integers, and its palindrome, both from the list 
# def extract(l):
#     for i in l:
#         if type(i)==int and int(str(i)[::-1]) in l:
#             yield i
# a=[12,'wed23',23.34,343,23,5,6,32,21]

# print(list(extract(a)))

# wap to print first 10 multiples of a number and store in a tuple

# def multiple(n):
#     for i in range(1,11):
#         yield n*i

# tup = tuple(i for i in multiple(5))

# print(tup)



a= ['hello', 56, 7.8, [1,2], 5+6j]

# out=[['hello',5],[56,1], [7.8,1], [[1,2],1],[5+6j,1]]

# def random_func(l):
#     for i in l:
#         if type(i) in [str, list, tuple, set ]:
#             yield [i,len(i)]
#         elif type(i) == dict:
#             yield [i,len(i.keys())]
#         else:
#             yield [i,1]


# for i in random_func(a):
#     print(i)     
# wap to extract all the prime numbers present in between 1 to 100

# def prime_func(a,b):
#     # a>3
    
#     for i in range(a,b+1):
#         # print(i)
#         prime=False
#         for j in range(2,i):
#             if i%j==0:
#                 prime=False
#                 # print("prime", i)
#                 break
#             else:
#                 prime=True
#         if prime:
#             yield i
#         # else:
#         #     yield 'Not Prime'


# print(list(prime_func(3,100)))
# for i in prime_func(1,100):
#     print(i)
            
# wap to print the perfect numbers between 1 and 1000

# def perfect_num():
#     for i in range(1,1000):
#         factors=0
#         for j in range(1,i):
#             if i%j ==0:
#                 factors +=j
#         if factors==i:
#             yield i
    
# print(list(perfect_num()))

# create generator, use yield
# tup = (i for i in range(10))
# for i in tup:
#     print(i)

# fibonacci generator

# def fib(n_terms):
#     a=-1
#     b=0
#     sum=0
#     # yield 0
#     # yield 1
#     for i in range(n_terms):
#         sum = a+b
#         a=b
#         b=sum
#         # print(sum)
#         yield sum
        
# for i in fib(10):
#     print(i)


# even number generator
# even = (i for i in range(10) if i%2==0)
# print(list(even))

# odd number generator
# odd = (i for i in range(10) if i%2!=0)
# print(list(odd))

# infinite generator


