#prit numbers which is divisible by 5
nums = [12,15,18,21,25]

for num in nums:
    if num%5==0:
        print(num)

#output:
#15
#25
#--------------------------------------------------------------------------------------------------------
# What if we want to print only first number that is divisible by 5
# By using break statement

nums = [12,15,18,21,25]

for num in nums:
    if num%5==0:
        print(num)
        break

# output:
#15
#-----------------------------------------------------------------------------------------------------------
# What idf we don't have number which is divisible by 5
nums = [12,16,18,21,26]
for num in nums:
    if num%5==0:
        print(num)
        break

#got the output as blank

#we can use else condition here :
nums = [12,16,18,21,26]
for num in nums:
    if num%5==0:
        print(num)
        break
    else:
        print("not found")

# Output :
# not found
# not found
# not found
# not found
# not found

#got not found 5 times, every iteration it is looking for condition if num%5==0: and else is part of if block, hence 'not found' 5 times we got
#We can just write else for for loop

nums = [12,16,18,21,26]
for num in nums:
    if num%5==0:
        print(num)
        break
else:
    print("not found")

#output:
#not found