# l = [i for i in range(1,11)]
# print(l)

# l = [i for i in range(1, 51) if i%2==0 ]
# print(l)

# l = [(i**3, i) for i in range(1,51) if i%3==0 and i %5==0]
# print(l)

# a=["Hello", 10, 3+5j, [1,2], 9.8, {'a': True, 'b': 2}]
# out = [5, 1, 1, 2, 1, 2]
# l = [len(i) if type(i) in [str, list, tuple, set, dict] else 1 for i in a]
# print(l)

# gen = (i for i in range(10)) # syntax to create generator


# a= 'Python is very easy'.split()
# output : [['Python', 6], ['is', 4], ['very', 4], ['easy', 8]]
# l = [[a[i], len(a[i])] if i%2==0 else [a[i], len(a[i])*2] for i in range(len(a))]
# print(l)

# a = 'aeroplane is very fast'.split()

# l = [[i, i.count('a')] for i in a]
# print(l)

# l = [i for k in range(10) for i in range(k)]
# print(l)

# s = {i**3 if i%2==0 else i**2 for i in range(1,11)}
# print(s)


# a = 'abcd efght abc abcdefgh'.split()
# # s = {(a[i], len(a[i])*2) if (i== 0 or i==len(a)-1) else (a[i], len(a[i])) for i in range(len(a)) }
# s = {(a[i], len(a[i])*2) if len(a[i])%2==0 else (a[i], len(a[i])) for i in range(len(a)) }
# print(s)

# for i in zip('python',[1,2], 'abi'):
#     print(i)


# dictionary comprehension

# d = {i:j for i, j in zip(['a','b','c'], [10, 20, 30])}
# print(d)

# d = {for i in range(1, 11)}
# for i in zip(range(10)): # single element in zip returns tuple elements of length 1
#     print(i, len(i))


# d = {i:i**3 if i%2==0 else i**2 for i in range(1,11)} # no need to metion key in the else part, only value needs to be mentioned, key is mentioned once
# print(d)


# a = ['Hai', 10, 'ab', 5.8, [1,2]]
# d = {i:len(i) for i in a if type(i) in [str]}
# print(d)


# LAMBDA FUNCTIONS
# x = "mHuPehla"
# y="Dusrka"
# out = (lambda x,y: {x:"python is easy"} if len(x)>len(y) else {y:"python is hard"})(x,y)
# # print(out(x,y))
# print(out)
# print(next(range(10)))

# a = map(lambda x: x**2, range(1,11))
# print(list(a))


a = 'good morning'
# out = list(map(lambda x:len(x), a.split()))
# print(out)

# d = {i:j for i,j in zip(a.split(), map(lambda x:len(x), a.split()))}
# print(d)

# d = {i:len(i) for i in a.split()}
# print(d)

# d = dict (map(lambda x: [x, len(x)], a.split()))
# print(d)
# print(list(map(lambda x: [x, len(x)],a.split())))

# print(dict(one = 1, two = 2))
# print(dict(([1,2], [3,4])))
# a = lambda x: x*a(x-1) if x!=0 else 1
# d = {i:j for i,j in zip(range(1,11),map(lambda x: x*a(x-1), range(1,11)))}

# print(d)


# from functools import filter

# d = filter(lambda x: x if x%2==0 else 0, range(1,101))
# print(list(d))


# filter fibonacci numbers between 1 to 1000 using filter function
def func(num):
    
    a = 0
    b = 1
    fib_num = [a,b]
    for i in range(num):
        sum = a+ b
        a = b
        b = sum
        fib_num+=[sum]
    return fib_num
    # if i in fib_num:
    #     return i

# fib = range(1001)
# print(func(100))
n=1000
fib = list(filter(func, range(n)))
print(fib)