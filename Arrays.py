# Even though we have list, tuples why Array?
# To store same set of values, same type of values
#example integer array, float array
#Then why Array? : because we can shrink the array, if we want 5 , if we want to increase we can

#when to use Array?

#Scenario :
# If in case I want to store marks of student, If i want tostore 10 students marks, I have to create 10 different variables right? like marks1, marks 2, marks 3
#If I have 100 students, I need to create 100 variables, it is difficult right?
#We can use Array then

#For that we need to create array, we can use module

# or

#Moment you change the type, it will increase byte or decrese byte
 # TypeCode        C Type         Python Type        Min. size in bytes
 #   'b'       signed char           int                    1
 #   'B'       unsigned char         int                    1
 #   'u'       Py_UNICODE        unicode character          2
 #   'h'       signed short          int                    2
 #   'H'       unsigned short        int                    2
 #   'i'       signed int            int                    2
 #   'I'      unsigned int           int                    2
 #   'l'      signed long            int                    4
 #   'L'      unsigned long          int                    4
 #   'f'          float             float                   4
 #   'd'          double            float                   8

 #By refering above table we can create a Array

from array import *

vals = array('i',[5,9,8,4,2])
print(vals)

#output:
#array('i', [5, 9, 8, 4, 2])

# What if I have value that is different like this :
from array import *

vals = array('i',[5,9,8.8,4,2])
print(vals) # got error

#we can use -ve numbers : ofcourse because it is 'i' signed integer

from array import *

vals = array('i',[5, 9, -8, 4, 2])
print(vals)

#output:
# array('i', [5, 9, -8, 4, 2])

from arrays import *

vals = array('I',[5,9,-8,4,2])
print(vals) # erro: we cannt add -ve numbers when it is initialised as 'I' unsigned integer

# As we work with Array, we can use some functions

#Functions:
#buffer_info() : it willgive you the size of the array
from array import *
vals = array('i',[5,9,-8,4,2])
print(vals.buffer_info())

#output :
# (2205113376720, 5) // [address of array, how many number of elements]
#
# from array import *
# vals = array('i',[5,9,-8,4,2])
# print(vals.typecode)

#output :
# i

from array import *
vals = array('i',[5,9,-8,4,2])
vals.reverse()
print(vals)

#output :
#array('i', [2, 4, -8, 9, 5])

#If I want to print values one by one
##we can use index number

from array import *
vals = ('i',[5,9,-8,4,2])

for i in range(len(vals)):
    print(vals[i])
#output

# 5
#9
#-8
#4
#2

from array import *

vals = array('i',[5,9,-8,4,2])
for e in vals:
    print(e)

#output:
# 5
# 9
# -8
# 4
# 2

# Can I work with characters

from array import *
vals = array('u',['a','e','i'])
for e in vals:
    print(e)

#output:
# a
# e
# i

# Create new array with same element in using existiing array
from array import *
vals = array('i',[5,9,8,4,2])
newArray = array(vals.typecode,(a for a in vals))
for e in newArray:
    print(e)

#output:
# 5
# 9
# 8
# 4
# 2

#square of existing array number
from array import *
vals = array('i',[5,9,8,4,2])
newArray = array(vals.typecode, (a*a for a in vals))

for e in newArray:
    print(e)
#output:
# 25
# 81
# 64
# 16
# 4

#instead of for loop we can use while loop as well

from array import *
vals = array('i',[5,9,8,4,2])
newArray = array(vals.typecode, (a*a for a in vals))

i=0
while i<len(newArray):
    print(newArray[i])
    i+=1

#output:
# 25
# 81
# 64
# 16
# 4

#--------------------------------------------------------------
#How to create arraysby taking user input, if youdon't know the size of the array
from array import *

arr = array('i',[])
n = int(input("Enter the length of the array:"))

for i in range(n):
    x = int(input("Enter the next value:"))
    arr.append(x)

print(arr)

#output:
# Enter the length of the array:4
# Enter the next value:16
# Enter the next value:20
# Enter the next value:14
# Enter the next value:52
# array('i', [16, 20, 14, 52])

#every time we ask the value from user, and if we want to search a value and it should say the index value


from array import *

arr = array('i',[])
n = int(input("Enter the length of the array:"))

for i in range(n):
    x = int(input("Enter the next value:"))
    arr.append(x)

print(arr)

val = int(input("Enter the value for search:"))

k=0
for e in arr:
    if e==val:
        print(k)
        break
    k+=1
#output:
# Enter the length of the array:4
# Enter the next value:14
# Enter the next value:16
# Enter the next value:24
# Enter the next value:13
# array('i', [14, 16, 24, 13])
# Enter the value for search:24
# 2

#search element by using function 'index()
from array import *
arr= array('i',[])
n  = int(input("Enter the length:"))
for i in range(n):
    x = int(input("Enter the value:"))
    arr.append(x)
print(arr)

val=int(input("Enter the search element:"))
print(arr.index(val))

#output:
# Enter the length:3
# Enter the value:1
# Enter the value:2
# Enter the value:3
# array('i', [1, 2, 3])
# Enter the search element:3
# 2