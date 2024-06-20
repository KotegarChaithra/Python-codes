####
####
####
####

print('# ',end='')
print('# ',end='')
print('# ',end='')
print('# ',end='')

#output:
# # # #

#instead of writing 4 print statement we can use for loop

for j in range(4):
    print('# ', end='')
print()
for j in range(4):
    print('# ', end='')

#output:
# # # #
# # # #

# #above also executing same code again and again
for i in range(4):
    for j in range(4):
        print('# ', end='')
    print() #new line
#-----------------------------------------------------------------------------------------------------------------

#
# #
# # #
# # # # #
for i in range(4):
    for j in range(i+1):
        print('# ',end='')

    print()

#---------------------------------------------------------------------------------------------------------------

# # # #
# # #
# #
#

for i in range(4):
    for j in range(4-i):
        print('# ', end='')
    print()
#--------------------------------------------------------------------------------------------------------------


