# pattern:-
'''
* * * * * * 
* * * * * * 
* * * * * *
* * * * * * 
* * * * * * 

'''
# n = 5
# for i in range(n):
#     for j in range(n):
#         print("* ", end = '')
#     print()


'''
*
* *
* * *
* * * * 
* * * * *
* * * * * *

'''
# n = 9
# for i in range(n):
#     for j in range(i+1):
#         print("* ", end="")
#     print()


'''

            *
          * *  
        * * *
      * * * *       
    * * * * *
'''

# n = 7
# for i in range(n):
#     for j in range(n-i-1):   # loop to print the initial spaces, n- (i+1) so that spaces are printed till second last element, as last element will be the star itself
#         print(" ", end =' ') 

#     for k in range(i+1): # loop to print the stars after the spaces, i+1 since i starts with 0
#         print("*",end=" ")
#     print()


'''
      * 
     * * 
    * * * 
   * * * * 
  * * * * * 
 * * * * * * 
* * * * * * * 

'''
# n=5

# for i in range(n):
#     for j in range(n-i-1):
#         # print(j)
#         print(" ",end="")

#     for k in range(i+1):
#         print("* ",end="")
#     print()


'''

* * * * * * * 
 * * * * * * 
   * * * * 
     * * 
      *

'''

# n = 5
# for i in range(n):
#     for k in range(i):
#         print(" ",end="")
#     for j in range(n-i):
#         print("* ", end="")

#     print()


'''

* * * * * 
* * * * 
* * * 
* * 
* 

'''

# n = 5
# for i in range(n):
#     for j in range(n-i):
#         print("* ", end="")

#     print()


'''

* * * * * * * * * *
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
* * * * * * * * * * 
'''
# n = 10

# for i in range(n):
#     for j in range(n):
#         if i == 0 or i ==n-1 or j==0 or j==n-1:
#             print("* ",end='')
#         else:
#             print("  ",end ='')
#     print()

'''

* * * * * * * * * *
*                 
*                 
*                 
*                 
*       * * * * * *
*                 *
*                 *
*                 *
* * * * * * * * * * 
'''
# n=10
# for i in range(n):
#     for j in range(n):
#         if i ==0 or j ==0 or i==n-1:
#             print("* ", end="")
#         elif i>=n//2 and j==n-1:
#             print("* ", end="")
#         elif i==n//2 and j>=n//2: 
#             print("* ", end="")           
#         else:
#             print("  ", end="")
#     print()


"""

* * * * * * * * * * 
* * * * * * * * * * 
* *             * * 
* *             * * 
* *             * * 
* *             * * 
* *             * * 
* *             * * 
* * * * * * * * * * 
* * * * * * * * * * 

"""

# n=8

# for i in range(n):
#     for j in range(n):
#         if i<2 or i>n-1-2 or j<2 or j>n-1-2:
#             print("* ",end="")
#         else:
#             print("  ",end="")

#     print()


"""

*         * * * * * * 
*         *           
*         *           
*         *           
*         *           
* * * * * * * * * * * 
          *         * 
          *         * 
          *         * 
          *         * 
* * * * * *         * 


"""

# n=11

# for i in range(n):
#     for j in range(n):
#         if i<n//2 and j==0  or j==n//2:
#             print("* ", end="")

#         elif i==0 and j>n//2:
#             print("* ", end="")

#         elif i == n-1 and j<n//2:
#             print("* ", end="")

#         elif i==n//2:
#             print("* ", end="")

#         elif j==n-1 and i>n//2:
#             print("* ", end="")

#         else:
#             print("  ",end="")
#     print()


"""

*                 * 
  *             *   
    *         *     
      *     *       
        * *         
        * *         
      *     *       
    *         *     
  *             *   
*                 * 

"""
# n=10
# for i in range(n):
#     for j in range(n):
#         if i==j or i == n-j-1:
#             print("* ",end="")
#         else:
#             print("  ",end="")

#     print()


"""

          *           
          *           
          *           
          *           
          *           
* * * * * * * * * * * 
          *           
          *           
          *           
          *           
          *   

"""
# n=11 # works best with odd numbers

# for i in range(n):
#     for j in range(n):
#         if i == n//2 or j== n//2 :
#             print("* ",end="")
#         else:
#             print("  ",end="")
#     print()


