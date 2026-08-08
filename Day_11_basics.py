# wap to print all the integers present inthe list
# indane=0
# a= ['heiij', 'wow', indane, 23, 4.4, 786,420]

# for i in a:
#     if type(i) == int:
#         print(i)


# wap to find the length of homogenous tuple without len()
# a=(786,420, 39847,23)
# homo = False
# count = 0
# for i in a: 
#     count+=1
#     if type(a[0]) == type(i):
#         homo = True
        
#     else:
#         homo = False
#         break
# if homo == True:
#     print(count)
# else:
#     print(count)
#     print("tuple not homo, no count")


# wap to extract all the even numbers prsesent in a list

# a= ['heiij', 'wow', 0, 23, 4.4, 786,420]
# out = []
# for i in a:
#     if type(i) ==int and i%2==0:
#         out+=[i]

# print(out)

# wap to remove duplicates from list

# a= ['heiij', 'wow', 0, 23, 4.4, 1, 2, 1 ,2 , 4.4,23, 786,420]
# duplicates = []
# print(a)

# for i in range(len(a)):
#     for index in range(i+1,len(a)):
#         if a[i]==a[index]:
#             duplicates+=[index]

# # print(duplicates)

# # a loop to remove the duplicate values at indexes stored in duplicates list
# for i in duplicates:
#     print(f'{i}: {a[i]}')
#     del a[i]
#     # print(a)
#     for j in range(len(duplicates)): # a loop to reduce index values of duplicates list by 1 for indexes greater than the index of removed values
#         if duplicates[j] > i:
#             duplicates[j] -=1
#             # print(duplicates)         
# print(a)

# wap to reverse a string without using slicing
# a = "good"
# out =''
# for i in range(len(a)-1, -1, -1):
#     out+=a[i]
        
# print(out)

# wap to extract all the lowecase characters in a string only if the ascii value is even
# a = "good Are You Fine KaKashiYo"

# for i in range(len(a)):
#     if 'a' <= a[i] <= 'z' and ord(a[i])%2==0:
#         print(a[i], end = ' ')
# print()

# wap to check whether the last digit of an integer is even or not
# indane= 345

# if indane%2==0:
#     print("Even last digit.")
# else:
#     print("Last digit not even.")

# wap to extract all the key value pairs from the dictionary only if the keys are of string datatype and values are integers.

# a = {
#     'wow': "food is gud",
#     "kheti": False,
#     'sheti': 100,
#     12: 1234,
#     False: 'some',
# }

# kv = a.items()

# for i in kv:
#     if type(i[0]) == str and type(i[1]) == int:
#         print(i)


# wap to extract key value pairs from the dictionary only if both keys and values are exactly same.
# a = {
#     'wow': "food is gud",
#     "kheti": False,
#     'sheti': 100,
#     12: 1234,
#     False: 'some',
#     True: False,
#     'right': 'right'
# }

# kv = a.items()
# for i in kv:
#     if i[0] == i[1]:
#         print(i)

# wap to get the following output using len function:
# S= 'power star'.split()
# out = {}

# for i in S:
#     out[i] = i[::-1]

# print(out)

# wap to get the following output
# S= 'power star'.split()
# out = {}
# for i in S:
#     out[i] = len(i)
# print(out)

# -------------------------
# 82 wap to get all the non default values from a list 

# a = [ 1,0,'wee', '', False, 0.0, 0j, 5+3j]
# out = []
# for i in a:
#     if bool(i) != False:
#         out +=[i]

# print(out)
# ---------------------------


# wap to check whether the list is homogenous or not 

# a = [1,2,3,4, 's']
# homo = False
# for i in range(len(a)):
#     if type(a[0]) == type(a[i]):
#         homo = True

#     else:
#         homo = False
#         break

# if homo == True:
#     print("Homogenous List")   
# else:
#     print("Hetrogenous")


# wap to replace the space by * present in string 
# a = 'wow this is so good'
# out = ''
# for i in a:
#     if i == ' ':
#         out = a.replace(i,"*")

# print(out)


# wap to count the number of occurence of a specified character
# a = "wow this is so good"
# n='o'
# occ =0
# for i in a:
#     if i ==n:
#         occ=a.count(n)

# print(occ)

# wap to get the following output

# S = 'always keep smiling'.split()
# out = '' 
# for i in S:
#     out += i[::-1] + " "
# print(out)


# wap to get the following output

# In = 'push maadi khushi padi'.split()
# out = {}

# for i in In:
#     if len(i)%2==0:
#         out[i] = i[0] + i[-1]

#     else:
#         out[i] = i[len(i)//2]

# print(out)


# wap to toggle a string 

# a = 'AdisdIUGdfnl;osffsdfSSDfiu'
# out=''
# for i in a:
#     if 'A' <= i <= 'Z':
#         out += chr(ord(i) + 32)
#     elif 'a' <= i <= 'z':
#         out += chr(ord(i) - 32)
#     else:
#         out+=i
# print(out)


# wap to extract the upper, lower, digit and special characters present in a string in a different output variable

# a = 'AdisdIUGdfnl;osffs2326dfSSDfiu'
# upper=''
# lower= ''
# digit= ''
# special = ''
# for i in a:
#     if 'A' <= i <= 'Z' :
#         upper += i
#     elif 'a' <= i <= 'z':
#         lower += i
#     elif '0'<= i <= '9':
#         digit+=i
#     else:
#         special+=i
# print(upper, lower, digit, special, sep = '* ')


