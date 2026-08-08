# a= int(input("Enter your number: "))

# l=[]
# i=1
# while i<a:
#     if a%i==0:
#         l.append(i)
#     i+=1

# if sum(l)==a:
#     print('Perfect number: ', a)
# else: 
#     print("not a perfect number")

# a= 'hello'
# b='bye'
# i=0
# out=''
# while i<len(a):
#     if i<len(a):
#         out+= a[i] 
#     if i<len(b):
#         out+= b[i]

#     i+=1

# print(out)


# for i in range(1,11):
#     print(i,end = '')
# print()

# for i in range(0,11,2):
#     print(i,end= " ")
# print()

# a= 'python'
# i=0
# while i<len(a)-1:
#     print(i,end= '  ' )
#     i+=1

# i=0
# while i<len(a):
#     print(i)
#     i+=1
# dic = {1:True, 2:'halwa', 3:"rewadi"}

# for i in dic:
#     print(f"{i}: {dic[i]}")

# wap to extract numbers which is divisible 3 and 5 and between range 1 to 100
# extract = []
# for i in range(1,101):
#     if i %3 ==0 and i%5==0:
        # extract+=[i]
#         print(i)

# wap to find the length of a collection without using len function

# a = [1,2,4,3,2]
# a="wowoowiosidh"
# a={1:True, 2:'halwa', 3:"rewadi"}
# count=0
# for i in a:
#     print(i)
#     count+=1

# print(count)

# wap to extract all the uppercase alphabet from a given string using for loop

# a='HeLLlwei:Opu'
# extract=''
# for i in a:
#     if 'A' <= i <='Z':
#         extract += i

# print(extract)

# wap to find the uppercase at even index position
# a='HeLLlwei:Opu'
# extract=''
# for i in range(len(a)):
#     if i%2 == 0 and 'A' <= a[i] <='Z':
#         extract += a[i]
# print(extract)

# wap to extract all the integers from a list 
# a=[1,2.3,4+5j, "wowo", [1,2,2], 3]
# extract =[]
# for i in a:
#     if type(i)==int:
#         extract += [i]
# print(extract)

# wap to find the factorial of a number

# a= int(input("Enter number: "))
# product = 1
# for i in range(1,a+1):
#     product *= i

# print(product)

a= "nitin ava is mam good naman".split()
# extract = ''
# out =''
# for item in a: 
#     if item == out:
#     # if i == i[::-1]:
#         extract+= item+" "

# print(extract)

# for i in range(len(a[0])-1,-1,-1):
#     print(a[0][i])

# for i in range(5,0,-1):
#     print(i)


# l= [1,2,12321, 232, 45645]
# out = []
# for i in l:
#     if type(i)==int:
#         a=i
#         rev = 0
#         while a!=0:
#             remainder = a%10
#             a=a//10
#             rev = rev *10 +remainder
#         if i ==rev:
#             out += [i]
# print(out)


# l= [1,2,12321, 232, 45645]
# out = []
# for i in l:
#     if type(i)==int and i == int(str(i)[::-1]):
#         out += [i]
# print(out)


# a = ['hello', 3+5j, [1,2], 7.8, 99]

# out = []
# for i in a:
#     if type(i) != complex and type(i) != int and type(i) != float:
#         out+=[len(i)]
#     else:
#         out+=[1]

# print(out)
    
# out = []
# a = {'hello', 3+5j, 7.8, 99}
# for i in a:
#     if type(i) == complex or type(i) == int or type(i) == float or type(i) == bool:
#         out +=[i]
# print(out)


# wap to remove duplicate characters from a string 
# a= 'hello wow'
# out = ''
# for i in a:
#     if i not in out:
#         out+=i
# print(out)

a= 'aabcdcabd'
# letter = 'abcdefghijklmnopqrstuvwzyz'
# out = ''
# for i in a:
#     out += i + str(letter.find(i) + 1)

# print(out)
# out = ''
# for i in a:
#     out += i + str(ord(i)-96)

# print(out)
out = ''
a= 'absutz'
for i in a:
    out += chr( 97 + (ord(i)-96)%26 )
print(out)