"""
* * * * * * * * * * * 
* *       *       * * 
*   *     *     *   * 
*     *   *   *     * 
*       * * *       * 
* * * * * * * * * * * 
*       * * *       * 
*     *   *   *     * 
*   *     *     *   * 
* *       *       * * 
* * * * * * * * * * * 
"""
# n=15 # works best with odd numbers

# for i in range(n):
#     for j in range(n):
#         if i==0 or i ==n-1 or j==0 or j==n-1 or i ==j  or j== n-1-i or i==n//2 or j==n//2:
#             print("* ",end="")
#         else:
#             print("  ",end="")

#     print()



"""

1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
6 6 6 6 6 6 
7 7 7 7 7 7 7 
8 8 8 8 8 8 8 8 
9 9 9 9 9 9 9 9 9 

"""

# n=10

# for i in range(n):
#     for j in range(i):
#         print(i,end=" ")
#     print()


"""

1 
0 0 
1 1 1 
0 0 0 0 
1 1 1 1 1 
0 0 0 0 0 0 
1 1 1 1 1 1 1 

"""

# n=7
# for i in range(n):
#     for j in range(i+1):
#         print(f"{(i+1)%2} ",end="")

#     print()


"""

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
1 2 3 4 5 6 
1 2 3 4 5 6 7 

"""

# n=7
# for i in range(n):
#     for j in range(i+1):
#         print(f"{j+1} ",end="")
#     print()



"""

1 
1 0 
1 0 1 
1 0 1 0 
1 0 1 0 1 
1 0 1 0 1 0 
1 0 1 0 1 0 1 

"""

# n=7

# for i in range(n):
#     for j in range(i+1):
#         print(f"{(j+1)%2} ",end="")

#     print()



"""

7 
6 6 
5 5 5 
4 4 4 4 
3 3 3 3 3 
2 2 2 2 2 2 
1 1 1 1 1 1 1

"""

# n=7
# for i in range(n):
#     for j in range(i+1):
#         print(f"{n-i} ",end="")
#     print()


"""

1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 

"""
# n = 5
# count = 1
# for i in range(n):
#     for j in range(i+1):
#         print(f"{count} ",end="")
#         count+=1

#     print()



"""

15
14      13
12      11      10
9       8       7       6
5       4       3       2       1

"""

# n=5
# final = n*(n+1) //2
# for i in range(n):
#     for j in range(i+1):
#         print(f"{final}\t",end="")
#         final-=1

#     print()


"""

1 
3 2 
6 5 4 
10 9 8 7 
15 14 13 12 11 

"""


# n=5
# count=1
# for i in range(n):
#     for j in range(i+1):
#         print(f"{count-j} ",end="")
#     count+=1+(i+1)
#     print()



"""

15
13      14
10      11      12
6       7       8       9
1       2       3       4       5

"""

# n=5
# final = n*(n+1)//2

# for i in range(n):
#     for j in range(i+1):
#         print(f"{final+j}\t",end="")

#     final = final - i-1 -1
#     print()


"""
E 
D D 
C C C 
B B B B 
A A A A A 

"""

# n=5
# method 1
# for i in range(n):
#     print((f"{chr(64 + n - i)} ")*(i+1))

# method 2
# for i in range(n):
#     for j in range(i+1):
#         print(f"{ chr(64+ n - i )} ",end='')
#     print()


"""
A 
A B 
A B C 
A B C D 
A B C D E 
A B C D E F 

"""
# n = 6
# for i in range(n):
#     for j in range(i+1):
#         print(f"{chr(64 + j +1)} ",end='')
#     print()





"""

* * * * * * * * * * 
  * * * * * * * * * 
    * * * * * * * * 
      * * * * * * * 
        * * * * * * 
          * * * * * 
            * * * * 
              * * * 
                * * 
                  * 

"""

# n=10
# for i in range(n):
#     for j in range(i):
#         print("  ",end="")
#     for k in range(n-i):
#         print("* ",end="")

#     print()



"""


# """
# n=10

# for i in range(n):
#     for j in range((n//2)-i,-1,-1):
#         # print(j,end="")
#         print("  ",end="")
#     for k in range(i*2+1):
#         print("* ",end="")
#     print()
#     if i>n//2:

