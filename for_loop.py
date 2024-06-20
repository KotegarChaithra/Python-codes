#Print the all the values of list one by one , use for loop
x=['chaithra',65,2.5] # list

for i in x:
    print(i)
#-------------------------------------------------
x='CHAITHRA' # Array
for i in x:
    print(i)
#--------------------------------------------------
for i in [2,6,'Paul']:
    print(i)
#---------------------------------------------------
#for sequence will use range in for loop
for i in range(10):
    print(i)
#---------------------------------------------------
for i in range(11,21,1): #(start,end,step)
    print(i)

#---------------------------------------------------
#going in reverse order
for i in range(20,10,-1):
    print(i)
#--------------------------------------------------
#Print values that is not divisible by 5 (if inside for)
for i in range(1,21):
    if i%5!=0:
        print(i)