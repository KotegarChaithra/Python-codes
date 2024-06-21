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

from array import *
vals = array('i',[5,9,-8,4,2])
print(vals.typecode)

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