#         for j in range(i+1):
#             print("  ",end="")
#         for k in range(n-i-1):
#             print("* ",end="")
#         print()


"""

            * 
          * * * 
        * * * * * 
      * * * * * * * 
    * * * * * * * * * 
  * * * * * * * * * * * 
* * * * * * * * * * * * * 

"""

# n=7

# for i in range(n):
#     for j in range(n-i-1):
#         print("  ",end="")
#     for k in range(i+1):
#         print("*   ",end="")
#     print()


"""

            *   
          *   *   
        *   *   *   
      *   *   *   *   
    *   *   *   *   *   
  *   *   *   *   *   *   
    *   *   *   *   *   
      *   *   *   *   
        *   *   *   
          *   *   
            *   


"""

# n=6
# for i in range(n-1):
#     for j in range(n-i):
#         print("  ",end='')
#     for k in range(i+1):
#         print("*   ",end="")
#     print()

# for i in range(n):
#     for j in range(i+1):
#         print("  ",end='')
#     for k in range(n-i):
#         print("*   ",end="")
#     print()



"""

       * 
      * * 
     * * * 
    * * * * 
   * * * * * 
  * * * * * * 
      * * 
      * * 
      * * 
      * * 
      * * 
      * * 

"""

# from math import log,floor
# n=8
# for i in range(n):
#     for j in range(n-i + 1):
#         print(" ",end='')
#     for k in range(i+1):
#         print("* ",end='')
#     print()

# for i in range(n):
#     for j in range(n):
#         print(" ",end='')
#     for k in range(2):
#         print("* ",end='')
#     print()


"""
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 

"""

# n=5

# for i in range(n):
#     for j in range(n-i):
#         print(f"{j+1} ",end="")
#     print()


"""
D C B A 
D C B 
D C 
D 

"""
# n = 4
# for i in range(n):
#     for j in range(n-i ):
#         print(f"{chr(64 + n -j)} ",end="")
#     print()



"""
D E F G 
D E F 
D E 
D 

"""

# n=4
# for i in range(n):
#     for j in range(n-i):
#         print(f"{chr(64 + n +j)} ",end="")
#     print()


"""
A B C D 
E F G 
H I 
J 

"""


# n=4
# k=1
# for i in range(n):
#     for j in range(n-i):
#         print(f"{chr(64 +k)} ",end="")
#         k+=1
#     print()


"""

      * 
    * * * 
  * * * * * 
* * * * * * * 

"""
# n=4

# for i in range(n):
#     for k in range(n-i):
#         print("  ",end="")
#     for j in range(2*i+1):
#         print("* ",end='')
#     print()

# method 2: single for loop using string multiplication
# for i in range(n):
#     print("  "*(n-i-1) + "* "*(2*i+1))


"""
      1 
    2 2 2 
  3 3 3 3 3 
4 4 4 4 4 4 4 

"""
# n=4
# for i in range(n):
#     print("  "*(n-1-i)+ f"{i+1} "*(2*i+1))


"""
            7 
          6 6 6 
        5 5 5 5 5 
      4 4 4 4 4 4 4 
    3 3 3 3 3 3 3 3 3 
  2 2 2 2 2 2 2 2 2 2 2 
1 1 1 1 1 1 1 1 1 1 1 1 1 

"""
# n=7
# for i in range(n):
#     print("  "*(n-i-1) + f"{n-i} "*(2*i+1))


"""
      A 
    B B B 
  C C C C C 
D D D D D D D 

"""

# n=4
# for i in range(n):
#     print("  "*(n-i-1) + f"{chr(65 +i)} "*(2*i+1))


"""
      D 
    C C C 
  B B B B B 
A A A A A A A 

"""

# n=4
# for i in range(n):
#     print("  "*(n-i-1) + f"{chr(64 +n -i)} "*(2*i+1))


"""
      *   
    *   *   
  *   *   *   
*   *   *   *  

"""
# n=4
# for i in range(n):
#     print("  "*(n-i-1) + "*   "*(i+1))


"""
      D   
    C   C   
  B   B   B   
A   A   A   A 
"""

# n=4
# for i in range(n):
#     print("  "*(n-i-1) + f"{chr(64+n-i)}   "*(i+1))