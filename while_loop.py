#if I want to print some things again and again for particualr time
#then we can go for loop concept, There are 2 loops :
# 1. while loop
# 2. for loop

#Let's go for while loop
# 3 things are important:
# 1. initialization
# 2. condition
# 3. increment/decrement
i=1 #initialization
while i<=5: # condition
   print("Chaithra")
   i=i+1 #increment

# decrement code
i=5 #initialization
while i>=1: # condition
    print("Chaithra",i) # no of time chaithra printed also printin in 'i'
    i=i-1 #decrement
-----------------------------------------------------------------------------------------------------------------------------------------------------------
# Can we use multiple while:
i=1 #initializatio
while i<=5: # condition
    print("Chaithra", end=" ")#end=" " - don't go to new line
    j=1
    while j<=4:
        print("Rocks", end=" ") #end=" " - don't go to new line
        j=j+1 #increment
    i=i+1 #increment
    print()

#output
# Chaithra Rocks Rocks Rocks Rocks
# Chaithra Rocks Rocks Rocks Rocks
# Chaithra Rocks Rocks Rocks Rocks
# Chaithra Rocks Rocks Rocks Rocks
# Chaithra Rocks Rocks Rocks Rocks

i=5
while i>=1:
    print("Chaithra",end=" ")
    j=5
    while j>=1:
        print("Rocks",end=" " )
        j=j-1#decrement
    i=i-1#decrement
    print()

#output:
# Chaithra Rocks Rocks Rocks Rocks Rocks
# Chaithra Rocks Rocks Rocks Rocks Rocks
# Chaithra Rocks Rocks Rocks Rocks Rocks
# Chaithra Rocks Rocks Rocks Rocks Rocks
# Chaithra Rocks Rocks Rocks Rocks Rocks

