#break:
#if the user want candies from candy machine, if in case user wants 100 candies , it go on print candies 100 times right?
x = int(input("How many candies you want?"))

i=1
while i<=x:
    print("Candy")
    i+=1
#-----------------------------------------------------------------------------------------------------------------------
#if in case 100 candies not available in the machine, how we can solve this issue?
# By using break statement we can terminate execution of while loop
available = 10 # initialize available candies here
x = int(input("How many candies you want?")) # take user input that how much user want

i=1 #counter initialization
while i<=x: #conditions
    if i>available:#if the number of candies more than available candies
        print("out of stock!")
        break # terminate the condition
    print("Candy") #print candies
    i+=1 # counter increase
print("Bye") # print bye so that if we don't have candies that we entered we will get to know

#output:
# How many candies you want?21
# Candy
# Candy
# Candy
# Candy
# Candy
# Candy
# Candy
# Candy
# Candy
# Candy
# Bye

for i in range(5):
    if i==3:
        break
    print("Hello",i)

#output:
# Hello 0
# Hello 1
# Hello 2
#-----------------------------------------------------------------------------------------------------------------------
#Continue:
#print the values ranges from 1 to 100 and which are not divisible by 3 and 5
for i in range(1,101):
    if i%3==0 or i%5==0:
        continue # it will skip the execution for the condition which is true
    print(i)

print("Bye")

for i in range(5):
    if i==3:
        continue
    print("Hello",i)

#output:
# Hello 0
# Hello 1
# Hello 2
# Hello 4
#-----------------------------------------------------------------------------------------------------------------------
#pass:
#If I want to print all the values and which are not odd numbers
for i in range(1,101):
    if i%2!=0:
        pass # there is no code just ignore it, that's what pass is doing
    else:
        print(i)
print("Bye")

def fun(): #if i want to right function, but I don't know what to put here , then to execute next code I can simply put 'pass'
    pass

a=5
#-----------------------------------------------------------------------------------------------------------------------
