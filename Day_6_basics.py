# a='abacbddabcddd'

# out = {}
# i=0
# while i<len(a):
#     out[a[i]] = a.count(a[i])
#     # if a[i] not in out.keys():
#     #     out[a[i]] = a.count(a[i])
#     i+=1

# print(out)

# a = "Python is very easy"
# out = a.split()
# dic = {}
# i=0
# while i<len(out):
#     dic[out[i]] = out[i][::-1]
#     i+=1

# print(dic)


# a = "Python is very easy"
# out = a.split()
# dic = {}
# i=0
# while i<len(out):
#     if i%2==0:
#         dic[out[i]] = out[i][::-1]
#     else:
#         dic[out[i]] = len(out[i])*2
#     i+=1

# print(dic)


# a= "Python is very easy"
# out = {}
# a = a.split()  
# i=0
# while i < len(a):
#     if i%2==0:
#         out[a[i]] = a[i] + str(len(a[i]))
#     else:
#         out[a[i]] = len(a[i])*2

#     i+=1

# print(out)


# num = int(input("Enter a Number: "))
# i=1
# while i<11:
#     print(f"{num} X {i} = {num*i}")
#     i+=1


# a = int(input("Enter a number: "))
# sum = 0
# num = a
# while num!=0:
    
#     remainder = num%10 
#     num= num//10
#     sum = sum + remainder
# print(sum)


# a= ['Hello', 3+5j, 'ab', 98, 'star', [1,2]]
# i =0
# l=[]
# while i < len(a):
#     if type(a[i]) == str and len(a[i]) >= 3:
#         l.append(len(a[i]))
#     else:
#         l += [a[i]]
#     i+=1

# print(l)


# a = input("Enter your string")
# out=''
# i=0
# while i < len(a):
#     if 'a'<= a[i] <='z':
#         out+=chr(ord(a[i]) - 32)
#     else:
#         out+=a[i]
#     i+=1
# print(out)

# a = "How are You"
# out = ''
# i=0
# while i< len(a):
#     if a[i] == ' ':
#         out+='_'
#     else:
#         out+=a[i]
#     i+=1
# print(out)


# a = 'aabcdabcbaddab'
# out=''  
# i = 0
# while i< len(a):
#     if a[i] not in out:
#         out += a[i]+ str(a.count(a[i]))
#     i+=1
# print(out)

# wap to check if a string is palindrome without using indexing

# a = 'asha'
# reverse = ''
# i = 0  # i = len(a) -1
# while i<len(a):
#     reverse += a[len(a)-(i+1)] # out += a[i]
#     i+=1 # i-=1
# print(reverse)

# if a== reverse:
#     print('palindrome')

# else:
#     print("not a palindrome")


# a = 'Hai Hello'.split() #['hai', 'hello']
# out = {}

# i =0
# while i < len(a):

#     out[a[i]] = [a[i], len(a[i]) * 2, a[i][::-1] + str(len(a[i]) * 2)]
#     i+=1

# print(out)

a= "(((())))("

print(a.count('(') - a.count(')'))

