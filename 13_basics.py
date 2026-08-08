# def up():
#     a = 'absHODIFjdkljo;iff'
#     out = ''
#     for i in a:
#             if 'A' <= i<= 'Z':
#                     out+=i
#     return out
# print(up())


# def random_func():
#     a = ['ab', 'hello', 3+5j, 'star', 'python', 'fo', [1,2]]
#     out={}
#     for i in range(len(a)):
#         if i%2!=0 and len(a[i])>=3:
#             out[a[i]]=len(a[i])
#     return out
# s = random_func()
# print(s)

# def random_func(string):
#     out=''
#     for i in string:
#         if 'A'<= i <='Z':
#             out+= chr(ord(i)+32)
#         elif 'a' <= i<'z':
#             out+=chr(ord(i) +1)

#         elif i=='z':
#             out+='a'
        
#     return out

# a = 'hizombIRoCKY HzBIBI'
# print(random_func(a))


def random_func(a,b): 

    anagram = True

    for i in b:
        if i not in a and len(a) == len(b):
            anagram = False
            break
    return anagram
    #another way
    # if len(a) ==len(b):
    #     if sorted(a) == sorted(b):
    #         return 'anagram'
    #     else:
    #         return 'not anagram'
    # else:
    #     return 'length not equal'


# d = random_func('listen', 'silent')    
# print(d)

# WAP TO create a calculator where it perform 4 functions : additon , subtractiton, division, multiplication, where our task is , if user press 1, it should do addition, if 2 - subtraction, if 3- multiplicaton, if 4 - division 

def calculator():
    print("1. Addition", "2. Subtraction","3. Multiplication", "4. Division", sep = '\n')
    n = int(input("What's your choice: "))
    
    selection = {1:"Addition", 2: " Subtraction", 3: "Multiplication", 4: "Division"}
    print(f"{selection[n]} Selected!!!!")

    a = int(input("Ener first Number: "))
    b = int(input("Ener second Number: "))
    if n == 1:   
        res = a+b
    elif n ==2:
        res = a-b
    elif n ==3:
        res = a*b
    elif n ==4:
        res = a/b

    return res

# ans = calculator()
# print(ans)


a = 10
b = 20
print('a,b = ', a, b)
def swap():
    global a, b
    print('a,b = ', a, b)
    a,b = b,a
    print('a,b = ', a, b)

swap()
print('a,b = ', a, b)