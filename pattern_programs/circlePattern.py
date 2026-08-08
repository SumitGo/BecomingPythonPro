from math import sqrt, floor

# cx = 10
# cy = 10
# # l=[]
# r = 5
# # x=5,15
# # y= 5, 15
# # print(f'\033[0;0H',end="")
# print(f'\033[15;15H',end="")
# for j in range(cx-r, cx+r+1):
#         x = cx +  sqrt(r**2 - (j-cy)**2 )
#         print(x,j)
#         print(f'\033[{x};{j}H',end="")
#         print("* ", end="")
#         # print(f'\033[15;15H',end="")
#         print(f'\033[{-x};{-j}H',end="")
#         # print(f'\033[15;15H',end="")
#         # print("* ", end="")
        

# dic = {}
# for i in l:
#     if i not in dic:
#         dic[i] = 1
#     else:
#         dic[i]+=1

# for key,val in dic.items():
#     print(f"{key} : {val}")



'''

(10.0, 5) : 11
(13.0, 6) : 11
(14.0, 7) : 11
(14.582575694955839, 8) : 11
(14.898979485566356, 9) : 11
(15.0, 10) : 11
(14.898979485566356, 11) : 11
(14.582575694955839, 12) : 11
(14.0, 13) : 11
(13.0, 14) : 11
(10.0, 15) : 11

'''




# for i in range(5,15 +1):
#     for j in range(5,15+1):
#         # perimeter = ((i-center[0]) ** 2) + ((j-center[1])**2)
#         print("* ",end="")
#     print('ESC[38;5;#m')

# print("\x1b[19D")
# print("\x1b[31mHello\x1b[0m")
# print("\033[91mBright Red\033[0m")

# print('\033[20;0H')  # y;xH
# print("\033[33mBright Red\033[0m")
# print('\x1b[u')


# print('\033[80;50H', "Hello World")
# print('\033[0;0H', "Hello You")
# All the coordinates refereces are taken from 0,0 coordinate, that means from top left corner 

r = 5
x = sqrt(r**2 - 0**2)
for i in range(r+1):
#     j_range = None
    # x^2 + y^2 = r^2 
#     x^2 = r^2 - y^2
    print(f"\033[{5};{x}H",f"{x},{i}")
    x = sqrt(r**2 - i**2)
#     y is i here
#     for j in range(floor(x)):
        





