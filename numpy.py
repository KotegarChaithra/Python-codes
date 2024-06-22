#why numpy? install numpy
# We worked on single dimensional array till now, what if I want to work with multidimensional array?
#Here comes concept of numpy then

# single dimension :

 # 2 5 6 8 4

# Two dimension
# 2 5 6 8 4
# 6 8 9 8 7
# 5 9 4 5 7
# 3 2 5 7 4

# etc....

# we have to install numpy manually
# we have pip --> go to command prompt
#-->pip3 install numpy --> Tis is for idle
# it will install numpy

#how to intsll for pycharm?
# file ->settings --> project project name-> python intepreter -> + -> search numpy -> click -> install package -> close->ok ->ok

from numpy import *
arr = array([2,4,5,6])
print(arr)

#output:
[2,4,5,6]