# wap to get the output
# S= 'hai hello'.split()
# dic = {}

# for i in S:
#     dic[i] = i[1] + i[-1]
# print(dic)


# 
# wap to get the following output 

# S=['jiocinema.com', 'file.py', 'web.html', 'amazon.com', 'www.org']
# out=[]

# for i in S:
#    val = i.split('.')[1]
#    if val not in out:
#         out+= [val]

# print(out)


# wap to get the output as we got from running the code below
# S=['jiocinema.com', 'file.py', 'web.html', 'amazon.com', 'www.org']
# out={}

# for i in S:
#     val = i.split('.')
#     if val[1] not in out:
#         out[val[1]] = [val[0]]
#     else:
#         out[val[1]] += [val[0]]

# print(out)


# wap to get the following output
# L = ['hai', 34, 3.4, 'hello', 90,'byebye']
# out={}
# for i in L:
#     if type(i) == str:
#         out[i] = i[0] + i[-1]

# print(out)

# wap to get the following output
# In = "hello"
# out = {}

# for i in range(len(In)):
#     out[i] = In[i]
# print(out)


# wap to extract all the string values present in list only f the string is palindrome

# a= ["wow", 'hellow', 1,13, 'foxof'] 
# out=[]
# for i in a:
#     if type(i)== str and i==i[::-1]:
#         out +=[i]

# print(out)


# wap to return the positions of vowels prsent in the given string 
# a= 'wow this is so good'
# vow_pos = []
# for i in range(len(a)):
#     if a[i] in "aeiouAEOIU":
#         vow_pos+=[i]

# print(vow_pos)



# wap to check whether the given collection is having a nested collection or not 

# a= [1,3,4,[434,562],(14,6,5,"234"),{3.6,34}]
# a=[1,3,4]
# nested = False
# for i in a:
#     if type(i) not in [int, float, bool, complex]:
#         nested = True

# if nested :
#     print("Nested elements are present")
# else:
#     print("No nested elements")


# wap to count the number of words in a string 
# a ="is this ok to make funeral"
# word_count=0
# for i in a.split():
#     word_count+=1
# print(word_count)


# wap to check whether the number is a neon number or not 
# n= 0
# sq = n**2
# sq= str(sq)
# sum=0
# for i in range(len(sq)):
#     sum += int(sq[i])
# if sum == n:
#     print(f"{n} is a neon number")
# else:
#     print("not a neon number")

# wap to find the longest word in a string 
# a= 'how do i make my funueral funny and internationalization'
# l=[]
# for i in a.split():
#     l+=[len(i)]
# print(max(l))


# wap to replace the special character present in a string by space 
# a = 'it can8r}?} be[,] a special#$ character'
# out = a
# for i in a:
#     if not ('A'<= i<= 'Z' or 'a' <= i <= 'z' or '0' <= i <= '9'):
#         out = out.replace(i," ")
# print(out)


# wap to print the square of all the integers present in a list 
# a = [1,3,4,[434,562],(14,6,5,"234"),{3.6,34}]

# for i in a:
#     if type(i) == int:
#         print(i**2)


# wap to extract all the odd numbers present at even index from a list 
# a = [1,3,4,45, 34, 4,6,2,65,[434,562],(14,6,5,"234"),{3.6,34}]
# for i in range(len(a)):
#     if type(a[i]) == int and i%2==0 and a[i]%2 != 0 :
#         print(i)


# wap to extract all the mutable valus present in a tuple
# a = (1,23,[343,54,"2"], "rvrf", 5+3j)
# for i in a:
#     if i not in [tuple, str]:
#         print(i)


# wap to get the following output
# In = '10100011231'
# out=''

# for i in In:
#     i=int(i)
#     if i ==0:
#         i+=1
#         out+= str(i)
#     elif i==1:
#         i-=1
#         out+= str(i)

# print(out)


# wap to get the following output

# In = 'abacbaacc'
# # out = {'a':4, 'b':2, 'c':3}
# dic = {}

# for i in In:
#     if i not in dic:
#         dic[i]=1
#     elif i in dic:
#         dic[i] += 1

# print(dic)


# wap to extract key value pair from the dictionary only if the key is Boolean datatype

# a = {
#     True: "always",
#     False: 'whyhh',
#     'hekkoi': 0,
#     'tekken': 'take',
# }
# b= a.items()
# dic={}
# for i in b:
#     if type(i[0]) == bool:
#         dic[i[0]] = i[1]

# print(dic)

# wap to get the following output. Extract even and odd digits separately and concatenate them both
# In = '127342'
# out= ''
# even, odd = '',''
# for i in In:
#     i = int(i)
#     if i%2==0:
#         even +=str(i)

#     elif i%2!=0:
#         odd +=str(i)
# out+= even + odd
# print(out)

# wap to check whether the string is having only lowercase or not using continue 

# a = "isf This dfoifoe;DIf"
# a='wow tis is'
# lower_only = False
# for i in a:
#     # print(i)
#     if 'a' <= i <= 'z' or i in [' ']:
#         lower_only = True
#     else:
#         lower_only = False
#         break

# if lower_only:
#     print('Lowercase only')
# else:
#     print('Not only lowercase')


# wap to find the sum square of individual digits of a string 
# a = '12345'
# sum=0
# for i in a:
#     i = int(i)**2
#     print(i)
#     sum+=i
# print(sum)
