# recursion
# find factorial using recursion

# def fact(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))

# import sys
# print(sys.getrecursionlimit())

# sys.setrecursionlimit(2000)
# print(sys.getrecursionlimit())

# sum of first 10 natural numbers
# def total(n):
#     if n==0:
#         return 0
#     return n+total(n-1)
# print(total(3))

# wap to find the uppercase letter from string 

# wap to extract numbers from a list using recursion 
# a=[1,2,3,4,'hel',(21,3+4j)]
# # {"wow",12,56}

# def extract(l,index=0, out=[]):
#     if index==len(l):
#         return out
#     if type(l[index])==int:
#         out+=[l[index]]
#     index+=1
#     return extract(l[index:])

# print(extract(a))

# wap to store 1 if data is single value datatype, else length of data
# def length(data, index=0, out={}):
    
#     if index>=len(data):
#         return out
#     if type(data[index]) in [int, float, complex, bool]:
#         out[data[index]] = 1
        
#     if type(data[index]) in [set, tuple, list, dict,str] :
#         out[str(data[index])] = len(data[index])
#     index+=1
#     return length(data[index:],index,out)

# print(length(a))

a='11100110001001'
b='00011100011000'

def cmp(a,b, index=0, out_a=0, out_b=0):
    if index>=len(a) or index>=len(b):
        return abs(out_a - out_b)
    if a[index] == '1':
        out_a+=1
    if b[index] == '1':
        out_b+=1
    return cmp(a[index:],b[index:],index+1,out_a,out_b)

print(cmp(a,b))
# print(a[0])

a=['one','two','three']
b=['one','one','one']

def add(a,b,index=0,s=0):

    num_map = {
        'one':1,
        'two':2,
        'three':3,
        'four':4,
        'five':5,
        'six':6,
        'seven':7,
        'eight':8,
        'nine':9,
        'zero':0
    }
    num=num_map[a[index]]