## We will use if when set of conditions to be happening
## Example :         statement 1
##                   statement 2
##                   statement 3
##    statement 4                  statement 7
##    statement 5                  statement 8
##    statement 6                  statement 9
##
if True:
    print("I'm right") ## If it is true output will be I'm right

if False:
    print("I'm right") ## If it is false , if block skipped it wont return any output

## we want some more, Everyone knows True and False , what in reality we have some logics, we'll get inputfrom user,
## how to do that
## Example: If the number is even or odd

##Even:
x=2
r=x%2 # 2 is even number

if r==0: #o/p will get reminder as '0'
    print("Even") # hence it will print 'Even' else it will print only 'Bye'
print("Bye") # this 'Bye' outside if statement hence  anyway whether the if conditiontrue or fasle it will
              # print 'Bye'

##Odd:
x=3 # 3 is even number
r=x%2 #o/p will get reminder as '1'

if r==1:
    print("Odd") # hence it will print 'Odd' else it will print only 'Bye'
print("Bye")# this 'Bye' outside if statement hence  anyway whether the if conditiontrue or fasle it will
              # print 'Bye'

## We wan't code to be in efficient way right?
# so,
x=2
r=x%2 # Since 2 is even

if r==0: #reminder will be 0
    print("Even") #Hence it prints even
else:
    print("Odd") # else it prints Odd
print("Bye") # Any how bye is out of if block , it will execute

## If there is sequence of conditions that need to be executed , then how?
#Example:
n=int(input("Enter a number")) # user input It could be any number
if n==1:
    print("One") # if n==1, then prints One
elif n==2:
    print("Two") # else if n==2 , then prints Two
elif n==3:
    print("Three")#else if n==3, then prints Three
elif n==4:
    print("Four")# else if n==4, then prints Four
else:
    print("Wrong Input")# if none of numbers match with n , then wrong input