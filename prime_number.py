# Prime number is a number which is divisible by only one number
#example : 10 is not a prime number because it divided by [1,2,5,10]
# example : [7,13,19] is a prime number

#How to check 7 is a prime number or not?
# Check
# 7   7  7  7  7
# _   _  _  _  _
# 2   3  4  5  6

#if you check 7 /2 , 7/3 , 7/4, 7/5, 7/6
# You'll get to know stating divide by number 2 to n-1

# means 2 to 7-1 i.e 6

num = 7
for i in range(2, num):
    if num%i==0:
        print("Not prime")
    else:
        print("Prime")

#output
# Prime
# Prime
# Prime
# Prime
# Prime

# 5 times prime , so use break statement inside if

num = 7
for i in range(2, num):
    if num%i==0:
        print("Not prime")
        break
else:
    print("Prime")

#output:
#Prime

num = 10
for i in range(2, num):
    if num%i==0:
        print("Not prime")
        break
else:
    print("Prime")

#output:
#Not prime






