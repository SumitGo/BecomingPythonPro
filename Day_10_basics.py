# a = 'how are you all'.split()
# count=[]
# for i in a:
#     c=0
#     for j in i:
#         if j in 'aeiouAEIOU':
#             c+=1
#     count+=[c]

# print(count)

# a = 'Power Star'.split()
# out = {}
# for i in a:
#     c=0
#     for j in i:
#         if j in 'aeiouAEIOU':
#             c+=1
#     out[i] = c

# print(out)

# wap to find the factorial of first 10 numbers and store in a list
# l=[]
# n=10
# for j in range(1,n+1):
#     product = 1
#     for i in range(1,j+1):
#         product = i*product
#     l.append(product)

# print(l)

# a = [10, 'hello', 3+5j, 321]
# out=[]

# for i in a:
#     if type(i)==int:
#         i = str(i) # ["10"]
#         add= 0
#         for item in i:
#             add += int(item)
#         out+=[add]

# print(out)


# a= [791, 'Hello', 3.4, 127, 43]
# s=[]

# for i in a:
#     if type(i) == int:
#         # i = int(str(i)[::-1])
#         # s+=[i]
#         i = str(i)
#         temp = ''
#         for j in range(len(i)-1,-1,-1):
#             temp+=i[j]
#         s+=[int(temp)]
# print(s)


# a = 'kabab is real love'.split()
# dic = {}
# for i in a:
#     vowel_count = 0
#     even_letters = ''
#     for j in range(len(i)):
#         if i[j] in "AEIOUaeiou":
#             vowel_count+=1
#         if j%2==0:
#             even_letters+=i[j]
        
#         dic[i]= [i[::-1], vowel_count, even_letters]

# print(dic)

# a = 'kabab is love'.split()
# dic = {}
# for i in a:
#     # m = i[::-1]
#     # if 
#     # dic[i]= [m,len(m), m[::-1]]
#     consonant=''
#     for j in range(len(i)):
#         if j%2==0:
#             consonant += i[j]
#     dic[i[0]+i[-1]] = [consonant, len(consonant), consonant[::-1]]

# print(dic)













# a = 'kabab is love'.split()
# dic = {}
# for i in a:
#     consonant=''
#     for j in i:
#         if j not in 'AEIOUaeiou':
#             consonant+=j
#     dic[i[0]+i[-1]] = [consonant, len(consonant), consonant[::-1]]

# print(dic)

# a= { 10: 'star', 20:'bye', 30:'moon', 40:'apple' }
# out={}
# for i in a:
#     for j in a[i]:
#         if j in 'aeiouAEIOU':
#             if i in out:
#                 out[i] += j
#             else:
#                 out[i] = j

# print(out)


inp = [100, 200, 50, 400, 300]
out = []  # [[100,200], [300]]
n= 300

for j in range(len(inp)):
    temp = []
    if inp[j] == n:
        temp.append(inp[j])
        out.append(temp)

    for i in range(j+1,len(inp)):
        if inp[j] + inp[i] == n :
            temp+=inp[i], inp[j]
            out.append(temp)

print("out",out)
